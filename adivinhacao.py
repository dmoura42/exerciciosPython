print('*****************************')
print('*    Jogo da adivinhação    *')
print('*****************************\n')

numero_secreto = 42
rodada = 1
total_de_tentativas = 0

print('Nível 1 = 20 tentativas')
print('Nível 2 = 10 tentativas1')
print('Nível 3 = 5 tentativas\n')
nivel = int(input('Escolha seu nível: '))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
elif nivel == 3:
    total_de_tentativas = 5

for i in range(1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute = int(input("Digite seu número: "))
    print("Seu número foi {}\n".format(chute))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou\n")
        break
    elif maior:
        print("Você errou! Seu número é maior que o número secreto.\n")
    elif menor:
        print("Você errou! Seu número é menor que o número secreto.\n")

    rodada = rodada + 1

print('Fim do jogo')

