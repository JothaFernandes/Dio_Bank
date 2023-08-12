def menu():
    menu = """
    ====== Menu ======
    [ d ] Deposito
    [ s ] Saque
    [ e ] Extrato
    [ c ] Nova Conta
    [ u ] Novo Usuário
    [ l ] Contas
    [ q ] Sair
    ===================
    => """
    return input(menu)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:>26,.2f}\n'.replace(",", "X").replace(".", ",").replace("X", ".")
        limpar()
        print("Depósito realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, nro_saques, limite_saques):

    if valor > saldo:
        limpar()
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        limpar()
        print("Operação falhou! O valor do saque excede o limite.")
    elif nro_saques >= limite_saques:
        limpar()
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:>29,.2f}\n'.replace(",", "X").replace(".", ",").replace("X", ".")
        nro_saques += 1
        limpar()
        print("Saque realizado com sucesso.")
    else:
        limpar()
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, nro_saques

def exibir_extrato(saldo,/,*, extrato):
    limpar()
    print("\n=============== EXTRATO ===============")
    print("Não foram realizados movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:>29,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print("========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        limpar()
        print("\nJá existe usuário com este CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    limpar()
    print("Usuário criado com sucesso!!") 


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        limpar()
        print("Conta criada com sucesso!!")
        return {"agencia": agencia, "numero_conta": numero_conta,"usuario": usuario}
    
    print("\nUsuário não encontrado, fluxo de criação encerrado!")


def listar_contas(contas):
    limpar()
    print("\n=============== CONTAS ===============")
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print(linha)
        print("-" * 40)

def limpar():
    print("\x1b[2J\x1b[1;1H")
    print(f'{"DIO BANK.":^60}')
    print('-' * 70)

def main():
    print()
    print(f'{"DIO BANK.":^60}')
    print('-' * 70)

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 2000
    extrato = ""
    nro_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            limpar()
            print("============= DEPÓSITO =============")
            valor = float(input("Infome o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            if nro_saques >= LIMITE_SAQUES:
                limpar()
                print("Operação não pode ser realizada! Número máximo de saques excedido.")
            else:
                limpar()
                print("=============== SAQUE ===============")
                valor = float(input("Informe o valor do saque: "))

                saldo, extrato, nro_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, nro_saques=nro_saques, limite_saques=LIMITE_SAQUES,)
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif  opcao == "u":
            limpar()
            print("=========== NOVO USUÁRIO ============")
            criar_usuario(usuarios)

        elif opcao == "c":
            limpar()
            print("============ NOVA CONTA ============")
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)
        
        elif opcao == "q":
            limpar()
            print(f'{"Obrigado por usar nossos serviços!":^60}')
            print('-' * 70)
            break

        else:
            limpar()
            print("Operação inválida, por favor selecione a operação desejada.")


main()