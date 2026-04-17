
while True:
    respostavar: str = input("Se você deseja prosseguir e ver o Portfólio digite (About), se deseja sair digite (Quit) e se deseja adicionar digite (Add). ")
    if respostavar == "About":
        print("Bem vindo ao Gestor de Portfólio do Augusto.")
    elif respostavar == "Add":
        addp = int(input("Quantos projetos você deseja cadastrar?"))
        if addp >= 1:
            for i in range(addp):
                nomes = input(f"Qual o nome para o seu {i+1}º projeto?")
                print(f"SUCESSO: Projeto {nomes} adicionado")
        else:
            print("Erro: Número Inválido.")
        print("Saindo do Gestor de Portfólio...")
        break
    elif respostavar == "Quit":
        print("Saindo do Gestor de Portfólio.")
        break
    else:
        print("Erro: Comando Inválido.")
print("Até logo!")
