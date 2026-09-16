package pl.maslak.fizykaquiz

import android.content.Context
import org.json.JSONObject

data class Modul(val id: String, val nazwa: String, val kolor: String, val rozdzialy: String)

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
    private var wczytany = false

    fun wczytaj(ctx: Context) {
        if (wczytany) return
        val root = JSONObject(ctx.assets.open("pytania.json").bufferedReader().use { it.readText() })

        root.getJSONObject("zrodlo").let {
            zrodloTytul = it.getString("tytul")
            zrodloLicencja = it.getString("licencja")
            zrodloUrl = it.getString("url")
        }

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
        wczytany = true
    }

    fun modul(id: String): Modul? = moduly.firstOrNull { it.id == id }
    fun filtruj(modul: String?): List<Pytanie> =
        pytania.filter { modul == null || it.modul == modul }
}
