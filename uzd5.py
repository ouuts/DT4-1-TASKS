import re

def notiri_text(text):
    cleaned = re.sub(r'http\S+|[@!]', '', text)
    cleaned = cleaned.lower()
    return cleaned

while True:

    teksts = input("Ieraksti tekstu (atstāj tukšu priekš piemēra): ").strip()
    if not teksts:
        teksts = "@John: Šis ir lielisks produkts!!! Vai ne? 👏 👏 👏 http://example.com"
        print(f"Piemērs: {teksts}")
    
    result = notiri_text(teksts)
    print(f"Notīrīts teksts: {result}")
