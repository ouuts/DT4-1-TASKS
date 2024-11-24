import spacy
from deep_translator import GoogleTranslator

def find_entities(text):
    # Tulkojam tekstu uz angļu valodu
    eng_text = GoogleTranslator(source='lv', target='en').translate(text)
    
    # Ielādējam angļu modeli
    nlp = spacy.load("en_core_web_sm")
    
    # Apstrādājam tekstu
    doc = nlp(eng_text)
    
    # Izveidojam sarakstus katram entitātes tipam
    personas = []
    organizacijas = []
    
    # Meklējam entitātes
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            # Tulkojam atpakaļ uz latviešu valodu
            lat_ent = GoogleTranslator(source='en', target='lv').translate(ent.text)
            personas.append(lat_ent)
        elif ent.label_ == "ORG":
            # Tulkojam atpakaļ uz latviešu valodu
            lat_ent = GoogleTranslator(source='en', target='lv').translate(ent.text)
            organizacijas.append(lat_ent)
            
    return personas, organizacijas

while True:
    # Ievade
    text = input("\nIevadiet tekstu (vai 'exit' lai beigtu): ")
    
    if text.lower() == 'exit':
        print("Programma beigta!")
        break
        
    if text == "":
        text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."
        print(f"Izmantojam piemēra tekstu: {text}")
    
    # Atrodam entitātes
    personas, organizacijas = find_entities(text)
    
    # Izvadām rezultātus
    print("\nAtrastās entitātes:")
    print("Personas:", ', '.join(personas) if personas else "Nav atrasts")
    print("Organizācijas:", ', '.join(organizacijas) if organizacijas else "Nav atrasts")
