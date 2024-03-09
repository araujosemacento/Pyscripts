# -*- coding: utf-8 -*-
from time import sleep
import json
import random

partida = "em andamento"
tentativas = 7
inputs = []


def escolherPalavra():
    opcoes = json.load(open("./temas.json", encoding="utf-8"))
    tema = random.choice(list(opcoes["temas"].keys()))
    return [tema, random.choice(opcoes["temas"][tema])]


def desenharHominho(tentativas, partida):
    match tentativas:
        case 7:
            print(
                """
                 _______
                |       |
                |
                |
                |
                |
           _____|_____
                  """
            )
        case 6:
            print(
                """
                 _______
                |       |
                |       o
                |
                |
                |
           _____|_____
                  """
            )
        case 5:
            print(
                """
                 _______
                |       |
                |       o
                |       |
                |
                |
           _____|_____
                  """
            )
        case 4:
            print(
                """
                 _______
                |       |
                |       o
                |      /|
                |
                |
           _____|_____
                  """
            )
        case 3:
            print(
                """
                 _______
                |       |
                |       o
                |      /|\\
                |
                |
           _____|_____
                  """
            )
        case 2:
            print(
                """
                 _______
                |       |
                |       o
                |      /|\\
                |       |
                |
           _____|_____
                  """
            )
        case 1:
            print(
                """
                 _______
                |       |
                |       o
                |      /|\\
                |       |
                |      /
           _____|_____
                  """
            )
        case 0:
            print(
                """
                 _______
                |       |
                |       o
                |      /|\\
                |       |
                |      / \\
           _____|_____
                  """
            )
    if partida == "perdida":
        print(
            """
 XXX                                                                   X;:xX    
x:::x                                                                 X+;:::x   
+::;x::x                                                               X+x;:;X  
X;;;:::;X     X+:::X                                                    Xx;:::x 
 X+:::;x+;+x X;::;;x                 $    $&                    XXX     X;;;;:;X
  x;;X::::::+x:;;;X                $$XXXXXXXXx...              ;::::X   X;Xxx;+X
  X;+;;;;::;x::;;X             ...:+;:::::::.$&&&x...          X;:::+  X;:::::+X
   XX;;;+;:::::;X            .;&&&&&.:::::::&:..X&&&X..         X;;:+ X::x:::::+
   XX;;;+::::::;x          .x+..x&&&&.;;;;;:&&&&&;;&&x;X         x;;;+::::Xx;;:+
    X;;;;::::::;X         x:&&xx&&&&&.;;;;;:$&&&&$$&++++xX       +;;;;;;;;;;;;;X
     X;;;:::x;;;X        X;.&&&&&x&&++XXXXX$++++++++++++++X      +;x::::;;;;;;X 
      x;;;:::;xx        x+++++++++++$XXXXXXXXX$X+;;;;;;;;++X     X+x:::;;;;+xX  
       X+;;:::X        x;+;x++X;XXXXXXXXXXXXXXXXXX;;;;++;+;;X     XX::;;;;xX    
         XxxxX        X;;+;;;;;XXXXX&&$XXXX&&XXXXXX;;;+++;+;x       XxxXX       
                      x:;;;;;;XXXX$&&&&$XX&&&&XXXXXX;+++++;;;X                  
                      +:;;;;;XXXXX&&&&&&&&&&&&&XXXXXX++++++;:X                  
                      +;;;;;+XXXX$&&&&&&&&&&&&&XXXXXXX++++;;:X                  
                      +;;;;;XXXXX$&&&&&&&&&&&&&$XXXXXX+;;;;;:X                  
                      x;;;;xXXXXXX&&&X;::::+X&&$XXXXXXX;;;;;;X                  
                      X;;;;XXXXXXXX+::::::::::xXXXXXXXXx;;;;+                   
                      Xx+;+XXXXXXX;;;::::::::::;XXXXXXXX;;+;X                   
                       Xx+XXXXXXx;;;;;;;;;;;;;;;;xXXXXXX+++x                    
                        x+XXXXX+;;;;;;;;;;;;;;;;;;;XXXXX++X                     
                        x;+xx+;;;;;;;;;;;;;;;;;;;;;;+XXx++X                     
                        X+::;x+;;;;;;;;;;;;;;;;;;;;;x++;;;X                     
                          XX X+++++;;;;;;;;;;;;;+++++xX+;x                      
                               Xx++++++++++++++++++X                            
                                  XXXxx++++++xXXX                               

                        Seu monstro! Você o deixou morrer T.T

"""
        )
    elif partida == "ganha":
        print(
            """
                                                                                
                                                                                
                                                                                
                                .::::;;;;:::.                                   
                           .:;;::::::::::::::;;;;.                              
                        .:;+++++++::::::::xXXXXXXx;;:                           
           ::.        :;:;X$$$$X+;::::::::;;+xX$$X;;;;:                         
    .;; ...:xx      .;:::::::::::::::::::::::::::::::;;+.                       
  ::;xX:::+$X:     :;:::::::::::::::::::::::::;;;;::::;;;;                      
  :::;X+:;X$.   .:;;:::::;+xXXX+:::;;::::::+X$$$$$$X+;;:;;;                     
  .;;+Xx :X::+X;;+$++X&&&&&&&&&&&&&&x;;x&&&&&$$$$$&&&&&&&&&&$                   
   .::;xX+$++x.xX+x$&&&&&$$$$$$$$$&&&&&&&&$$$$$$$$$$&&&$;:;+$;                  
   .::;x$&$X$+.X::xx:$&&$$$$$$$$$$$&&&$&&$$$$$$$$$$$$&&;::;+XX                  
   .::;+$&X+.  .:+X;:x&&$$$$$$$$$$$&&$X&&&$$$$$$$$$$&&X;::;;x$:                 
   :;:;x$X:;:..:xX::::X&&&$$$$$$$$&&&x:x&&&$$$$$$$&&&$;:::;;+:                  
   .++X$&++xXx;;+;:::::;&&&&&$&&&&&&;:::;$&&&$$&&&&&+;::::;++;                  
   .;::+XX:    :+;:::::::;X$$&$$$X;::::::::+X$$$X+;;;;;;:;;+x;    .             
               .++;:;;+x++;;;:::::::::::::::;;++xx+XX+;;;;;+X:  ;:  :           
                ++;;;:::;+;+;;;;;;;;;;;;;;;::;+:;++;::::::;XX   x;:;;           
                :x+;::::::;++;+;;;+;;;x;;;+;;+x;:;::;;;;;;+X;   +: .;.          
                 ;x;;;::::::::::..:...:...:..:;:::;;;;;;;+Xx    X;::..          
                 .++;;;;;;;;;:::;:::.:::::;::::;;++;;;;;+xX.    +$+;;;::.       
                  .+++;;;;;;++;;::::::::::::;;+xx+;;;+++xx:     +XX:     .:.    
                    ;x++;;;;;;+++;;;;;;;;;;+xx++;;;+++xX+.     :XX$+::::::;;    
                     :+x+++;;;;;;+++xxxxx+++++++++++xXx:      ..;x++;::;;++.    
                       .+xx++++++++++++++++++++++xXXx:        .:xXx;:      ;    
                         .;+XXxx+++++++++++xxxXXX+;            .+XXX+;;;;:::    
                              :;xXXXXXXXX$$X+;.                 .x:     .:.     
                                                                 +;:... .:.     
                                                                   .:::::.      
                                                                                
                        Obrigado por me salvar! :D
                        Tamo junto, meu confrade.
                            """
        )


def checagem(tentativas, letra, inputs, palavra, statusDaPalavra):
    letra_minuscula = letra.lower()
    palavra_minuscula = palavra.lower()
    termos =palavra_minuscula.split(" ")
    
    if len(letra_minuscula) > 1:
        if letra_minuscula == palavra_minuscula:
            for caractere in palavra_minuscula:
                statusDaPalavra[caractere][0] = True
        elif letra_minuscula in termos:
            for caractere in letra_minuscula:
                statusDaPalavra[caractere][0] = True
        return [tentativas, inputs]
        
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
    if letra_minuscula in palavra_minuscula and letra_minuscula not in inputs:
        inputs.append(letra_minuscula)
        inputs.sort()
        statusDaPalavra[letra_minuscula][0] = True
    if letra_minuscula in letras_variantes:
        for variante in letras_variantes[letra_minuscula]:
            if variante in palavra_minuscula:
                if letra_minuscula not in inputs:
                    inputs.append(letra_minuscula)
                    inputs.sort()
                statusDaPalavra[variante][0] = True
                break
            elif (
                variante == letras_variantes[letra_minuscula][-1]
                and letra_minuscula not in inputs
            ):
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
            desenharHominho(tentativas, partida)
            retorno = input(
                f"""Dica: {dica}
                            
Digite uma letra ou numeral se quiser salvá-lo: """
            )
            print(
                "\n—————————————————————x—————————————————————x—————————————————————\n"
            )
            if len(retorno) != 0 and any(char.isalnum() for char in retorno):
                break
            print("Digite uma LETRA ou NUMERAL, se quiser salvá-lo!\n-> ")
            continue
        [tentativas, inputs] = checagem(
            tentativas, retorno, inputs, palavra, statusDaPalavra
        )
        print("\n")
        for letra in palavra:
            if statusDaPalavra[letra.lower()][0]:
                print(letra, end="")
            else:
                print("_", end="")
        print("\n")
        if all(statusDaPalavra[opcao][0] == True for opcao in statusDaPalavra):
            partida = "ganha"
            desenharHominho(tentativas, partida)
            sleep(7)
            break
        if tentativas <= 0:
            partida = "perdida"
            desenharHominho(tentativas, partida)
            sleep(7)
            break


jogo(tentativas, partida, inputs)
