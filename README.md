# Fizyka — quiz na Androida

Aplikacja do powtórki przed egzaminem rocznym z fizyki. **Wzory składane w LaTeX-u**
i wyświetlane w treści pytań, wykresy i schematy rysowane programowo.
Działa w pełni offline.

**78 pytań** w 11 modułach, **304 wzorów** złożonych w LaTeX-u
i 11 ilustracji rysowanych programowo.

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

## Moduły

| | moduł | pytań | rozdziały podręcznika |
|---|---|---|---|
| M1 | Mechanika — kinematyka i dynamika | 10 | 1–6 (wiadomości wstępne, ruch, dynamika, grawitacja) |
| M2 | Praca, energia, pęd i zderzenia | 8 | 7–10 (praca i energia, zasady zachowania, zderzenia) |
| M3 | Ruch obrotowy i drgania | 8 | 11–12 (ruch obrotowy, ruch drgający) |
| M4 | Fale sprężyste i płyny | 8 | 13–14 (fale w ośrodkach sprężystych, płyny) |
| M5 | Termodynamika i teoria kinetyczna | 8 | 15–16 (kinetyczna teoria gazów i termodynamika) |
| M6 | Elektrostatyka | 6 | 17–20 (pole elektryczne, prawo Gaussa, potencjał, kondensatory) |
| M7 | Prąd i pole magnetyczne | 6 | 21–23 (prąd elektryczny, pole magnetyczne) |
| M8 | Indukcja i fale elektromagnetyczne | 6 | 24–27 (indukcja, drgania i fale elektromagnetyczne, równania Maxwella) |
| M9 | Optyka | 6 | 28–31 (optyka geometryczna i falowa, interferencja, dyfrakcja, polaryzacja) |
| M10 | Fizyka kwantowa | 6 | 32–35 (fizyka kwantowa, fale i cząstki, mechanika kwantowa) |
| M11 | Atomy, ciało stałe, jądro | 6 | 36–38 (atomy wieloelektronowe, materia skondensowana, fizyka jądrowa) |

## Jak to jest zrobione

**Wzory nie są obrazkami wklejonymi z podręcznika.** Każdy zapisany jest jako LaTeX
w pliku banku, np. `$E_k = \\tfrac{1}{2}mv^2$`. Skrypt `narzedzia/wzory.py` składa go
`pdflatex`-em i rasteryzuje `pdftocairo` do PNG z przezroczystym tłem w 420 dpi.
Nazwą pliku jest skrót SHA-1 treści wzoru, więc ten sam wzór składa się raz, a przy
ponownym uruchomieniu pomijane jest to, co już gotowe.

W aplikacji znaczniki `[[w_xxxx]]` podmieniane są na obrazki przez `ImageSpan`,
skalowane do wysokości wiersza tekstu. Dzięki temu wzór rośnie razem z ustawioną
w systemie wielkością czcionki i stoi na linii pisma, a nie obok tekstu.

**Ilustracje modułów** rysuje `narzedzia/grafiki.py` w matplotlibie — rzut ukośny, zderzenie,
drgania tłumione, fala stojąca, izotermy, pole dipola, pole wokół przewodnika, fala
elektromagnetyczna, soczewka, poziomy energetyczne i krzywa rozpadu. Każda w kolorze
swojego modułu.

## Budowanie

```bash
./zbuduj.sh        # wzory → grafiki → JSON → APK, jedną komendą
```

Wymaga Pythona z matplotlibem, `pdflatex` i `pdftocairo` oraz Android SDK z JDK 21.

## Aplikacja

| | |
|---|---|
| `minSdk` | **24** — działa od Androida 7 |
| zależności | tylko `androidx.appcompat` |
| uprawnienia | brak, działa bez internetu |
| rozmiar | ok. 5,4 MB (w tym 304 obrazków wzorów) |

Trzy tryby: **nauka** z wyjaśnieniem i odsyłaczem do rozdziału podręcznika,
**egzamin próbny** z wynikiem na końcu, **powtórka błędów**. W menu paski skuteczności
dla każdego modułu, żeby było widać, gdzie są braki.
