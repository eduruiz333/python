# A princípio, strings  e números naturais iguais declarados em variáveis diferentes, apontam para a mesma alocação da memória
a = 'banana'
b = 'banana'
print(a)
print(b)
print('É a mesma lista de texto? = ', a is b)

print()
print('------------')
print()

num1 = 3.5
num2 = 3.5
print(num1)
print(num2)
print('É a mesma lista de números? = ', num1 is num2)

print()
print('------------')
print()

# A princípio, listas iguais declaradas em variáveis diferentes apontam para locais diferentes da memória
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1)
print(l2)
print('É a mesma lista de arrays? = ', l1 is l2)

print()
print('------------')
print()

lista_base = ['água', 'fogo', 'terra', 'ar']
print(lista_base)
lista_base[0] = 'Eter'
lista_clone = [lista_base * 3]
print(lista_base)
print(lista_clone)
print()
