entrada = input('Voce deseja entrar? S / N')
senha = input('Digite a sua senha')

senha_permitida = '123456'

if (entrada == 'S' or entrada == 's') and senha == senha_permitida:
    print('Voce entrou!')

elif not senha:
    print('sem senha')

else:
    print('Voce escolheu sair')