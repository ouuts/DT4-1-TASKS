from transformers import pipeline
from deep_translator import GoogleTranslator

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Input the article
raksts = input("Ievadi rakstu (atstāj tukšu piemēram):")
if raksts == "":
    raksts = """
    Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga,
    kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. Latvija robežojas ar Lietuvu, Igauniju un Krieviju, 
    kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm.
    """

# Translate the input article to English
translated_to_en = GoogleTranslator(source='lv', target='en').translate(raksts)

# Summarize the translated article
summary = summarizer(translated_to_en, min_length=10, max_length=30)

# Translate the summary back to Latvian
translated_to_lv = GoogleTranslator(source='en', target='lv').translate(summary[0]['summary_text'])

# Print the final summary in Latvian
print(translated_to_lv)
