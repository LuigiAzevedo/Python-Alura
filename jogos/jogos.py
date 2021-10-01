import forca
import adivinhacao

print("*********************************")
print("********Escolha um jogo!*********")
print("*********************************")

print("(1) Forca\n(2) Adivinhação")

jogo = int(input("Qual jogo? "))

if jogo == 1:
    print("Forca")
    forca.jogar()
else:
    print("Adivinhação")
    adivinhacao.jogar()
