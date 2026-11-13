from banco_dados import cart
from temporiza import tempp

tentativa = 0

while True:
    nc = input('Digite os 16 numéros do seu cartão: ')

    if len(nc) != 16:
        print('Quantidade de caracteres inválido!')
        continue

    elif nc in cart:

        while tentativa < 3:
            senha = cart[nc][0]
            nome = cart[nc][1]

            sc = input('Digite os 4 dígitos do seu cartão: ')

            if len(sc) != 4:
                print('Quantidade de caracteres inválido!')
                tentativa += 1

            elif sc == senha:
                tempp()
                print(f'Seja bem vindo {nome}')
                break

            else:
                print('Senha inválida!')
                tentativa += 1

        if tentativa == 3:
            print('Senha bloqueada!')
            break

    else:
        print('Cartão não encontrado!')