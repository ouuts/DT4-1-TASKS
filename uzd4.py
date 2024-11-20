#Pagaidām nestrādā


from transformers import pipeline

# Use a pre-trained Latvian sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis", model="AiLab-IMCS-UL/lvbert")

while True:
    text = input("Ievadiet tekstu (raksti 'atā', lai pārtrauktu): ")
    if text.lower() in ["atā", "ata"]:
        print("Uz redzēšanos!")
        break

    # Analyze sentiment
    result = sentiment_analyzer(text)

    sentiment = result[0]['label']
    if sentiment == 'LABEL_1':  # Negative sentiment
        print("Emocionālais noskaņojums: Negatīvs")
    elif sentiment == 'LABEL_2':  # Neutral sentiment
        print("Emocionālais noskaņojums: Neitrāls")
    else:  # Positive sentiment
        print("Emocionālais noskaņojums: Pozitīvs")
