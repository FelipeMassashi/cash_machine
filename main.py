import locale

# Configurar o locale para aceitar números no formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class CaixaEletronico:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.extrato = []

    def consultar_saldo(self):
        return self.saldo

    def sacar_dinheiro(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append(f"Saque: -{valor:.2f}")
            return True
        else:
            return False

    def depositar_dinheiro(self, valor):
        self.saldo += valor
        self.extrato.append(f"Depósito: +{valor:.2f}")
        return True

    def ver_extrato(self):
        return self.extrato

    def transferir(self, outro_caixa, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            outro_caixa.depositar_dinheiro(valor)
            self.extrato.append(f"Transferência para poupança: -{valor:.2f}")
            return True
        else:
            return False

def criar_senha():
    senha = input("Crie uma senha para acessar o caixa eletrônico: ")
    return senha

def solicitar_senha():
    senha_correta = criar_senha()
    tentativas = 3

    while tentativas > 0:
        senha_digitada = input("\nDigite a senha: ")
        if senha_digitada == senha_correta:
            print("\nSenha correta. Acesso permitido.")
            return True
        else:
            tentativas -= 1
            print(f"\nSenha incorreta. Você tem {tentativas} tentativas restantes.")
    print("Número de tentativas excedido. Acesso negado.")
    return False

def obter_valor_monetario(mensagem):
    while True:
        entrada = input(mensagem)
        try:
            valor = locale.atof(entrada.replace(",", "."))
            return valor
        except ValueError:
            print("\nEntrada inválida! Por favor, insira um valor numérico no formato 19,00 ou 19.00.")

def main():
    if solicitar_senha():
        caixa_principal = CaixaEletronico(saldo_inicial=1000)
        caixa_poupanca = CaixaEletronico(saldo_inicial=500)

        while True:
            print("\n=== Caixa Eletrônico ===\n")
            print("1. Consultar Saldo")
            print("2. Sacar Dinheiro")
            print("3. Depositar Dinheiro")
            print("4. Ver Extrato")
            print("5. Transferir Dinheiro")
            print("6. Sair")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                print(f"\nSaldo disponível: R${caixa_principal.consultar_saldo():.2f}")

            elif opcao == "2":
                valor = obter_valor_monetario("Digite o valor a ser sacado: ")
                if caixa_principal.sacar_dinheiro(valor):
                    print("\nSaque realizado com sucesso!")
                else:
                    print("\nSaldo insuficiente!")

            elif opcao == "3":
                valor = obter_valor_monetario("Digite o valor a ser depositado: ")
                caixa_principal.depositar_dinheiro(valor)
                print("\nDepósito realizado com sucesso!")

            elif opcao == "4":
                extrato = caixa_principal.ver_extrato()
                print("\nExtrato:")
                for operacao in extrato:
                    print(operacao)

            elif opcao == "5":
                valor = obter_valor_monetario("Digite o valor a ser transferido: ")
                if caixa_principal.transferir(caixa_poupanca, valor):
                    print("\nTransferência realizada com sucesso!")
                else:
                    print("\nSaldo insuficiente para transferência!")

            elif opcao == "6":
                print("\nSaindo...")
                break

            else:
                print("\nOpção inválida!")

if __name__ == "__main__":
    main()
