package pl.maslak.fizykaquiz

import android.content.Context
import org.json.JSONObject

class Postepy(ctx: Context) {
    private val prefs = ctx.getSharedPreferences("postepy", Context.MODE_PRIVATE)
    private fun dane() = JSONObject(prefs.getString("pytania", "{}") ?: "{}")

    fun zapisz(id: String, dobrze: Boolean) {
        val d = dane()
        val w = if (d.has(id)) d.getJSONObject(id) else JSONObject().put("razem", 0).put("dobrze", 0)
        w.put("razem", w.getInt("razem") + 1)
        if (dobrze) w.put("dobrze", w.getInt("dobrze") + 1)
        prefs.edit().putString("pytania", d.put(id, w).toString()).apply()
    }

    fun bledne(): Set<String> {
        val d = dane()
        return d.keys().asSequence()
            .filter { d.getJSONObject(it).let { o -> o.getInt("dobrze") < o.getInt("razem") } }
            .toSet()
    }

    /** Zwraca (ile pytan przerobionych, dobrych odpowiedzi, wszystkich odpowiedzi). */
    fun statystyki(): Triple<Int, Int, Int> {
        val d = dane(); var r = 0; var db = 0; var u = 0
        d.keys().forEach { k -> d.getJSONObject(k).let { r += it.getInt("razem"); db += it.getInt("dobrze"); u++ } }
        return Triple(u, db, r)
    }

    /** Skutecznosc w obrebie jednego modulu — do paskow postepu w menu. */
    fun wgModulu(pytania: List<Pytanie>): Map<String, Pair<Int, Int>> {
        val d = dane()
        val out = HashMap<String, Pair<Int, Int>>()
        pytania.forEach { p ->
            if (d.has(p.id)) {
                val o = d.getJSONObject(p.id)
                val (db, r) = out.getOrDefault(p.modul, 0 to 0)
                out[p.modul] = (db + o.getInt("dobrze")) to (r + o.getInt("razem"))
            }
        }
        return out
    }

    fun wyczysc() = prefs.edit().clear().apply()
}
