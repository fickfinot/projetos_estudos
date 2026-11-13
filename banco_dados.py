import time

cart = {
    '0000000000000000': ('0000', 'Mário'),
    '0000000000000001': ('0001', 'Luide'),
    '0000000000000002': ('0002', 'Kratos'),
    '0000000000000003': ('0003', 'Atreus'),
    '0000000000000004': ('0004', 'Eron'),
    '0000000000000005': ('0005', 'Kael'),
    '0000000000000006': ('0006', 'Rei Julian')
}


def ctg():
    contador = 5
    print('Aguarde!')
    while contador >= 1:

        time.sleep(1)
        print(contador)
        contador -= 1
    
    time.sleep(1)

