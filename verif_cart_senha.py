from banco_dados import cart, ctg
import time

tentativa = 0
acesso = False

# Enquanto for verdade o usuário digita os 16 numeros do cartão
while True:
    n_cart = input('Digite os 16 números do seu cartão de crédito!:\n')
    time.sleep(1)
#=================================================================
# Checa para ver se a quantidade digitada é diferente de 16
# Se for qualquer quantidade exceto 16 ele diz que é inválido e volta para o input
    if len(n_cart) != 16:
        print('Quantidade de caracteres inválido!')
        continue
#=================================================================
# Se o usuário digitar corretamente os 16 números e por exatamente os números que corresponde ao seu cartão registrado ele começa um novo 'Enquanto', um novo imput para digitar a senha e com a condição de checagem de tentativas
    elif n_cart in cart:
        while tentativa < 3:
            n_senha = input('Digite os 4 digitos da sua senha!:\n')
            nome =cart[n_cart][1]
            senha = cart[n_cart][0]
#=================================================================
            # Verifica se a quantidade de caracteres é diferente de 4 dígitos, se for diferente, ele conta até três erros e diz que a quantidade de caracteres é inválido
            if len(n_senha) != 4:
                tentativa +=1
                print(f'Quantidade de caracteres inválido! {tentativa} de 3 tentativas!')
#=================================================================
            # Se o usuário digitar os 4 digitos da senha e por a senha vinculada ao cartão, ele dar as boas vindas e diz o nome do usuário
            elif n_senha == senha:
                ctg()
                print(f'Seja bem-vindo {nome}!')
                acesso = True
                break
#=================================================================
            # Se a senha estiver com os 4 digitos, mas estiver incorreta ele ele conta até três erros e diz que a senha é inválida 
            else:
                tentativa +=1
                ctg()
                print(f'Senha incorreta, {tentativa} de 3 tentativas!')
#=================================================================
# Aqui verifica as tentativas falhas das senhas e quando elas batem três tentativas essa condição se ativa e bloquea o acesso por um curto periodo de tempo e libera novamente do inicio
        if tentativa == 3:
            print('Acesso bloqueado aguarde 30 segundos para uma nova tentativa!')
            time.sleep(5)
            print('Acesso liberado, tente novamente!')
            time.sleep(2)
            tentativa = 0
            continue
# Verifica se o acesso foi autorizado. Se a variável for True, executa o break para encerrar o laço externo (while True), evitando que o programa solicite o cartão novamente
        if acesso:
            break
#=================================================================
# Se o usuário digitar os 16 números do cartão, mas a númeração não bater com o banco de dados, ele diz que o cartão não foi encontrado e volta para o imput do cartão
    else:
        print('Cartão não encontrado, tente novamente!')
        time.sleep(2)

# OBS: a maioria dos sleeps servem para dar um tempo entre uma interface e outra
