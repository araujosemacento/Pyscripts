# -*- coding: utf-8 -*-

import json
import random

partida = "em andamento"
tentativas = 7
inputs = []


def escolherPalavra():
    opcoes = json.load(open("./temas.json", encoding="utf-8"))
    tema = random.choice(list(opcoes["temas"].keys()))
    return [tema, random.choice(opcoes["temas"][tema])]


def checagem(tentativas, letra, inputs, palavra, statusDaPalavra):
    letra_minuscula = letra.lower()
    palavra_minuscula = palavra.lower()
    letras_variantes = {
        "a": ["á", "ã", "â", "ä", "à"],
        "e": ["é", "ê", "ë"],
        "i": ["í", "î", "ï"],
        "o": ["ó", "õ", "ô", "ö"],
        "u": ["ú", "û", "ü"],
        "c": ["ç"],
        "n": ["ñ"],
        "s": ["ß"],
        "y": ["ý", "ÿ"],
        "z": ["ž"],
    }
    if letra_minuscula in palavra_minuscula:
        inputs.append(letra_minuscula)
        inputs.sort()
        statusDaPalavra[letra_minuscula][0] = True
    if letra_minuscula in letras_variantes and letra_minuscula not in inputs:
        for variante in letras_variantes[letra_minuscula]:
            if variante in palavra_minuscula:
                inputs.append(letra_minuscula)
                inputs.sort()
                statusDaPalavra[variante][0] = True
                break
            elif variante == letras_variantes[letra_minuscula][-1]:
                inputs.append(letra_minuscula)
                inputs.sort()
                tentativas -= 1
                print(f"Tentativas restantes: {tentativas}")
    elif letra_minuscula not in inputs:
        inputs.append(letra_minuscula)
        inputs.sort()
        tentativas -= 1
        print(f"Tentativas restantes: {tentativas}")

    print(f"\nLetras já inseridas: {inputs}")

    return [tentativas, inputs]


def jogo(tentativas, partida, inputs):
    [dica, palavra] = escolherPalavra()
    statusDaPalavra = {letra.lower(): [False] for letra in palavra}
    for chave in statusDaPalavra:
        if not chave.isalnum():
            statusDaPalavra[chave][0] = True
    while partida == "em andamento":
        retorno = ""
        while True:
            retorno = input(
                f"""Dica: {dica}
                            
Digite uma letra ou numeral se quiser salvá-lo: """
            )
            if len(retorno) == 0:
                continue
            elif len(retorno) > 1:
                print("Digite apenas UMA letra ou número.\n")
            else:
                break
        [tentativas, inputs] = checagem(
            tentativas, retorno, inputs, palavra, statusDaPalavra
        )
        print("\n")
        for letra in palavra:
            if statusDaPalavra[letra.lower()][0]:
                print(letra, end="")
            else:
                print("\033[4m \033[0m", end="")
        print("\n")
        if all(statusDaPalavra[opcao][0] == True for opcao in statusDaPalavra):
            print(
                """
                  
                  """
            )
            partida = "ganha"
            break
        if tentativas <= 0:
            print(
                """
                  
                  """
            )
            partida = "perdida"
            break


jogo(tentativas, partida, inputs)
