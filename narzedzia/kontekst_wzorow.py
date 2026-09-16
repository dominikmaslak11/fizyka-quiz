#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dopisuje do kazdego wzoru kluczowego kontekst wyciagniety z podrecznika:
rozdzial, w ktorym wystepuje, oraz zdanie z okolicy.

To daje odpowiedz na pytanie "czego ten wzor dotyczy" dla WSZYSTKICH wzorow,
bez recznego pisania. Pelniejszy komentarz (zastosowanie, przyklad) dopisujemy
recznie w bank/komentarze.py — tam, gdzie to sie naprawde oplaca.
"""
import json, pathlib, re, subprocess

KATALOG = pathlib.Path(__file__).resolve().parent.parent
PDF = pathlib.Path.home() / "Pobrane" / "Fizyka_2023.pdf"
PLIK = KATALOG / "bank" / "wyciag.json"

# naglowek rozdzialu: "2.3.1 Przyspieszenie jednostajne" albo "12 Ruch drgający"
NAGLOWEK = re.compile(r"^\s{0,6}(\d{1,2}(?:\.\d{1,2}){0,2})\s+([A-ZŻŹĆĄŚĘŁÓŃ][^\n]{3,70})\s*$")
PAGINA = re.compile(r"Moduł\s+[IVX]+\s*[–-]")
SMIECI = re.compile(r"^\s*\d{1,3}\s*$")


def zdania(tekst):
    """Rozbija tekst strony na zdania, odrzucajac pagine i resztki wzorow."""
    linie = []
    for l in tekst.splitlines():
        l = l.strip()
        if not l or PAGINA.search(l) or SMIECI.match(l):
            continue
        # linie z duza iloscia znakow matematycznych to zwykle sam wzor
        litery = sum(c.isalpha() for c in l)
        if litery < len(l) * 0.55:
            continue
        linie.append(l)
    tekst = " ".join(linie)
    return [z.strip() for z in re.split(r"(?<=[.!?])\s+", tekst) if 40 < len(z.strip()) < 320]


def main():
    strony = subprocess.run(["pdftotext", "-layout", str(PDF), "-"],
                            capture_output=True, text=True).stdout.split("\f")
    # Dla kazdej strony: naglowek obowiazujacy na jej poczatku oraz lista naglowkow
    # z pozycja (numer linii), zeby dobrac ten, ktory stoi NAD wzorem.
    wejsciowy, naglowki, ost = {}, {}, ""
    for nr, t in enumerate(strony, 1):
        wejsciowy[nr] = ost
        lok = []
        linie = t.splitlines()
        for i, l in enumerate(linie):
            m = NAGLOWEK.match(l)
            # tytul rozdzialu nie zawiera znaku rownosci ani cyfr jednostek —
            # bez tego linia w rodzaju "7 N = 14.003074 u." udaje naglowek
            if m and not m.group(2).strip().endswith("...") \
                   and "=" not in m.group(2) \
                   and sum(c.isdigit() for c in m.group(2)) <= 2:
                ost = f"{m.group(1)} {m.group(2).strip()}"
                lok.append((i / max(len(linie), 1), ost))
        naglowki[nr] = lok

    # Strony podsumowan i materialow dodatkowych nie maja numerowanych naglowkow,
    # wiec bez tego dostawalyby ostatni naglowek zwyklego rozdzialu — myląco.
    specjalne = {}
    for nr, t in enumerate(strony, 1):
        g = t[:400]
        if re.search(r"Materia[łl]y dodatkowe", g):
            specjalne[nr] = "Materiały dodatkowe"
        elif re.search(r"Podsumowanie", g):
            specjalne[nr] = "Podsumowanie modułu"
        elif re.search(r"Test kontrolny|–\s*Test", g):
            specjalne[nr] = "Test kontrolny"

    d = json.loads(PLIK.read_text(encoding="utf-8"))
    WYS_STRONY_PX = 1650   # wysokosc renderu strony przy 150 dpi
    bez = 0
    for w in d["kluczowe"]:
        nr = w["strona"]
        # udzial wysokosci, na ktorym stoi wzor — porownujemy z pozycjami naglowkow
        ulamek = min(max(w.get("y", 0) / WYS_STRONY_PX, 0.0), 1.0)
        if nr in specjalne:
            w["rozdzial"] = specjalne[nr]
        else:
            pasujace = [h for (poz, h) in naglowki.get(nr, []) if poz <= ulamek]
            w["rozdzial"] = pasujace[-1] if pasujace else wejsciowy.get(nr, "")
        # zdanie opisowe: najpierw z tej strony, jak brak — z poprzedniej
        z = zdania(strony[nr - 1]) if nr - 1 < len(strony) else []
        if not z and nr - 2 >= 0:
            z = zdania(strony[nr - 2])
        w["opis_zrodlowy"] = z[0] if z else ""
        if not w["rozdzial"]:
            bez += 1

    PLIK.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Dopisano kontekst do {len(d['kluczowe'])} wzorów (bez rozdziału: {bez})")
    for w in d["kluczowe"][:4]:
        print(f"\n  {w['plik']}  str. {w['strona']}  [{w['modul']}]")
        print(f"    rozdział: {w['rozdzial']}")
        print(f"    opis:     {w['opis_zrodlowy'][:110]}")


if __name__ == "__main__":
    main()
