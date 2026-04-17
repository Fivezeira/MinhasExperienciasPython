respostavar: str = input("Se você deseja prosseguir e ver o Portfólio digite (About), caso contrário digite (Quit). ")

if respostavar == "About":
    print("Bem vindo ao Gestor de Portfólio do Augusto.")
elif respostavar == "Quit":
    print("Saindo do Gestor de Portfólio.")
else:
    print("Erro: Comando Inválido.")
print("Até logo!")
