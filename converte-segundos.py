segundos_str = input('Digite a quantidade de segundos que quer converter: ')
total_segundos = int(segundos_str)

dias = total_segundos // 86400
horas = (total_segundos % 86400) // 3600
segundos_restantes = total_segundos % 3600
minutos = segundos_restantes // 60
segundos_restantes_final = segundos_restantes % 60

print(dias, 'dias', horas, 'horas', minutos, 'minutos e', segundos_restantes_final, 'segundos')
