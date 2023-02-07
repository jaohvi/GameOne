import random

print("***************")
print("BEM VINDO PARA ADIVINHAR")
print("***************")

#numero=round(random.random()*100) #random gera entre 0.0 e 1.0
numero= random.randrange(1,101)
print(numero)
tentativas=3
#rodada=1
#while(rodada <= tentativas):
for (rodada) in range(1,tentativas+1):
    print("Tentativa {} de {}".format(rodada, tentativas))
    chute_str = input("Digite um número entre 0 e 100:")
    chute = int(chute_str)
    print("Você digitou:", chute_str)

    if(chute<1 or chute >100):
        print("Digite um valor entre 0 e 100!")
        continue
    x = numero - chute
    if (x==0):
        print("Parabéns, você acertou!!")
        print("Fim de jogo.")
        break #serve para acabar com o loop do for
        #rodada=5
    elif(x!=0):
        if(x<0):
                print("O seu chute foi maior que o numero secreto")
        else:
                print("O seu chute foi menor que o numero secreto")

        #chute_str = input("Digite o seu número:")
      #  print("Você digitou:", chute_str)
      #  chute = int(chute_str)
       # x = numero - chute
       # rodada= rodada + 1