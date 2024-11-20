#NAV LATVIEŠU VALODĀĀĀĀ

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer() 

while True:
    text = input("Ievadiet tekstu (raksti 'atā', lai pārtrauktu): ")
    if text.lower() in ["atā", "ata"]:
        print("Uz redzēšanos!")
        break

    sentiment_dict = sia.polarity_scores(text)
    compound = sentiment_dict['compound']

    if compound >= 0.05:
        print("Emocionālais noskaņojs: Pozitīvs")
    elif compound <= -0.05:
        print("Emocionālais noskaņojums: Negatīvs")
    else:
        print("Emocionālais noskaņojums: Neitrāls")
