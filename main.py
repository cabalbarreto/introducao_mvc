from app.controllers.livro_controller import LivroController
from database.db import Database

def main():
    # Configurações do banco de dados
    db_config = {
        "dbname": "biblioteca",
        "user": "seu_usuario",
        "password": "sua_senha",
        "host": "localhost",
        "port": "5432"
    }

    # Inicialização do controlador
    livro_controller = LivroController()

    # Exemplo de uso
    livro_controller.adicionar_livro(1, "O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "9780544003415")

if __name__ == "__main__":
    main()
