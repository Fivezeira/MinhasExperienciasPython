listadologin = []

def nick_existe(listadologin, nomedigitado):
    for user in listadologin:
        if user["nome"] == nomedigitado:
            print("Usuário já existente")
            return True
        
    return False


def registraruser():
    nomedigitado = input("Digite o seu nickname(nome):")
    senha = input("Agora digite a sua senha:")
    resultado = nick_existe(listadologin, nomedigitado)
    if resultado:
        print("Esse nick de usuário já existe.")
    else:
        usuario = {"nome": nomedigitado, "senha": senha}
        listadologin.append(usuario)

def login_usuario(listadologin):
    nomelogin = input("Digite seu nick de login:")
    senhalogin = input("Digite sua senha de login:")
    for user in listadologin:
        if user["nome"] == nomelogin and user["senha"] == senhalogin:
            print('Você logou!')
            return True
    else:
        print('Login incorreto ou não existente.')
        return False
    
def menu_login():
    while True:
        try:
            escolha = int(input("1 - Cadastrar\n2 - Login\n3 - listar usuários\n4 - Sair\n"))

            if escolha not in [1, 2, 3, 4]:
                print("Escolha uma opção válida!")
                continue

        except ValueError:
            print("Digite apenas números!")
            continue

        if escolha == 1:
            registraruser()

        elif escolha == 2:
            login_usuario(listadologin)

        elif escolha == 3:
            print(listadologin)

        elif escolha == 4:
            break

menu_login() 