menu = """
==================================================
                 [d] Depositar
                 [s] Sacar
                 [e] Extrato
                 [q] Sair
==================================================
=> """

detalhe = "==================================================\n"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
historico_depositos=[]
historico_saques=[]
LIMITE_SAQUES = 3
limite = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = "Depósito"
        print(detalhe)
        print(deposito.center(50))
        saldo_depositado = float(input("\n\n    Insira o quanto deseja depositar: "))
        if saldo_depositado > 0:
            saldo += saldo_depositado
            historico_depositos += [saldo_depositado]
            print("\n    Depósito efetuado com sucesso.\n\n")
        else:
            print("\n    Não é permitido saldo negativo.\n\n")
        print(detalhe)
       

    elif opcao == "s":
        saque = "Saque"
        print(detalhe)
        print(saque.center(50))
        saldo_saque = float(input("\n\n   Insira o quanto deseja sacar: "))

        if LIMITE_SAQUES != limite:
            if saldo_saque < 0:
                print("\n    Não é permitido saldo negativo\n\n")
            elif saldo_saque > 500:
                print("\n   Seu limite máximo de saque é de R$ 500.00 por vez.\n\n")
            elif saldo_saque > saldo:
                print("\n    Você não tem saldo o suficiente para completar a transação.\n\n")
            else:
                saldo -= saldo_saque
                limite += 1
                historico_saques += [saldo_saque]
                print ("\n   Saque efetuado com sucesso.\n\n")
        else:
            print("\n   Limite de saque diário atingido.\n\n")
        print(detalhe)

    elif opcao == "e":
        extrato = "Extrato\n"
        transacoes ="Transações efetuadas.\n\n"
        saques = "Houve um saque no valor de: R${:.2f}"
        depositos = " Houve um depósito no valor de R${:.2f}"
        saldo_total = "Saldo total da conta é de: R${:.2f}"
        print(detalhe)
        print(extrato.center(50))
        print(saldo_total.format(saldo).center(50))
        print("\n")
        print(transacoes.center(50))

        for deposito in historico_depositos:
            print(depositos.format(deposito).center(50))

        print("\n")

        for saque in historico_saques:
            print(saques.format(saque).center(50))

        print("\n")

        print(detalhe)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")