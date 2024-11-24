from transformers import pipeline, set_seed
from deep_translator import GoogleTranslator

def generate_story(sakums):

    eng_sakums = GoogleTranslator(source='lv', target='en').translate(sakums)
    generator = pipeline('text-generation', model='gpt2')
    set_seed(42) 
    generated_text = generator(eng_sakums,max_length=100,num_return_sequences=1,temperature=0.7,truncation=True,pad_token_id=generator.tokenizer.eos_token_id)[0]['generated_text']
    lat_teksts = GoogleTranslator(source='en', target='lv').translate(generated_text)
    return lat_teksts

while True:

    sakums = input("Ievadiet sākuma frāzi (vai 'ata' lai beigtu): ").strip()
    if sakums.lower() == 'ata':
        print("Programma beigta!")
        break
    if not sakums:
        sakums = "Reiz kādā tālā zemē"
        print(f"Izmantojam piemēra sākuma frāzi: {sakums}")

    print("\nĢenerētais stāsts:")
    print(generate_story(sakums))
    print()
