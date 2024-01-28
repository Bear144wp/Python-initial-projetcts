lista = [ ]

while True:
    inicio = input('[i]nserir, [a]pagar, [l]istar')
    if inicio == 'i':
        valor = input('Qual valor para inserir?')
        lista.append(valor)
        print(f'Valor "{valor}" inserido na lista')
    
    elif inicio == 'a':
        valor_apagar = input(f'Qual dos valores deseja apagar: {valor}')
        try:
            valor_int = int(valor_apagar)
            del lista[valor_int]
        except IndexError or SyntaxError:
            print('erro')
        

    elif inicio == 'l':

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)

    
    else:
        print('Tente novamente, opção inválida')