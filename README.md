# DT4-1

## Apraksts
Šis projekts ietver 10 Python skriptus, kas demonstrē dažādas teksta apstrādes, tulkošanas un mašīnmācīšanās funkcionalitātes. Projektā tiek izmantotas modernas NLP (dabiskās valodas apstrādes) bibliotēkas un rīki.

**Piezīme**: Dažas NLP bibliotēkas, piemēram, `spaCy`, var nebūt saderīgas ar Python 3.13. Lai izvairītos no problēmām, **ieteicams izmantot Python 3.12**.

---

## Funkcijas
- Vārdu biežuma analīze.
- Valodas noteikšana tekstam.
- Semantiskās līdzības aprēķins starp tekstiem.
- Sentimentu analīze un teksta tulkošana.
- Automātiska teksta ģenerēšana un rezumēšana.

---

## Instalācija

### Prasības
- **Python**: 3.12
- Nepieciešamās bibliotēkas:
  - `nltk`
  - `spacy`
  - `langdetect`
  - `deep-translator`
  - `transformers`
  - `gensim`
  - `scikit-learn`
  - `torch`
  - `numpy`

### Instalācijas soļi
1. Klonējiet repozitoriju:
   ```bash
   git clone https://github.com/ouuts/DT4-1.git

Uzdevumi un prasības
1. uzd1.py

Funkcija: Vārdu biežuma aprēķins tekstā, ignorējot pieturzīmes un lielos/malos burtus.
Nepieciešamās bibliotēkas: nltk
2. uzd2.py

Funkcija: Teksta valodas noteikšana.
Nepieciešamās bibliotēkas: langdetect
3. uzd3.py

Funkcija: Semantiskās līdzības noteikšana starp diviem tekstiem.
Nepieciešamās bibliotēkas: spacy

    Piezīme: Instalējiet angļu valodas modeli:

    python -m spacy download en_core_web_md

4. uzd4.py

Funkcija: Sentimenta analīze Latvijā rakstītam tekstam, izmantojot tulkojumu uz angļu valodu.
Nepieciešamās bibliotēkas: nltk, deep-translator

    Piezīme: Nodrošiniet, lai vader_lexicon ir lejupielādēts:

    import nltk
    nltk.download('vader_lexicon')

5. uzd5.py

Funkcija: Teksta attīrīšana, noņemot URL, simbolus un pārvēršot tekstu mazajiem burtiem.
Nepieciešamās bibliotēkas: Nav (izmanto tikai iebūvēto re moduli).
6. uzd6.py

Funkcija: Teksta rezumēšana, tulkojot starp latviešu un angļu valodu.
Nepieciešamās bibliotēkas: transformers, deep-translator

    Piezīme: Tiek izmantots facebook/bart-large-cnn modelis.

7. uzd7.py

Funkcija: Semantiskās līdzības aprēķins starp vārdiem, izmantojot Latvian FastText modeli.
Nepieciešamās bibliotēkas: gensim, scikit-learn, numpy

    Piezīme: Nodrošiniet, lai FastText modelis (cc.lv.300.bin) būtu pieejams.

8. uzd8.py

Funkcija: Personu un organizāciju nosaukumu atpazīšana latviešu tekstā, izmantojot spaCy.
Nepieciešamās bibliotēkas: spacy, deep-translator

    Piezīme: Lejupielādējiet spaCy angļu valodas modeli:

    python -m spacy download en_core_web_sm

9. uzd9.py

Funkcija: Automātiska stāstu ģenerēšana no sākuma frāzes.
Nepieciešamās bibliotēkas: transformers, torch, deep-translator

    Piezīme: Izmanto gpt2 modeli teksta ģenerēšanai.

10. uzd10.py

Funkcija: Teksta tulkošana starp latviešu un angļu valodu.
Nepieciešamās bibliotēkas: deep-translator
