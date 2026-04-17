memoria = []

def addnovo(memoria):
    nome = input("Nome do jogo: ")

    projeto = {
        "nome": nome,
        "concluido": False,
        "historico": []
    }

    memoria.append(projeto)
    print("Jogo adicionado!")


def listnovo(memoria):
    if len(memoria) == 0:
        print("Nenhum jogo cadastrado.")
    else:
        for i, projeto in enumerate(memoria, 1):
            print(f"\n{i}º Jogo:")
            print("Nome:", projeto["nome"])
            print("Concluido:", projeto["concluido"])
            print("Historico:", projeto["historico"])


def aboutnovo():
    print("Bem-vindo ao Gestor de Jogos do Augusto!")


def procurar_projeto(memoria, nome_busca):
    for projeto in memoria:
        if projeto["nome"] == nome_busca:
            return projeto
    return None


def update_projeto(memoria):
    nome_busca = input("Qual jogo você quer atualizar? ")

    projeto = procurar_projeto(memoria, nome_busca)

    if projeto is not None:

        novo_nome = input("Novo nome (ou ENTER pra manter): ")
        novo_status = input("Concluido? (true/false): ")

        if novo_nome != "":
            projeto["nome"] = novo_nome

        if novo_status == "true":
            projeto["concluido"] = True
        elif novo_status == "false":
            projeto["concluido"] = False

        data = input("Digite a data da mudança: ")

        projeto["historico"].append(
            (data, projeto["concluido"], projeto["nome"])
        )

        print("Atualizado!")
    else:
        print("Jogo não encontrado.")


def delete_projeto(memoria):
    nome_busca = input("Qual jogo deseja deletar? ")

    projeto = procurar_projeto(memoria, nome_busca)

    if projeto is not None:
        memoria.remove(projeto)
        print("Removido!")
    else:
        print("Jogo não encontrado.")


while True:
    respostavar = input(
        "\nDigite:\n"
        "About / Add / List / Update / Delete / Quit\n-> "
    ).lower()

    if respostavar == "about":
        aboutnovo()

    elif respostavar == "add":
        addnovo(memoria)

    elif respostavar == "list":
        listnovo(memoria)

    elif respostavar == "update":
        update_projeto(memoria)

    elif respostavar == "delete":
        delete_projeto(memoria)

    elif respostavar == "quit":
        print("Saindo...")
        break

    else:
        print("Comando inválido.")

print("Até logo!")