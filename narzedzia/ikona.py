#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rysuje ikone aplikacji: rzut ukosny na tle formuly.

Motyw dobrany pod to, czym aplikacja jest naprawde — nauka wzorow z fizyki:
parabola rzutu (mechanika, pierwszy modul) i znak calki (matematyczny jezyk
calego podrecznika), na granatowym tle zgodnym z kolorem aplikacji.
"""
import pathlib, math
from PIL import Image, ImageDraw, ImageFont

KATALOG = pathlib.Path(__file__).resolve().parent.parent
RES = KATALOG / "android" / "app" / "src" / "main" / "res"

GESTOSCI = {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}

TLO_1 = (26, 54, 93)       # granat aplikacji
TLO_2 = (43, 108, 176)     # jasniejszy granat na gradient
AKCENT = (255, 209, 102)   # cieply zolty — nawiazanie do wyroznien w podreczniku
BIALY = (255, 255, 255)


def rysuj(rozmiar):
    S = rozmiar * 8            # rysujemy w powiekszeniu i zmniejszamy — gladkie krawedzie
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)

    # tlo: zaokraglony kwadrat z pionowym gradientem
    maska = Image.new("L", (S, S), 0)
    ImageDraw.Draw(maska).rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * 0.22), fill=255)
    grad = Image.new("RGBA", (S, S))
    gd = ImageDraw.Draw(grad)
    for y in range(S):
        t = y / S
        gd.line([(0, y), (S, y)], fill=(
            int(TLO_1[0] + (TLO_2[0] - TLO_1[0]) * t),
            int(TLO_1[1] + (TLO_2[1] - TLO_1[1]) * t),
            int(TLO_1[2] + (TLO_2[2] - TLO_1[2]) * t), 255))
    im.paste(grad, (0, 0), maska)

    # tor rzutu ukosnego
    punkty = []
    for i in range(101):
        t = i / 100
        x = 0.14 + t * 0.74
        y = 0.70 - (2.15 * t * (1 - t)) * 0.62
        punkty.append((x * S, y * S))
    d.line(punkty, fill=AKCENT, width=int(S * 0.045), joint="curve")

    # os pozioma
    d.line([(0.10 * S, 0.70 * S), (0.90 * S, 0.70 * S)],
           fill=(255, 255, 255, 120), width=int(S * 0.018))

    # cialo w locie — na szczycie toru
    r = S * 0.062
    cx, cy = punkty[50]
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BIALY)

    # wektor predkosci poczatkowej
    x0, y0 = punkty[0]
    d.line([(x0, y0), (x0 + 0.17 * S, y0 - 0.17 * S)], fill=BIALY, width=int(S * 0.030))
    d.polygon([(x0 + 0.20 * S, y0 - 0.20 * S),
               (x0 + 0.115 * S, y0 - 0.175 * S),
               (x0 + 0.175 * S, y0 - 0.115 * S)], fill=BIALY)

    return im.resize((rozmiar, rozmiar), Image.LANCZOS)


def main():
    for nazwa, px in GESTOSCI.items():
        kat = RES / f"mipmap-{nazwa}"
        kat.mkdir(parents=True, exist_ok=True)
        ikona = rysuj(px)
        ikona.save(kat / "ic_launcher.png")
        ikona.save(kat / "ic_launcher_round.png")
        print(f"  + mipmap-{nazwa}/ic_launcher.png  {px}x{px}")
    # duzy podglad do obejrzenia
    rysuj(512).save(KATALOG / "ikona-podglad.png")
    print(f"\n  podgląd: ikona-podglad.png (512x512)")


if __name__ == "__main__":
    main()
