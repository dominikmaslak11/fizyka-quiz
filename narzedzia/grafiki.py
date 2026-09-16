#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rysuje ilustracje modulow — po jednym charakterystycznym wykresie na modul.

Kazda grafika to mala plansza w kolorze modulu, uzywana jako naglowek ekranu
pytania. Rysowane programowo, wiec nie ma pytania o prawa do obrazkow.
"""
import pathlib, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

KATALOG = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KATALOG / "narzedzia"))
from dzialy import MODULY, KOLORY  # noqa: E402

WYJSCIE = KATALOG / "android" / "app" / "src" / "main" / "assets" / "grafiki"
SZER, WYS, DPI = 4.0, 1.5, 160


def plansza(kolor):
    fig, ax = plt.subplots(figsize=(SZER, WYS), dpi=DPI)
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])
    return fig, ax


def m1(ax, k):   # rzut ukosny
    t = np.linspace(0, 1, 200)
    for v, a in [(1.0, 0.35), (1.0, 0.55), (1.0, 0.75)]:
        x = v * np.cos(a) * t * 2.6
        y = v * np.sin(a) * t * 2.6 - 3.1 * t**2
        m = y >= 0
        ax.plot(x[m], y[m], color=k, lw=2, alpha=0.85)
    ax.axhline(0, color=k, lw=1.4, alpha=0.5)
    ax.set_xlim(-0.05, 2.3); ax.set_ylim(-0.05, 0.75)

def m2(ax, k):   # zderzenie i wymiana pedu
    ax.arrow(0.1, 0.5, 0.28, 0, head_width=0.09, head_length=0.07, fc=k, ec=k, lw=2)
    ax.add_patch(plt.Circle((0.52, 0.5), 0.1, color=k, alpha=0.85))
    ax.add_patch(plt.Circle((0.78, 0.5), 0.1, color=k, alpha=0.35))
    ax.arrow(0.92, 0.5, 0.22, 0, head_width=0.09, head_length=0.07, fc=k, ec=k, lw=2, alpha=0.5)
    ax.set_xlim(0, 1.3); ax.set_ylim(0.1, 0.9)

def m3(ax, k):   # drgania tlumione
    t = np.linspace(0, 4 * np.pi, 400)
    y = np.exp(-t / 7) * np.sin(t * 1.6)
    ax.plot(t, y, color=k, lw=2)
    ax.plot(t, np.exp(-t / 7), color=k, lw=1, ls="--", alpha=0.5)
    ax.plot(t, -np.exp(-t / 7), color=k, lw=1, ls="--", alpha=0.5)
    ax.axhline(0, color=k, lw=0.8, alpha=0.4)

def m4(ax, k):   # fala stojaca
    x = np.linspace(0, 2 * np.pi, 300)
    for a in (1, -1):
        ax.plot(x, a * np.sin(x * 1.5), color=k, lw=2, alpha=0.85 if a > 0 else 0.4)
    ax.axhline(0, color=k, lw=0.8, alpha=0.4)
    for w in np.arange(0, 2.1, 2 / 3) * np.pi:
        ax.plot([w], [0], "o", color=k, ms=5)

def m5(ax, k):   # izotermy pV
    V = np.linspace(0.25, 1.4, 200)
    for T in (0.35, 0.55, 0.8):
        ax.plot(V, T / V, color=k, lw=2, alpha=0.5 + 0.2 * (T / 0.8))
    ax.set_xlim(0.2, 1.45); ax.set_ylim(0, 2.6)
    ax.set_xlabel("V", color=k, fontsize=9); ax.set_ylabel("p", color=k, fontsize=9)

def m6(ax, k):   # dipol — linie pola
    ax.plot([-0.5], [0], "o", color=k, ms=11)
    ax.plot([0.5], [0], "o", color=k, ms=11, alpha=0.4)
    for h in (0.12, 0.34, 0.62, 1.0):
        t = np.linspace(0, np.pi, 160)
        ax.plot(np.cos(t) * 0.5 * (1 + h), np.sin(t) * h * 0.72, color=k, lw=1.4, alpha=0.7)
        ax.plot(np.cos(t) * 0.5 * (1 + h), -np.sin(t) * h * 0.72, color=k, lw=1.4, alpha=0.7)
    ax.set_xlim(-1.35, 1.35); ax.set_ylim(-0.85, 0.85)

def m7(ax, k):   # przewodnik i pole magnetyczne
    ax.plot([0.5, 0.5], [0.05, 0.95], color=k, lw=3)
    for r in (0.12, 0.22, 0.33):
        t = np.linspace(0, 2 * np.pi, 200)
        ax.plot(0.5 + r * np.cos(t), 0.5 + r * np.sin(t) * 0.42, color=k, lw=1.4, alpha=0.75)
    ax.arrow(0.5, 0.82, 0, 0.1, head_width=0.035, head_length=0.05, fc=k, ec=k)
    ax.set_xlim(0.05, 0.95); ax.set_ylim(0, 1)

def m8(ax, k):   # fala elektromagnetyczna
    x = np.linspace(0, 4 * np.pi, 300)
    ax.plot(x, np.sin(x), color=k, lw=2)
    ax.plot(x, 0.45 * np.sin(x), color=k, lw=2, alpha=0.4, ls="--")
    ax.axhline(0, color=k, lw=0.8, alpha=0.4)

def m9(ax, k):   # soczewka skupiajaca
    t = np.linspace(-1, 1, 100)
    ax.plot(0.1 * (1 - t**2), t, color=k, lw=2)
    ax.plot(-0.1 * (1 - t**2), t, color=k, lw=2)
    for y in (-0.62, -0.3, 0.3, 0.62):
        ax.plot([-1.3, 0], [y, y], color=k, lw=1.2, alpha=0.75)
        ax.plot([0, 1.25], [y, 0], color=k, lw=1.2, alpha=0.75)
    ax.plot([1.25], [0], "o", color=k, ms=5)
    ax.axhline(0, color=k, lw=0.8, alpha=0.35)
    ax.set_xlim(-1.35, 1.4); ax.set_ylim(-0.95, 0.95)

def m10(ax, k):  # skwantowane poziomy energetyczne
    for n in range(1, 5):
        E = -1.0 / n**2
        ax.plot([0.15, 0.85], [E, E], color=k, lw=2.2, alpha=0.5 + 0.12 * n)
    ax.annotate("", xy=(0.5, -1 / 4), xytext=(0.5, -1.0),
                arrowprops=dict(arrowstyle="->", color=k, lw=1.8))
    ax.set_xlim(0, 1); ax.set_ylim(-1.15, 0.12)

def m11(ax, k):  # rozpad promieniotworczy
    t = np.linspace(0, 4, 200)
    ax.plot(t, np.exp(-t * 0.9), color=k, lw=2.2)
    for i in (1, 2, 3):
        x = i * 0.77
        ax.plot([x, x], [0, np.exp(-x * 0.9)], color=k, lw=1, ls=":", alpha=0.7)
    ax.set_xlim(0, 4); ax.set_ylim(0, 1.08)
    ax.set_xlabel("t", color=k, fontsize=9); ax.set_ylabel("N", color=k, fontsize=9)


RYSUNKI = {"M1": m1, "M2": m2, "M3": m3, "M4": m4, "M5": m5, "M6": m6,
           "M7": m7, "M8": m8, "M9": m9, "M10": m10, "M11": m11}


def main():
    WYJSCIE.mkdir(parents=True, exist_ok=True)
    for kod, nazwa, kolor in MODULY:
        fig, ax = plansza(kolor)
        RYSUNKI[kod](ax, kolor)
        if ax.get_xlabel():
            ax.tick_params(colors=kolor, labelsize=7)
        plik = WYJSCIE / f"{kod.lower()}.png"
        fig.savefig(plik, transparent=True, bbox_inches="tight", pad_inches=0.06)
        plt.close(fig)
        print(f"  + {plik.name:10s} {nazwa}")
    print(f"\n  {len(MODULY)} grafik w {WYJSCIE.relative_to(KATALOG)}")


if __name__ == "__main__":
    main()
