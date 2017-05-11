"""
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(A[2][0])
"""


def cria_matriz(num_linhas, num_colunas, valor):  # (int, int, value)

    matriz = []
    for x in range(num_linhas):
        linha = []
        for y in range(num_colunas):
            valor = int(input('Digite o elemento [' + str(x) + '][' + str(y) + ']'))
            linha.append(valor)
        matriz.append(linha)
    return matriz


def le_matriz():
    lin = int(input('Digite a quantidade de linhas: '))
    col = int(input('Digite a quantidade de colunas: '))
    return cria_matriz(lin, col)
le_matriz()
