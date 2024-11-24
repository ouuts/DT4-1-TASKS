import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

while True:
    lat_teksts = str(input("Ievadiet tekstu (raksti 'atā', lai pārtrauktu): "))
    
    if lat_teksts.lower() in ["atā", "ata"]:
        print("Uz redzēšanos!")
        break
        
    # Translate from Latvian to English
    eng_teksts = GoogleTranslator(source='lv', target='en').translate(lat_teksts)
    print(f"Tulkojums uz angļu: {eng_teksts}")
    
    # Analyze sentiment
    sentiment_dict = sia.polarity_scores(eng_teksts)
    compound = sentiment_dict['compound']
    
    if compound >= 0.05:
        print("Emocionālais noskaņojums: Pozitīvs")
    elif compound <= -0.05:
        print("Emocionālais noskaņojums: Negatīvs")
    else:
        print("Emocionālais noskaņojums: Neitrāls")
    print()
