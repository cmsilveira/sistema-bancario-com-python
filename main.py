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

