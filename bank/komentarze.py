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

# ---------------- MODUŁ I: uzupełnienie ----------------
K.update({
 "1.2.2": dict(
  czego="Suma wektorów i rozkład wektora na składowe.",
  kiedy="Zawsze, gdy działa kilka sił naraz albo ruch odbywa się w dwóch wymiarach. Dodajemy składowe osobno wzdłuż każdej osi, nigdy samych długości wektorów.",
  przyklad="Siły 3 N i 4 N prostopadłe do siebie dają wypadkową √(9+16) = 5 N, a nie 7 N."),
 "2.2.1": dict(
  czego="Prędkość w ruchu jednostajnym.",
  kiedy="Gdy prędkość nie zmienia się w czasie. Wykres drogi od czasu jest wtedy linią prostą, a jej nachylenie to prędkość.",
  przyklad="Pociąg jedzie 3 h ze stałą prędkością 80 km/h: s = 240 km."),
 "2.2.2": dict(
  czego="Prędkość chwilowa jako pochodna drogi po czasie.",
  kiedy="Gdy ruch jest nierównomierny i pytamy o prędkość w konkretnym momencie, a nie na odcinku. To nachylenie stycznej do wykresu s(t).",
  przyklad="Dla x(t) = 5t² prędkość v = dx/dt = 10t, więc w 3 sekundzie wynosi 30 m/s."),
 "2.3.1": dict(
  czego="Przyspieszenie jako zmiana prędkości w czasie.",
  kiedy="Jednostka to m/s². Przyspieszenie ujemne oznacza hamowanie tylko wtedy, gdy ma zwrot przeciwny do prędkości.",
  przyklad="Auto rozpędza się od 0 do 100 km/h (27,8 m/s) w 8 s: a = 27,8/8 ≈ 3,5 m/s²."),
 "3.1": dict(
  czego="Przemieszczenie, prędkość i przyspieszenie w ruchu płaskim, zapisane wektorowo.",
  kiedy="Ruch na płaszczyźnie rozkładamy na dwa niezależne ruchy wzdłuż osi. Każdą składową liczymy osobno, a na końcu składamy wyniki.",
  przyklad="Łódź płynie 4 m/s w poprzek rzeki, nurt niesie 3 m/s. Prędkość względem brzegu: 5 m/s, pod kątem do osi rzeki."),
 "4.1.4": dict(
  czego="Siła jako zmiana pędu w czasie.",
  kiedy="To ogólniejsza postać drugiej zasady dynamiki. Przydaje się, gdy masa się zmienia, oraz przy uderzeniach, gdzie łatwiej mierzyć zmianę pędu niż samą siłę.",
  przyklad="Piłka 0,4 kg odbija się od ściany: przed 10 m/s, po −8 m/s. Zmiana pędu 7,2 kg·m/s w 0,02 s daje siłę 360 N."),
 "5.1": dict(
  czego="Siły kontaktowe: nacisk i tarcie.",
  kiedy="Siła nacisku N nie zawsze równa się ciężarowi — na równi jest mniejsza, w windzie zmienia się z przyspieszeniem.",
  przyklad="Na równi o kącie 30° nacisk wynosi N = mg·cos30° ≈ 0,87 mg."),
 "5.2": dict(
  czego="Siły bezwładności w układach nieinercjalnych.",
  kiedy="Pojawiają się dopiero, gdy opisujemy ruch z układu przyspieszającego. Nie mają źródła w oddziaływaniu ciał, więc nie ma do nich siły reakcji.",
  przyklad="W hamującym autobusie z opóźnieniem 3 m/s² pasażer 70 kg czuje siłę 210 N pchającą go do przodu."),
 "6.1": dict(
  czego="Prawo powszechnego ciążenia.",
  kiedy="Zawsze przy ruchu ciał niebieskich i przy liczeniu ciężaru na innej wysokości. Zależność od r² sprawia, że podwojenie odległości osłabia siłę czterokrotnie.",
  przyklad="Satelita na wysokości 6370 km, czyli r = 2R: przyciąganie spada do jednej czwartej wartości przy powierzchni."),
 "6.4": dict(
  czego="Pole grawitacyjne i jego natężenie.",
  kiedy="Natężenie pola to siła na jednostkę masy, czyli po prostu przyspieszenie grawitacyjne. Opis polowy wygodniejszy, gdy źródeł jest wiele.",
  przyklad="Na powierzchni Ziemi γ = GM/R² ≈ 9,81 m/s², niezależnie od masy ciała próbnego."),
})

# ---------------- MODUŁ II ----------------
K.update({
 "7.2": dict(
  czego="Praca siły zmiennej jako całka.",
  kiedy="Gdy siła zmienia się na drodze — sprężyna, opór powietrza. Praca to pole pod wykresem F(s).",
  przyklad="Rozciąganie sprężyny k = 100 N/m o 0,2 m: W = ½·100·0,04 = 2 J."),
 "8.1": dict(
  czego="Podział sił na zachowawcze i niezachowawcze.",
  kiedy="Tylko dla zachowawczych da się zdefiniować energię potencjalną. Test: praca po drodze zamkniętej równa zeru.",
  przyklad="Grawitacja jest zachowawcza, tarcie nie — przy tarciu droga tam i z powrotem kosztuje energię dwa razy."),
 "8.2.1": dict(
  czego="Energia potencjalna i potencjał pola grawitacyjnego.",
  kiedy="Dla dużych odległości nie wolno używać mgh — to przybliżenie tylko przy powierzchni. Energia jest ujemna, bo zero przyjmujemy w nieskończoności.",
  przyklad="Druga prędkość kosmiczna wynika z warunku ½mv² = GMm/R, stąd v = √(2GM/R) ≈ 11,2 km/s."),
 "9.2": dict(
  czego="Ruch środka masy układu.",
  kiedy="Środek masy porusza się tak, jakby cała masa była w nim skupiona, a siły zewnętrzne działały tylko na niego. Siły wewnętrzne go nie ruszą.",
  przyklad="Po wybuchu pocisku w locie środek masy odłamków leci dalej po tej samej paraboli."),
 "9.3": dict(
  czego="Pęd układu punktów materialnych.",
  kiedy="Pęd całości to suma wektorowa pędów. Przy braku sił zewnętrznych pozostaje stały, także co do kierunku.",
  przyklad="Człowiek 80 kg wyskakuje z łódki 200 kg z prędkością 2 m/s — łódka odpływa z 0,8 m/s."),
 "10.2": dict(
  czego="Zderzenia na płaszczyźnie.",
  kiedy="Pęd zachowuje się osobno wzdłuż każdej osi, więc zapisujemy dwa równania. Przy zderzeniu sprężystym dochodzi trzecie — zachowanie energii.",
  przyklad="Przy centralnym zderzeniu sprężystym równych mas ciała wymieniają się prędkościami."),
})

# ---------------- MODUŁ III ----------------
K.update({
 "11.1": dict(
  czego="Kinematyka ruchu obrotowego: kąt, prędkość i przyspieszenie kątowe.",
  kiedy="Wzory są bliźniacze do ruchu prostoliniowego, tylko z wielkościami kątowymi. Związek z wielkościami liniowymi: v = ωR, a = εR.",
  przyklad="Koło o R = 0,3 m kręci się z ω = 20 rad/s: prędkość obwodowa v = 6 m/s."),
 "11.2": dict(
  czego="Dynamika ruchu obrotowego — moment siły.",
  kiedy="Moment zależy od ramienia, nie tylko od siły. Ta sama siła przyłożona dalej od osi daje większy moment.",
  przyklad="Śruba stawia opór 30 N·m. Kluczem 0,25 m trzeba przyłożyć 120 N, kluczem 0,5 m już tylko 60 N."),
 "11.2.1": dict(
  czego="Moment pędu.",
  kiedy="Odpowiednik pędu dla obrotu. Dla punktu materialnego L = r × p, dla bryły L = Iω.",
  przyklad="Krążek I = 0,02 kg·m² przy ω = 50 rad/s ma moment pędu 1 kg·m²/s."),
 "11.2.2": dict(
  czego="Zasada zachowania momentu pędu.",
  kiedy="Gdy wypadkowy moment sił zewnętrznych wynosi zero. Zmniejszenie momentu bezwładności zwiększa prędkość kątową.",
  przyklad="Łyżwiarka przyciąga ręce, I maleje dwukrotnie, więc ω rośnie dwukrotnie, a energia obrotu podwaja się kosztem pracy jej mięśni."),
 "12.2.1": dict(
  czego="Wahadło matematyczne.",
  kiedy="Wzór obowiązuje tylko dla małych wychyleń, do kilku stopni. Okres nie zależy od masy ani od amplitudy.",
  przyklad="Wahadło o długości 1 m: T = 2π√(1/9,81) ≈ 2,0 s."),
 "12.2.2": dict(
  czego="Wahadło fizyczne — bryła zawieszona poza środkiem masy.",
  kiedy="Gdy ciała nie da się uznać za punkt. Potrzebny moment bezwładności względem osi zawieszenia i odległość do środka masy.",
  przyklad="Pręt długości L zawieszony za koniec ma okres krótszy niż wahadło matematyczne o tej samej długości."),
 "12.3": dict(
  czego="Energia w ruchu harmonicznym prostym.",
  kiedy="Energia całkowita jest stała i proporcjonalna do kwadratu amplitudy. Wymienia się cyklicznie między potencjalną a kinetyczną.",
  przyklad="Sprężyna k = 80 N/m, A = 0,1 m: E = ½·80·0,01 = 0,4 J, tyle samo w skrajnym wychyleniu co w środku."),
 "12.4": dict(
  czego="Oscylator harmoniczny tłumiony.",
  kiedy="Gdy występuje opór proporcjonalny do prędkości. Amplituda maleje wykładniczo, a przy dużym tłumieniu ruch przestaje być drgający.",
  przyklad="Amortyzator w aucie dobiera się tak, by był bliski tłumieniu krytycznemu — nadwozie wraca bez kołysania."),
 "12.4.1": dict(
  czego="Straty mocy i współczynnik dobroci Q.",
  kiedy="Q mówi, ile energii układ traci na okres. Wysokie Q to wolne wygasanie i ostry rezonans.",
  przyklad="Kamerton ma Q rzędu tysiąca, amortyzator samochodowy poniżej jedności."),
 "12.5": dict(
  czego="Drgania wymuszone oscylatora harmonicznego.",
  kiedy="Gdy na układ działa siła okresowa. Po czasie przejściowym układ drga z częstotliwością siły, a nie własną.",
  przyklad="Silnik na podeście wymusza drgania o swojej częstotliwości obrotów, niezależnie od częstotliwości własnej podestu."),
 "12.5.1": dict(
  czego="Rezonans.",
  kiedy="Gdy częstotliwość wymuszająca zbliża się do własnej, amplituda gwałtownie rośnie, a ogranicza ją wyłącznie tłumienie.",
  przyklad="Dlatego kolumna wojska nie przechodzi przez most krokiem defiladowym."),
 "12.6.1": dict(
  czego="Składanie drgań równoległych.",
  kiedy="Dwa drgania wzdłuż tej samej prostej. Wynik zależy od różnicy faz: zgodne wzmacniają się, przeciwne wygaszają.",
  przyklad="Dwa drgania A = 3 i A = 4 zgodne w fazie dają 7, przeciwne w fazie dają 1."),
 "12.6.2": dict(
  czego="Składanie drgań prostopadłych — krzywe Lissajous.",
  kiedy="Gdy drgania odbywają się wzdłuż dwóch prostopadłych osi. Kształt toru zależy od stosunku częstotliwości i różnicy faz.",
  przyklad="Równe częstotliwości i przesunięcie o 90° dają okrąg, zgodność faz daje odcinek prostej."),
})

# ---------------- MODUŁ IV: fale sprężyste i płyny ----------------
K.update({
 "13.2": dict(
  czego="Rozchodzenie się fal w przestrzeni — funkcja falowa.",
  kiedy="Argument ma postać (kx − ωt): znak minus to fala biegnąca w prawo, plus w lewo. Liczba falowa k = 2π/λ, częstość ω = 2πf.",
  przyklad="Fala o λ = 2 m i f = 50 Hz: k = π rad/m, ω = 100π rad/s, v = λf = 100 m/s."),
 "13.3": dict(
  czego="Prędkość fali i równanie falowe.",
  kiedy="Prędkość zależy wyłącznie od ośrodka. Przy przejściu do innego ośrodka zmienia się długość fali, a częstotliwość zostaje ta sama.",
  przyklad="Dźwięk 340 m/s w powietrzu i 1500 m/s w wodzie — ta sama nuta ma w wodzie ponad cztery razy dłuższą falę."),
 "13.4": dict(
  czego="Przenoszenie energii przez fale.",
  kiedy="Moc fali rośnie z kwadratem amplitudy i z kwadratem częstotliwości. Podwojenie amplitudy to czterokrotnie większa energia.",
  przyklad="Fala kulista słabnie jak 1/r², bo ta sama moc rozkłada się na coraz większą sferę."),
 "13.5": dict(
  czego="Interferencja fal.",
  kiedy="Fale o tej samej częstotliwości nakładają się. Różnica dróg będąca wielokrotnością λ daje wzmocnienie, nieparzysta wielokrotność λ/2 — wygaszenie.",
  przyklad="Dwa głośniki 1,7 m od siebie przy λ = 1,7 m: w punkcie równo oddalonym słychać wzmocnienie."),
 "13.5.1": dict(
  czego="Fale stojące i częstotliwości własne.",
  kiedy="Powstają z nałożenia fali biegnącej i odbitej. Na zamocowanych końcach muszą być węzły, co kwantuje dozwolone częstotliwości.",
  przyklad="Struna 0,65 m, v = 260 m/s: ton podstawowy f = 260/(2·0,65) = 200 Hz."),
 "13.6": dict(
  czego="Analiza fal złożonych — rozkład Fouriera.",
  kiedy="Każdy przebieg okresowy da się rozłożyć na sumę drgań harmonicznych. To podstawa syntezy dźwięku i analizy widmowej.",
  przyklad="Barwa dźwięku to udział wyższych harmonicznych — skrzypce i flet grają to samo a, ale brzmią inaczej."),
 "13.7": dict(
  czego="Dudnienia — nakładanie fal o zbliżonych częstotliwościach.",
  kiedy="Częstotliwość dudnień równa się różnicy częstotliwości składowych. Stosowane przy strojeniu instrumentów.",
  przyklad="Struny 440 Hz i 443 Hz dają 3 dudnienia na sekundę; strojenie polega na ich wyeliminowaniu."),
 "13.8": dict(
  czego="Zjawisko Dopplera dla fal w ośrodku.",
  kiedy="Uwaga: inne wzory dla ruchu źródła, a inne dla ruchu obserwatora — to nie jest symetryczne, bo ośrodek wyróżnia układ odniesienia.",
  przyklad="Karetka 30 m/s z syreną 1000 Hz: zbliżając się słychać ok. 1097 Hz, oddalając ok. 919 Hz."),
 "14.1": dict(
  czego="Ciśnienie i gęstość, ciśnienie hydrostatyczne.",
  kiedy="Ciśnienie w cieczy zależy tylko od głębokości i gęstości, nie od kształtu naczynia — to paradoks hydrostatyczny.",
  przyklad="Na 10 m pod wodą ciśnienie rośnie o ρgh = 1000·10·10 = 100 kPa, czyli o jedną atmosferę."),
 "14.4": dict(
  czego="Ogólny opis przepływu płynów i równanie ciągłości.",
  kiedy="Dla cieczy nieściśliwej iloczyn przekroju i prędkości jest stały. W zwężeniu ciecz płynie szybciej.",
  przyklad="Rura zwęża się z 10 cm² do 2 cm² — prędkość rośnie pięciokrotnie."),
 "14.5": dict(
  czego="Równanie Bernoulliego.",
  kiedy="Dla przepływu ustalonego cieczy doskonałej. Gdzie prędkość większa, tam ciśnienie mniejsze. Nie stosować przy dużej lepkości i turbulencji.",
  przyklad="Zwężka Venturiego mierzy przepływ właśnie ze spadku ciśnienia w przewężeniu."),
 "14.6": dict(
  czego="Dynamiczna siła nośna.",
  kiedy="Różnica prędkości opływu nad i pod skrzydłem daje różnicę ciśnień. Siła rośnie z kwadratem prędkości i z powierzchnią skrzydła.",
  przyklad="Podwojenie prędkości startu czterokrotnie zwiększa siłę nośną — dlatego rozbieg ma taką długość."),
})

# ---------------- MODUŁ V: termodynamika ----------------
K.update({
 "15.1": dict(
  czego="Ciśnienie gazu doskonałego w ujęciu kinetycznym.",
  kiedy="Ciśnienie to skutek zderzeń cząsteczek ze ściankami. Wiąże wielkość makroskopową ze średnią energią kinetyczną cząsteczek.",
  przyklad="Ogrzanie gazu w sztywnym zbiorniku zwiększa ciśnienie, bo cząsteczki uderzają częściej i mocniej."),
 "15.2.2": dict(
  czego="Kinetyczna interpretacja temperatury.",
  kiedy="Temperatura jest miarą średniej energii kinetycznej cząsteczek, a nie ilości ciepła. Dwa ciała o tej samej temperaturze mogą mieć różną energię wewnętrzną.",
  przyklad="Iskra ma tysiące stopni, ale znikomą energię — nie poparzy tak jak wrzątek o 100°C."),
 "15.2.3": dict(
  czego="Równanie stanu gazu doskonałego.",
  kiedy="Dobre przybliżenie przy niskim ciśnieniu i wysokiej temperaturze. Blisko skraplania trzeba sięgnąć po równanie Van der Waalsa.",
  przyklad="Mol gazu w warunkach normalnych zajmuje V = RT/p = 8,31·273/101325 ≈ 22,4 dm³."),
 "15.2.4": dict(
  czego="Skale temperatur.",
  kiedy="We wszystkich wzorach termodynamicznych temperatura musi być w kelwinach. Podstawienie stopni Celsjusza to najczęstszy błąd rachunkowy.",
  przyklad="Ogrzanie z 27°C do 327°C to wzrost z 300 K do 600 K, czyli dwukrotny, a nie dwunastokrotny."),
 "15.3": dict(
  czego="Zasada ekwipartycji energii.",
  kiedy="Na każdy stopień swobody przypada ½k_BT. Gaz jednoatomowy ma 3 stopnie, dwuatomowy w temperaturze pokojowej 5.",
  przyklad="Stąd ciepło molowe przy stałej objętości: 3/2 R dla helu i 5/2 R dla azotu."),
 "15.4": dict(
  czego="Pierwsza zasada termodynamiki.",
  kiedy="Zasada zachowania energii dla układów cieplnych. Pilnuj znaków: ciepło dostarczone dodatnie, praca wykonana PRZEZ układ dodatnia.",
  przyklad="Gaz pochłania 500 J i wykonuje 200 J pracy — energia wewnętrzna rośnie o 300 J."),
 "15.5.1": dict(
  czego="Ciepło właściwe przy stałej objętości.",
  kiedy="Cała dostarczona energia idzie na wzrost energii wewnętrznej, bo gaz nie wykonuje pracy.",
  przyklad="Dla gazu jednoatomowego c_V = 3/2 R ≈ 12,5 J/(mol·K)."),
 "15.5.2": dict(
  czego="Ciepło właściwe przy stałym ciśnieniu i relacja Mayera.",
  kiedy="c_p jest większe od c_V o R, bo część ciepła idzie na pracę rozprężania.",
  przyklad="Dla gazu jednoatomowego c_p = 5/2 R ≈ 20,8 J/(mol·K), stąd κ = c_p/c_V = 1,67."),
 "15.6.1": dict(
  czego="Rozprężanie izotermiczne.",
  kiedy="Temperatura stała, więc energia wewnętrzna się nie zmienia i całe pobrane ciepło zamienia się w pracę.",
  przyklad="Mol gazu w 300 K rozprężony dwukrotnie wykonuje W = nRT·ln2 ≈ 1730 J."),
 "15.6.2": dict(
  czego="Rozprężanie adiabatyczne.",
  kiedy="Bez wymiany ciepła, więc praca odbywa się kosztem energii wewnętrznej i gaz się oziębia. Adiabata jest stromsza niż izoterma.",
  przyklad="Na tym polega chłodzenie powietrza wypuszczanego z butli nurkowej."),
 "16.1": dict(
  czego="Średnia droga swobodna cząsteczki.",
  kiedy="Odległość między kolejnymi zderzeniami. Maleje z gęstością gazu i rozmiarem cząsteczek.",
  przyklad="W powietrzu w warunkach normalnych to około 70 nm — stąd tak duża liczba zderzeń na sekundę."),
 "16.2": dict(
  czego="Rozkład Maxwella prędkości cząsteczek.",
  kiedy="Cząsteczki nie mają jednej prędkości, tylko rozkład. Uwaga na trzy różne wielkości: najbardziej prawdopodobna, średnia i średnia kwadratowa.",
  przyklad="Ogrzanie gazu spłaszcza rozkład i przesuwa maksimum w stronę wyższych prędkości."),
 "16.3": dict(
  czego="Równanie Van der Waalsa.",
  kiedy="Poprawka do gazu doskonałego: a uwzględnia przyciąganie cząsteczek, b ich własną objętość. Potrzebne przy wysokich ciśnieniach i blisko skraplania.",
  przyklad="Bez tych poprawek nie da się opisać skraplania gazu — gaz doskonały nigdy nie skropliłby się."),
 "16.4.2": dict(
  czego="Cykl Carnota i jego sprawność.",
  kiedy="To górna granica sprawności każdego silnika cieplnego między dwiema temperaturami. Żadna konstrukcja jej nie przekroczy.",
  przyklad="Silnik między 600 K a 300 K ma sprawność najwyżej 1 − 300/600 = 50%."),
 "16.5.1": dict(
  czego="Termodynamiczna skala temperatur.",
  kiedy="Definiowana przez sprawność cyklu Carnota, niezależnie od substancji roboczej. Stąd bierze się zero bezwzględne.",
  przyklad="Stosunek temperatur to stosunek ciepeł wymienianych ze źródłami w cyklu odwracalnym."),
 "16.5.2": dict(
  czego="Entropia.",
  kiedy="Funkcja stanu: zmiana zależy tylko od stanu początkowego i końcowego. W procesie odwracalnym dS = δQ/T.",
  przyklad="Topnienie 1 kg lodu w 273 K: ΔS = 334000/273 ≈ 1220 J/K."),
 "16.5.3": dict(
  czego="Entropia a nieuporządkowanie — wzór Boltzmanna.",
  kiedy="Entropia mierzy liczbę mikrostanów odpowiadających danemu stanowi makroskopowemu. Stąd statystyczne uzasadnienie drugiej zasady.",
  przyklad="Gaz sam z siebie nie wróci do połowy naczynia, bo stanów rozproszonych jest nieporównanie więcej."),
 "16.6.2": dict(
  czego="Zjawiska transportu: dyfuzja, przewodnictwo cieplne, lepkość.",
  kiedy="Wszystkie opisuje ten sam schemat — strumień proporcjonalny do gradientu wielkości.",
  przyklad="Przewodzenie ciepła przez ścianę: strumień rośnie z różnicą temperatur i maleje z grubością."),
})

# ---------------- MODUŁ VI: elektrostatyka ----------------
K.update({
 "17.2": dict(
  czego="Prawo Coulomba.",
  kiedy="Dla ładunków punktowych w spoczynku. Postać identyczna jak w grawitacji, ale siła może odpychać, a stała jest o rzędy wielkości większa.",
  przyklad="Dwa ładunki 1 μC w odległości 10 cm: F = 9·10⁹·10⁻¹²/0,01 = 0,9 N."),
 "17.3": dict(
  czego="Natężenie pola elektrycznego.",
  kiedy="Siła na jednostkę ładunku próbnego. Opis polowy uwalnia od liczenia sił dla każdej pary ładunków osobno.",
  przyklad="Pole 1000 V/m działa na elektron siłą 1,6·10⁻¹⁶ N."),
 "18.1": dict(
  czego="Strumień pola elektrycznego.",
  kiedy="Liczba linii pola przechodzących przez powierzchnię. Dla powierzchni prostopadłej to po prostu E·S.",
  przyklad="Pole 500 V/m przez ramkę 0,2 m² ustawioną prostopadle: strumień 100 V·m."),
 "18.2": dict(
  czego="Prawo Gaussa.",
  kiedy="Najkrótsza droga do pola przy dużej symetrii: kulistej, walcowej albo płaskiej. Powierzchnię dobiera się tak, by E było stałe i prostopadłe.",
  przyklad="Dla naładowanej sfery na zewnątrz pole jest takie, jakby cały ładunek siedział w środku."),
 "18.3.2": dict(
  czego="Pole jednorodnie naładowanej sfery.",
  kiedy="W środku sfery pole wynosi ZERO, na zewnątrz jak od ładunku punktowego. To wynik, który zaskakuje na egzaminie.",
  przyklad="Wewnątrz metalowej kuli nie ma pola — stąd ekranowanie w klatce Faradaya."),
 "18.3.3": dict(
  czego="Pole jednorodnie naładowanej kuli pełnej.",
  kiedy="W środku rośnie liniowo z promieniem, na zewnątrz maleje jak 1/r². Maksimum wypada na powierzchni.",
  przyklad="W połowie promienia pole jest dwa razy mniejsze niż na powierzchni."),
 "18.4.1": dict(
  czego="Pole liniowego rozkładu ładunku.",
  kiedy="Dla długiego naładowanego przewodu pole maleje jak 1/r, a nie 1/r². Wynika to z symetrii walcowej.",
  przyklad="Podwojenie odległości od przewodu osłabia pole dwukrotnie, a nie czterokrotnie."),
 "18.4.2": dict(
  czego="Pole płaskiego rozkładu ładunku.",
  kiedy="Dla nieskończonej naładowanej płaszczyzny pole NIE zależy od odległości. To dobre przybliżenie blisko dużej płyty.",
  przyklad="Między okładkami kondensatora płaskiego pole jest jednorodne w całej objętości."),
 "18.4.3": dict(
  czego="Pole tuż przy powierzchni przewodnika.",
  kiedy="Pole jest prostopadłe do powierzchni i równe σ/ε₀. Ładunek gromadzi się gęściej tam, gdzie krzywizna większa.",
  przyklad="Na ostrzu pole jest największe — stąd zasada działania piorunochronu."),
 "19.1": dict(
  czego="Energia potencjalna ładunku w polu elektrycznym.",
  kiedy="Praca sił pola nie zależy od drogi, tylko od punktów końcowych. Pole elektrostatyczne jest zachowawcze.",
  przyklad="Przeniesienie ładunku 2 μC przez różnicę 100 V kosztuje 2·10⁻⁴ J."),
 "19.2": dict(
  czego="Potencjał elektryczny i napięcie.",
  kiedy="Potencjał to energia na jednostkę ładunku. Powierzchnie ekwipotencjalne są prostopadłe do linii pola, a wzdłuż nich praca wynosi zero.",
  przyklad="Przy ładunku punktowym V = kQ/r; dwa razy dalej to dwa razy mniejszy potencjał."),
 "20.1": dict(
  czego="Pojemność elektryczna.",
  kiedy="Zdolność do gromadzenia ładunku przy danym napięciu. Zależy wyłącznie od geometrii i dielektryka, nie od ładunku.",
  przyklad="Kondensator 100 μF przy 12 V gromadzi Q = CU = 1,2 mC."),
 "20.2": dict(
  czego="Energia zgromadzona w kondensatorze i gęstość energii pola.",
  kiedy="Energia siedzi w polu elektrycznym między okładkami. Trzy równoważne zapisy: ½CU², ½QU, Q²/2C.",
  przyklad="Kondensator 1000 μF przy 400 V ma 80 J — dość, by zabić, długo po odłączeniu zasilania."),
 "20.3": dict(
  czego="Kondensator z dielektrykiem.",
  kiedy="Dielektryk zwiększa pojemność ε_r razy. Uwaga: przy stałym napięciu rośnie ładunek, przy stałym ładunku maleje napięcie.",
  przyklad="Wstawienie dielektryka o ε_r = 5 zwiększa pojemność pięciokrotnie."),
})

# ---------------- MODUŁ VII: prąd i magnetyzm ----------------
K.update({
 "21.1": dict(
  czego="Natężenie prądu i gęstość prądu.",
  kiedy="Natężenie to ładunek przepływający w jednostce czasu. Gęstość prądu opisuje, jak rozkłada się on w przekroju.",
  przyklad="Prąd 2 A w przewodzie 1 mm²: gęstość 2·10⁶ A/m²."),
 "21.2": dict(
  czego="Prawo Ohma.",
  kiedy="Obowiązuje dla przewodników metalicznych w stałej temperaturze. Dioda i żarówka mu nie podlegają — ich opór zależy od napięcia.",
  przyklad="Grzałka 2000 W na 230 V ma opór R = U²/P ≈ 26 Ω."),
 "21.3": dict(
  czego="Praca i moc prądu.",
  kiedy="Trzy równoważne postacie: P = UI = I²R = U²/R. Wybór zależy od tego, co jest stałe w zadaniu.",
  przyklad="Przy przesyle energii liczy się I²R, dlatego podnosi się napięcie, żeby zmniejszyć prąd."),
 "21.3.1": dict(
  czego="Straty cieplne, prawo Joule'a-Lenza.",
  kiedy="Straty rosną z kwadratem prądu. Stąd linie wysokiego napięcia — dziesięciokrotnie wyższe napięcie to stukrotnie mniejsze straty.",
  przyklad="Przewód 0,5 Ω przy 10 A grzeje 50 W, przy 20 A już 200 W."),
 "21.4.1": dict(
  czego="Siła elektromotoryczna i opór wewnętrzny.",
  kiedy="Napięcie na zaciskach jest mniejsze od SEM o spadek na oporze wewnętrznym. Przy zwarciu prąd ogranicza właśnie ten opór.",
  przyklad="Bateria 12 V o r = 0,1 Ω przy prądzie 20 A daje na zaciskach 10 V."),
 "21.4.2": dict(
  czego="Prawa Kirchhoffa.",
  kiedy="Prądowe dla węzłów, napięciowe dla oczek. Niezbędne przy obwodach, których nie da się sprowadzić do szeregowych i równoległych.",
  przyklad="W węźle wpływa 3 A i 2 A, więc wypływa 5 A — niezależnie od tego, co dalej."),
 "22.1": dict(
  czego="Siła magnetyczna działająca na ładunek — siła Lorentza.",
  kiedy="Prostopadła do prędkości i do pola, więc nie wykonuje pracy i nie zmienia energii kinetycznej.",
  przyklad="Elektron wpadający prostopadle w pole magnetyczne porusza się po okręgu ze stałą szybkością."),
 "22.3": dict(
  czego="Ruch naładowanych cząstek w polu magnetycznym.",
  kiedy="Promień okręgu r = mv/(qB), a okres nie zależy od prędkości. Na tym opiera się cyklotron.",
  przyklad="Proton 10⁶ m/s w polu 0,5 T zatacza okrąg o promieniu około 2 cm."),
 "22.4": dict(
  czego="Siła działająca na przewodnik z prądem.",
  kiedy="F = BIL·sinα. Maksymalna, gdy przewodnik prostopadły do pola; zerowa, gdy równoległy.",
  przyklad="Przewód 0,2 m z prądem 5 A w polu 0,4 T prostopadle: F = 0,4 N."),
 "22.4.1": dict(
  czego="Moment siły na obwód z prądem.",
  kiedy="Podstawa działania silnika elektrycznego i miernika wskazówkowego. Moment zależy od kąta między normalną ramki a polem.",
  przyklad="Ramka ustawia się prostopadle do pola — w tym położeniu moment znika."),
 "22.4.2": dict(
  czego="Magnetyczny moment dipolowy.",
  kiedy="Opisuje ramkę z prądem jak dipol magnetyczny: μ = IS. Wygodne przy opisie magnetyzmu materii.",
  przyklad="Ramka 100 zwojów o powierzchni 4 cm² z prądem 0,5 A: μ = 0,02 A·m²."),
 "22.5": dict(
  czego="Efekt Halla.",
  kiedy="Pozwala wyznaczyć znak i koncentrację nośników ładunku. Stosowany w czujnikach pola i położenia.",
  przyklad="Napięcie Halla zmienia znak, gdy nośnikami są dziury zamiast elektronów."),
 "23.1.2": dict(
  czego="Prawo Ampère'a.",
  kiedy="Odpowiednik prawa Gaussa dla magnetyzmu. Skuteczne przy dużej symetrii: przewodnik prostoliniowy, solenoid, toroid.",
  przyklad="Całka po okręgu wokół przewodu zależy tylko od objętego prądu, nie od promienia okręgu."),
 "23.1.3": dict(
  czego="Pole wokół prostoliniowego przewodnika.",
  kiedy="B = μ₀I/(2πr), linie pola to współśrodkowe okręgi. Kierunek wskazuje reguła prawej dłoni.",
  przyklad="10 cm od przewodu z prądem 10 A: B = 2·10⁻⁵ T, czyli rzędu pola ziemskiego."),
 "23.1.4": dict(
  czego="Pole wewnątrz solenoidu.",
  kiedy="B = μ₀nI, gdzie n to liczba zwojów na metr. Pole jest jednorodne w środku i praktycznie znika na zewnątrz.",
  przyklad="Solenoid 1000 zwojów na metr przy 2 A daje B ≈ 2,5 mT."),
 "23.2": dict(
  czego="Oddziaływanie równoległych przewodników z prądem.",
  kiedy="Prądy zgodne przyciągają się, przeciwne odpychają. Na tej sile opierała się dawna definicja ampera.",
  przyklad="Dwa przewody 1 m od siebie z prądem 1 A działają na siebie siłą 2·10⁻⁷ N na metr."),
 "23.3": dict(
  czego="Prawo Biota-Savarta.",
  kiedy="Ogólny sposób liczenia pola od dowolnego kształtu przewodnika, gdy brak symetrii do prawa Ampère'a. Wymaga całkowania po długości.",
  przyklad="Stąd wyprowadza się pole w środku kołowej pętli: B = μ₀I/(2R)."),
})

# ---------------- MODUŁ VIII: indukcja i fale EM ----------------
K.update({
 "24.3.1": dict(
  czego="Transformator.",
  kiedy="Stosunek napięć równy stosunkowi liczby zwojów, prądy odwrotnie. Działa TYLKO na prąd zmienny — przy stałym strumień się nie zmienia.",
  przyklad="Uzwojenia 1000 i 50 zwojów: 230 V zamienia się na 11,5 V, a prąd rośnie dwudziestokrotnie."),
 "24.3.2": dict(
  czego="Indukcyjność własna cewki i SEM samoindukcji.",
  kiedy="Cewka przeciwstawia się zmianom prądu. Stąd iskrzenie przy rozłączaniu obwodu z cewką.",
  przyklad="Cewka 0,5 H przy zmianie prądu 2 A/s wytwarza SEM 1 V."),
 "24.4": dict(
  czego="Energia pola magnetycznego cewki.",
  kiedy="W = ½LI². Odpowiednik energii kondensatora, tylko że zmagazynowanej w polu magnetycznym.",
  przyklad="Cewka 0,1 H przy 10 A gromadzi 5 J — to ta energia powoduje łuk przy przerwaniu obwodu."),
 "25.1": dict(
  czego="Drgania swobodne w obwodzie LC.",
  kiedy="Energia przechodzi cyklicznie z kondensatora do cewki. To elektryczny odpowiednik wahadła, bez tłumienia trwałby w nieskończoność.",
  przyklad="L = 1 mH i C = 1 μF dają f = 1/(2π√(10⁻⁹)) ≈ 5 kHz."),
 "25.2": dict(
  czego="Obwód szeregowy RLC — impedancja i przesunięcie fazowe.",
  kiedy="Reaktancje X_L = ωL i X_C = 1/(ωC) odejmują się, bo działają przeciwnie. Rezonans, gdy się zrównają.",
  przyklad="Przy rezonansie impedancja spada do samego R i prąd osiąga maksimum."),
 "25.4": dict(
  czego="Moc w obwodzie prądu zmiennego i współczynnik mocy.",
  kiedy="Moc czynna P = UI·cosφ. Elementy reaktancyjne nie zużywają energii, tylko ją odsyłają.",
  przyklad="Silnik o cosφ = 0,7 przy 230 V i 10 A pobiera 2300 VA pozornej, ale tylko 1610 W czynnej."),
 "26.1": dict(
  czego="Prawo Gaussa dla pola magnetycznego.",
  kiedy="Strumień przez powierzchnię zamkniętą zawsze wynosi zero, bo nie ma monopoli. Linie pola magnetycznego są zamknięte.",
  przyklad="Przełamanie magnesu nie da osobnego bieguna N i S — powstaną dwa pełne magnesy."),
 "26.2": dict(
  czego="Indukowane wirowe pole elektryczne.",
  kiedy="Zmienne pole magnetyczne wytwarza pole elektryczne o zamkniętych liniach. To pole NIE jest zachowawcze.",
  przyklad="Prądy wirowe w rdzeniu transformatora to właśnie skutek tego zjawiska — stąd rdzenie z blach."),
 "26.3": dict(
  czego="Indukowane pole magnetyczne i prąd przesunięcia.",
  kiedy="Wkład Maxwella do prawa Ampère'a: zmienne pole elektryczne działa jak prąd. Bez tego członu fale elektromagnetyczne nie mogłyby istnieć.",
  przyklad="Między okładkami ładowanego kondensatora nie płynie prąd, a pole magnetyczne jest."),
 "27.1": dict(
  czego="Widmo fal elektromagnetycznych.",
  kiedy="Wszystkie biegną w próżni z prędkością c i różnią się tylko częstotliwością. Światło widzialne to wąski pasek od 380 do 780 nm.",
  przyklad="Fala radiowa 100 MHz ma λ = c/f = 3 m, a światło zielone około 550 nm."),
 "27.2": dict(
  czego="Równanie falowe dla fali elektromagnetycznej.",
  kiedy="Wynika wprost z równań Maxwella. Z dwóch stałych elektrycznej i magnetycznej wychodzi prędkość światła.",
  przyklad="c = 1/√(ε₀μ₀) ≈ 3·10⁸ m/s — to był argument, że światło jest falą elektromagnetyczną."),
 "27.4": dict(
  czego="Wektor Poyntinga — gęstość strumienia energii fali.",
  kiedy="Opisuje, ile energii niesie fala przez jednostkę powierzchni. Kierunek pokrywa się z kierunkiem rozchodzenia się fali.",
  przyklad="Stała słoneczna nad atmosferą wynosi około 1360 W/m²."),
})

# ---------------- MODUŁ IX: optyka ----------------
K.update({
 "28.2.2": dict(
  czego="Prawo odbicia i prawo załamania Snella.",
  kiedy="Kąty mierzymy od normalnej, nie od powierzchni. Przy przejściu do ośrodka gęstszego promień zbliża się do normalnej.",
  przyklad="Światło z powietrza do wody pod 45°: sin45°/sin r = 1,33, stąd r ≈ 32°."),
 "28.2.3": dict(
  czego="Równanie soczewki cienkiej i zdolność skupiająca.",
  kiedy="Pilnuj znaków: dla soczewki rozpraszającej f ujemne, dla obrazu pozornego y ujemne. Zdolność skupiająca to odwrotność ogniskowej w metrach.",
  przyklad="Soczewka +2 dioptrie ma f = 0,5 m; przedmiot w 1 m daje obraz w 1 m, rzeczywisty i odwrócony."),
 "29.1": dict(
  czego="Doświadczenie Younga — interferencja na dwóch szczelinach.",
  kiedy="Dowód falowej natury światła. Odstęp prążków rośnie z długością fali i odległością ekranu, a maleje z odstępem szczelin.",
  przyklad="λ = 600 nm, d = 0,2 mm, L = 2 m: odstęp prążków Δy = λL/d = 6 mm."),
 "29.3": dict(
  czego="Rozkład natężenia w doświadczeniu Younga.",
  kiedy="Natężenie zmienia się jak cos² różnicy faz. W maksimum jest czterokrotnie większe niż od jednej szczeliny, nie dwukrotnie.",
  przyklad="Dwie fale o natężeniu I dają w maksimum 4I, a w minimum zero — energia się nie gubi, tylko przemieszcza."),
 "29.4": dict(
  czego="Interferencja w cienkich warstwach.",
  kiedy="Uwzględnij skok fazy o π przy odbiciu od ośrodka gęstszego. To on decyduje, czy warunek wzmocnienia ma λ/2 czy nie.",
  przyklad="Barwy plamy oleju na wodzie i powłoki antyodblaskowe na obiektywach."),
 "30.2": dict(
  czego="Dyfrakcja na pojedynczej szczelinie.",
  kiedy="Uwaga na pułapkę: a·sinθ = mλ to warunek MINIMÓW, nie maksimów. Im węższa szczelina, tym szersze maksimum centralne.",
  przyklad="Szczelina 0,1 mm i λ = 500 nm: pierwsze minimum pod kątem 0,29°."),
 "30.3": dict(
  czego="Rozkład natężenia w obrazie dyfrakcyjnym.",
  kiedy="Maksimum centralne jest dwa razy szersze od pozostałych i skupia większość energii.",
  przyklad="Pierwsze maksimum boczne ma zaledwie około 4,7% natężenia centralnego."),
 "30.4": dict(
  czego="Interferencja i dyfrakcja na dwóch szczelinach jednocześnie.",
  kiedy="Prążki interferencyjne są modulowane obwiednią dyfrakcyjną. Niektóre prążki mogą zniknąć, gdy wypadną w minimum dyfrakcyjnym.",
  przyklad="Przy d = 3a znika co trzeci prążek interferencyjny."),
 "30.5": dict(
  czego="Siatka dyfrakcyjna.",
  kiedy="Im więcej szczelin, tym węższe i jaśniejsze maksima, czyli lepsza zdolność rozdzielcza. Podstawa spektroskopii.",
  przyklad="Siatka 500 rys/mm przy λ = 600 nm: pierwsze maksimum pod kątem 17,5°."),
 "30.6": dict(
  czego="Dyfrakcja promieni X i prawo Bragga.",
  kiedy="Długość fali porównywalna z odległościami atomów w krysztale. Stąd badanie struktury kryształów.",
  przyklad="2d·sinθ = nλ — pomiar kąta odbicia daje odległość płaszczyzn sieciowych."),
 "31.2": dict(
  czego="Płytki polaryzujące i prawo Malusa.",
  kiedy="Światło niespolaryzowane traci na pierwszym polaryzatorze połowę natężenia. Dalej obowiązuje cos² kąta między osiami.",
  przyklad="Dwa polaryzatory pod kątem 60°: przechodzi ½·cos²60° = 12,5% natężenia początkowego."),
 "31.4": dict(
  czego="Dwójłomność.",
  kiedy="W kryształach anizotropowych współczynnik załamania zależy od polaryzacji, więc promień rozszczepia się na dwa.",
  przyklad="Kryształ kalcytu daje podwójny obraz napisu położonego pod nim."),
})

# ---------------- MODUŁ X: fizyka kwantowa ----------------
K.update({
 "32.2": dict(
  czego="Ciało doskonale czarne i prawo Stefana-Boltzmanna.",
  kiedy="Moc promieniowania rośnie z czwartą potęgą temperatury. Podwojenie temperatury to szesnastokrotnie większe promieniowanie.",
  przyklad="Ciało 600 K promieniuje szesnaście razy silniej niż to samo ciało w 300 K."),
 "32.3.2": dict(
  czego="Teoria Plancka i kwantowanie energii.",
  kiedy="Energia promieniowania zmienia się skokowo, porcjami hν. To założenie usunęło katastrofę w nadfiolecie.",
  przyklad="Foton światła zielonego 550 nm ma energię hc/λ ≈ 3,6·10⁻¹⁹ J, czyli 2,25 eV."),
 "32.4": dict(
  czego="Zjawisko fotoelektryczne zewnętrzne.",
  kiedy="Istnieje częstotliwość progowa: poniżej niej elektrony nie wylatują niezależnie od natężenia światła. Tego nie da się wyjaśnić falowo.",
  przyklad="Cynk o pracy wyjścia 4,3 eV wymaga fotonów o λ krótszej niż 290 nm, czyli nadfioletu."),
 "32.4.1": dict(
  czego="Równanie Einsteina dla fotoefektu.",
  kiedy="hν = W + E_kmax. Natężenie światła wpływa na LICZBĘ elektronów, a częstotliwość na ich ENERGIĘ.",
  przyklad="Foton 5 eV na metalu o W = 2 eV wybija elektron o energii kinetycznej 3 eV."),
 "32.5": dict(
  czego="Efekt Comptona.",
  kiedy="Rozproszony foton ma dłuższą falę, bo oddał część energii elektronowi. Dowód, że foton ma pęd.",
  przyklad="Przy rozproszeniu o 90° przyrost długości fali wynosi około 2,4 pm, niezależnie od fali początkowej."),
 "33.3": dict(
  czego="Model Bohra atomu wodoru.",
  kiedy="Skwantowany moment pędu daje dozwolone orbity i poziomy energetyczne. Model działa dobrze dla wodoru, zawodzi dla atomów wieloelektronowych.",
  przyklad="Promień pierwszej orbity to 0,053 nm, a energia poziomu podstawowego −13,6 eV."),
 "33.4": dict(
  czego="Stany energetyczne i widmo atomowe wodoru.",
  kiedy="Różnica poziomów daje energię emitowanego fotonu. Stąd linie widmowe, a nie widmo ciągłe.",
  przyklad="Przejście z n=3 na n=2 daje foton 1,89 eV, czyli czerwoną linię 656 nm serii Balmera."),
 "34.1": dict(
  czego="Fale materii i hipoteza de Broglie'a.",
  kiedy="Każdej cząstce odpowiada fala λ = h/p. Dla ciał makroskopowych długość jest tak mała, że efektów nie widać.",
  przyklad="Elektron rozpędzony napięciem 100 V ma λ ≈ 0,12 nm — porównywalną z odległościami atomów."),
 "34.2": dict(
  czego="Falowe uzasadnienie kwantowania w atomie.",
  kiedy="Na orbicie musi zmieścić się całkowita liczba fal de Broglie'a, inaczej fala wygasiłaby samą siebie.",
  przyklad="Warunek 2πr = nλ daje wprost postulat Bohra o kwantowaniu momentu pędu."),
 "35.2": dict(
  czego="Zasada nieoznaczoności Heisenberga.",
  kiedy="To ograniczenie natury, nie niedoskonałość przyrządów. Analogicznie wiąże energię i czas życia stanu.",
  przyklad="Elektron zamknięty w 0,1 nm ma nieoznaczoność pędu dającą energię rzędu kilku eV."),
 "35.3.1": dict(
  czego="Równanie Schrödingera.",
  kiedy="Podstawowe równanie mechaniki kwantowej. Warunki brzegowe prowadzą do kwantowania energii w sposób naturalny.",
  przyklad="Dla cząstki w studni nieskończonej wychodzą poziomy E_n proporcjonalne do n²."),
 "35.3.2": dict(
  czego="Kwantowomechaniczny opis atomu wodoru.",
  kiedy="Zamiast orbit mamy orbitale — rozkłady prawdopodobieństwa. Pojawiają się trzy liczby kwantowe n, l, m.",
  przyklad="Orbital 1s jest kulisto symetryczny, a najbardziej prawdopodobna odległość równa promieniowi Bohra."),
 "35.3.3": dict(
  czego="Funkcje falowe i ich interpretacja.",
  kiedy="Kwadrat modułu to gęstość prawdopodobieństwa. Funkcja musi być unormowana, ciągła i jednoznaczna.",
  przyklad="Całka z |ψ|² po całej przestrzeni równa się jeden — cząstka gdzieś na pewno jest."),
 "35.3.4": dict(
  czego="Energia elektronu w atomie.",
  kiedy="Poziomy zależą od głównej liczby kwantowej n. Energia ujemna oznacza stan związany.",
  przyklad="Jonizacja z poziomu podstawowego wodoru wymaga dokładnie 13,6 eV."),
})

# ---------------- MODUŁ XI: atomy, ciało stałe, jądro ----------------
K.update({
 "36.1.1": dict(
  czego="Orbitalny moment pędu elektronu i jego kwantowanie.",
  kiedy="Wartość zależy od poboczej liczby kwantowej l, a rzut na oś od magnetycznej m. Stąd rozszczepienie linii w polu magnetycznym.",
  przyklad="Dla l = 1 rzut momentu pędu przyjmuje tylko trzy wartości: −ħ, 0, +ħ."),
 "36.3": dict(
  czego="Układ okresowy pierwiastków i zapełnianie powłok.",
  kiedy="Kolejność wynika z zakazu Pauliego i energii podpowłok. Własności chemiczne zależą od elektronów walencyjnych.",
  przyklad="Gazy szlachetne mają zamkniętą powłokę, dlatego praktycznie nie reagują."),
 "36.4": dict(
  czego="Promienie X — widmo ciągłe i charakterystyczne.",
  kiedy="Widmo ciągłe pochodzi z hamowania elektronów, a linie charakterystyczne z przejść na wewnętrznych powłokach.",
  przyklad="Krótkofalowa granica widma zależy tylko od napięcia lampy: λ_min = hc/(eU)."),
 "36.5.3": dict(
  czego="Rozkład Boltzmanna obsadzenia poziomów.",
  kiedy="Stosunek obsadzeń zależy wykładniczo od różnicy energii i temperatury. Klucz do zrozumienia inwersji obsadzeń w laserze.",
  przyklad="W temperaturze pokojowej poziomy oddalone o 1 eV są obsadzone w stosunku rzędu 10⁻¹⁷."),
 "37.5": dict(
  czego="Własności magnetyczne ciał stałych.",
  kiedy="Diamagnetyki osłabiają pole, paramagnetyki nieznacznie wzmacniają, ferromagnetyki wielokrotnie. Powyżej temperatury Curie ferromagnetyk staje się paramagnetykiem.",
  przyklad="Żelazo traci własności ferromagnetyczne powyżej 770°C."),
 "38.1": dict(
  czego="Budowa jądra atomowego, liczby A i Z.",
  kiedy="A to liczba nukleonów, Z liczba protonów. Izotopy różnią się liczbą neutronów przy tym samym Z.",
  przyklad="Węgiel-14 ma Z = 6 i A = 14, czyli 8 neutronów, wobec 6 w węglu-12."),
 "38.2": dict(
  czego="Oddziaływanie nukleon-nukleon i energia wiązania.",
  kiedy="Siły jądrowe są krótkozasięgowe i niezależne od ładunku. Niedobór masy odpowiada energii wiązania przez E = Δmc².",
  przyklad="Największa energia wiązania na nukleon przypada na żelazo — stąd synteza opłaca się do żelaza, a rozszczepienie od żelaza w górę."),
 "38.3.4": dict(
  czego="Prawo rozpadu promieniotwórczego.",
  kiedy="Rozpad jest losowy i niezależny od warunków zewnętrznych. Czas połowicznego rozpadu wiąże się ze stałą przez T = ln2/λ.",
  przyklad="Po trzech okresach połowicznego rozpadu zostaje jedna ósma początkowej liczby jąder."),
})

# ---------------- uzupełnienia końcowe ----------------
K.update({
 "38.4.3": dict(
  czego="Źródła energii gwiazd — synteza termojądrowa.",
  kiedy="Gwiazdy świecą kosztem różnicy mas: cztery jądra wodoru łączą się w hel, a brakująca masa zamienia się w energię wedle E = Δmc². Synteza opłaca się energetycznie tylko do żelaza.",
  przyklad="Przy każdej syntezie helu z wodoru ubywa około 0,7% masy — to ta różnica zasila Słońce od miliardów lat."),
 "Materiały dodatkowe": dict(
  czego="Wzory z materiałów dodatkowych — rozszerzenia i wyprowadzenia poza głównym tokiem modułu.",
  kiedy="Autor umieszcza tu rzeczy potrzebne do zrozumienia wyprowadzeń: średnią ważoną, rachunek na wektorach, przekształcenia, których nie chciał wtrącać w tok wykładu. Na egzaminie zwykle nie są pytane wprost, ale pojawiają się w rachunkach.",
  przyklad="Do tej grupy trafia między innymi wyprowadzenie ruchu przyspieszonego po okręgu przez różniczkowanie współrzędnych x = R·cosφ, y = R·sinφ."),
 "Podsumowanie modułu": dict(
  czego="Zestawienie najważniejszych wzorów modułu w jednym miejscu.",
  kiedy="To gotowa ściąga przed egzaminem. Jeśli masz mało czasu, zacznij powtórkę właśnie od tych wzorów — autor wybrał je jako reprezentatywne dla całego modułu.",
  przyklad="Przejrzyj je na dzień przed egzaminem i sprawdź, czy przy każdym umiesz powiedzieć, co oznaczają symbole i kiedy wzór obowiązuje."),
 "Test kontrolny": dict(
  czego="Wzory pojawiające się w zadaniach testowych kończących moduł.",
  kiedy="Jeśli wzór trafił do zadania, to znaczy, że autor uważa jego zastosowanie za sprawdzian zrozumienia modułu.",
  przyklad="Warto przeliczyć odpowiadające zadanie z zakładki „Zadania z testów”."),
})
