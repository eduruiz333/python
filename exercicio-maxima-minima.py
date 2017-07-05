# Definir um programa para exibir temperaturas mínimas e máximas das médias em um range de tempo
# Plano: quebrar o problema em pequenas tarefas, pequenos problemas
# Testes automatizados


def MinMax(temperaturas):
    print('A menor temperatura do mês foi: ', minima(temperaturas), 'Cº')
    print('A maior temperatura do mês foi: ', maxima(temperaturas), 'Cº')


def minina(temps):
    min = 0
    i = 0
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i += 1
    return min

print(minina([0, 1, 2, 3]))
