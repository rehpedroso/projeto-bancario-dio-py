menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = int(input(menu))
    
    if opcao == 1:
        #Deposito
        depositar = float(input("Insira o valor que sera depositado: "))

        if depositar > 0:
            saldo += depositar
            print("Deposito realizado com sucesso!")
            extrato += f'\nDeposito: R$ {depositar:.2f}'
        else: 
            print("Operacao falhou! Valor digitado esta invalido.")
        
    elif opcao == 2:
        #Saque
        if saldo > 0:
            sacar = float(input("Insira o valor que sera sacado: "))
            
            if sacar <= 500:
                if numero_saque <= LIMITE_SAQUE:
                    saldo -= sacar
                    print(f'Foi realizado o saque no valor de R$ {sacar:.2f}')
                    print('\nSaque realizado com sucesso!')
                    print(f'Saldo: {saldo:.2f}')
                    extrato += f'\nSaque: R$ {sacar:.2f}'
                    numero_saque += 1
                else:
                    print('Operacao falhou! O limite de saque foi execedido.')
            else:
                print('Operacao falhou! O valor do saque excede o limite.')

        else:
            print(f'Operacao falhou! Saldo é de R$ {saldo}')
    
    elif opcao == 3:
        #Extrato
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        
    elif opcao == 0:
        break
    
    else:
        print("Operacao invalida, por favor selecione novamente a operacao desejada.")