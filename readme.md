# Projeto Intro_MVC: Uma Implementação Educacional do Padrão MVC com Python e PostgreSQL

Este projeto demonstra uma aplicação CRUD (Create, Read, Update, Delete) utilizando Python, PostgreSQL e o padrão de arquitetura MVC (Model-View-Controller). O objetivo principal é ilustrar como organizar um projeto Python orientado a objetos, separando responsabilidades em camadas para promover a manutenibilidade e escalabilidade do código.

## Arquitetura MVC (Model-View-Controller)

O padrão MVC é um padrão de arquitetura de software que divide a aplicação em três partes interconectadas:

-   **Model (Modelo):** Representa os dados da aplicação e a lógica de negócios. É responsável por acessar, manipular e notificar sobre as mudanças nos dados.
-   **View (Visão):** Apresenta os dados ao usuário. A visão consulta o modelo para obter os dados e os exibe de forma apropriada.
-   **Controller (Controlador):** Atua como intermediário entre o modelo e a visão. Ele recebe as requisições do usuário, interage com o modelo para realizar as ações necessárias e, em seguida, atualiza a visão para refletir as mudanças.


### 1. Model (Modelo) - `models/livro.py`

-   A classe `Livro` representa a entidade "livro" no sistema.
-   Define os atributos (id, titulo, autor, ano, isbn) que compõem um livro.
-   É responsável por encapsular os dados e fornecer uma estrutura para representá-los.

### 2. View (Visão) - `views/livro_views.py`

-   A classe `LivroView` é responsável por exibir os dados dos livros ao usuário.
-   Utiliza a biblioteca Tkinter para criar uma interface gráfica simples.
-   O método `_show_livros_screen()` exibe os livros em uma tabela (Treeview).
-   O método `iniciar_login_banco()` cria a tela de conexão com o banco de dados.

### 3. Controller (Controlador) - `controllers/livro_controller.py`

-   A classe `LivroController` atua como intermediário entre o modelo e a visão.
-   Recebe as configurações do banco de dados e instancia a classe `Database` para gerenciar a conexão.
-   Implementa métodos para criar a tabela (se não existir), adicionar livros e listar os livros.
-   O método `adicionar_livro()` interage com o modelo para inserir um novo livro no banco de dados.
-   O método `listar_livros()` consulta o modelo para obter a lista de livros e a retorna para a visão.

### 4. Conexão com o Banco de Dados - `database/db.py`

-   A classe `Database` é responsável por gerenciar a conexão com o banco de dados PostgreSQL.
-   Implementa métodos para criar o banco de dados (se não existir) e conectar ao banco.
-   Encapsula a lógica de conexão e fornece uma interface para as operações de banco de dados.

### 5. Ponto de Entrada - `main.py`

-   O arquivo `main.py` é o ponto de entrada da aplicação.
-   Importa a classe `LivroView` e chama o método `iniciar_login_banco()` para iniciar a interface gráfica.

## Como o Projeto Promove a Arquitetura MVC

-   **Separação de Responsabilidades:** Cada camada (Model, View, Controller) tem uma responsabilidade bem definida, facilitando a manutenção e o teste do código.
-   **Reutilização de Código:** As classes e funções podem ser reutilizadas em diferentes partes da aplicação.
-   **Facilidade de Manutenção:** As alterações em uma camada não afetam as outras camadas, desde que a interface entre elas seja mantida.
-   **Testabilidade:** Cada camada pode ser testada isoladamente, facilitando a identificação e correção de erros.

## Observações

-   Este projeto é uma implementação simplificada do padrão MVC e serve como um exemplo educacional.
-   Sinta-se à vontade para expandir as funcionalidades (editar, remover livros) e adaptar para outros tipos de entidades.
-   O código foi desenvolvido para fins didáticos e pode ser adaptado para outros cenários.

## Tecnologias Utilizadas

-   Python 3.x
-   PostgreSQL
-   psycopg2 (driver de conexão com PostgreSQL)
-   Tkinter (para a interface gráfica)

## Instruções de Uso

1.  Certifique-se de ter o Python e o PostgreSQL instalados.
2.  Instale as dependências necessárias: `pip install psycopg2`
3.  Configure o banco de dados no arquivo `database/db.py` com as suas credenciais.
4.  Execute o arquivo `main.py` para iniciar a aplicação.

---
**Desenvolvido para fins educacionais.**