print("Bem-vindo ao Sistema de Contatos Comerciais - Desenvolvido por Filipi Buffalo") 

# Lista que armazenará os contatos (lista de dicionários)
lista_contatos = []  

# ID global 
id_global = 1234567   
#     FUNÇÃO: CADASTRAR CONTATO
def cadastrar_contato(id):
    """Cadastra um contato com id, nome, atividade e telefone."""
    print("\n--- Cadastro de Contato ---")

    nome = input("Nome do contato: ")
    atividade = input("Atividade do contato: ")
    telefone = input("Telefone do contato: ")

    #  dicionário do contato
    contato = {
        "id": id,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }

    #  lista
    lista_contatos.append(contato.copy())  

    print(f"Contato {nome} cadastrado com sucesso!\n")
#     FUNÇÃO: CONSULTAR CONTATOS
def consultar_contatos():
    """Menu interno de consulta de contatos."""
    while True:
        print("\n--- Menu de Consultas ---")
        print("1 - Consultar Todos")
        print("2 - Consultar por Id")
        print("3 - Consultar por Atividade")
        print("4 - Retornar ao Menu Principal")

        opc = input("Escolha uma opção: ")

        # CONSULTAR TODOS
        if opc == "1":
            print("\n--- Lista Completa de Contatos ---")
            if not lista_contatos:
                print("Nenhum contato cadastrado.")
            else:
                for c in lista_contatos:
                    print(f"ID: {c['id']} | Nome: {c['nome']} | Atividade: {c['atividade']} | Telefone: {c['telefone']}")

        # CONSULTAR POR ID
        elif opc == "2":
            try:
                id_busca = int(input("Digite o ID: "))
                encontrado = False
                for c in lista_contatos:
                    if c["id"] == id_busca:
                        print(f"\nID: {c['id']} | Nome: {c['nome']} | Atividade: {c['atividade']} | Telefone: {c['telefone']}")
                        encontrado = True
                        break
                if not encontrado:
                    print("ID não encontrado.")
            except:
                print("Entrada inválida.")

        # CONSULTAR POR ATIVIDADE
        elif opc == "3":
            atividade = input("Digite a atividade: ").strip().lower()
            encontrados = [c for c in lista_contatos if c["atividade"].lower() == atividade]

            if encontrados:
                for c in encontrados:
                    print(f"ID: {c['id']} | Nome: {c['nome']} | Atividade: {c['atividade']} | Telefone: {c['telefone']}")
            else:
                print("Nenhum contato encontrado com essa atividade.")

        # RETORNAR AO MENU PRINCIPAL
        elif opc == "4":
            return  #  sair e voltar ao menu principal

        # OPÇÃO INVÁLIDA
        else:
            print("Opção inválida! Tente novamente.")

#     FUNÇÃO: REMOVER CONTATO

def remover_contato():
    """Remove um contato pelo ID."""
    while True:
        try:
            id_remover = int(input("\nDigite o ID do contato a remover: "))
        except:
            print("Entrada inválida!")
            continue

        for c in lista_contatos:
            if c["id"] == id_remover:
                lista_contatos.remove(c)
                print("Contato removido com sucesso!")
                return  

        print("ID inválido! Tente novamente.")

#     MENU PRINCIPAL

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Cadastrar Contato")
    print("2 - Consultar Contato")
    print("3 - Remover Contato")
    print("4 - Encerrar Programa")

    opcao = input("Escolha uma opção: ")

    # CADASTRAR
    if opcao == "1":
        cadastrar_contato(id_global)
        id_global += 1  # incrementa ID automaticamente

    # CONSULTAR
    elif opcao == "2":
        consultar_contatos()

    # REMOVER
    elif opcao == "3":
        remover_contato()

    # SAIR
    elif opcao == "4":
        print("Programa encerrado. Até logo!")
        break

    # OPÇÃO INVÁLIDA            #foram usados blocos de codigos e funçoes de repetiçao 
    else:
        print("Opção inválida! Tente novamente.")