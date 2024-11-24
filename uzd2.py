from langdetect import detect

while True:
    # Lietotājs ievada tekstu
    text = input("Ievadiet tekstu (raksti 'atā', lai pārtrauktu): ").strip()
    
    # Vai lietotājs grib beigt ciklu (ievadot "atā")
    if text.lower() == "atā":
        print("atā")
        break

    # Nosakām valodu, izmantojot langdetect
    detected_language = detect(text)
    
    # Izvada valodu
    print(f"valoda: {detected_language}")
