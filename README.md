# Fizyka — quiz na Androida

Aplikacja do powtórki przed egzaminem rocznym z fizyki. **Wzory składane w LaTeX-u**
i wyświetlane w treści pytań, wykresy i schematy rysowane programowo.
Działa w pełni offline.

> **Projekt w budowie.** Repozytorium założone 16.09.2026.

## Źródło materiału

Pytania powstają na podstawie podręcznika:

> **Zbigniew Kąkol, „Fizyka dla inżynierów"**, Wydział Fizyki i Informatyki Stosowanej,
> Akademia Górniczo-Hutnicza w Krakowie, Kraków 2023.
> https://zasoby.open.agh.edu.pl/zasob/fizyka-podrecznik/

Podręcznik udostępniony jest na licencji **Creative Commons Uznanie autorstwa —
Na tych samych warunkach 4.0 (CC BY-SA 4.0)**, która pozwala na adaptację pod warunkiem
zachowania atrybucji i tej samej licencji dla utworów pochodnych.

## Licencje — dwie, i to nie jest przeoczenie

| co | licencja | dlaczego |
|---|---|---|
| **treść pytań** (`bank/`) | **CC BY-SA 4.0** | utwór pochodny podręcznika — licencja musi być ta sama |
| **kod** (`narzedzia/`, `android/`) | **MIT** | napisany od zera, nie jest pochodną podręcznika |

## Stan prac

- [x] silnik składu wzorów LaTeX → PNG z przezroczystym tłem
- [ ] bank pytań
- [ ] generator wykresów i schematów
- [ ] aplikacja na Androida
