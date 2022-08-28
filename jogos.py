import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    while True:
        print("(1) Forca (2) Adivinhação")
        jogo = (input("Qual jogo? "))

        if jogo == '1':
            print("Jogando forca")
            forca.jogar()
            break

        elif jogo == '2':
            print("Jogando adivinhação")
            adivinhacao.jogar()
            break

        else:
            print("Por favor, digite uma opção válida!")

if __name__ == "__main__":
    escolhe_jogo()
