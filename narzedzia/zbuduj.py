#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scala banki, sklada wzory i eksportuje pytania.json do zasobow aplikacji.

Wzory zapisane w tekscie miedzy znakami $...$ sa wyciagane, skladane do PNG
i zastepowane znacznikiem [[w_xxxx]], ktory aplikacja podmienia na obrazek.
"""
import json, pathlib, random, re, sys

KATALOG = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KATALOG / "bank"))
sys.path.insert(0, str(KATALOG / "narzedzia"))

from dzialy import MODULY, NAZWY, KOLORY, ROZDZIALY   # noqa: E402
import wzory                                          # noqa: E402

SEED = 20260616
WZOR = re.compile(r"\$(.+?)\$", re.S)


def zbierz():
    """Wczytuje KAZDY plik bank/bank_*.py, ktory definiuje liste P.

    Dzieki temu dopisanie nowego pliku z pytaniami nie wymaga zmian tutaj —
    wystarczy go dodac do katalogu bank/.
    """
    import importlib
    p, zrodla = [], []
    for plik in sorted((KATALOG / "bank").glob("bank_*.py")):
        modul = importlib.import_module(plik.stem)
        if hasattr(modul, "P"):
            p.extend(modul.P)
            zrodla.append(f"{plik.stem} ({len(modul.P)})")
    print("  banki: " + ", ".join(zrodla))
    return p


def wyciagnij_wzory(pytania):
    """Zbiera wszystkie unikalne fragmenty LaTeX-a z calego banku."""
    znalezione = set()
    for p in pytania:
        teksty = [p["pytanie"], p["wyj"]] + list(p["odp"])
        for t in teksty:
            znalezione.update(m.strip() for m in WZOR.findall(t))
    return znalezione


def podmien(tekst, indeks):
    """Zamienia $...$ na znacznik [[nazwa]] rozpoznawany przez aplikacje."""
    def zamien(m):
        w = m.group(1).strip()
        if w in indeks:
            return "[[" + indeks[w]["plik"].removesuffix(".png") + "]]"
        return m.group(0)
    return WZOR.sub(zamien, tekst)


def sprawdz(pytania):
    bledy, widziane = [], set()
    moduly = {k for k, _, _ in MODULY}
    for p in pytania:
        pid = p.get("id", "???")
        if pid in widziane:
            bledy.append(f"{pid}: zduplikowane id")
        widziane.add(pid)
        if len(p.get("odp", [])) != 4:
            bledy.append(f"{pid}: musi byc 4 odpowiedzi")
        if len(set(p.get("odp", []))) != 4:
            bledy.append(f"{pid}: powtorzone odpowiedzi")
        if not 0 <= p.get("ok", -1) < 4:
            bledy.append(f"{pid}: zly indeks poprawnej odpowiedzi")
        if p.get("modul") not in moduly:
            bledy.append(f"{pid}: nieznany modul {p.get('modul')!r}")
        if not p.get("wyj"):
            bledy.append(f"{pid}: brak wyjasnienia")
        # niesparowany $ oznacza urwany wzor — latwo o to przy pisaniu
        for pole in ["pytanie", "wyj"] + list(p.get("odp", [])):
            if pole.count("$") % 2:
                bledy.append(f"{pid}: nieparzysta liczba znakow $ w: {pole[:40]}")
    return bledy


def main():
    pytania = zbierz()
    bledy = sprawdz(pytania)
    if bledy:
        for b in bledy:
            print("BLAD:", b)
        raise SystemExit(1)
    print(f"Pytania: {len(pytania)}, bez bledow.")

    print("\nSkładam wzory:")
    indeks = wzory.zloz_wszystkie(wyciagnij_wzory(pytania))

    # pytania wygenerowane z materialu podrecznika dolaczamy do recznie pisanych
    gen_plik = KATALOG / "bank" / "pytania_generowane.json"
    generowane = json.loads(gen_plik.read_text(encoding="utf-8")) if gen_plik.exists() else []
    pytania = pytania + generowane
    print(f"  w tym wygenerowanych z podręcznika: {len(generowane)}")

    rnd = random.Random(SEED)
    wyjscie = []
    for p in pytania:
        # przy odpowiedziach obrazkowych tasujemy rownolegle teksty i pliki
        obrazki = p.get("odp_obrazki")
        pary = list(enumerate(p["odp"]))
        rnd.shuffle(pary)
        rekord = {
            "id": p["id"],
            "modul": p["modul"],
            "rozdzial": p.get("rozdzial", ""),
            "pytanie": podmien(p["pytanie"], indeks),
            "odpowiedzi": [podmien(t, indeks) for _, t in pary],
            "poprawna": next(i for i, (s, _) in enumerate(pary) if s == p["ok"]),
            "wyjasnienie": podmien(p["wyj"], indeks),
        }
        if p.get("obrazek"):
            rekord["obrazek"] = p["obrazek"]
        if obrazki:
            rekord["odpowiedzi_obrazki"] = [obrazki[s] for s, _ in pary]
        wyjscie.append(rekord)

    # material wyciagniety z podrecznika: wzory kluczowe, definicje, prawa, zadania
    wyciag_plik = KATALOG / "bank" / "wyciag.json"
    wyciag = json.loads(wyciag_plik.read_text(encoding="utf-8")) if wyciag_plik.exists() else {}

    # komentarze do wzorow — kluczowane numerem rozdzialu, wiec jeden wpis
    # obsluguje wszystkie wzory z danego rozdzialu
    try:
        from komentarze import K as KOMENTARZE
    except ImportError:
        KOMENTARZE = {}
    z_komentarzem = 0
    for w in wyciag.get("kluczowe", []):
        rozdz = w.get("rozdzial") or ""
        # najpierw pelna nazwa (dla "Materiały dodatkowe"), potem sam numer
        klucz = rozdz if rozdz in KOMENTARZE else rozdz.split(" ")[0]
        if klucz in KOMENTARZE:
            w["komentarz"] = KOMENTARZE[klucz]
            z_komentarzem += 1
    print(f"  wzorów z komentarzem: {z_komentarzem} z {len(wyciag.get('kluczowe', []))}")

    dane = {
        "wersja": "1.1",
        "zrodlo": {
            "tytul": "Zbigniew Kąkol, „Fizyka dla inżynierów”",
            "wydawca": "Wydział Fizyki i Informatyki Stosowanej, AGH w Krakowie, 2023",
            "url": "https://zasoby.open.agh.edu.pl/zasob/fizyka-podrecznik/",
            "licencja": "CC BY-SA 4.0",
        },
        "moduly": [{"id": k, "nazwa": n, "kolor": c, "rozdzialy": ROZDZIALY[k]}
                   for k, n, c in MODULY],
        # em_px jest jednakowe dla wszystkich wzorow (staly PT i DPI przy skladaniu).
        # Aplikacja skaluje kazdy obrazek TYM SAMYM wspolczynnikiem, a nie do wspolnej
        # wysokosci — inaczej wzor z ulamkiem wychodzilby drobniejszy od jednowierszowego.
        "em_px": wzory.EM_PX,
        "wzory": {v["plik"].removesuffix(".png"): {"w": v["w"], "h": v["h"]}
                  for v in indeks.values()},
        "pytania": wyjscie,
        "kluczowe": wyciag.get("kluczowe", []),
        "definicje": [d | {"id": f"D{i+1:03d}"} for i, d in enumerate(wyciag.get("definicje", []))],
        "prawa": [d | {"id": f"P{i+1:03d}"} for i, d in enumerate(wyciag.get("prawa", []))],
        "zadania": [d | {"id": f"Z{i+1:03d}"} for i, d in enumerate(wyciag.get("zadania", []))],
    }

    cel = KATALOG / "android" / "app" / "src" / "main" / "assets" / "pytania.json"
    cel.parent.mkdir(parents=True, exist_ok=True)
    cel.write_text(json.dumps(dane, ensure_ascii=False, indent=1), encoding="utf-8")

    from collections import Counter
    print(f"\nZapisano {cel.relative_to(KATALOG)}")
    for k, _, _ in MODULY:
        n = sum(1 for p in wyjscie if p["modul"] == k)
        print(f"  {k:4s} {NAZWY[k][:40]:42s} {n:3d}")
    print(f"\n  Pytań: {len(wyjscie)}   Wzorów w pytaniach: {len(indeks)}")
    print(f"  Z podręcznika: {len(dane['kluczowe'])} wzorów kluczowych, "
          f"{len(dane['definicje'])} definicji, {len(dane['prawa'])} praw, "
          f"{len(dane['zadania'])} zadań")


if __name__ == "__main__":
    main()
