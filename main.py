menu = """
  
  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair

=> """

saldo = 0
extrato = ""
numero_saques = 0
LIMITE = 500
LIMITE_SAQUES = 3

while True:

  opcao = input(menu)

  if opcao == "d":
    print("Depósito")
    valor = float(input("Informe o valor a ser depositado: "))
    saldo += valor
    extrato += f"Depósito R$ {valor:.2f} \n"
    print("Operação realizada com sucesso.") 
  
  elif opcao == "s":
    print("Saque")
    valor = float(input("Informe o valor a ser sacado: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > LIMITE
    excedeu_saques = numero_saques == LIMITE_SAQUES
    if excedeu_saldo:
      print("Operação falhou: Você não tem saldo suficiente para realizar esse saque.")
    elif excedeu_limite:
      print("Operação falhou: O valor desejado para saque é maior que o seu valor de limite.")
    elif excedeu_saques:
      print("Operação falhou: Você atingiu o número de saques diários permitidos.")
    elif valor <= 0:
      print("Operação falhou: O valor informado é inválido.")
    else:
      saldo -= valor
      numero_saques += 1
      extrato += f"Saque R$ {valor:.2f} \n"  
      print("Operação realizada com sucesso.")  

  elif opcao == "e":
    print("Extrato")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
  
  elif opcao == "q":
    break
  
  else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")