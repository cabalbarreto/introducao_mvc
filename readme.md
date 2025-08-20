nome_do_projeto/
│
├── app/
│   ├── controllers/
│   │   └── __init__.py
│   │   └── livro_controller.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── livro.py
│   │
│   ├── views/
│   │   ├── __init__.py
│   │   └── livro_view.py
│   │
│   └── __init__.py
│
├── database/
│   ├── __init__.py
│   └── db.py
│
├── main.py
│
└── README.md

## Explicação dos Arquivos, Classes e Funções

### `main.py`
- **Função principal do projeto.**
- Define as configurações do banco de dados e inicializa o controlador de livros.
- Exemplo de uso: adiciona um livro ao banco.

### `controllers/livro_controller.py`
- **Classe:** `LivroController`
  - Responsável pela lógica de controle dos livros.
  - Recebe as configurações do banco e instancia a classe de conexão.
  - **Funções principais:**
    - `__init__(self, db_config)`: Inicializa o controller e cria a tabela se não existir.
    - `create_table_if_not_exists(self)`: Cria a tabela `livros` no banco, se necessário.
    - `adicionar_livro(self, id, titulo, autor, ano, isbn)`: Insere um novo livro no banco.
    - (Você pode implementar: listar, atualizar e remover livros.)

### `models/livro.py`
- **Classe:** `Livro`
  - Representa a entidade Livro.
  - **Atributos:** `id`, `titulo`, `autor`, `ano`, `isbn`.
  - Utilizada para estruturar os dados dos livros.

### `views/livro_views.py`
- **Funções para interação com o usuário.**
- Exibe informações e recebe entradas (pode ser expandido para interface CLI ou GUI).

### `database/db.py`
- **Classe:** `Database`
  - Gerencia a conexão com o banco de dados PostgreSQL.
  - **Funções principais:**
    - `__init__(self, dbname, user, password, host, port)`: Inicializa os parâmetros de conexão.
    - `create_database_if_not_exists(self)`: Cria o banco de dados se não existir.
    - `connect(self)`: Retorna uma conexão ativa com o banco.

### `__init__.py`
- Arquivos para tornar os diretórios módulos Python.

---

## Como Executar

1. **Configure o banco de dados PostgreSQL:**
   - Usuário: `postgres`
   - Senha: `geleira@1`
   - Banco: `intro_mvc`
   - Porta: `5432` (ou ajuste conforme sua instalação)

2. **Instale as dependências:
3. **Execute o projeto:**

---

## Observações

- O projeto segue o padrão MVC para facilitar manutenção e evolução.
- Sinta-se à vontade para expandir as funcionalidades (listar, editar, remover livros).
- O código é didático e pode ser adaptado para outros tipos de entidades.

---

Desenvolvido para fins educacionais.
