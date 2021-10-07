import forca
import adivinhacao

print("*********************************")
print("********Escolha um jogo!*********")
print("*********************************")

print("(1) Forca\n(2) Adivinhação")

jogo = int(input("Qual jogo? "))

if jogo == 1:
    print("Escolheu Forca!")
    forca.jogar()
else:
    print("Escolheu Adivinhação!")
    adivinhacao.jogar()
