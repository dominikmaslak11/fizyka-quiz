package pl.maslak.fizykaquiz

import android.app.AlertDialog
import android.content.Intent
import android.graphics.Color
import android.os.Bundle
import android.view.Gravity
import android.view.View
import android.widget.*
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    private lateinit var modulyKlucze: List<String?>
    private val ileOpcje = listOf(10, 20, 30, 0)

    private lateinit var spModul: Spinner
    private lateinit var spIle: Spinner

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        Bank.wczytaj(this)

        spModul = findViewById(R.id.spModul)
        spIle = findViewById(R.id.spIle)

        modulyKlucze = listOf<String?>(null) + Bank.moduly.map { it.id }
        spModul.adapter = adapter(modulyKlucze.map { k ->
            if (k == null) "Wszystkie moduły" else Bank.modul(k)!!.let { "${it.id} · ${it.nazwa}" }
        })
        spIle.adapter = adapter(ileOpcje.map { if (it == 0) "Wszystkie" else "$it pytań" })
        spIle.setSelection(1)

        spModul.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(p: AdapterView<*>?, v: View?, i: Int, id: Long) = pokazPule()
            override fun onNothingSelected(p: AdapterView<*>?) {}
        }

        findViewById<Button>(R.id.btnNauka).setOnClickListener { start("nauka") }
        findViewById<Button>(R.id.btnEgzamin).setOnClickListener { start("egzamin") }
        findViewById<Button>(R.id.btnBledy).setOnClickListener { start("bledy") }
        findViewById<Button>(R.id.btnReset).setOnClickListener { potwierdzReset() }

        // Materiał z podręcznika — ten sam filtr modułu co dla quizu.
        mapOf(R.id.btnWzory to "wzory", R.id.btnDefinicje to "definicje",
              R.id.btnPrawa to "prawa", R.id.btnZadania to "zadania").forEach { (id, rodzaj) ->
            findViewById<Button>(id).setOnClickListener {
                startActivity(Intent(this, MaterialyActivity::class.java).apply {
                    putExtra("rodzaj", rodzaj)
                    putExtra("modul", wybranyModul())
                })
            }
        }

        findViewById<TextView>(R.id.txtZrodlo).text =
            "Na podstawie: ${Bank.zrodloTytul}, AGH Kraków 2023 — licencja ${Bank.zrodloLicencja}.\n" +
            "${Bank.zrodloUrl}\nWzory składane w LaTeX-u. Aplikacja działa bez internetu."
    }

    override fun onResume() {
        super.onResume()
        pokazPule()
        val (u, db, r) = Postepy(this).statystyki()
        findViewById<TextView>(R.id.txtPodsumowanie).text =
            if (r == 0) "${Bank.pytania.size} pytań · ${Bank.kluczowe.size} wzorów · " +
                        "${Bank.definicje.size} definicji · ${Bank.prawa.size} praw · ${Bank.zadania.size} zadań"
            else "${Bank.pytania.size} pytań · przerobione $u · skuteczność ${db * 100 / r}% ($db/$r)"
        rysujModuly()
    }

    private fun adapter(poz: List<String>) =
        ArrayAdapter(this, android.R.layout.simple_spinner_item, poz).apply {
            setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        }

    private fun wybranyModul() = modulyKlucze[spModul.selectedItemPosition]

    private fun pokazPule() {
        val n = Bank.filtruj(wybranyModul()).size
        val b = Postepy(this).bledne().size
        findViewById<TextView>(R.id.txtPula).text =
            "Pasujących pytań: $n" + if (b > 0) "   ·   do powtórki: $b" else ""
        findViewById<Button>(R.id.btnBledy).isEnabled = b > 0
    }

    /** Pasek skuteczności dla każdego modułu, w kolorze tego modułu. */
    private fun rysujModuly() {
        val box = findViewById<LinearLayout>(R.id.boxModuly)
        box.removeAllViews()
        val staty = Postepy(this).wgModulu(Bank.pytania)
        Bank.moduly.forEach { m ->
            val (db, r) = staty[m.id] ?: (0 to 0)
            val kolor = try { Color.parseColor(m.kolor) } catch (e: Exception) { Color.GRAY }

            val wiersz = LinearLayout(this).apply {
                orientation = LinearLayout.HORIZONTAL
                gravity = Gravity.CENTER_VERTICAL
                setPadding(0, 6, 0, 6)
            }
            wiersz.addView(TextView(this).apply {
                text = m.id; setTextColor(kolor); textSize = 12f
                setTypeface(typeface, android.graphics.Typeface.BOLD)
                layoutParams = LinearLayout.LayoutParams(dp(48), LinearLayout.LayoutParams.WRAP_CONTENT)
            })
            wiersz.addView(TextView(this).apply {
                text = m.nazwa; setTextColor(resources.getColor(R.color.tekst, null)); textSize = 12f
                layoutParams = LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.WRAP_CONTENT, 1f)
            })
            wiersz.addView(ProgressBar(this, null, android.R.attr.progressBarStyleHorizontal).apply {
                max = 100
                progress = if (r > 0) db * 100 / r else 0
                progressDrawable?.setTint(kolor)
                layoutParams = LinearLayout.LayoutParams(dp(70), dp(6))
            })
            wiersz.addView(TextView(this).apply {
                text = if (r > 0) "  $db/$r" else "  —"
                setTextColor(resources.getColor(R.color.szary, null)); textSize = 11f
                layoutParams = LinearLayout.LayoutParams(dp(46), LinearLayout.LayoutParams.WRAP_CONTENT)
            })
            box.addView(wiersz)
        }
    }

    private fun dp(v: Int) = (v * resources.displayMetrics.density).toInt()

    private fun start(tryb: String) {
        if (Bank.filtruj(wybranyModul()).isEmpty()) {
            Toast.makeText(this, "Brak pytań dla tego wyboru.", Toast.LENGTH_SHORT).show(); return
        }
        startActivity(Intent(this, QuizActivity::class.java).apply {
            putExtra("tryb", tryb)
            putExtra("modul", wybranyModul())
            putExtra("ile", ileOpcje[spIle.selectedItemPosition])
        })
    }

    private fun potwierdzReset() {
        AlertDialog.Builder(this)
            .setTitle("Wyczyścić postępy?")
            .setMessage("Skasuje to historię odpowiedzi i listę błędów. Pytań to nie usuwa.")
            .setPositiveButton("Wyczyść") { _, _ -> Postepy(this).wyczysc(); onResume() }
            .setNegativeButton("Anuluj", null).show()
    }
}
