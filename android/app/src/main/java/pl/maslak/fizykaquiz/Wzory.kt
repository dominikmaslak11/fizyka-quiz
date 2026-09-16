package pl.maslak.fizykaquiz

import android.content.Context
import android.graphics.BitmapFactory
import android.graphics.drawable.Drawable
import android.text.Spannable
import android.text.SpannableStringBuilder
import android.text.style.ImageSpan
import android.util.TypedValue
import androidx.core.graphics.drawable.toDrawable

/**
 * Podmienia znaczniki [[w_xxxx]] na obrazki wzorow zlozonych w LaTeX-u.
 *
 * Obrazki sa skalowane do wysokosci wiersza tekstu razy wspolczynnik, dzieki czemu
 * wzor rosnie razem z ustawiona w systemie wielkoscia czcionki.
 */
object Wzory {
    private val ZNACZNIK = Regex("""\[\[(w_[0-9a-f]+)]]""")
    private val pamiec = HashMap<String, Drawable?>()

    /**
     * Ile razy wiekszy od wysokosci czcionki ma byc firet wzoru.
     * 1.0 znaczy "wzor tej samej wielkosci co tekst wokol".
     */
    private const val SKALA = 1.05f

    private fun wczytaj(ctx: Context, nazwa: String): Drawable? = pamiec.getOrPut(nazwa) {
        try {
            ctx.assets.open("wzory/$nazwa.png").use { s ->
                BitmapFactory.decodeStream(s)?.toDrawable(ctx.resources)
            }
        } catch (e: Exception) {
            null
        }
    }

    /**
     * Zamienia tekst ze znacznikami na tekst z osadzonymi obrazkami.
     * [rozmiarTekstuPx] to wysokosc czcionki, do ktorej dopasowujemy wzory.
     */
    fun zloz(ctx: Context, tekst: String, rozmiarTekstuPx: Float): CharSequence {
        if (!ZNACZNIK.containsMatchIn(tekst)) return tekst

        val sb = SpannableStringBuilder()
        var pozycja = 0
        for (m in ZNACZNIK.findAll(tekst)) {
            sb.append(tekst, pozycja, m.range.first)
            val nazwa = m.groupValues[1]
            val d = wczytaj(ctx, nazwa)
            if (d == null) {
                sb.append("[wzór]")
            } else {
                // WSZYSTKIE wzory skalujemy tym samym wspolczynnikiem, liczonym z firetu.
                // Skalowanie do wspolnej wysokosci obrazka byloby bledem: wzor z ulamkiem
                // jest wyzszy, wiec wyszedlby drobniejszy od jednowierszowego.
                val skala = (rozmiarTekstuPx * SKALA) / Bank.emPx
                d.setBounds(0, 0, (d.intrinsicWidth * skala).toInt(),
                            (d.intrinsicHeight * skala).toInt())
                val start = sb.length
                sb.append("￼")   // znak zastepczy pod obrazek
                sb.setSpan(ImageSpan(d, ImageSpan.ALIGN_BASELINE),
                           start, sb.length, Spannable.SPAN_EXCLUSIVE_EXCLUSIVE)
            }
            pozycja = m.range.last + 1
        }
        sb.append(tekst, pozycja, tekst.length)
        return sb
    }

    fun sp(ctx: Context, sp: Float): Float = TypedValue.applyDimension(
        TypedValue.COMPLEX_UNIT_SP, sp, ctx.resources.displayMetrics)
}
