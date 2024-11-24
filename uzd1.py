from nltk.tokenize import TreebankWordTokenizer
from collections import Counter
import re

def biezzums(text):

    text = text.lower()
    tokenizer = TreebankWordTokenizer()
    words = tokenizer.tokenize(text)
    words = [word for word in words if word not in [".", ","]]
    return dict(Counter(words))

text = input("Ievadi tekstu (atstāj tukšu priekš piemēra): ").strip()
if not text:
    text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēgas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."
    print(text)

atbilde = biezzums(text)

for word, count in atbilde.items():
    print(f"{word}: {count}")
