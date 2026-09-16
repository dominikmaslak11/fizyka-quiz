#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sklada wzory LaTeX-owe do plikow PNG z przezroczystym tlem.

Kazdy unikalny wzor dostaje nazwe z skrotu SHA-1, wiec ten sam wzor sklada sie raz,
a ponowne uruchomienie pomija to, co juz jest.

Obok obrazka zapisywana jest jego wysokosc nad linia pisma (depth), zeby aplikacja
mogla wyrownac wzor do tekstu zamiast stawiac go na sztywno.
"""
import hashlib, json, pathlib, subprocess, tempfile, shutil, sys

KATALOG = pathlib.Path(__file__).resolve().parent.parent
WYJSCIE = KATALOG / "android" / "app" / "src" / "main" / "assets" / "wzory"
INDEKS = KATALOG / "bank" / "wzory-indeks.json"

DPI = 420          # wysokie, zeby wzor byl ostry na ekranie telefonu
KOLOR = "1C2530"   # ten sam kolor co tekst w aplikacji

SZABLON = r"""\documentclass[preview,border=1pt,12pt]{standalone}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{xcolor}
\usepackage[T1]{fontenc}
\begin{document}
\color[HTML]{%(kolor)s}$\displaystyle %(wzor)s$
\end{document}
"""


def nazwa(wzor: str) -> str:
    return "w_" + hashlib.sha1(wzor.encode("utf-8")).hexdigest()[:16]


def zloz(wzor: str, cel: pathlib.Path) -> bool:
    """Sklada pojedynczy wzor. Zwraca True przy powodzeniu."""
    with tempfile.TemporaryDirectory() as tmp:
        t = pathlib.Path(tmp)
        (t / "w.tex").write_text(SZABLON % {"wzor": wzor, "kolor": KOLOR}, encoding="utf-8")
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "w.tex"],
                           cwd=t, capture_output=True)
        if not (t / "w.pdf").exists():
            log = (t / "w.log").read_text(encoding="utf-8", errors="replace") if (t / "w.log").exists() else ""
            blad = [l for l in log.splitlines() if l.startswith("!")]
            print(f"  BLAD skladu: {wzor[:60]}")
            for l in blad[:3]:
                print(f"     {l}")
            return False
        # pdftocairo, nie pdftoppm — tylko on obsluguje -transp w tej wersji poppler
        subprocess.run(["pdftocairo", "-png", "-r", str(DPI), "-transp", "-singlefile",
                        "w.pdf", "w"], cwd=t, capture_output=True)
        png = t / "w.png"
        if not png.exists():
            print(f"  BLAD rasteryzacji: {wzor[:60]}")
            return False
        cel.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(png, cel)
        return True


def zloz_wszystkie(wzory, verbose=True):
    """wzory: iterowalne z napisami LaTeX. Zwraca slownik {wzor: {plik, w, h}}."""
    from PIL import Image
    WYJSCIE.mkdir(parents=True, exist_ok=True)
    indeks = {}
    if INDEKS.exists():
        indeks = json.loads(INDEKS.read_text(encoding="utf-8"))

    nowe = 0
    for w in sorted(set(wzory)):
        n = nazwa(w)
        plik = WYJSCIE / f"{n}.png"
        if w in indeks and plik.exists():
            continue
        if not zloz(w, plik):
            continue
        with Image.open(plik) as im:
            szer, wys = im.size
        indeks[w] = {"plik": f"{n}.png", "w": szer, "h": wys}
        nowe += 1
        if verbose:
            print(f"  + {n}.png  {szer}x{wys}  {w[:52]}")

    # posprzataj obrazki wzorow, ktorych juz nie ma w banku
    uzywane = {indeks[w]["plik"] for w in indeks if w in set(wzory)}
    indeks = {w: v for w, v in indeks.items() if w in set(wzory)}
    for p in WYJSCIE.glob("w_*.png"):
        if p.name not in uzywane:
            p.unlink()

    INDEKS.parent.mkdir(parents=True, exist_ok=True)
    INDEKS.write_text(json.dumps(indeks, ensure_ascii=False, indent=1), encoding="utf-8")
    if verbose:
        print(f"\n  Wzorów w indeksie: {len(indeks)} (nowych: {nowe})")
    return indeks


if __name__ == "__main__":
    probki = [r"F = ma", r"E_k = \tfrac{1}{2}mv^2", r"\oint \vec{E}\cdot d\vec{A} = \frac{Q}{\varepsilon_0}",
              r"\Delta x \,\Delta p \geq \frac{\hbar}{2}", r"\nabla \times \vec{B} = \mu_0\vec{J} + \mu_0\varepsilon_0\frac{\partial \vec{E}}{\partial t}"]
    zloz_wszystkie(probki)
