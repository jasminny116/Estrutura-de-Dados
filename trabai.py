usuarios = {"admin": "12345"}

def fazer_login():
    print("************TELA DE LONGIN************")

    login = input("Digite o seu usuário: ")
    senha = input("Digite a sua senha: ")
                  
    if login in usuarios and senha == usuarios[login]:
        print("Login realizado com sucesso!\n")
        return True 
    else:
        print("Usuário ou senha incorretos.\n")
    
def adicionar_usuario():
    print("************ADICIONAR USUÁRIO************")

    nome = input("Digite o nome do novo usuário: ")
    senha = input("Digite a senha do novo usuário: ")

    usuarios[nome] = senha

    print(f"Usuário '{nome}' adicionado com sucesso!")

def remover_usuario():
    print("************REMOVER USUÁRIO************")

    nome = input("Digite o nome do usuário que deseja remover: ")

    if nome in usuarios:
        del usuarios[nome] 
        print(f"Usuário '{nome}' removido com sucesso!")
    else:
        print(f"Usuário '{nome}' não encontrado.")

def pesquisar_usuarios():
    print("************PESQUISAR USUÁRIO************")

    nome = input("Digite o nome do usuário que deseja pesquisar: ")

    if nome in usuarios:
        print(f"Usuário '{nome}' encontrado!")
    else:
        print(f"Usuário '{nome}' não encontrado.")

def menu():
    while True:
        print("************ MENU ************")
        print("1 - Adicionar usuário")
        print("2 - Remover usuário")
        print("3 - Pesquisar usuário")
        print("4 - Sair")

        opcao = input("Escolha uma opção do menu: ")

        if opcao == "1":
            adicionar_usuario()
        elif opcao == "2":
            remover_usuario()
        elif opcao == "3":
            pesquisar_usuarios()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("\nOpção inválida, tente novamente.")

if fazer_login():
    menu()