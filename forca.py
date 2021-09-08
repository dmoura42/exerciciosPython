import random

###### Variáveis do jogo ######

enforcou = False

acertou = False

erros = 0

tentativas = 5

palavras = ['banana', 'melancia', 'morango', 'manga', 'abacaxi', 'uva', 'tomate', 'limao']

numero = random.randrange(0, len(palavras))

palavra_secreta = palavras[numero].upper()

letras_acertadas = ['_' for letra in palavra_secreta]

###### Jogo ######

print('*********************************')
print('***Bem vindo ao jogo da Forca!***')
print('*********************************')

print('\nVocê tem direito a errar {} vezes. A dica é: FRUTA'.format(tentativas))

print('\n', letras_acertadas)


while not acertou and not enforcou:
    
    chute = input('\nDigite uma letra? ').upper()

    if chute in palavra_secreta:
        posicao = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[posicao] = letra
            posicao += 1
    else:
        erros += 1
        print('\nErrou! Você ainda tem ', tentativas - erros, ' tentativas.' )

    enforcou = erros == 5
    acertou = '_' not in letras_acertadas
    print('\n', letras_acertadas)

if acertou:
    print('Você ganhou!')
else:
    print('Você perdeu!')
print('\nFim do jogo.')
