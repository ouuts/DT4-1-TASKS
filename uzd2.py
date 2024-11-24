from langdetect import detect

while True:

    text = input("Ievadiet tekstu (raksti atā, lai pārtrauktu): ").strip()
    
    if text.lower() == "atā":
        print("Uz redzēšanos!")
        break

    detected_language = detect(text)
    
    print(f"valoda: {detected_language}")
