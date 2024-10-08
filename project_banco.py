class ContaBancaria:
    def __init__(self, nome):
        """Inicializa uma nova conta bancária com titular e saldo inicial."""
        self.nome = nome
        self.saldo = 0.0
        print(f"Conta criada para {self.nome} com saldo inicial de R$: {self.saldo:.2f}")

    def verificar_saldo(self):
        """Exibe o saldo atual da conta."""
        print(f"Saldo atual de {self.nome}: R$: {self.saldo:.2f}")

    def depositar(self, valor):
        """Deposita uma quantia no saldo da conta."""
        self.saldo += valor
        print(f"Depósito de R$: {valor:.2f} realizado. Saldo atual: R$: {self.saldo:.2f}")

    def sacar(self, valor):
        """Saca uma quantia do saldo da conta se houver saldo suficiente."""
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$: {valor:.2f} realizado. Saldo atual: R$: {self.saldo:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")

def menu():
    """Exibe o menu de operações disponíveis ao usuário."""
    print("\nEscolha uma operação:")
    print("1 - Criar conta")
    print("2 - Verificar saldo")
    print("3 - Depositar dinheiro")
    print("4 - Sacar dinheiro")
    print("5 - Encerrar atendimento")
    return input("Digite o número da operação desejada: ")

def main():
    conta = None
    while True:
        opcao = menu()
        if opcao == "1":
            nome = input("Digite o nome do titular: ")
            conta = ContaBancaria(nome)
        elif opcao == "2" and conta:
            conta.verificar_saldo()
        elif opcao == "3" and conta:
            valor = float(input("Digite o valor para depósito: R$: "))
            conta.depositar(valor)
        elif opcao == "4" and conta:
            valor = float(input("Digite o valor para saque: R$: "))
            conta.sacar(valor)
        elif opcao == "5":
            print("Encerrando o atendimento.")
            break
        else:
            print("Opção inválida ou conta não criada.")

if __name__ == "__main__":
    main()
