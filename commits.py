#Davi Machado - https://github.com/davimcruz/

import subprocess
import os

clear = lambda: os.system('cls')

def make_commit(commit_type, local, message):
    commitMessage = f"{commit_type}({local}): {message}"
    
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commitMessage])
    subprocess.run(["git", "push"])
    
    print("Commit realizado com sucesso!")

options = [
    ("feat", "Novo recurso"),
    ("fix", "Correção de bug"),
    ("refactor", "Refatoração"),
    ("chore", "Manutenção"),
    ("docs", "Documentação"),
    ("style", "Estilo"),
    ("test", "Teste"),
    ("perf", "Desempenho")
]

def show_rules():
    print("-----------------------------------------")
    print("Regras e boas práticas para commits: \n")
    print("- Use o imperativo na mensagem do commit.")
    print("- Exemplo: 'Adicionar nova funcionalidade' em vez de 'Adicionando' ou 'Adicionado'.")
    print("- Seja claro e conciso.")
    print("- Sempre explique o que foi feito e por quê. \n")
    print("-----------------------------------------")

def main_menu():
    clear()
    show_rules()
    print("1. Continuar")
    print("2. Cancelar")
    print("-----------------------------------------")

    try:
        choice = int(input("Escolha uma opção: "))
        if choice == 1:
            main()  
        elif choice == 2:
            print("Até mais!")
            exit()
        else:
            print("Opção inválida.")
            main_menu()  
    except ValueError:
        print("Por favor, insira um número válido.")
        main_menu()  

def main():
    clear()
    print("-----------------------------------------")
    print("Escolha uma opção de commit:")
    for idx, (commit_type, description) in enumerate(options):
        print(f"{idx + 1}. {description}")
    print("-----------------------------------------")

    try:
        choice = int(input("Digite o número da opção desejada: "))
        if 1 <= choice <= len(options):
            commit_type = options[choice - 1][0]
            print("-----------------------------------------")
            local = input("Digite o que foi afetado pelo commit (Qual diretório / Qual arquivo): ")
            print("-----------------------------------------")
            message = input("Digite a mensagem de commit: ")
            local = local.lower()
            message = message.lower()

            make_commit(commit_type, local, message)
        else:
            print("Opção inválida.")
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main_menu()
