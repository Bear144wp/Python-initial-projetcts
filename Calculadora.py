while True:
    numero1 = input('Digite o primeiro número: ')
    numero2 = input('Digite o segundo número: ')
    operador = input('Digite o operador: (+-/*)')

    numeros_validos = None

    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('O numero não é válido!')
        
        continue

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('O operador não é permitido ou está errado! ')
        continue

    if len(operador) > 1:
        print('Só é permitido 1 operador! ')
        continue

    print('Realizanod sua conta, resultado abaixo: ')

    if operador == '+':
        print(numero1_float + numero2_float)

    if operador == '-':
        print(numero1_float - numero2_float)

    if operador == '/':
        print(numero1_float / numero2_float)

    if operador == '*':
        print(numero1_float * numero2_float)


    sair = (input('Para sair [S]: ')).lower().startswith('s')
    print(sair)

    if sair is True:
        break