saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

        =>"""

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor do deposito: "))
        if valor >= 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f} \n"
        else:
            print("Operação falhou!! O valor informado está incorreto.")

    elif opcao == "s":
        valor = float(input("Digite o valor do Saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_de_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou!!! Sem saldo.")

        elif excedeu_limite:
            print("Operação falhou!!! Operação ultrapassou o limite.")

        elif excedeu_saques:
            print("Operação falhou!!!! Excedeu o liite de saques diários.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
        else:
            print("Operação falhou!!! O valor informado é invalido")

    elif opcao == "e":
        print("\n====================EXTRATO================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("===========================================")
    
    elif opcao == "q":
        break

    else:
        print("Operação invalida. Selecionar operação desejada.")

            


    