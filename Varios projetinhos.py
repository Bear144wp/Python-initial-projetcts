numero = input('Digite um número inteiro')

if numero.isdigit:
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'impar'
    
    if par_impar:
        par_impar_texto = 'par'
        print(f'O número {numero_int} é {par_impar_texto}')

else:
    print('Voce nao digitou um numero inteiro')
    



'''hora = int(input('Digite o horario atual'))
if hora <= 13:
    print('Bom dia')
elif hora <= 18:
    print('Boa tarde')
else: 
    print('Boa noite')'''




'''nome = input('Digite seu nome')
len_do_nome = len(nome)

if len_do_nome <= 4:
    print('Seu nome é curto')
elif len_do_nome <=6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')'''

