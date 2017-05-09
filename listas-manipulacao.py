primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print(primos[5:10])
print(primos[:10])
print(primos[15:])
print(primos[:])  # Isso cria um CLONE da lista
print()

lista1 = ['vermelho', 'verde', 'azul']
lista2 = lista1

print(lista2)
lista2[0] = 'rosa'
print(lista2)
print(lista1)
# Ao alterar a lista 2, a lista 1 também é alterada, pois ambas as listas apontam para a mesma alocação da memória
# Para criar clones, podemosu usar da seguinte forma:


def clone(lista):
    clone = []
    for coisas in lista:
        clone.append(coisas)
    return clone

# mas existe outra forma muito mais simples que é:
lista1 = ['vermelho', 'verde', 'azul']
lista2 = lista1[:]
lista2[0] = 'rosa'
print(lista1)
print(lista2)
print('rosa' in lista1)
print('rosa' in lista2)

lista3 = ['a', 'e', 'i', 'o', 'u'] + ['b', 'c', 'd', 'e']
print(lista3)

# É possível fazer cálculos com os itens das listas
a = [1, 2, 3]
b = [4, 5, 6]
print(a[0] + b[1])
# OBS.: O APPEND ALTERA UMA LISTA EXISTENTE, POIS ELE ADICIONA INTENS À LISTA, A CONCATENAÇÃO GERA UMA NOVA LISTA A PARTIR DE DUAS OU MAIS

# ABAIXO É UM EXEMPLO DE CONCATENAÇÃO DE LISTAS INTEIRAS UTILIZANDO OPERADOR DE MULTIPLICAÇÃO
animais = ['gato', 'cachorro', 'peixe']
animais_x3 = animais * 3
print(animais_x3)
del animais[1]
animais_x3 = animais * 3
print(animais)
print(animais_x3)

ota_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del ota_lista[0:4]
print(ota_lista)
