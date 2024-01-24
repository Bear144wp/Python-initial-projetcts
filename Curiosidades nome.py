nome = input('Digite seu nome ')
idade = input('Digite a sua idade ')

nome_padrao = (f'Seu nome é {nome}')
nome_invertido = (f'Seu nome invertido é: {nome[::-1]}')
letras = (f'Seu nome tem {[len(nome)]} letras')
primeira_letra = (f'A primeira letra do seu nome é: {nome[0:1:]}')
ultima_letra = (f'A ultima letra do seu nome é: {nome[-1::]}')



if nome and idade:
    print(nome_padrao)
    print(nome_invertido)
    
    if ' ' in nome:
        print('Seu nome tem espaços')
    else:
        print('Seu nome não contém espaços!') 

    print(letras)
    print(primeira_letra)
    print(ultima_letra)
else:
    print('Desculpe, um dos campos está vazio')