resposta = ""
pontuacao = 0
nome = input("Como te chamas ? ")
nome = nome.title()
while resposta != "fim":
    resposta = input(nome + " Vamos estudar a tabuada ? Se quiseres acabar escreve 'fim' ")
    if resposta != "fim":
        tabuada = input("Qual é a tabuada que queres estudar? ")
        t = int(tabuada)
        limite = 11
        for x in range(1, limite):
            x1 = str(x)
            r = int(input("Quanto é " + tabuada + " X " + x1 + " = "))
            if r == t*x:
                print("CERTO")
                pontuacao += 1
            else:
                print("ERRADO")
                pontuacao -= 0.5
print("Boa " + nome + ". A tua pontuação foi ")
print(pontuacao*100)
import time
time.sleep(5)
print("Adeus " + nome)
time.sleep(5)
