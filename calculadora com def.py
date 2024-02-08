#requisitos:

while True:
    comprimento = int(input('Qual o comprimento da senha? (Entre 8 e 12)'))
    if comprimento < 8 or comprimento > 12:
        print('A senha deve ter entre 8 e 12 caracteres, tente novamente! ')
        continue