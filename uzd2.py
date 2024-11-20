from langdetect import detect

while True:
    # Lietotājs ievada tekstu
    text = input("Ievadiet tekstu (raksti atā, lai pārtrauktu): ")
    
    # Vai lietotājs grib beigt ciklu (ievadot "ata" vai "atā")
    if text.lower() == "ata" or text.lower() == "atā":
        print("atā")
        break

    try:
        # Nosakām valodu, izmantojot langdetect
        detected_language = detect(text)
        
        # Izvada valodu
        print(f"valoda: {detected_language}")
    
    # Pārbauda kļūdas, piemēram, tukšs input)
    except Exception as e:
        print(f"Kļūda: {e}")  # Izvade: Kļūdas ziņojums, ja tiek izsists izņēmums
