#converter dias em semanas
numero = int(input('Insira o número a ser convertido '))
semana = 7
diasRestantes = numero % 7
calculo = numero//semana
print(f'tem {calculo} semanas e {diasRestantes} dias')