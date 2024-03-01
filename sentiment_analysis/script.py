# -*- coding: utf-8 -*-

from textblob import TextBlob
from translate import Translator

def analisar_sentimento(texto, lang="pt-BR"):
    
    tradutor = Translator(from_lang=f"{lang}", to_lang="en-US")
    traducao = tradutor.translate(texto)
    
    #print(f"\n{traducao}\n")
    
    blob = TextBlob(traducao)
    
    if blob.sentiment.polarity > 0:
        return "positivo"
    elif blob.sentiment.polarity < 0:
        return "negativo"
    else:
        return "neutro"

frase = input("\nEscreva uma frase, por favor. Tentarei aferir que sentimento ela passa:\n-> ")
sentimento = analisar_sentimento(frase)

print(f"\033[4mAcho que o sentimento exposto em \"{frase}\" é {sentimento}.\033[0m\n")
