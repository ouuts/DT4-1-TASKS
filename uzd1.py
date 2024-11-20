from nltk.tokenize import TreebankWordTokenizer
from collections import Counter
import re

def biezzums(text):
    # .lower izdarā tā lai Kaķis un kaķis skaitas kopā
    text = text.lower()
    
    # izmantojam TreebankWordTokenizer
    tokenizer = TreebankWordTokenizer()
    words = tokenizer.tokenize(text)
    
    # Izfiltrē punktus un komatus
    words = [word for word in words if word not in ['.', ',']]
    
    # Saskaitā vārdu biežumu
    return dict(Counter(words))

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēgas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."

# analizē textu izmantojot funkciju biezzums
atbilde = biezzums(text)

# Izprintē rezultātus
for word, count in atbilde.items():
    print(f"{word}: {count}")
