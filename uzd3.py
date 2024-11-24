import spacy

nlp = spacy.load("en_core_web_md")

text1 = input("Ievadiet pirmo tekstu: ").strip()
text2 = input("Ievadiet otro tekstu: ").strip()

doc1 = nlp(text1)
doc2 = nlp(text2)

similarity = doc1.similarity(doc2)
print(f"Līdzība: {similarity * 100:.2f}%")
