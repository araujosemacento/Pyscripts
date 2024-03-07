import json
import random

partida = "em andamento"
tentativas = 7


def escolherPalavra():
    opcoes = json.load(open("./temas.json", encoding="utf-8"))
    temas = opcoes["temas"]["filmes"]
    return random.choice(temas)


def checagem(letra, palavra, statusDaPalavra):
    letra_minuscula = letra.lower()
    palavra_minuscula = palavra.lower()
    if not letra_minuscula.isalnum():
        statusDaPalavra[letra_minuscula][0] = True
    if letra_minuscula in palavra_minuscula:
        statusDaPalavra[letra_minuscula][0] = True
        letras_variantes = {
            "a": ["á", "ã", "â", "ä"],
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
        for variante in letras_variantes.get(letra_minuscula, []):
            if variante in palavra_minuscula:
                statusDaPalavra[variante][0] = True
    """ else:
        tentativas -= 1 """


def jogo(partida):
    palavra = escolherPalavra()
    statusDaPalavra = {letra.lower(): [False] for letra in palavra}
    print(statusDaPalavra)
    while partida == "em andamento":
        retorno = ""
        while True:
            retorno = input("digite uma letra: ")
            if len(retorno) == 0:
                continue
            elif len(retorno) > 1:
                print("digite apenas uma letra\n")
            else:
                break
        checagem(retorno, palavra, statusDaPalavra)
        for letra in palavra:
            if statusDaPalavra[letra.lower()][0]:
                print(letra, end="")
            else:
                print("_", end="")
        print()
        if all(statusDaPalavra.values()):
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠒⠋⠉⠭⠓⠲⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⡋⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠶⠛⠋⠁⠀⠀⠀⠁⠹⠝⠛⠢⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⢀⣴⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢨⠛⢦⣄⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠲⣌⠙⢦⣰⠿⠋⢀⣀⡠⠴⠶⠒⠚⣫⣽⣯⣉⡛⠒⠲⠶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⢀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣶⢻⣶⠚⠋⠁⠀⢀⣠⢤⣾⡿⠟⠛⠻⢿⣤⣀⣀⠀⠀⠉⠓⠢⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣾⣧⠀⠚⠉⠉⠁⡿⠋⠀⠀⠀⠀⠈⠀⠀⠉⠛⠲⣤⢀⠀⢀⣽⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠒⠲⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠽⡇⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⠿⠻⢿⣿⣗⣆⠀⠀⠀⠀⠀⠀")
            print("⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⢀⣠⣤⣂⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⠈⠳⡄⠀⠀⠀⠀")
            print("⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⢄⡀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢠⣿⠟⠉⠀⠈⠓⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠀⠀⠙⣆⠀⠀⠀")
            print("⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢦⡀⠙⢦⡀⠀⠀⠀⠀⣼⠁⠀⠀⡾⠁⠀⣠⣀⡀⠀⠈⣧⠀⠀⠀⠀⣠⡴⠖⠦⣤⡀⠀⠀⠀⠀⠀⠘⣧⠀⠀")
            print("⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠙⢦⡀⢀⡴⠃⠀⠀⢰⠃⢠⡞⠙⣿⣿⡆⠀⠸⡆⠀⠀⣼⠃⣅⣀⣀⠀⠉⢳⡄⠀⠀⠀⠀⠸⣆⠀")
            print("⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠶⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⠀⢻⡉⠐⠓⠒⠤⢼⣀⢸⣿⣶⣿⣿⣿⠀⢀⡇⠀⠀⡇⣾⠛⢻⣿⣧⠀⠀⢹⡀⠀⠀⠀⠀⠹⡀")
            print("⠘⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠲⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠣⠘⡇⠀⠀⠀⠀⠀⠈⠛⢿⣿⣬⣿⠃⠀⣼⠁⠀⠀⣷⣿⣷⣿⣿⣿⠀⠀⠀⣷⠀⠀⠀⠀⠀⡇")
            print("⠀⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣇⣠⠤⣤⣀⡀⠀⠀⠀⠻⡉⠁⢀⡴⠁⠀⠀⠀⠘⣿⣿⣇⣿⡟⠀⠀⢂⡟⠀⠀⠀⠀⠀⠁")
            print("⠀⠀⠹⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⡈⠻⣦⠀⠀⠀⠀⠀⠀⣠⠟⠁⠀⠀⠀⢻⡙⠂⠀⠀⠀⢹⠔⠋⠀⠀⠀⠀⠀⠀⠙⢎⡉⠁⢀⣠⠤⠾⠦⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠘⢦⡶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢆⠈⢧⣀⣀⣠⡤⠞⠁⠀⠀⠀⠀⠀⠀⢻⣄⠄⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠙⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⢸⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⣀⣤⣤⣀⠀⠀⠀⠀⠀⡀")
            print("⠀⠀⠀⠀⠀⠀⠀⠈⠙⠶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣳⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠽⣿⣆⠈⠙⠲⠦⣄⣀⣀⣀⠀⠀⠀⠀⢀⣀⣈⡵⠞⠁⠈⠁⠀⠀⠀⢀⠇")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠲⠤⠤⠤⠴⠖⠺⣏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢿⣿⣷⣄⠀⠀⠀⠀⠀⠉⠉⠉⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⡟⠻⢿⣷⣶⣤⣄⣀⣀⣤⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠁⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠻⠿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡽⠃⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⣘⣦⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠁⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⠿⠿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠦⠖⠒⠀⠀⠀⠀⠀⠀⠀⣠⡴⠋⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⠤⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠷⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            partida = "ganha"
            print("Parabéns, você ganhou!")
            break
        if tentativas == 0:
            partida = "perdida"
            break


jogo(partida)
