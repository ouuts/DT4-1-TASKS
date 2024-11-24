from deep_translator import GoogleTranslator

while True:
    print("\nIzvēlieties valodu (rakstiet numuru):")
    print("1. No latviešu uz angļu")
    print("2. No angļu uz latviešu")
    print("3. Iziet")
    
    izvele = input("Jūsu izvēle: ")
    
    if izvele == "3":
        print("Uz redzēšanos!")
        break
        
    if izvele == "1":
        teksts = input("\nIevadiet tekstu latviešu valodā: ")
        tulkojums = GoogleTranslator(source='lv', target='en').translate(teksts)
        print(f"\nTulkojums angļu valodā: {tulkojums}")
        
    elif izvele == "2":
        teksts = input("\nIevadiet tekstu angļu valodā: ")
        tulkojums = GoogleTranslator(source='en', target='lv').translate(teksts)
        print(f"\nTulkojums latviešu valodā: {tulkojums}")
        
    else:
        print("Nederīga izvēle. Lūdzu izvēlieties 1, 2 vai 3.")
