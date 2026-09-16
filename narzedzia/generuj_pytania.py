#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generuje pytania z materialu wyciagnietego z podrecznika.

Wszystkie tresci pochodza wprost z ksiazki — nic nie jest zmyslane. Generator
tylko przestawia je w pytania zamkniete i dobiera dystraktory z TEGO SAMEGO
modulu, zeby nie byly oczywiste.

Cztery rodzaje:
  D1  tresc definicji  -> ktore to pojecie
  D2  nazwa pojecia    -> ktora definicja
  P1  tresc prawa      -> ktore to prawo
  W1  obrazek wzoru    -> z ktorego rozdzialu pochodzi

Pytanie powstaje tylko wtedy, gdy da sie wyluskac czysta nazwe i znalezc trzy
rozne dystraktory. Wszystko inne jest pomijane — lepiej mniej pytan niz belkot.
"""
import json, pathlib, random, re, sys

KATALOG = pathlib.Path(__file__).resolve().parent.parent
WYCIAG = KATALOG / "bank" / "wyciag.json"
WYJSCIE = KATALOG / "bank" / "pytania_generowane.json"
SEED = 20260616

LACZNIKI = [" jest ", " to ", " nazywamy ", " są ", " oznacza ", " określa ",
            " definiujemy ", " nazywa się "]


def czysty(t):
    """Przycina nazwe i odrzuca to, co nie wyglada na pojecie."""
    t = re.sub(r"\s*\([^)]*\)", "", t).strip(" ,;:.")
    t = re.sub(r"\s+[A-Za-z]$", "", t)          # ogon w rodzaju "siłą bezwładności Fb"
    slowa = t.split()
    if not (1 <= len(slowa) <= 5) or len(t) < 4:
        return None
    return t


def termin(tresc):
    """Nazwa pojecia z definicji. Sprawdzamy trzy uklady zdania."""
    # 1) "Pod pojęciem X rozumiemy ..."
    m = re.match(r"Pod poj[ęe]ciem\s+(.{3,45}?)\s+rozumiemy\b", tresc, re.I)
    if m:
        t = czysty(m.group(1))
        if t:
            return t[0].upper() + t[1:]

    # 2) "X jest / to / definiujemy jako ..." — nazwa na poczatku
    for l in LACZNIKI:
        i = tresc.find(l)
        if 0 < i < 70:
            t = czysty(tresc[:i])
            if t and t[0].isupper():
                return t

    # 3) "... nazywamy X." — nazwa na koncu
    m = re.search(r"\bnazywamy\s+(.{4,45})\.?\s*$", tresc)
    if m:
        t = czysty(m.group(1))
        if t:
            return t[0].upper() + t[1:]
    return None


def nazwa_prawa(kontekst):
    """Nazwa prawa z linii poprzedzajacej blok, o ile wyglada na tytul."""
    k = kontekst.strip().rstrip(":").strip()
    if not (12 <= len(k) <= 110):
        return None
    if not re.search(r"(zasad|prawo|prawa|twierdzeni|regu[łl]|hipotez|postulat)", k, re.I):
        return None
    if k.endswith((",", "i", "oraz", "że")):        # urwane zdanie, nie tytul
        return None
    k = re.sub(r"^(Sformu[łl]owanie|Tre[śs][ćc]|Zapiszmy|Mo[żz]emy zapisa[ćc])\s+", "", k, flags=re.I)
    return k[0].upper() + k[1:]


def skroc(t, n=230):
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + "…"


def dobierz(rnd, pula, poprawna, ile=3):
    """Trzy rozne dystraktory, najpierw z tego samego modulu."""
    kandydaci = [x for x in pula if x != poprawna]
    if len(kandydaci) < ile:
        return None
    return rnd.sample(kandydaci, ile)


def main():
    d = json.loads(WYCIAG.read_text(encoding="utf-8"))
    rnd = random.Random(SEED)
    pytania = []

    # ---------- definicje ----------
    defs = []
    for x in d["definicje"]:
        t = termin(x["tresc"])
        if t:
            defs.append({**x, "termin": t})

    wg_modulu = {}
    for x in defs:
        wg_modulu.setdefault(x["modul"], []).append(x)

    for x in defs:
        rodzenstwo = [y["termin"] for y in wg_modulu[x["modul"]] if y["termin"] != x["termin"]]
        if len(rodzenstwo) < 3:
            rodzenstwo = [y["termin"] for y in defs if y["termin"] != x["termin"]]
        dyst = dobierz(rnd, rodzenstwo, x["termin"])
        if dyst:
            pytania.append({
                "id": f"G-D1-{len(pytania)+1:04d}", "modul": x["modul"], "rozdzial": f"str. {x['strona']}",
                "pytanie": f"Które pojęcie podręcznik definiuje tak: „{skroc(x['tresc'])}”?",
                "odp": [x["termin"]] + dyst, "ok": 0,
                "wyj": f"Definicja z podręcznika, strona {x['strona']}: {x['tresc']}",
            })

        # wersja odwrotna: nazwa -> tresc definicji
        inne = [y["tresc"] for y in wg_modulu[x["modul"]] if y["tresc"] != x["tresc"]]
        if len(inne) < 3:
            inne = [y["tresc"] for y in defs if y["tresc"] != x["tresc"]]
        dyst2 = dobierz(rnd, inne, x["tresc"])
        if dyst2:
            pytania.append({
                "id": f"G-D2-{len(pytania)+1:04d}", "modul": x["modul"], "rozdzial": f"str. {x['strona']}",
                "pytanie": f"Jak podręcznik definiuje pojęcie „{x['termin']}”?",
                "odp": [skroc(x["tresc"])] + [skroc(y) for y in dyst2], "ok": 0,
                "wyj": f"Definicja ze strony {x['strona']}.",
            })

    # ---------- prawa i twierdzenia ----------
    prawa = []
    for x in d["prawa"]:
        n = nazwa_prawa(x.get("kontekst", ""))
        if n:
            prawa.append({**x, "nazwa": n})

    nazwy = [p["nazwa"] for p in prawa]
    for x in prawa:
        dyst = dobierz(rnd, nazwy, x["nazwa"])
        if dyst:
            pytania.append({
                "id": f"G-P1-{len(pytania)+1:04d}", "modul": x["modul"], "rozdzial": f"str. {x['strona']}",
                "pytanie": f"Które prawo lub twierdzenie brzmi: „{skroc(x['tresc'])}”?",
                "odp": [x["nazwa"]] + dyst, "ok": 0,
                "wyj": f"Podręcznik, strona {x['strona']}: {x['tresc']}",
            })

    # ---------- wzory kluczowe ----------
    rozdzialy_modulu = {}
    for w in d["kluczowe"]:
        if w.get("rozdzial"):
            rozdzialy_modulu.setdefault(w["modul"], set()).add(w["rozdzial"])

    for w in d["kluczowe"]:
        r = w.get("rozdzial")
        if not r:
            continue
        pula = sorted(rozdzialy_modulu.get(w["modul"], set()) - {r})
        if len(pula) < 3:
            continue
        dyst = rnd.sample(pula, 3)
        pytania.append({
            "id": f"G-W1-{len(pytania)+1:04d}", "modul": w["modul"], "rozdzial": f"str. {w['strona']}",
            "pytanie": "Do którego zagadnienia odnosi się ten wzór?",
            "obrazek": w["plik"],
            "odp": [r] + dyst, "ok": 0,
            "wyj": f"Wzór wyróżniony przez autora na stronie {w['strona']}, rozdział {r}.",
        })

    # ---------- W2: rozpoznaj wzor wsrod czterech ----------
    # Odwrotnosc W1 i znacznie mocniejsze cwiczenie: zagadnienie podane slowami,
    # a odpowiedziami sa OBRAZKI wzorow. Dystraktory z tego samego modulu, zeby
    # nie dalo sie zgadnac po samym wygladzie.
    wg_rozdzialu = {}
    for w in d["kluczowe"]:
        if w.get("rozdzial"):
            wg_rozdzialu.setdefault((w["modul"], w["rozdzial"]), []).append(w)

    for (modul, rozdz), lista in sorted(wg_rozdzialu.items()):
        obce = [w for w in d["kluczowe"]
                if w["modul"] == modul and w.get("rozdzial") and w["rozdzial"] != rozdz]
        if len(obce) < 3:
            continue
        for w in lista[:3]:          # najwyzej trzy wzory z rozdzialu, zeby nie zalac banku
            dyst = rnd.sample(obce, 3)
            pytania.append({
                "id": f"G-W2-{len(pytania)+1:04d}", "modul": modul, "rozdzial": f"str. {w['strona']}",
                "pytanie": f"Który wzór dotyczy zagadnienia „{rozdz}”?",
                "odp_obrazki": [w["plik"]] + [x["plik"] for x in dyst], "ok": 0,
                "odp": ["", "", "", ""],
                "wyj": f"Wzór ze strony {w['strona']}, rozdział {rozdz}. Pozostałe pochodzą z innych rozdziałów tego samego modułu.",
            })

    WYJSCIE.write_text(json.dumps(pytania, ensure_ascii=False, indent=1), encoding="utf-8")

    from collections import Counter
    c = Counter(p["id"].split("-")[1] for p in pytania)
    print(f"Wygenerowano {len(pytania)} pytań:")
    for k, n in sorted(c.items()):
        opis = {"D1": "definicja → pojęcie", "D2": "pojęcie → definicja",
                "P1": "treść prawa → nazwa", "W1": "wzór → zagadnienie",
                "W2": "zagadnienie → wzór (obrazki)"}[k]
        print(f"   {k}  {opis:26s} {n:4d}")
    m = Counter(p["modul"] for p in pytania)
    print("\nwg modułu:", {f"M{i}": m.get(f"M{i}", 0) for i in range(1, 12)})
    print(f"\nzapisano {WYJSCIE.relative_to(KATALOG)}")


if __name__ == "__main__":
    main()
