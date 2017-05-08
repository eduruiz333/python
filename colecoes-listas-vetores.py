"""
lista_qualquer = ['Aqui é um texto, bla bla bla', 122, -58.0, 'E']

lista_qualquer[3] = 'X'
lista_qualquer.append('Mais um item inserido')

print(lista_qualquer[3])
print(len(lista_qualquer))
print(type(lista_qualquer[0]))
print(type(lista_qualquer[2]))

"""


def ordena_numeros():
    lista = []
    print('Digite números inteiros começando com 0 (ZERO), ex: 010, 0145, etc, e digite 0 para finalizar', end='\n\n')

    entrada = int(input('Digite aqui: '))
    while entrada != 0:
        lista.append(entrada)
        entrada = int(input('Digite aqui: '))
    return print(lista)

ordena_numeros()
