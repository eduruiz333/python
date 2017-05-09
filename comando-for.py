primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

"""
bandas_de_rock = ['Slayer', 'Ramones', 'Body Count', 'Living Colour', 'Infectious Groove']

for banda in bandas_de_rock:
    print('Eu curto ' + banda)
    print()
    print()

for x in primos:
    print(x * x)
for i in range(0, 100, 3):
    print(i)

pares = range(0, 20, 2)
for i in pares:
    print(i)
"""
for i in range(len(primos)):
    primos[i] = primos[i]**3
print(primos)
