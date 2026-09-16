# -*- coding: utf-8 -*-
"""Podzial materialu — zgodny z modulami podrecznika Kakola."""

MODULY = [
    ("M1",  "Mechanika — kinematyka i dynamika",   "#1F6FB2"),
    ("M2",  "Praca, energia, pęd i zderzenia",     "#2E8B57"),
    ("M3",  "Ruch obrotowy i drgania",             "#8B5A2B"),
    ("M4",  "Fale sprężyste i płyny",              "#0E7C7B"),
    ("M5",  "Termodynamika i teoria kinetyczna",   "#C05621"),
    ("M6",  "Elektrostatyka",                      "#6B46C1"),
    ("M7",  "Prąd i pole magnetyczne",             "#B7791F"),
    ("M8",  "Indukcja i fale elektromagnetyczne",  "#2C7A7B"),
    ("M9",  "Optyka",                              "#B83280"),
    ("M10", "Fizyka kwantowa",                     "#2B6CB0"),
    ("M11", "Atomy, ciało stałe, jądro",           "#4A5568"),
]

# Rozdzialy podrecznika przypisane do modulow — do wskazywania zrodla w wyjasnieniu.
ROZDZIALY = {
    "M1":  "1–6 (wiadomości wstępne, ruch, dynamika, grawitacja)",
    "M2":  "7–10 (praca i energia, zasady zachowania, zderzenia)",
    "M3":  "11–12 (ruch obrotowy, ruch drgający)",
    "M4":  "13–14 (fale w ośrodkach sprężystych, płyny)",
    "M5":  "15–16 (kinetyczna teoria gazów i termodynamika)",
    "M6":  "17–20 (pole elektryczne, prawo Gaussa, potencjał, kondensatory)",
    "M7":  "21–23 (prąd elektryczny, pole magnetyczne)",
    "M8":  "24–27 (indukcja, drgania i fale elektromagnetyczne, równania Maxwella)",
    "M9":  "28–31 (optyka geometryczna i falowa, interferencja, dyfrakcja, polaryzacja)",
    "M10": "32–35 (fizyka kwantowa, fale i cząstki, mechanika kwantowa)",
    "M11": "36–38 (atomy wieloelektronowe, materia skondensowana, fizyka jądrowa)",
}

NAZWY = dict((k, n) for k, n, _ in MODULY)
KOLORY = dict((k, c) for k, _, c in MODULY)
