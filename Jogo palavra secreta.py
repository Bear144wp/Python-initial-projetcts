palavra_secreta = 'Bear'.lower()
palavras_acertadas = ''

while True:
    tentativa = input('Digite apenas uma letra para adivinhar: ')
    numero_de_letras = len(tentativa)
    if numero_de_letras < 2:

        if tentativa in palavra_secreta:
            palavras_acertadas += tentativa
            
            palavra_formada = ''
            for letra_secreta in palavra_secreta:
                if letra_secreta in palavras_acertadas:
                    palavra_formada += letra_secreta
                else: 
                    palavra_formada += '*'
            print(palavra_formada)
        else: 
            print('*****')

        
    else:
        print('Digite apenas uma letra!!!!!!!!!')