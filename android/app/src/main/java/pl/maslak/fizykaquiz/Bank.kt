package pl.maslak.fizykaquiz

import android.content.Context
import org.json.JSONObject

data class Modul(val id: String, val nazwa: String, val kolor: String, val rozdzialy: String)

/** Wzór wyróżniony przez autora żółtym tłem — wycinek ze strony podręcznika. */
data class Wzor(val plik: String, val modul: String, val strona: Int, val w: Int, val h: Int)

/** Definicja, prawo albo zadanie z testu — tekst wyciągnięty z podręcznika. */
data class Wpis(val id: String, val modul: String, val strona: Int,
                val kontekst: String, val tresc: String, val nr: Int = 0)

data class Pytanie(
    val id: String,
    val modul: String,
    val rozdzial: String,
    val tresc: String,
    val odpowiedzi: List<String>,
    val poprawna: Int,
    val wyjasnienie: String
)

/** Bank wczytywany raz z assets/pytania.json — ten sam plik, ktory generuje narzedzia/zbuduj.py. */
object Bank {
    lateinit var pytania: List<Pytanie>; private set
    lateinit var moduly: List<Modul>; private set
    lateinit var zrodloTytul: String; private set
    lateinit var zrodloLicencja: String; private set
    lateinit var zrodloUrl: String; private set
    /** Ile pikseli ma firet na obrazkach wzorów — stałe dla całego banku. */
    var emPx: Float = 70f; private set
    lateinit var kluczowe: List<Wzor>; private set
    lateinit var definicje: List<Wpis>; private set
    lateinit var prawa: List<Wpis>; private set
    lateinit var zadania: List<Wpis>; private set
    private var wczytany = false

    fun wczytaj(ctx: Context) {
        if (wczytany) return
        val root = JSONObject(ctx.assets.open("pytania.json").bufferedReader().use { it.readText() })

        root.getJSONObject("zrodlo").let {
            zrodloTytul = it.getString("tytul")
            zrodloLicencja = it.getString("licencja")
            zrodloUrl = it.getString("url")
        }

        emPx = root.optDouble("em_px", 70.0).toFloat()

        moduly = root.getJSONArray("moduly").let { a ->
            (0 until a.length()).map { i ->
                val m = a.getJSONObject(i)
                Modul(m.getString("id"), m.getString("nazwa"), m.getString("kolor"),
                      m.optString("rozdzialy", ""))
            }
        }

        pytania = root.getJSONArray("pytania").let { a ->
            (0 until a.length()).map { i ->
                val p = a.getJSONObject(i)
                val odp = p.getJSONArray("odpowiedzi").let { o -> (0 until o.length()).map { o.getString(it) } }
                Pytanie(p.getString("id"), p.getString("modul"), p.optString("rozdzial", ""),
                        p.getString("pytanie"), odp, p.getInt("poprawna"), p.getString("wyjasnienie"))
            }
        }
        kluczowe = root.optJSONArray("kluczowe")?.let { a ->
            (0 until a.length()).map { i ->
                val w = a.getJSONObject(i)
                Wzor(w.getString("plik"), w.optString("modul", "M1"),
                     w.optInt("strona"), w.optInt("w"), w.optInt("h"))
            }
        } ?: emptyList()

        definicje = wpisy(root, "definicje")
        prawa = wpisy(root, "prawa")
        zadania = wpisy(root, "zadania")

        wczytany = true
    }

    private fun wpisy(root: JSONObject, klucz: String): List<Wpis> =
        root.optJSONArray(klucz)?.let { a ->
            (0 until a.length()).map { i ->
                val o = a.getJSONObject(i)
                Wpis(o.optString("id"), o.optString("modul", "M1"), o.optInt("strona"),
                     o.optString("kontekst", ""), o.optString("tresc"), o.optInt("nr", 0))
            }
        } ?: emptyList()

    fun modul(id: String): Modul? = moduly.firstOrNull { it.id == id }
    fun filtruj(modul: String?): List<Pytanie> =
        pytania.filter { modul == null || it.modul == modul }
}
