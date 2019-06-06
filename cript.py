numero = int(input('Digite um número qualquer: '))
numero2 = int(input('Digite outro número qualquer: '))

resultado = numero % 2 # Pega o resto do número
if resultado % 2 == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é IMPAR'.format(numero))
