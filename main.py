menu = '''
Selecione uma das opções abaixo:
--------------------------------
  [1] depósito
  [2] saque
  [3] extrato
  ---
  [0] Sair
=> '''

saldo_atual = 0.0
limite_por_saque = 500.00
extrato = ""
quantidade_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    match opcao:
        # opção DEPOSITO
        case '1':
            print("--- DEPOSITO --- ")
            valor_deposito = float(input("Insira o valor que deseja depositar: R$ "))
            print(f"O valor a ser depositado é R$ {valor_deposito:.2f}.", end = " ")
            confirmar = input("Confirma? S/N: ")
            if confirmar.upper() == 'S':
                saldo_atual += valor_deposito
                extrato = extrato + " - Deposito...... R$ " + str(valor_deposito) + "\n"
                print("Depósito efetuado com sucesso!")
            else:
                print("N\nOperação não efetuada.")

        # opção SAQUE
        case '2':
            # verifica se quantidade de saques diários alcançou o limite
            if quantidade_saques == LIMITE_SAQUES:
                print("Não é possível efetuar mais saques hoje. Quantidade diária atingiu o limite.")
            else:
                print('''--- SAQUE ---\n Informações:\n  - até 03 saques diários\n  - até R$ 500.00 por saque
                ''')
                valor_saque = float(input("Insira o valor que deseja retirar: R$ "))
                # verifica se valor do saque é menor ou igual a zero
                if valor_saque <= 0:
                    print("Valor do saque não pode ser menor ou igual a zero. Por favor, insira um valor válido.")
                # verifica se valor do saque é maior que o limite permitido
                elif valor_saque > limite_por_saque:
                    print("Operação não efetuada. Valor acima do limite (até R$ 500.00 por saque).")
                # verifica se saldo em conta é suficiente para o saque
                elif valor_saque > saldo_atual:
                    print("Operação não efetuada. Saldo insuficiente!")
                else:
                    print(f"O valor a ser retirado é R$ {valor_saque:.2f}.", end = " ")
                    confirmar = input("Confirma? S/N: ")
                    if confirmar.upper() == 'S':
                        saldo_atual -= valor_saque
                        extrato = extrato + " - Saque......... R$ " + str(valor_saque) + "\n"
                        quantidade_saques += 1
                        print(f"Operação efetuada com sucesso! Quantidade de saques restantes para a data de hoje: {LIMITE_SAQUES - quantidade_saques}")

        # opção EXTRATO
        case '3':
            print("--- EXTRATO ---\nMovimentações:")
            print(extrato)
            print("\n------------------------------\n")
            print(f"Saldo atual... R$ {saldo_atual:.2f}")
        # opção SAIR

        case '0':
            print("Aplicativo será encerrado.", end = " ")
            confirmar = input("Confirma? S/N: ")
            if confirmar.upper() == 'S':
                break
        case other:
            print("Opção inválida")

