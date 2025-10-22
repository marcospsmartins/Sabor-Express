# IMPORTAÇÕES DE BIBLIOTECAS
import os
import json

#*******************************************************************************************************
# VARIÁVEIS GLOBAIS
ARQUIVO_JSON = 'restaurantes.json'
restaurantes = []  # AGORA SERÁ UMA LISTA DE DICIONÁRIOS
CATEGORIAS = ['Italiana', 'Japonesa', 'Brasileira', 'Mexicana', 'Chinesa', 'Árabe', 'Fast Food', 'Vegetariana', 'Frutos do Mar', 'Café', 'Outra']

#*******************************************************************************************************
# FUNÇÃO PARA MIGRAR DA ESTRUTURA ANTIGA PARA A NOVA
def migrar_para_nova_estrutura(lista_antiga):
    print("🔄 Migrando dados para nova estrutura...")
    nova_lista = []
    for nome in lista_antiga:
        novo_restaurante = {
            'nome': nome,
            'categoria': 'Brasileira',  # Categoria padrão
            'ativo': True  # Todos ativos por padrão na migração
        }
        nova_lista.append(novo_restaurante)
    return nova_lista

#*******************************************************************************************************
# FUNÇÃO PARA CARREGAR DADOS DO JSON
def carregar_dados():
    global restaurantes
    try:
        # Verifica se o arquivo existe
        if os.path.exists(ARQUIVO_JSON):
            with open(ARQUIVO_JSON, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                
            # Verifica se é a nova estrutura ou antiga
            if dados and isinstance(dados[0], dict):
                # Já está na nova estrutura
                restaurantes = dados
            else:
                # Migra da estrutura antiga para a nova
                restaurantes = migrar_para_nova_estrutura(dados)
                salvar_dados()
                
            print(f"📂 Dados carregados: {len(restaurantes)} restaurantes")
        else:
            # Se o arquivo não existe, começa com dados de exemplo na NOVA estrutura
            restaurantes = [
                {'nome': 'Sabor do Nordeste', 'categoria': 'Brasileira', 'ativo': True},
                {'nome': 'Pizzaria do João', 'categoria': 'Italiana', 'ativo': False},
                {'nome': 'Churrascaria do Gaúcho', 'categoria': 'Brasileira', 'ativo': True}
            ]
            salvar_dados()
            print("📄 Arquivo de dados criado com restaurantes de exemplo (nova estrutura)")
    except Exception as e:
        print(f"❌ Erro ao carregar dados: {e}")
        restaurantes = []

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
# FUNÇÃO PARA EXIBIR O NOME DO PROGRAMA
def exibir_nome_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██║░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
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
    print("3. Listar por Categoria")
    print("4. Ativar/Desativar Restaurante")
    print("5. Sair\n")

#*******************************************************************************************************
# FUNÇÃO PARA FINALIZAR O APP
def finalizar_app():
    limpar_tela()
    print("\n💾 Salvando dados antes de sair...")
    salvar_dados()
    print("👋 Finalizando o App.\n")

#*******************************************************************************************************
# FUNÇÃO PARA LIMPAR A TELA (REFATORADA)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#*******************************************************************************************************
# FUNÇÃO PARA OPÇÃO INVÁLIDA
def opcao_invalida():
    print("\n❌ Opção inválida. Tente novamente.\n")
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
    
    # Nome do restaurante
    nome_restaurante = input("\nDigite o nome do restaurante: ").strip()
    
    if not nome_restaurante:
        print("\n❌ Erro: O nome do restaurante não pode estar vazio!")
        voltar_menu_principal()
        return
    
    # Verifica se já existe
    nomes_existentes = [r['nome'].lower() for r in restaurantes]
    if nome_restaurante.lower() in nomes_existentes:
        print(f"\n⚠️  O restaurante '{nome_restaurante}' já está cadastrado!")
        voltar_menu_principal()
        return
    
    # Seleção de categoria
    print("\n📋 Categorias disponíveis:")
    for idx, categoria in enumerate(CATEGORIAS, start=1):
        print(f"{idx:>2}. {categoria}")
    
    try:
        escolha_categoria = int(input(f"\nEscolha a categoria (1-{len(CATEGORIAS)}): "))
        if 1 <= escolha_categoria <= len(CATEGORIAS):
            categoria_escolhida = CATEGORIAS[escolha_categoria - 1]
        else:
            print("❌ Opção inválida. Usando categoria padrão 'Brasileira'.")
            categoria_escolhida = 'Brasileira'
    except ValueError:
        print("❌ Entrada inválida. Usando categoria padrão 'Brasileira'.")
        categoria_escolhida = 'Brasileira'
    
    # Cria o novo restaurante
    novo_restaurante = {
        'nome': nome_restaurante,
        'categoria': categoria_escolhida,
        'ativo': False  # Novo restaurante começa inativo
    }
    
    restaurantes.append(novo_restaurante)
    salvar_dados()
    print(f"\n✅ Restaurante '{nome_restaurante}' ({categoria_escolhida}) cadastrado com sucesso!")
    print("💡 Lembre-se de ativar o restaurante no menu principal para ficar visível.")
    
    voltar_menu_principal()

#*******************************************************************************************************
# FUNÇÃO PARA LISTAR RESTAURANTES
def listar_restaurantes():
    exibir_submenu("LISTA DE RESTAURANTES".center(50))
    
    if restaurantes:
        # Contadores por categoria
        contador_categorias = {}
        for restaurante in restaurantes:
            categoria = restaurante['categoria']
            contador_categorias[categoria] = contador_categorias.get(categoria, 0) + 1
        
        print(f"\n🍽️  Total de restaurantes: {len(restaurantes)}")
        print("📊 Por categoria:")
        for categoria, quantidade in contador_categorias.items():
            print(f"   • {categoria}: {quantidade}")
        
        print("\n" + "="*50)
        print("📋 LISTA COMPLETA:\n")
        
        for idx, restaurante in enumerate(restaurantes, start=1):
            status = "✅ ATIVO" if restaurante['ativo'] else "❌ INATIVO"
            print(f"{idx:>2}. {restaurante['nome']}")
            print(f"    📍 Categoria: {restaurante['categoria']}")
            print(f"    🚀 Status: {status}\n")
            
    else:
        print("\n📝 Nenhum restaurante cadastrado.")
        print("💡 Use a opção 1 para cadastrar o primeiro restaurante!")
    
    print(f"\n💾 Dados carregados de: {ARQUIVO_JSON}")
    voltar_menu_principal()

#*******************************************************************************************************
# FUNÇÃO PARA LISTAR RESTAURANTES POR CATEGORIA
def listar_por_categoria():
    exibir_submenu("RESTAURANTES POR CATEGORIA".center(50))
    
    if not restaurantes:
        print("\n📝 Nenhum restaurante cadastrado.")
        voltar_menu_principal()
        return
    
    print("\n📋 Escolha uma categoria:\n")
    for idx, categoria in enumerate(CATEGORIAS, start=1):
        # Conta quantos restaurantes tem nessa categoria
        quantidade = len([r for r in restaurantes if r['categoria'] == categoria])
        print(f"{idx:>2}. {categoria} ({quantidade} restaurantes)")
    
    try:
        escolha = int(input(f"\nEscolha a categoria (1-{len(CATEGORIAS)}): "))
        if 1 <= escolha <= len(CATEGORIAS):
            categoria_escolhida = CATEGORIAS[escolha - 1]
            
            # Filtra restaurantes da categoria
            restaurantes_categoria = [r for r in restaurantes if r['categoria'] == categoria_escolhida]
            restaurantes_ativos = [r for r in restaurantes_categoria if r['ativo']]
            
            print(f"\n🍽️  RESTAURANTES DE {categoria_escolhida.upper()}:")
            print(f"Total: {len(restaurantes_categoria)} | Ativos: {len(restaurantes_ativos)}\n")
            
            if restaurantes_ativos:
                print("✅ RESTAURANTES ATIVOS:")
                for idx, restaurante in enumerate(restaurantes_ativos, start=1):
                    print(f"   {idx}. {restaurante['nome']}")
            
            restaurantes_inativos = [r for r in restaurantes_categoria if not r['ativo']]
            if restaurantes_inativos:
                print("\n❌ RESTAURANTES INATIVOS:")
                for idx, restaurante in enumerate(restaurantes_inativos, start=1):
                    print(f"   {idx}. {restaurante['nome']}")
            
            if not restaurantes_categoria:
                print("📝 Nenhum restaurante nesta categoria.")
                
        else:
            print("❌ Opção inválida.")
    except ValueError:
        print("❌ Entrada inválida.")
    
    voltar_menu_principal()

#*******************************************************************************************************
# FUNÇÃO PARA ATIVAR/DESATIVAR RESTAURANTE
def ativar_restaurante():
    exibir_submenu("ATIVAR/DESATIVAR RESTAURANTE".center(50))
    
    if not restaurantes:
        print("\n📝 Nenhum restaurante cadastrado para gerenciar.")
        voltar_menu_principal()
        return
    
    # Filtra restaurantes inativos para mostrar primeiro
    restaurantes_inativos = [r for r in restaurantes if not r['ativo']]
    restaurantes_ativos = [r for r in restaurantes if r['ativo']]
    
    print("\n🔄 Restaurantes disponíveis para gerenciar:\n")
    
    idx_global = 1
    # Mostra inativos primeiro
    if restaurantes_inativos:
        print("❌ RESTAURANTES INATIVOS (para ativar):")
        for restaurante in restaurantes_inativos:
            print(f"{idx_global:>2}. {restaurante['nome']} - {restaurante['categoria']}")
            idx_global += 1
        print()
    
    # Mostra ativos
    if restaurantes_ativos:
        print("✅ RESTAURANTES ATIVOS (para desativar):")
        for restaurante in restaurantes_ativos:
            print(f"{idx_global:>2}. {restaurante['nome']} - {restaurante['categoria']}")
            idx_global += 1
        print()
    
    try:
        escolha = int(input(f"Escolha o número do restaurante (1-{len(restaurantes)}): "))
        if 1 <= escolha <= len(restaurantes):
            # Reconstroi a lista completa na ordem de exibição
            lista_completa = restaurantes_inativos + restaurantes_ativos
            restaurante_selecionado = lista_completa[escolha - 1]
            
            # Encontra o restaurante na lista original
            for restaurante in restaurantes:
                if restaurante['nome'] == restaurante_selecionado['nome']:
                    novo_status = not restaurante['ativo']
                    restaurante['ativo'] = novo_status
                    
                    acao = "ativado" if novo_status else "desativado"
                    salvar_dados()
                    print(f"\n✅ Restaurante '{restaurante['nome']}' foi {acao} com sucesso!")
                    break
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
            listar_por_categoria()
        elif opcao_escolhida == 4:
            ativar_restaurante()
        elif opcao_escolhida == 5:
            print("\n💾 Salvando dados...")
            salvar_dados()
            print("👋 Saindo...")
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

#*******************************************************************************************************
# FUNÇÃO PRINCIPAL DO PROGRAMA
def main():
    carregar_dados()
    limpar_tela()
    exibir_nome_programa()
    exibir_menu()
    escolher_opcao()

#*******************************************************************************************************
# INICIAR O PROGRAMA
if __name__ == "__main__":
    main()