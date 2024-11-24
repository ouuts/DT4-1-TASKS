from transformers import pipeline, set_seed
import torch
from deep_translator import GoogleTranslator

def generate_story(sakums):
    # Tulkojam sākuma tekstu uz angļu valodu
    eng_sakums = GoogleTranslator(source='lv', target='en').translate(sakums)
    
    # Inicializējam teksta ģenerēšanas pipeline
    generator = pipeline('text-generation', model='gpt2')
    
    # Ģenerējam tekstu
    set_seed(42)  # Lai rezultāti būtu atkārtojami
    generated_text = generator(eng_sakums, 
                             max_length=100, 
                             num_return_sequences=1,
                             temperature=0.7)[0]['generated_text']
    
    # Tulkojam rezultātu atpakaļ uz latviešu valodu
    lat_teksts = GoogleTranslator(source='en', target='lv').translate(generated_text)
    
    return lat_teksts

while True:
    sakums = input("Ievadiet sākuma frāzi (vai 'exit' lai beigtu): ")
    if sakums.lower() == 'exit':
        break
        
    if sakums == "":
        sakums = "Reiz kādā tālā zemē..."
        
    print("\nĢenerētais stāsts:")
    print(generate_story(sakums))
    print()
