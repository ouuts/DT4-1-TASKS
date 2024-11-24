import spacy
from deep_translator import GoogleTranslator

def find_entities(text):

    eng_text = GoogleTranslator(source="lv", target="en").translate(text)

    nlp = spacy.load("en_core_web_sm")

    doc = nlp(eng_text)

    personas = []
    organizacijas = []

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            lat_ent = GoogleTranslator(source="en", target="lv").translate(ent.text)
            personas.append(lat_ent)
        elif ent.label_ == "ORG":
            lat_ent = GoogleTranslator(source="en", target="lv").translate(ent.text)
            organizacijas.append(lat_ent)
            
    return personas, organizacijas

while True:

    text = input("\nIevadiet tekstu (vai ata lai beigtu, vai atstāj tukšu piemēram): ").strip()
    
    if text.lower() == "atā":
        print("Uz redzēšanos!")
        break
        
    if not text:
        text = "Valsts prezidents Edgars Rinkēvičs piedalījās pasākumā, ko organizēja Latvijas Universitāte."
        print(f"Izmantojam piemēra tekstu: {text}")

    personas, organizacijas = find_entities(text)

    print("Personas:", ", ".join(personas) if personas else "Nav atrasts")
    print("Organizācijas:", ", ".join(organizacijas) if organizacijas else "Nav atrasts")
