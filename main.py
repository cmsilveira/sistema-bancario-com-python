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

