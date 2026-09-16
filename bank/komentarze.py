# -*- coding: utf-8 -*-
"""Komentarze do wzorow, kluczowane NUMEREM ROZDZIALU podrecznika.

Dlaczego po rozdziale, a nie po pliku obrazka: nazwy plikow (k_020_3) zaleza
od numeru strony i kolejnosci wycinania, wiec zmienilyby sie przy kazdej zmianie
filtra. Numer rozdzialu jest stabilny — komentarz trafia do wszystkich wzorow
z danego rozdzialu.

Pola:
  czego   — czego wzór dotyczy, jednym zdaniem
  kiedy   — kiedy i gdzie się go używa, na co uważać
  przyklad— konkretny rachunek z liczbami
"""

K = {
 "1.2.3": dict(
  czego="Iloczyn skalarny dwóch wektorów — daje liczbę, nie wektor.",
  kiedy="Wszędzie tam, gdzie liczy się tylko składowa jednego wektora wzdłuż drugiego: praca siły, strumień pola, rzut wektora na kierunek. Gdy wektory są prostopadłe, iloczyn wynosi zero.",
  przyklad="Siła 10 N ciągnie skrzynię pod kątem 60° do kierunku ruchu na drodze 5 m. Praca: W = 10·5·cos60° = 25 J, a nie 50 J."),

 "1.2.4": dict(
  czego="Iloczyn wektorowy — wynikiem jest wektor prostopadły do obu mnożonych.",
  kiedy="Moment siły, moment pędu, siła Lorentza. Kierunek wyznacza reguła prawej dłoni. Dla wektorów równoległych wynik jest zerowy.",
  przyklad="Klucz o ramieniu 0,3 m, siła 40 N prostopadle: M = 0,3·40·sin90° = 12 N·m. Ta sama siła wzdłuż klucza daje moment zero."),

 "2.2.3": dict(
  czego="Prędkość średnia — całkowita droga podzielona przez całkowity czas.",
  kiedy="Gdy ruch jest nierównomierny. Uwaga: prędkość średnia to NIE średnia arytmetyczna prędkości, jeśli odcinki trwały różnie długo.",
  przyklad="100 km z prędkością 100 km/h i 100 km z 50 km/h. Czas 1 h + 2 h = 3 h, więc v_śr = 200/3 ≈ 66,7 km/h, a nie 75 km/h."),

 "2.3.3": dict(
  czego="Położenie i prędkość w ruchu jednostajnie zmiennym.",
  kiedy="Spadek swobodny, hamowanie, rozpędzanie ze stałym przyspieszeniem. Warunek: a = const. Przy hamowaniu podstawiamy a ujemne.",
  przyklad="Samochód hamuje z 20 m/s z opóźnieniem 5 m/s². Droga: v²=v₀²+2as → 0 = 400 − 2·5·s → s = 40 m."),

 "3.2": dict(
  czego="Rzut ukośny — tor jest parabolą, ruch rozkłada się na dwa niezależne.",
  kiedy="Poziomo ruch jednostajny, pionowo jednostajnie zmienny z przyspieszeniem g. Zasięg maksymalny przy 45°, a kąty dopełniające dają ten sam zasięg.",
  przyklad="v₀ = 20 m/s, α = 30°. Zasięg z = v₀²sin2α/g = 400·sin60°/10 ≈ 34,6 m."),

 "3.3": dict(
  czego="Ruch jednostajny po okręgu i przyspieszenie dośrodkowe.",
  kiedy="Zawsze, gdy tor jest zakrzywiony: zakręt, wirówka, satelita. Przyspieszenie dośrodkowe zmienia kierunek prędkości, nie jej wartość.",
  przyklad="Auto 72 km/h = 20 m/s na zakręcie o R = 50 m: a = v²/R = 400/50 = 8 m/s². To musi zapewnić tarcie."),

 "4.2": dict(
  czego="Zasady dynamiki Newtona.",
  kiedy="Podstawa całej mechaniki. Druga zasada w postaci F = dp/dt działa też przy zmiennej masie (rakieta), a F = ma tylko przy stałej.",
  przyklad="Winda rusza w górę z a = 2 m/s², człowiek 70 kg. Nacisk na podłogę: N = m(g+a) = 70·12 = 840 N zamiast 700 N."),

 "5.1.1": dict(
  czego="Siła tarcia — statycznego i kinetycznego.",
  kiedy="Zależy od siły nacisku, nie od pola styku. Tarcie statyczne ma wartość maksymalną; poniżej niej dopasowuje się do siły zewnętrznej.",
  przyklad="Skrzynia 50 kg, μ = 0,3. Siła potrzebna do ruszenia: T = 0,3·50·10 = 150 N."),

 "6": dict(
  czego="Prawo powszechnego ciążenia.",
  kiedy="Ruch planet, satelity, ciężar na innej wysokości. Siła maleje z kwadratem odległości — dwa razy dalej to cztery razy słabiej.",
  przyklad="Na wysokości równej promieniowi Ziemi (r = 2R) ciężar spada czterokrotnie."),

 "7.1": dict(
  czego="Praca siły stałej i zmiennej.",
  kiedy="Praca to iloczyn skalarny, więc siła prostopadła do przesunięcia nie wykonuje pracy. Dla siły zmiennej liczymy całkę, czyli pole pod wykresem F(s).",
  przyklad="Podnosząc 20 kg na 2 m wykonujesz W = mgh = 400 J. Niosąc ten sam ciężar poziomo — zero pracy w sensie fizycznym."),

 "7.3": dict(
  czego="Energia kinetyczna ciała w ruchu postępowym.",
  kiedy="Twierdzenie o pracy i energii: praca wypadkowej siły równa się przyrostowi energii kinetycznej. Zależność od KWADRATU prędkości ma ogromne skutki praktyczne.",
  przyklad="Podwojenie prędkości z 50 na 100 km/h czterokrotnie zwiększa energię, a więc i drogę hamowania."),

 "8.2": dict(
  czego="Energia potencjalna — grawitacyjna i sprężystości.",
  kiedy="Definiowalna tylko dla sił zachowawczych. Poziom odniesienia wybieramy dowolnie; liczą się różnice energii, nie wartości bezwzględne.",
  przyklad="Sprężyna k = 200 N/m ściśnięta o 10 cm: E = ½kx² = ½·200·0,01 = 1 J."),

 "8.3": dict(
  czego="Zasada zachowania energii mechanicznej.",
  kiedy="Obowiązuje, gdy działają wyłącznie siły zachowawcze. Przy tarciu część energii przechodzi w ciepło i trzeba ją dopisać.",
  przyklad="Ciało spada z 5 m: v = √(2gh) = √100 = 10 m/s, niezależnie od masy."),

 "9.1": dict(
  czego="Pęd i zasada jego zachowania.",
  kiedy="Gdy wypadkowa sił zewnętrznych to zero. Działa też w zderzeniach niesprężystych, w których energia kinetyczna maleje.",
  przyklad="Wagon 10 t przy 2 m/s uderza w stojący 10 t i sczepiają się: v = 10·2/20 = 1 m/s."),

 "11.3": dict(
  czego="Moment bezwładności i druga zasada dynamiki dla obrotu.",
  kiedy="Im dalej masa od osi, tym trudniej rozkręcić ciało. Dla walca ½mR², dla obręczy mR², dla kuli ⅖mR².",
  przyklad="Obręcz i walec o tej samej masie staczają się z równi — walec dojedzie pierwszy, bo ma mniejszy moment bezwładności."),

 "12.1": dict(
  czego="Ruch harmoniczny prosty i jego równanie.",
  kiedy="Gdy siła jest proporcjonalna do wychylenia i skierowana przeciwnie. Okres nie zależy od amplitudy — to własność, na której opiera się zegar wahadłowy.",
  przyklad="Sprężyna k = 50 N/m z masą 0,5 kg: T = 2π√(m/k) = 2π√0,01 ≈ 0,63 s."),
}
