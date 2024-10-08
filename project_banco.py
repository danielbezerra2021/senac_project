# Dicionário para armazenar informações da conta
conta = {"nome": None, "senha": None, "saldo": 0.0}

def criar_conta():
    """Cria uma nova conta bancária."""
    conta["nome"] = input("Nome e Sobrenome: ")
    conta["senha"] = input("Crie sua senha (A senha deve ter 4 dígitos): ")
    print(f"Conta criada para {conta['nome']}. Sua senha é {conta['senha']} (não compartilhe com ninguém).")

def verificar_saldo():
    """Exibe o saldo atual da conta."""
    print(f"Seu saldo é de R$ {conta['saldo']:.2f}")

def depositar_saldo():
    """Permite depositar um valor na conta."""
    valor = float(input("Digite quanto você quer depositar: "))
    conta["saldo"] += valor
    print(f"Depósito realizado. Seu saldo foi atualizado para R$ {conta['saldo']:.2f}")

def sacar_dinheiro():
    """Permite sacar um valor da conta, se houver saldo suficiente."""
    valor = float(input("Quanto você quer sacar: "))
    if valor > conta["saldo"]:
        print(f"Erro. Seu saldo atual é de R$ {conta['saldo']:.2f}")
    else:
        conta["saldo"] -= valor
        print(f"Saque realizado com sucesso! Saldo atual: R$ {conta['saldo']:.2f}")

def menu():
    """Exibe o menu de operações para o usuário."""
    print("\n1 - Criar Conta")
    print("2 - Verificar Saldo")
    print("3 - Depositar Saldo")
    print("4 - Sacar Dinheiro")
    print("5 - Encerrar o Atendimento")
    return input("Digite o número da operação desejada: ")

while True:
    opcao = menu()
    if opcao == "1" and not conta["nome"]:
        criar_conta()
    elif opcao == "2" and conta["nome"]:
        verificar_saldo()
    elif opcao == "3" and conta["nome"]:
        depositar_saldo()
    elif opcao == "4" and conta["nome"]:
        sacar_dinheiro()
    elif opcao == "5":
        print("Encerrando o atendimento.")
        break
    else:
        print("Opção inválida ou conta não criada.")
