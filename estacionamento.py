def hash_linear(chave, tamanho_tabela):
    posicao = hash(chave) % tamanho_tabela
    while tabela_hash[posicao] is not None and tabela_hash[posicao][0] != chave:
        posicao = (posicao + 1) % tamanho_tabela
    return posicao

def inserir(chave, valor):
    posicao = hash_linear(chave, tamanho_tabela)
    tabela_hash[posicao] = (chave, valor)
    print(f"Par chave-valor inserido: ({chave}, {valor})")

def buscar(chave):
    posicao = hash_linear(chave, tamanho_tabela)
    entrada = tabela_hash[posicao]
    if entrada is not None and entrada[0] == chave and not entrada[2]:
        return entrada[1]
    else:
        return None

def exibir():
    for i, entrada in enumerate(tabela_hash):
        if entrada is not None:
            chave, valor, excluido = entrada
            if not excluido:
                print(f"Posição {i}: ({chave}, {valor})")
            else:
                print(f"Posição {i}: excluída")
        else:
            print(f"Posição {i}: vazia")

def excluir(chave):
    posicao = hash_linear(chave, tamanho_tabela)
    entrada = tabela_hash[posicao]
    if entrada is not None and entrada[0] == chave:
        tabela_hash[posicao] = (chave, entrada[1], True)
        print(f"Par chave-valor excluído: ({chave}, {entrada[1]})")
    else:
        print("Chave não encontrada")

# Cria uma tabela hash vazia
tamanho_tabela = 10
tabela_hash = [(None, None, False)] * tamanho_tabela

def salvar_arquivo(nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        for i, entrada in enumerate(tabela_hash):
            if entrada is not None:
                chave, valor, excluido = entrada
                if not excluido:
                    linha = f"{i},{chave},{valor}\n"
                    arquivo.write(linha)

# Cria uma tabela hash vazia
tamanho_tabela = 29
tabela_hash = [(None, None, False)] * tamanho_tabela

# Loop principal do menu
while True:
    print("\nMENU")
    print("1. Inserir par chave-valor")
    print("2. Buscar valor por chave")
    print("3. Exibir tabela hash")
    print("4. Excluir entrada por chave")
    print("5. Salvar tabela hash em arquivo")
    print("6. Sair")

    opcao = int(input("\nDigite a opção desejada: "))

    if opcao == 1:
        chave = input("Digite a chave: ")
        valor = input("Digite o valor: ")
        inserir(chave, valor)
    elif opcao == 2:
        chave = input("Digite a chave: ")
        valor = buscar(chave)
        if valor is not None:
            print(f"Valor correspondente: {valor}")
        else:
            print("Chave não encontrada")
    elif opcao == 3:
        exibir()
    elif opcao == 4:
        chave = input("Digite a chave: ")
        excluir(chave)
    elif opcao == 5:
        nome_arquivo = input("Digite o nome do arquivo: ")
        salvar_arquivo(nome_arquivo)
        print(f"Tabela hash salva em {nome_arquivo}")
    elif opcao == 6:
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida")