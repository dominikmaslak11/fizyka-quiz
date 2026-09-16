#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wyciaga z podrecznika Kakola material zrodlowy do aplikacji.

Co wyciaga:
  1. WZORY KLUCZOWE — fragmenty wyroznione przez autora czystym zoltym tlem (255,255,0).
     Kazdy zapisywany jako przyciety PNG. To sa wzory, ktore autor uznal za najwazniejsze.
  2. DEFINICJE — bloki zaczynajace sie od wciecia i slowa "Definicja".
  3. PRAWA, ZASADY, TWIERDZENIA — bloki "Prawo, zasada, twierdzenie".
  4. ZADANIA z testow konczacych kazdy modul.

Przynaleznosc do modulu ustalamy z zywej paginy ("Moduł I – ..."), a nie z numeru strony,
bo numeracja drukowana rozjezdza sie z numeracja PDF.

Podrecznik na licencji CC BY-SA 4.0 — wyciag jest utworem pochodnym na tej samej licencji.
"""
import json, pathlib, re, subprocess, sys, tempfile

KATALOG = pathlib.Path(__file__).resolve().parent.parent
PDF = pathlib.Path.home() / "Pobrane" / "Fizyka_2023.pdf"
WYJ_WZORY = KATALOG / "android" / "app" / "src" / "main" / "assets" / "kluczowe"
WYJ_DANE = KATALOG / "bank" / "wyciag.json"

DPI = 150
RZYMSKIE = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"]
MODUL_Z_RZYMSKIEGO = {r: f"M{i+1}" for i, r in enumerate(RZYMSKIE)}

NAGLOWEK = re.compile(r"Moduł\s+([IVX]+)\s*[–-]")


def tekst_stron():
    """Zwraca liste tekstow stron (indeks 0 = strona 1)."""
    out = subprocess.run(["pdftotext", "-layout", str(PDF), "-"],
                         capture_output=True, text=True).stdout
    return out.split("\f")


def modul_stron(strony):
    """Mapa numer_strony -> kod modulu, na podstawie zywej paginy."""
    mapa, ostatni = {}, None
    for i, t in enumerate(strony, start=1):
        m = NAGLOWEK.search(t)
        if m and m.group(1) in MODUL_Z_RZYMSKIEGO:
            ostatni = MODUL_Z_RZYMSKIEGO[m.group(1)]
        mapa[i] = ostatni
    return mapa


def wytnij_zolte(strona_nr, tmp):
    """Renderuje strone i zwraca liste przycietych obrazkow wyroznionych fragmentow."""
    from PIL import Image
    import numpy as np

    baza = tmp / f"s{strona_nr}"
    subprocess.run(["pdftoppm", "-png", "-r", str(DPI), "-f", str(strona_nr),
                    "-l", str(strona_nr), "-singlefile", str(PDF), str(baza)],
                   capture_output=True)
    plik = baza.with_suffix(".png")
    if not plik.exists():
        return []

    im = Image.open(plik).convert("RGB")
    a = np.array(im)
    maska = (a[:, :, 0] > 245) & (a[:, :, 1] > 245) & (a[:, :, 2] < 80)
    if maska.sum() < 400:          # pomijamy pojedyncze zolte piksele z rysunkow
        return []

    ys = np.where(maska.any(axis=1))[0]
    wycinki, start, prev = [], ys[0], ys[0]
    for y in ys[1:]:
        if y - prev > 12:          # przerwa pionowa = osobne wyroznienie
            wycinki.append((start, prev)); start = y
        prev = y
    wycinki.append((start, prev))

    obrazki = []
    for (y1, y2) in wycinki:
        if y2 - y1 < 14:           # zbyt cienki pasek to najczesciej artefakt
            continue
        pas = maska[y1:y2 + 1]
        xs = np.where(pas.any(axis=0))[0]
        if len(xs) == 0:
            continue
        m = 6
        obrazki.append((im.crop((max(0, xs.min() - m), max(0, y1 - m),
                                 min(im.width, xs.max() + m + 1),
                                 min(im.height, y2 + m + 1))), int(y1)))
    return obrazki


def zdaniowa(linia):
    """Czy linia to zdanie, a nie urwany wzor. Wzory maja malo liter i duzo symboli."""
    l = linia.strip()
    if len(l) < 12:
        return False
    litery = sum(c.isalpha() or c.isspace() for c in l)
    if litery < len(l) * 0.80:
        return False
    return len(l.split()) >= 3


def bloki(strony, etykieta):
    """Bloki tekstu zaczynajace sie linia [etykieta] i ciagnace sie wcieciem.

    Zapisujemy tez ostatnia sensowna linie PRZED blokiem — to zwykle tytul
    ("Sformulowanie drugiej zasady dynamiki Newtona:"), z ktorego bierze sie nazwa.
    """
    wynik = []
    for nr, t in enumerate(strony, start=1):
        linie = t.splitlines()
        for i, l in enumerate(linie):
            if l.strip() != etykieta:
                continue

            kontekst = ""
            for wstecz in range(i - 1, max(-1, i - 7), -1):
                k = linie[wstecz].strip()
                if not k or NAGLOWEK.search(k) or re.fullmatch(r"\d{1,3}", k):
                    continue
                kontekst = k
                break

            tresc = []
            for nast in linie[i + 1:]:
                if not nast.strip():
                    if tresc:
                        break
                    continue
                if len(nast) - len(nast.lstrip()) < 4:
                    break
                if zdaniowa(nast):
                    tresc.append(nast.strip())
            if tresc:
                wynik.append({"strona": nr, "kontekst": kontekst, "tresc": " ".join(tresc)})
    return wynik


def zadania_testow(strony):
    """Zbiera tresci zadan z testow konczacych moduly."""
    wynik = []
    for nr, t in enumerate(strony, start=1):
        if not re.search(r"Moduł\s+[IVX]+\s*[–-]\s*Test", t) and not re.match(r"\s*Test\s+[IVX]+\s*$", t.strip().split("\n")[0] if t.strip() else ""):
            continue
        for m in re.finditer(r"^\s*(\d{1,2})\.\s+(.+?)(?=^\s*\d{1,2}\.\s|\Z)", t, re.S | re.M):
            tresc = " ".join(m.group(2).split())
            tresc = re.sub(r"\s*\d{1,3}\s*$", "", tresc)     # urwany numer strony
            if len(tresc) > 40:
                wynik.append({"strona": nr, "nr": int(m.group(1)), "tresc": tresc})
    return wynik


def main():
    if not PDF.exists():
        sys.exit(f"Brak pliku {PDF}")
    print("Czytam tekst stron…")
    strony = tekst_stron()
    print(f"  stron: {len(strony)}")
    mapa = modul_stron(strony)

    print("Szukam definicji i praw…")
    defs = bloki(strony, "Definicja")
    prawa = bloki(strony, "Prawo, zasada, twierdzenie")
    zadania = zadania_testow(strony)
    for lista in (defs, prawa, zadania):
        for x in lista:
            x["modul"] = mapa.get(x["strona"])

    print(f"  definicji: {len(defs)}   praw i twierdzeń: {len(prawa)}   zadań z testów: {len(zadania)}")

    if "--tylko-tekst" in sys.argv:
        stare = json.loads(WYJ_DANE.read_text(encoding="utf-8")) if WYJ_DANE.exists() else {}
        WYJ_DANE.write_text(json.dumps(
            {"definicje": defs, "prawa": prawa, "zadania": zadania,
             "kluczowe": stare.get("kluczowe", [])}, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"\nTryb tylko-tekst: zapisano {WYJ_DANE.relative_to(KATALOG)}, wzory bez zmian.")
        return

    print("Wycinam wzory wyróżnione na żółto (to potrwa)…")
    WYJ_WZORY.mkdir(parents=True, exist_ok=True)
    for p in WYJ_WZORY.glob("k_*.png"):
        p.unlink()

    kluczowe = []
    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td)
        for nr in range(1, len(strony) + 1):
            for j, (im, y) in enumerate(wytnij_zolte(nr, tmp)):
                nazwa = f"k_{nr:03d}_{j}"
                im.save(WYJ_WZORY / f"{nazwa}.png")
                # y potrzebne, zeby przypisac wzorowi naglowek rozdzialu stojacy NAD nim,
                # a nie ostatni naglowek na stronie
                kluczowe.append({"plik": nazwa, "strona": nr, "y": y,
                                 "modul": mapa.get(nr), "w": im.width, "h": im.height})
            if nr % 50 == 0:
                print(f"    strona {nr}/{len(strony)} — wzorów do tej pory: {len(kluczowe)}")

    print(f"  wzorów kluczowych: {len(kluczowe)}")

    WYJ_DANE.parent.mkdir(parents=True, exist_ok=True)
    WYJ_DANE.write_text(json.dumps(
        {"definicje": defs, "prawa": prawa, "zadania": zadania, "kluczowe": kluczowe},
        ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nZapisano {WYJ_DANE.relative_to(KATALOG)}")


if __name__ == "__main__":
    main()
