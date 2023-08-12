print()
print(f'{"DIO BANK.":^40}')
print('-' * 50)
menu = """
==== Menu ====
[d] Deposito
[s] Saque
[e] Extrato
[q] Sair
===============
=> """

saldo = 0
limite = 2000
extrato = ""
n_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Infome o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:>26,.2f}\n'.replace(",", "X").replace(".", ",").replace("X", ".")
            print("Depósito realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif n_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:>29,.2f}\n'.replace(",", "X").replace(".", ",").replace("X", ".")
            n_saques += 1
            print("Saque realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:>29,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        print("========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione a operação desejada.")