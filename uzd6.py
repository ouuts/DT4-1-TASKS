from transformers import pipeline
from deep_translator import GoogleTranslator


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_and_translate(text):

    translated_to_en = GoogleTranslator(source='lv', target='en').translate(text)
    summary = summarizer(translated_to_en, min_length=10, max_length=30)
    translated_to_lv = GoogleTranslator(source='en', target='lv').translate(summary[0]['summary_text'])
    return translated_to_lv

raksts = input("Ievadi rakstu (atstāj tukšu piemēram): ").strip()
if not raksts:
    raksts = """
    Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga,
    kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. Latvija robežojas ar Lietuvu, Igauniju un Krieviju, 
    kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm.
    """
    print(f"Piemērs: {raksts}")

final_summary = summarize_and_translate(raksts)

print(f"Kopsavilkums: {final_summary}")
