import spacy

# Ielāde valodas moduli. Diemžēl spacy nav lv modulis, bet tāpat strādā
nlp = spacy.load("en_core_web_md")
while True:
    text1 = input("Ievadiet pirmo tekstu: ")
    text2 = input("Ievadiet otro tekstu: ")

# Pārbauda tekstus
    doc1 = nlp(text1)
    doc2 = nlp(text2)

# Aprēķina līdzību
    similarity = doc1.similarity(doc2)
    print(f"Līdzība: {similarity * 100:.2f}%")
