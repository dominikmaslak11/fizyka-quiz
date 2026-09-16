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
    import bank_mechanika, bank_fale_termo, bank_elektro, bank_optyka_kwanty
    p = []
    for m in (bank_mechanika, bank_fale_termo, bank_elektro, bank_optyka_kwanty):
        p.extend(m.P)
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

    rnd = random.Random(SEED)
    wyjscie = []
    for p in pytania:
        pary = list(enumerate(p["odp"]))
        rnd.shuffle(pary)
        wyjscie.append({
            "id": p["id"],
            "modul": p["modul"],
            "rozdzial": p.get("rozdzial", ""),
            "pytanie": podmien(p["pytanie"], indeks),
            "odpowiedzi": [podmien(t, indeks) for _, t in pary],
            "poprawna": next(i for i, (s, _) in enumerate(pary) if s == p["ok"]),
            "wyjasnienie": podmien(p["wyj"], indeks),
        })

    dane = {
        "wersja": "1.0",
        "zrodlo": {
            "tytul": "Zbigniew Kąkol, „Fizyka dla inżynierów”",
            "wydawca": "Wydział Fizyki i Informatyki Stosowanej, AGH w Krakowie, 2023",
            "url": "https://zasoby.open.agh.edu.pl/zasob/fizyka-podrecznik/",
            "licencja": "CC BY-SA 4.0",
        },
        "moduly": [{"id": k, "nazwa": n, "kolor": c, "rozdzialy": ROZDZIALY[k]}
                   for k, n, c in MODULY],
        "wzory": {v["plik"].removesuffix(".png"): {"w": v["w"], "h": v["h"]}
                  for v in indeks.values()},
        "pytania": wyjscie,
    }

    cel = KATALOG / "android" / "app" / "src" / "main" / "assets" / "pytania.json"
    cel.parent.mkdir(parents=True, exist_ok=True)
    cel.write_text(json.dumps(dane, ensure_ascii=False, indent=1), encoding="utf-8")

    from collections import Counter
    print(f"\nZapisano {cel.relative_to(KATALOG)}")
    for k, _, _ in MODULY:
        n = sum(1 for p in wyjscie if p["modul"] == k)
        print(f"  {k:4s} {NAZWY[k][:40]:42s} {n:3d}")
    print(f"\n  Pytań: {len(wyjscie)}   Wzorów: {len(indeks)}")


if __name__ == "__main__":
    main()
