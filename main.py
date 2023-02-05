print("***************")
print("BEM VINDO PARA ADIVINHAR")
print("***************")
numero=65
chute_str=input("Digite o seu número.:")
print("Você digitou:", chute_str)
chute=int(chute_str)
x= numero-chute
tentativas=3
rodada=1
while(rodada <= tentativas):
    print("Tentativa {} de {}".format(rodada, tentativas))
    if (x==0):
        print("Parabéns, você acertou!!")
        print("Fim de jogo.")
        rodada=5
    elif(x!=0):
        if(x<0):
                print("O seu chute foi maior que o numero secreto")
        else:
                print("O seu chute foi menor que o numero secreto")

        chute_str = input("Digite o seu número:")
        print("Você digitou:", chute_str)
        chute = int(chute_str)
        x = numero - chute
        rodada= rodada + 1