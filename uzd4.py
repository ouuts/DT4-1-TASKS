import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

while True:
    teksts = str(input("Ievadiet tekstu (raksti 'atā', lai pārtrauktu): "))
    
    if teksts.lower() in ["atā", "ata"]:
        print("Uz redzēšanos!")
        break

    text = GoogleTranslator(source='lv', target='en').translate(teksts)
    print(f"Tulkojums uz angļu: {text}")
    
    sentiment_dict = sia.polarity_scores(text)
    compound = sentiment_dict['compound']
    
    if compound >= 0.05:
        print("Emocionālais noskaņojums: Pozitīvs")
    elif compound <= -0.05:
        print("Emocionālais noskaņojums: Negatīvs")
    else:
        print("Emocionālais noskaņojums: Neitrāls")
    print()
