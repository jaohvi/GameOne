import adivinhacao1
import adivinhacao2

def escolha_jogo():
    print("Escolha o jogo")
    print ("(1) Adivinhação 1 (2) Adicinhação 2")
    jogo=int(input("Qual jogo? Digite: "))
    if(jogo==1):
        print("Jogo 1")
        adivinhacao1.jogar_adivinhacao1()
    elif(jogo==2):
        print("Jogo 2")
        adivinhacao2.jogar_adivinhacao2()
if(__name__=="__main__"):
    escolha_jogo()