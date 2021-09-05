lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

print('Maior número da lista')
maiorNumero = 0
for i in range(0, len(lista)):
    if maiorNumero < lista[i]:
        maiorNumero = lista[i]
print(maiorNumero)

print('\nMenor número da lista')
menorNumero = 0
for i in range(0, len(lista)):
    if menorNumero > lista[i]:
        menorNumero = lista[i]
print(menorNumero)

print('\nNúmeros pares')
listaPares = []
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        listaPares.append(lista[i])
print(listaPares)

print('\nOcorrência do primeiro item da lista')
ocorrenciaItem1 = 0
for i in range(0, len(lista)):
    if lista[i] == lista[0]:
        ocorrenciaItem1 = ocorrenciaItem1 + 1
print(ocorrenciaItem1)

print('\nA média dos elementos')
somaNumeros = 0
for i in range(0, len(lista)):
    somaNumeros = somaNumeros + lista[i]
mediaNumeros = somaNumeros / len(lista)
print(mediaNumeros)

print('\nA soma dos elementos de valor negativo')
somaNegativos = 0
for i in range(0, len(lista)):
    if lista[i] < 0:
        somaNegativos = somaNegativos + lista[i]
print(somaNegativos)
