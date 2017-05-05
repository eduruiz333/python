fim = int(input('Digite um número para calcular a sequência de Fibonacci: '))


def calculaFibonacci():
    numero = fim
    pri = 0
    seg = 1
    fib = seg + pri
    print("Sequência de Fibonatti até: ", numero)

    cont = 0

    while cont <= fim:
        print(fib)
        pri = seg
        seg = fib
        fib = seg + pri
        cont = cont + 1
calculaFibonacci()
print()
