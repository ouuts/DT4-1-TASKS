from langdetect import detect

# Loop to accept multiple inputs
while True:
    # Ask for user input
    text = input("Ievadiet tekstu (raksti atā, lai pārtrauktu): ")
    
    # Exit condition
    if text.lower() == "ata" or text.lower() == "atā":
        print("atā")
        break

    try:
        # Detect language
        detected_language = detect(text)
        print(f"valoda: {detected_language}")
    except Exception as e:
        print(f"Error detecting language: {e}")
