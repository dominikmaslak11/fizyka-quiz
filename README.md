# Fizyka — quiz na Androida

Aplikacja do powtórki przed egzaminem rocznym z fizyki. **Wzory składane w LaTeX-u**
i wyświetlane w treści pytań, wykresy i schematy rysowane programowo.
Działa w pełni offline.

**725 pytań** w 11 modułach, **304 wzorów** złożonych w LaTeX-u
i 11 ilustracji rysowanych programowo. Do tego **wyciąg z całego podręcznika**:
**310 wzorów kluczowych**, **52 definicji**,
**82 praw i twierdzeń** oraz **101 zadań** z testów kończących moduły.

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

## Skąd bierze się 725 pytań

| źródło | ile | jak powstaje |
|---|---|---|
| pisane ręcznie | 78 | wzory w LaTeX-u, wyjaśnienie i odsyłacz do rozdziału |
| definicja → pojęcie | 29 | treść definicji z podręcznika, dystraktory to inne pojęcia z tego samego modułu |
| pojęcie → definicja | 29 | odwrotność powyższego |
| treść prawa → nazwa | 19 | „Które prawo brzmi…", nazwa brana z tytułu nad blokiem |
| wzór → zagadnienie | 310 | obrazek wzoru, odpowiedzi to rozdziały |
| **zagadnienie → wzór** | **260** | odpowiedziami są **obrazki wzorów** — najmocniejsze ćwiczenie, bo wymaga rozpoznania wzoru wśród czterech z tego samego modułu |

**Pytania generowane nie są zmyślane.** Generator tylko przestawia materiał wyjęty z książki
w pytania zamknięte i dobiera dystraktory z tego samego modułu, żeby nie dało się zgadnąć.
Pytanie powstaje wyłącznie wtedy, gdy uda się wyłuskać czystą nazwę i znaleźć trzy różne
dystraktory — reszta jest pomijana.

## Komentarze do wzorów

Dotknięcie wzoru na liście rozwija kartę z trzema sekcjami: **czego dotyczy**,
**kiedy go używać** i **przykład** z konkretnymi liczbami.

Komentarze są kluczowane **numerem rozdziału**, a nie nazwą pliku obrazka — nazwy plików
zależą od numeru strony i kolejności wycinania, więc zmieniałyby się przy każdej zmianie
filtra. Jeden wpis w `bank/komentarze.py` obsługuje wszystkie wzory z danego rozdziału.

**Pokrycie: 310 z 310 wzorów**, 156 wpisów komentarza.

Wzory z podsumowań i materiałów dodatkowych dostają własne etykiety zamiast numeru rozdziału.
Tamte strony nie mają numerowanych nagłówków, więc bez tego dziedziczyłyby ostatni nagłówek
zwykłego rozdziału i były opisane myląco — dwanaście wzorów z podsumowania modułu XI
trafiało w ten sposób pod „38.4.3 Źródła energii gwiazd".

## Wyciąg z podręcznika

Oprócz pytań pisanych ręcznie aplikacja zawiera materiał wyciągnięty z podręcznika
programowo przez `narzedzia/wyciag_pdf.py`:

| co | ile | jak wyciągane |
|---|---|---|
| **wzory kluczowe** | 310 | autor wyróżnia najważniejsze wzory **czystym żółtym tłem** (255,255,0). Skrypt renderuje każdą stronę, znajduje żółte obszary i wycina je jako osobne obrazki |
| **definicje** | 52 | bloki zaczynające się słowem „Definicja" i ciągnące się wcięciem |
| **prawa i twierdzenia** | 82 | bloki „Prawo, zasada, twierdzenie" |
| **zadania** | 101 | testy kończące każdy moduł |

Przynależność do modułu ustalana jest z **żywej paginy** („Moduł VII – …"), a nie z numeru
strony, bo numeracja drukowana rozjeżdża się z numeracją PDF.

⚠ **Filtr na wycinkach.** Sama detekcja żółtego wyłapuje też ikonki i tła ramek, więc wycinki
przechodzą przez filtr odrzucający zbyt małe, pozbawione ciemnego tekstu oraz zawierające
kolory inne niż żółty i czarny. Z 441 surowych wycinków zostaje 310 prawdziwych wzorów.

⚠ **Zadania z testów są otwarte i podręcznik nie podaje do nich rozwiązań.** W aplikacji są
więc treściami do samodzielnego przeliczenia, a nie pytaniami zamkniętymi. Aplikacja mówi
o tym wprost na ekranie zadań.

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
