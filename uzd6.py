from transformers import pipeline

# Load a pre-trained summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

raksts = input("Ievadi rakstu (atstāj tukšu piemēram):")
if raksts == "":
    raksts = """
    Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga,
    kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. Latvija robežojas ar Lietuvu, Igauniju un Krieviju, 
    kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm.
    """

summary = summarizer(raksts)
print(summary[0]['summary_text'])
