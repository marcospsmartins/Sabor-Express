# Sabor-Express
Cadastro de Resurantes
🍽️ Sabor Express - Sistema de Gerenciamento de Restaurantes

Um sistema simples e eficiente para gerenciamento de restaurantes desenvolvido em Python, perfeito para pequenos negócios e aprendizado de programação.

-------------------------------------------------------------------------------------------------
📋 Índice

Visão Geral
Funcionalidades
Pré-requisitos
Instalação
Como Usar
Estrutura do Projeto
Tecnologias Utilizadas
Contribuição
Licença
Roadmap

-------------------------------------------------------------------------------------------------
🎯 Visão Geral
O Sabor Express é uma aplicação de console desenvolvida em Python que permite o gerenciamento básico de estabelecimentos gastronômicos. Ideal para donos de pequenos negócios ou para fins educacionais no aprendizado de Python.

-------------------------------------------------------------------------------------------------
✨ Funcionalidades
✅ Cadastro de Restaurantes - Adicione novos estabelecimentos ao sistema
📋 Listagem Completa - Visualize todos os restaurantes cadastrados
🟢 Ativação de Restaurantes - Simule a ativação de estabelecimentos
🎨 Interface Amigável - Design clean com feedback visual intuitivo
⚠️ Tratamento de Erros - Validações robustas para entradas inválidas
🖥️ Compatibilidade Multiplataforma - Funciona em Windows, Linux e macOS

-------------------------------------------------------------------------------------------------
🛠️ Pré-requisitos
Python 3.6 ou superior
Sistema operacional: Windows, Linux ou macOS

-------------------------------------------------------------------------------------------------
📥 Instalação

*******************
Método 1: Clone o repositório
bash
# Clone o repositório
git clone https://github.com/seu-usuario/sabor-express.git

# Acesse o diretório
cd sabor-express

# Execute o programa
python main.py

*****************
Método 2: Download direto
Faça o download dos arquivos do projeto
Extraia em uma pasta de sua preferência
Execute o comando:

bash
python sabor_express.py

-------------------------------------------------------------------------------------------------
🚀 Como Usar
Executando o Sistema
bash
python sabor_express.py

-------------------------------------------------------------------------------------------------
Navegação no Menu
text
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░

1. Cadastrar Restaurante
2. Listar Restaurantes
3. Ativar Restaurante
4. Sair

-------------------------------------------------------------------------------------------------
Fluxo de Trabalho
Cadastrar Restaurante: Digite o nome do estabelecimento

Listar Restaurantes: Veja todos os cadastrados com numeração

Ativar Restaurante: Selecione pelo número para ativar

Sair: Encerra o programa


-------------------------------------------------------------------------------------------------
📁 Estrutura do Projeto

SABOR-EXPRESS/
├── Sabor-Express/      # (provavelmente uma pasta)
├── gitattributes/      
├── LICENSE            # Arquivo de licença
├── README.md          # Este arquivo
├── app.py             # Seu código principal (não sabor_express.py)


-------------------------------------------------------------------------------------------------
🏗️ Estrutura de Código

***********************
Principais Funções
python
# Navegação
exibir_nome_programa()    # Banner inicial
exibir_menu()             # Menu principal
voltar_menu_principal()   # Navegação de retorno

# Operações CRUD
cadastrar_restaurante()   # Adiciona novos
listar_restaurantes()     # Lista todos
ativar_restaurante()      # Ativa específicos

# Utilitários
limpar_tela()             # Limpa terminal
opcao_invalida()          # Trata erros
finalizar_app()           # Encerra sistema

**********************
Variáveis Globais
python
restaurantes = []  # Lista que armazena todos os restaurantes

-------------------------------------------------------------------------------------------------
🛠️ Tecnologias Utilizadas
Python 3.6+ - Linguagem de programação
Biblioteca OS - Operações do sistema
Arte ASCII - Interface visual
Tratamento de Exceções - Robustez do sistema

*********************
🤝 Contribuição
Contribuições são sempre bem-vindas! Siga estos passos:

Fork o projeto
Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)
Commit suas mudanças (git commit -m 'Add some AmazingFeature')
Push para a branch (git push origin feature/AmazingFeature)
Abra um Pull Request

*********************
Padrões de Código
Use nomes descritivos para variáveis e funções
Mantenha a consistência com o estilo existente
Documente novas funcionalidades
Teste suas alterações

********************
📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

*******************
🗺️ Roadmap
Versão 1.1 (Próxima)
Persistência em arquivo JSON
Edição de restaurantes
Exclusão de restaurantes
Sistema de categorias

Versão 1.2 (Futuro)
Interface gráfica (Tkinter)
Sistema de avaliações
Exportação de relatórios
Busca e filtros

Versão 2.0 (Longo Prazo)
API REST
Frontend web
Banco de dados SQL
Sistema de usuários

🐛 Reportar Bugs
Encontrou um bug? Por favor, abra uma issue incluindo:
Descrição detalhada do problema
Passos para reproduzir
Comportamento esperado vs atual
Screenshots (se aplicável)

📞 Suporte
Tem dúvidas ou sugestões? Entre em contato:
📧 Email: seu-email@dominio.com
💬 Issues: GitHub Issues
👨‍💻 Desenvolvedor: Marcos Paulo Sunto Martins

GitHub: @seu-usuario
LinkedIn: Seu Perfil

<div align="center">
⭐️ Se este projeto te ajudou, considere dar uma estrela!
</div>