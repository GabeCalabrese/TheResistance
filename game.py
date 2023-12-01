import time
import random
tipo_players = {"resistentes":[],
                "espioes":[]}
players = []
def perguntaPLayer():
    qntPlayers = input("Insira a quantidade de players:")
    qntPlayers = int(qntPlayers)
    while qntPlayers < 5 or qntPlayers > 10:
        qntPlayers = input("Insira a quantidade de players:")
        qntPlayers = int(qntPlayers)
    print("tudo ok")
    return qntPlayers

def nomeJogadores(n):
    for i in range(n):
        players[i] = input("Insira o nome do Player " + i + ":")

def defineClasse(qnt_players):
    if qnt_players == 5 or qnt_players == 6:
        qnt_espioes = 2
    elif qnt_players >= 7 and qnt_players <= 9:
        qnt_espioes = 3
    elif qnt_players > 9:
        qnt_espioes = 4
    for i in range(qnt_espioes):
        selecionado = random.choice(players)
        tipo_players["espioes"][i] = selecionado
        players.remove(selecionado)
    for j in range(players.length):
        tipo_players["resistentes"][j] = players[j]

