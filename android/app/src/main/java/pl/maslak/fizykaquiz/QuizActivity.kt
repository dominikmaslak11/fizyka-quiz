package pl.maslak.fizykaquiz

import android.graphics.BitmapFactory
import android.graphics.Color
import android.os.Bundle
import android.util.TypedValue
import android.view.Gravity
import android.view.View
import android.widget.*
import androidx.appcompat.app.AppCompatActivity

class QuizActivity : AppCompatActivity() {

    private lateinit var tryb: String
    private lateinit var pytania: List<Pytanie>
    private lateinit var postepy: Postepy

    private var nr = 0
    private val wybory = mutableMapOf<String, Int>()
    private var odpowiedziano = false

    private val LITERY = listOf("A", "B", "C", "D")
    private val PROG = 60      // fizyka jest trudniejsza od SEP-u, prog nizszy

    private lateinit var boxOdp: LinearLayout
    private lateinit var boxWyj: LinearLayout
    private lateinit var boxWynik: LinearLayout
    private lateinit var btnDalej: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_quiz)
        Bank.wczytaj(this)
        postepy = Postepy(this)

        tryb = intent.getStringExtra("tryb") ?: "nauka"
        val modul = intent.getStringExtra("modul")
        val ile = intent.getIntExtra("ile", 0)

        var pula = Bank.filtruj(modul)
        if (tryb == "bledy") {
            val b = postepy.bledne()
            pula = pula.filter { it.id in b }
        }
        pula = pula.shuffled()
        if (ile > 0 && ile < pula.size) pula = pula.take(ile)
        pytania = pula

        title = when (tryb) {
            "egzamin" -> "Egzamin próbny"; "bledy" -> "Powtórka błędów"; else -> "Tryb nauki"
        }
        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        boxOdp = findViewById(R.id.boxOdpowiedzi)
        boxWyj = findViewById(R.id.boxWyjasnienie)
        boxWynik = findViewById(R.id.boxWynik)
        btnDalej = findViewById(R.id.btnDalej)
        btnDalej.setOnClickListener { dalej() }

        if (pytania.isEmpty()) { pokazWynik(); return }
        pokazPytanie()
    }

    override fun onSupportNavigateUp(): Boolean { finish(); return true }

    private fun kolorModulu(m: String): Int =
        try { Color.parseColor(Bank.modul(m)?.kolor ?: "#1A365D") } catch (e: Exception) { Color.DKGRAY }

    private fun pokazPytanie() {
        val p = pytania[nr]
        odpowiedziano = false
        val kolor = kolorModulu(p.modul)

        findViewById<LinearLayout>(R.id.pasekGorny).setBackgroundColor(kolor)
        findViewById<TextView>(R.id.txtPostep).text = "Pytanie ${nr + 1} z ${pytania.size}"
        findViewById<ProgressBar>(R.id.pasek).apply { max = pytania.size; progress = nr }

        // ilustracja modulu — rysowana programowo przez narzedzia/grafiki.py
        findViewById<ImageView>(R.id.grafika).apply {
            try {
                assets.open("grafiki/${p.modul.lowercase()}.png").use {
                    setImageBitmap(BitmapFactory.decodeStream(it)); visibility = View.VISIBLE
                }
            } catch (e: Exception) { visibility = View.GONE }
        }

        findViewById<TextView>(R.id.txtMeta).apply {
            text = "${p.modul} · ${Bank.modul(p.modul)?.nazwa ?: ""}"
            setTextColor(kolor)
        }

        val rozmiar = Wzory.sp(this, 17f)
        findViewById<TextView>(R.id.txtPytanie).text = Wzory.zloz(this, p.tresc, rozmiar)

        boxWyj.visibility = View.GONE
        btnDalej.visibility = View.GONE
        findViewById<ScrollView>(R.id.scroll).scrollTo(0, 0)

        boxOdp.removeAllViews()
        val rozmiarOdp = Wzory.sp(this, 15f)
        p.odpowiedzi.forEachIndexed { i, tresc ->
            val b = Button(this).apply {
                text = TextUtilsPrefix(LITERY[i], Wzory.zloz(this@QuizActivity, tresc, rozmiarOdp))
                gravity = Gravity.START or Gravity.CENTER_VERTICAL
                isAllCaps = false
                setTextSize(TypedValue.COMPLEX_UNIT_SP, 15f)
                setTextColor(resources.getColor(R.color.tekst, null))
                setBackgroundResource(R.drawable.tlo_odpowiedzi)
                setPadding(28, 30, 28, 30)
                layoutParams = LinearLayout.LayoutParams(
                    LinearLayout.LayoutParams.MATCH_PARENT,
                    LinearLayout.LayoutParams.WRAP_CONTENT).apply { topMargin = 14 }
                setOnClickListener { wybierz(i) }
            }
            boxOdp.addView(b)
        }
    }

    /** Skleja literę odpowiedzi z treścią, która może zawierać obrazki wzorów. */
    private fun TextUtilsPrefix(litera: String, tresc: CharSequence): CharSequence =
        android.text.SpannableStringBuilder("$litera)  ").append(tresc)

    private fun wybierz(w: Int) {
        if (odpowiedziano) return
        odpowiedziano = true
        val p = pytania[nr]
        val dobrze = w == p.poprawna
        wybory[p.id] = w
        postepy.zapisz(p.id, dobrze)

        for (i in 0 until boxOdp.childCount) boxOdp.getChildAt(i).isEnabled = false

        if (tryb == "egzamin") {
            boxOdp.getChildAt(w).setBackgroundResource(R.drawable.tlo_odpowiedzi_ok)
        } else {
            boxOdp.getChildAt(p.poprawna).setBackgroundResource(R.drawable.tlo_odpowiedzi_ok)
            if (!dobrze) boxOdp.getChildAt(w).setBackgroundResource(R.drawable.tlo_odpowiedzi_zle)

            findViewById<TextView>(R.id.txtWerdykt).apply {
                text = if (dobrze) "✓ Dobrze" else "✗ Źle"
                setTextColor(resources.getColor(if (dobrze) R.color.ok else R.color.zle, null))
            }
            findViewById<TextView>(R.id.txtWyjasnienie).text =
                Wzory.zloz(this, p.wyjasnienie, Wzory.sp(this, 14f))
            findViewById<TextView>(R.id.txtRozdzial).text =
                "Podręcznik Kąkola, rozdz. ${p.rozdzial} · moduł ${p.modul}"
            boxWyj.visibility = View.VISIBLE
        }

        btnDalej.setBackgroundColor(kolorModulu(p.modul))
        btnDalej.text = if (nr == pytania.size - 1) "ZAKOŃCZ I POKAŻ WYNIK" else "DALEJ"
        btnDalej.visibility = View.VISIBLE
    }

    private fun dalej() { if (nr < pytania.size - 1) { nr++; pokazPytanie() } else pokazWynik() }

    private fun pokazWynik() {
        boxOdp.removeAllViews()
        boxWyj.visibility = View.GONE
        findViewById<ImageView>(R.id.grafika).visibility = View.GONE
        findViewById<TextView>(R.id.txtMeta).text = ""

        if (pytania.isEmpty()) {
            findViewById<TextView>(R.id.txtPostep).text = "Brak pytań"
            findViewById<TextView>(R.id.txtPytanie).text =
                "Nie ma błędów do powtórki — rozwiąż najpierw kilka pytań."
            btnDalej.visibility = View.GONE
            return
        }

        val dobre = pytania.count { wybory[it.id] == it.poprawna }
        val proc = dobre * 100 / pytania.size
        findViewById<TextView>(R.id.txtPostep).text = "Koniec"
        findViewById<ProgressBar>(R.id.pasek).progress = pytania.size
        findViewById<TextView>(R.id.txtPytanie).apply {
            text = "Wynik: $dobre / ${pytania.size}  ($proc%)"
            setTextColor(resources.getColor(if (proc >= PROG) R.color.ok else R.color.zle, null))
        }

        boxWynik.removeAllViews()
        boxWynik.visibility = View.VISIBLE

        val zle = pytania.filter { wybory[it.id] != it.poprawna }
        if (zle.isNotEmpty()) {
            val wgModulu = zle.groupingBy { it.modul }.eachCount().toList().sortedByDescending { it.second }
            boxWynik.addView(naglowek("CZEGO SIĘ DOUCZYĆ"))
            wgModulu.forEach { (m, n) ->
                boxWynik.addView(TextView(this).apply {
                    text = "  ${Bank.modul(m)?.nazwa ?: m}:  $n"
                    setTextColor(kolorModulu(m)); textSize = 13f
                    setPadding(0, 3, 0, 3)
                })
            }
            boxWynik.addView(naglowek("OMÓWIENIE BŁĘDÓW"))
            zle.forEach { p ->
                boxWynik.addView(TextView(this).apply {
                    text = Wzory.zloz(this@QuizActivity, p.tresc, Wzory.sp(this@QuizActivity, 14f))
                    setTextColor(resources.getColor(R.color.tekst, null)); textSize = 14f
                    setTypeface(typeface, android.graphics.Typeface.BOLD)
                    setPadding(0, 14, 0, 4)
                })
                wybory[p.id]?.let { w ->
                    boxWynik.addView(TextView(this).apply {
                        text = Wzory.zloz(this@QuizActivity, "Twoja: " + p.odpowiedzi[w], Wzory.sp(this@QuizActivity, 13f))
                        setTextColor(resources.getColor(R.color.zle, null)); textSize = 13f
                    })
                }
                boxWynik.addView(TextView(this).apply {
                    text = Wzory.zloz(this@QuizActivity, "Poprawna: " + p.odpowiedzi[p.poprawna], Wzory.sp(this@QuizActivity, 13f))
                    setTextColor(resources.getColor(R.color.ok, null)); textSize = 13f
                })
                boxWynik.addView(TextView(this).apply {
                    text = Wzory.zloz(this@QuizActivity, p.wyjasnienie, Wzory.sp(this@QuizActivity, 13f))
                    setTextColor(resources.getColor(R.color.szary, null)); textSize = 13f
                    setPadding(0, 4, 0, 0)
                })
            }
        } else {
            boxWynik.addView(TextView(this).apply {
                text = "Komplet poprawnych odpowiedzi."
                setTextColor(resources.getColor(R.color.ok, null)); textSize = 15f
                setPadding(0, 12, 0, 0)
            })
        }

        btnDalej.apply {
            text = "WRÓĆ DO MENU"; visibility = View.VISIBLE
            setBackgroundColor(resources.getColor(R.color.akcent, null))
            setOnClickListener { finish() }
        }
    }

    private fun naglowek(t: String) = TextView(this).apply {
        text = t
        setTextColor(resources.getColor(R.color.szary, null))
        textSize = 11f
        setTypeface(typeface, android.graphics.Typeface.BOLD)
        setPadding(0, 18, 0, 4)
    }
}
