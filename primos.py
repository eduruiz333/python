def primo(x):
    fator = 2
    if x == 2:
        return True

    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True

imprime_primos = int(input('Digite o limite de númeris primos a exibir: '))

n = 2
while n < imprime_primos:
    if primo(n):
        print(n, end=', ')
    n = n + 1
