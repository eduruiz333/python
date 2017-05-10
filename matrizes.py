"""
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(A[2][0])
"""


def cria_matriz(num_linhas, num_colunas, valor):  # (int, int, int)
    matriz = []
    for x in range(num_linhas):
        linha = []
        for y in range(num_colunas):
            linha.append(valor)
        matriz.append(linha)
    return print(matriz)
cria_matriz(5, 8, ' :-) ')
