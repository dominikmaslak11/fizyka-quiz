package pl.maslak.fizykaquiz

import android.graphics.BitmapFactory
import android.graphics.Color
import android.graphics.Typeface
import android.os.Bundle
import android.util.TypedValue
import android.view.View
import android.widget.*
import androidx.appcompat.app.AppCompatActivity

/**
 * Przeglądarka materiału z podręcznika: wzory kluczowe, definicje, prawa i zadania.
 *
 * Wszystko rysowane w kodzie, bo liczba pozycji jest z góry znana i niewielka
 * (najwięcej 310 wzorów), a ScrollView z LinearLayout jest prostszy i mniej zawodny
 * niż RecyclerView przy tak statycznej liście.
 */
class MaterialyActivity : AppCompatActivity() {

    private lateinit var rodzaj: String
    private var modul: String? = null
    private lateinit var box: LinearLayout

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        Bank.wczytaj(this)
        rodzaj = intent.getStringExtra("rodzaj") ?: "wzory"
        modul = intent.getStringExtra("modul")

        val scroll = ScrollView(this)
        box = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(dp(14), dp(10), dp(14), dp(24))
        }
        scroll.addView(box)
        setContentView(scroll)

        title = when (rodzaj) {
            "definicje" -> "Definicje"
            "prawa" -> "Prawa i twierdzenia"
            "zadania" -> "Zadania z testów"
            else -> "Wzory kluczowe"
        }
        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        when (rodzaj) {
            "wzory" -> rysujWzory()
            "zadania" -> rysujWpisy(Bank.zadania, zadanie = true)
            "definicje" -> rysujWpisy(Bank.definicje)
            else -> rysujWpisy(Bank.prawa)
        }
    }

    override fun onSupportNavigateUp(): Boolean { finish(); return true }

    private fun dp(v: Int) = (v * resources.displayMetrics.density).toInt()

    /** Rozdzielczość, w jakiej narzedzia/wyciag_pdf.py wycina wzory ze stron podręcznika. */
    private val DPI_WYCINKA = 150
    private fun kolor(m: String) =
        try { Color.parseColor(Bank.modul(m)?.kolor ?: "#1A365D") } catch (e: Exception) { Color.DKGRAY }

    private fun naglowekModulu(m: String, ile: Int) {
        box.addView(TextView(this).apply {
            text = "${Bank.modul(m)?.nazwa ?: m}   ·   $ile"
            setTextColor(kolor(m))
            setTextSize(TypedValue.COMPLEX_UNIT_SP, 13f)
            setTypeface(typeface, Typeface.BOLD)
            setPadding(0, dp(18), 0, dp(6))
        })
        box.addView(View(this).apply {
            setBackgroundColor(kolor(m))
            layoutParams = LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, dp(2))
        })
    }

    private fun rysujWzory() {
        val wg = Bank.kluczowe.filter { modul == null || it.modul == modul }.groupBy { it.modul }
        if (wg.isEmpty()) { pusto("Brak wzorów."); return }
        box.addView(wstep("Wzory wyróżnione w podręczniku żółtym tłem — zdaniem autora najważniejsze."))
        Bank.moduly.forEach { m ->
            val lista = wg[m.id] ?: return@forEach
            naglowekModulu(m.id, lista.size)
            lista.forEach { w ->
                box.addView(ImageView(this).apply {
                    try {
                        assets.open("kluczowe/${w.plik}.png").use {
                            setImageBitmap(BitmapFactory.decodeStream(it))
                        }
                    } catch (e: Exception) { }
                    adjustViewBounds = true
                    scaleType = ImageView.ScaleType.FIT_START
                    // Wycinki powstaly przy 150 dpi. Skalujemy je wedlug gestosci ekranu,
                    // a nie na cala szerokosc — inaczej krotki wzor zostalby rozciagniety
                    // i rozmyty, a dlugi i krotki mialyby rozna wielkosc czcionki.
                    val dostepne = resources.displayMetrics.widthPixels - dp(28)
                    val docelowa = (w.w * resources.displayMetrics.densityDpi / DPI_WYCINKA)
                        .coerceAtMost(dostepne)
                    layoutParams = LinearLayout.LayoutParams(
                        docelowa, LinearLayout.LayoutParams.WRAP_CONTENT
                    ).apply { topMargin = dp(10) }
                })
                box.addView(TextView(this).apply {
                    text = "str. ${w.strona}"
                    setTextColor(resources.getColor(R.color.szary, null))
                    setTextSize(TypedValue.COMPLEX_UNIT_SP, 10f)
                })
            }
        }
        box.addView(stopka())
    }

    private fun rysujWpisy(zrodlo: List<Wpis>, zadanie: Boolean = false) {
        val wg = zrodlo.filter { modul == null || it.modul == modul }.groupBy { it.modul }
        if (wg.isEmpty()) { pusto("Brak pozycji."); return }
        box.addView(wstep(
            if (zadanie) "Zadania kończące moduły w podręczniku. To zadania otwarte — " +
                         "podręcznik nie podaje do nich rozwiązań."
            else "Wyciąg z podręcznika, w oryginalnym brzmieniu."))
        Bank.moduly.forEach { m ->
            val lista = wg[m.id] ?: return@forEach
            naglowekModulu(m.id, lista.size)
            lista.forEach { w ->
                val karta = LinearLayout(this).apply {
                    orientation = LinearLayout.VERTICAL
                    setBackgroundResource(R.drawable.tlo_karty)
                    setPadding(dp(12), dp(10), dp(12), dp(10))
                    layoutParams = LinearLayout.LayoutParams(
                        LinearLayout.LayoutParams.MATCH_PARENT,
                        LinearLayout.LayoutParams.WRAP_CONTENT).apply { topMargin = dp(8) }
                }
                val tytul = if (zadanie) "Zadanie ${w.nr}"
                            else w.kontekst.takeIf { it.length in 6..120 && !it.endsWith(".") } ?: ""
                if (tytul.isNotBlank()) {
                    karta.addView(TextView(this).apply {
                        text = tytul
                        setTextColor(kolor(m.id))
                        setTextSize(TypedValue.COMPLEX_UNIT_SP, 12f)
                        setTypeface(typeface, Typeface.BOLD)
                    })
                }
                karta.addView(TextView(this).apply {
                    text = w.tresc
                    setTextColor(resources.getColor(R.color.tekst, null))
                    setTextSize(TypedValue.COMPLEX_UNIT_SP, 14f)
                    setLineSpacing(0f, 1.25f)
                    setPadding(0, if (tytul.isNotBlank()) dp(4) else 0, 0, 0)
                })
                karta.addView(TextView(this).apply {
                    text = "str. ${w.strona}"
                    setTextColor(resources.getColor(R.color.szary, null))
                    setTextSize(TypedValue.COMPLEX_UNIT_SP, 10f)
                    setPadding(0, dp(4), 0, 0)
                })
                box.addView(karta)
            }
        }
        box.addView(stopka())
    }

    private fun wstep(t: String) = TextView(this).apply {
        text = t
        setTextColor(resources.getColor(R.color.szary, null))
        setTextSize(TypedValue.COMPLEX_UNIT_SP, 12f)
        setLineSpacing(0f, 1.2f)
    }

    private fun stopka() = TextView(this).apply {
        text = "Źródło: ${Bank.zrodloTytul}, AGH Kraków 2023 · licencja ${Bank.zrodloLicencja}"
        setTextColor(resources.getColor(R.color.szary, null))
        setTextSize(TypedValue.COMPLEX_UNIT_SP, 10f)
        setPadding(0, dp(22), 0, 0)
    }

    private fun pusto(t: String) = box.addView(wstep(t))
}
