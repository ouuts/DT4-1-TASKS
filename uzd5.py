#pagaidām neizmanto nekādu NLP
import re

def notiri_text(text):
    # Noņem URL un izvēlētos simbolus
    notirits = re.sub(r'http\S*|[@!]|', '', text)
   
    # Pārveido uz mazajiem burtiem
    mazi_burti = notirits.lower()
    return mazi_burti

while True:
    # Piemērs
    input_text = input("Ieraksti tekstu (atstāj tukšu priekš piemēra): ")
    if input_text == "":
        input_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏 👏 👏 http://example.com"
    result = notiri_text(input_text)
    print(result)
