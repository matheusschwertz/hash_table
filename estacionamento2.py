import pickle

class Estacionamento:
    def __init__(self):
        self.tabela = {}
        
    def adicionar_carro(self, letra, placa):
        if letra.isalpha() and len(letra) == 1:
            self.tabela[letra] = placa
            print(f"Carro com placa {placa} adicionado na posição {letra.upper()}.")
        else:
            print("Erro: chave inválida.")

    def remover_carro(self, letra):
        if letra in self.tabela:
            placa = self.tabela.pop(letra)
            print(f"Carro com placa {placa} removido da posição {letra.upper()}.")
        else:
            print("Erro: chave não encontrada.")
    
    def listar_carros(self):
        print("Lista de carros:")
        for letra, placa in self.tabela.items():
            print(f"{letra.upper()}: {placa}")
    
    def salvar_entradas(self, arquivo):
        with open(arquivo, 'wb') as f:
            pickle.dump(list(self.tabela.items()), f)

    def carregar_entradas(self, arquivo):
        with open(arquivo, 'rb') as f:
            self.tabela = dict(pickle.load(f))

def exibir_menu():
    print("Sistema de estacionamento")
    print("1 - Adicionar carro")
    print("2 - Remover carro")
    print("3 - Listar carros")
    print("4 - Salvar entradas")
    print("5 - Carregar entradas")
    print("0 - Sair")

estacionamento = Estacionamento()

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        letra = input("Digite a letra da posição (A-Z): ")
        placa = input("Digite a placa do carro: ")
        estacionamento.adicionar_carro(letra, placa)
    elif opcao == '2':
        letra = input("Digite a letra da posição (A-Z): ")
        estacionamento.remover_carro(letra)
    elif opcao == '3':
        estacionamento.listar_carros()
    elif opcao == '4':
        arquivo = input("Digite o nome do arquivo para salvar as entradas: ")
        estacionamento.salvar_entradas(arquivo)
    elif opcao == '5':
        arquivo = input("Digite o nome do arquivo para carregar as entradas: ")
        estacionamento.carregar_entradas(arquivo)
    elif opcao == '0':
        break
    else:
        print("Opção inválida.")

print("Obrigado por usar o sistema de estacionamento!")
