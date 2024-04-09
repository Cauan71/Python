import os

os.system("cls || clear")

loginCadastrado: str = "abc"
senhaCadastrada = 123

login = str(input("Digite o login: "))
senha = int(input("Digite a senha : "))

if login == loginCadastrado and senha == senhaCadastrada:
    print(f"Bem - Vindo(a)")
else:
    print(f"Usuário e Senha Inválidos!")



