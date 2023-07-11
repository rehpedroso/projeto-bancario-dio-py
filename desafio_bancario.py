import textwrap

def menu():
    menu = """
    ========== MENU ==========
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Cadastrar novo usuário
    [5] Cadastrar nova conta bancária
    [6] Listar contas
    [0] Sair
    => """
    return int(input(menu))

def depositar(saldo, extrato, valor_depositar, /):
    if valor_depositar > 0:
        saldo += valor_depositar
        print("\nDeposito realizado com sucesso!\n")
        extrato += f'\tDeposito: R$ {valor_depositar:.2f}'
    else: 
        print("\nOperacao falhou! Valor digitado esta invalido.\n")
    return saldo, extrato

def sacar(*, saldo, extrato, valor_saque, limite, numero_saques, limite_saques):
    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('Operacao falhou ! Saldo insuficiente.')
        print(f'Saldo = R$ {saldo}')
    
    elif excedeu_limite:
        print('Operacao falhou ! O valor do saque excede ao limite.')

    elif excedeu_saques:
        print('Operação falhou ! Numero de saque excede ao limite permitido')

    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f'\tSaque: R$ {valor_saque:.2f}'
        numero_saques += 1
        print('\nSaque realizado com sucesso!')
        saque_restante = limite_saques - numero_saques
        print(f'Você pode realizar mais {saque_restante} saque(s)')
        #saque_restante -= 1 => verificar a questão da quantodade de saques feito

    else:
        print('\nOperacao falhou ! Valor inválido.')

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

def novo_usuario(usuarios):
    cpf = input('Informe o CPF do usuario (somente numeros): ')
    
    if validar_cpf(cpf):
        print("CPF Válido!")
    else:
        print("CPF inválido ! CPf precisa conter 11 dígitos.")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nCPF já cadastrado no sistema!')
        return
    
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario cadastardo com sucesso!")

def validar_cpf(cpf):
    if len(cpf) == 11:
        return True
    else:
        return False

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    if validar_cpf(cpf):
        print("CPF Válido!")
    else:
        print('CPF Inválido ! CPf precisa conter 11 dígitos.')

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nConta cadastrada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('\nUsuário não encontrado, fluxo de criação de conta encerrado!')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print('=' * 100)
        print(textwrap.dedent(linha))

def main():
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []
    #numero_conta = 1

    while True:
        opcao = menu()
        
        if opcao == 1:
            #Deposito
            valor_depositar = float(input("\nInsira o valor que sera depositado: "))
            saldo, extrato = depositar(saldo, extrato, valor_depositar)
            
        elif opcao == 2:
            #Saque
            valor_saque = float(input("\nInsira o valor que sera sacado: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo, 
                extrato=extrato,
                valor_saque=valor_saque,
                limite=limite,
                numero_saques = numero_saques,
                limite_saques = limite_saques,
            )
        
        elif opcao == 3:
            #Extrato
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == 4:
            #Cadastrar novo usuario
            novo_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                #numero_conta += 1

        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 0:
            break
        
        else:
            print("\nOperacao invalida, por favor selecione novamente a operacao desejada.\n")

main()