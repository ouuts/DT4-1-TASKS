import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

def translate_and_analyze(text):

    translated_text = GoogleTranslator(source="lv", target="en").translate(text)
    print(f"Tulkojums uz angļu: {translated_text}")
    sentiment_dict = sia.polarity_scores(translated_text)
    compound = sentiment_dict["compound"]
    if compound >= 0.05:
        sentiment = "Pozitīvs"
    elif compound <= -0.05:
        sentiment = "Negatīvs"
    else:
        sentiment = "Neitrāls"
    print(f"Emocionālais noskaņojums: {sentiment}")
while True:
    text = input("Ievadiet tekstu (raksti atā, lai pārtrauktu): ").strip()
    
    if text.lower() == "atā":
        print("Uz redzēšanos!")
        break
    
    translate_and_analyze(text)
