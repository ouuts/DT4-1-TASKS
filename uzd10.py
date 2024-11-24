from deep_translator import GoogleTranslator

def translate_text(source_lang, target_lang, text):
    return GoogleTranslator(source=source_lang, target=target_lang).translate(text)

while True:
    print("\nIzvēlieties valodu (rakstiet numuru):")
    print("1. No latviešu uz angļu")
    print("2. No angļu uz latviešu")
    print("3. Iziet")
    
    izvele = input("Jūsu izvēle: ").strip()
    
    if izvele == "3":
        print("Uz redzēšanos!")
        break
        
    if izvele == "1":
        teksts = input("\nIevadiet tekstu latviešu valodā: ").strip()
        if not teksts:
            print("Lūdzu, ievadiet kādu tekstu.")
            continue
        tulkojums = translate_text("lv", "en", teksts)
        print(f"\nTulkojums angļu valodā: {tulkojums}")
        
    elif izvele == "2":
        teksts = input("\nIevadiet tekstu angļu valodā: ").strip()
        if not teksts:
            print("Lūdzu, ievadiet kādu tekstu.")
            continue
        tulkojums = translate_text("en", "lv", teksts)
        print(f"\nTulkojums latviešu valodā: {tulkojums}")
        
    else:
        print("Nederīga izvēle. Lūdzu izvēlieties 1, 2 vai 3.")
