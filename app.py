# IMPORTAÇÕES DE BIBLIOTECAS
import os
import json  # ⬅️ NOVA IMPORTAÇÃO

#*******************************************************************************************************
# VARIÁVEIS GLOBAIS
ARQUIVO_JSON = 'restaurantes.json'  # ⬅️ NOVA VARIÁVEL
restaurantes = []  # ⬅️ AGORA COMEÇA VAZIA

#*******************************************************************************************************
# FUNÇÃO PARA CARREGAR DADOS DO JSON
def carregar_dados():
    global restaurantes
    try:
        # Verifica se o arquivo existe
        if os.path.exists(ARQUIVO_JSON):
            with open(ARQUIVO_JSON, 'r', encoding='utf-8') as f:
                restaurantes = json.load(f)
            print(f"📂 Dados carregados: {len(restaurantes)} restaurantes")
        else:
            # Se o arquivo não existe, começa com dados de exemplo
            restaurantes = ['Sabor do Nordeste', 'Pizzaria do João', 'Churrascaria do Gaúcho']
            salvar_dados()  # Cria o arquivo com dados iniciais
            print("📄 Arquivo de dados criado com restaurantes de exemplo")
    except Exception as e:
        print(f"❌ Erro ao carregar dados: {e}")
        restaurantes = []  # Lista vazia em caso de erro

#*******************************************************************************************************
# FUNÇÃO PARA SALVAR DADOS NO JSON
def salvar_dados():
    try:
        with open(ARQUIVO_JSON, 'w', encoding='utf-8') as f:
            json.dump(restaurantes, f, indent=4, ensure_ascii=False)
        print("💾 Dados salvos com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao salvar dados: {e}")

#*******************************************************************************************************
# VARIÁVEIS GLOBAIS
restaurantes = ['Sabor do Nordeste', 'Pizzaria do João', 'Churrascaria do Gaúcho']

#*******************************************************************************************************
# FUNÇÃO PARA EXIBIR O NOME DO PROGRAMA
def exibir_nome_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

#*******************************************************************************************************
# FUNÇÃO PARA EXIBIR O MENU
def exibir_menu():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Ativar Restaurante")
    print("4. Sair\n")

#*******************************************************************************************************
# FUNÇÃO PARA FINALIZAR O APP
def finalizar_app():
    limpar_tela()
    print("\nFinalizando o App.\n")

#*******************************************************************************************************
# FUNÇÃO PARA LIMPAR A TELA (REFATORADA)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#*******************************************************************************************************
# FUNÇÃO PARA OPÇÃO INVÁLIDA
def opcao_invalida():
    print("\nOpção inválida. Tente novamente.\n")
    input("Pressione Enter para continuar...")
    main()

#*******************************************************************************************************
# VOLTAR PARA O MENU PRINCIPAL
def voltar_menu_principal():
    print('-' * 50)
    input("Pressione Enter para voltar ao menu principal...")
    main()

#*******************************************************************************************************
def exibir_submenu(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-' * 50)
    print(texto)
    print('-' * 50)

#*******************************************************************************************************
# FUNÇÃO PARA CADASTRAR RESTAURANTE
def cadastrar_restaurante():
    exibir_submenu("CADASTRAR NOVO RESTAURANTE".center(50))
    nome_restaurante = input("\nDigite o nome do restaurante: ").strip()
    
    if not nome_restaurante:
        print("\n❌ Erro: O nome do restaurante não pode estar vazio!")
        voltar_menu_principal()
        return
    
    if nome_restaurante in restaurantes:
        print(f"\n⚠️  O restaurante '{nome_restaurante}' já está cadastrado!")
    else:
        restaurantes.append(nome_restaurante)
        print(f"\n✅ Restaurante '{nome_restaurante}' cadastrado com sucesso!")
    
    voltar_menu_principal()

#*******************************************************************************************************
# FUNÇÃO PARA LISTAR RESTAURANTES
def listar_restaurantes():
    exibir_submenu("LISTA DE RESTAURANTES".center(50))
    
    if restaurantes:
        print(f"\nTotal de restaurantes: {len(restaurantes)}\n")
        for idx, restaurante in enumerate(restaurantes, start=1):
            print(f"{idx:>2}. {restaurante}")
    else:
        print("\n📝 Nenhum restaurante cadastrado.")
    
    voltar_menu_principal()

#*******************************************************************************************************
# FUNÇÃO PARA ATIVAR RESTAURANTE
def ativar_restaurante():
    exibir_submenu("ATIVAR RESTAURANTE".center(50))
    
    if not restaurantes:
        print("\n📝 Nenhum restaurante cadastrado para ativar.")
        voltar_menu_principal()
        return
    
    print("\nRestaurantes disponíveis:\n")
    for idx, restaurante in enumerate(restaurantes, start=1):
        print(f"{idx:>2}. {restaurante}")
    
    try:
        escolha = int(input("\nEscolha o número do restaurante que deseja ativar: "))
        if 1 <= escolha <= len(restaurantes):
            restaurante_ativado = restaurantes[escolha - 1]
            print(f"\n✅ Restaurante '{restaurante_ativado}' foi ativado com sucesso!")
        else:
            print(f"\n❌ Número inválido. Escolha entre 1 e {len(restaurantes)}.")
    except ValueError:
        print("\n❌ Erro: Digite apenas números!")
    
    voltar_menu_principal()

#*******************************************************************************************************
# OPÇÃO ESCOLHIDA PELO USUÁRIO
def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif opcao_escolhida == 4:
            print("\n👋 Saindo...")
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

#*******************************************************************************************************
# FUNÇÃO PRINCIPAL DO PROGRAMA
def main():
    limpar_tela()
    exibir_nome_programa()
    exibir_menu()
    escolher_opcao()

#*******************************************************************************************************
# INICIAR O PROGRAMA
if __name__ == "__main__":
    main()