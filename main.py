from controllers.livro_controller import LivroController

def main():
    db_config = {
        "dbname": "intro_mvc",         # Nome do banco criado
        "user": "postgres",            # Usuário
        "password": "geleira@1",       # Senha
        "host": "127.0.0.1",           # Endereço IP, tive problema com o localhost
        "port": "5433"
    }

    livro_controller = LivroController(db_config)

    # Exemplo de uso
    livro_controller.adicionar_livro(1, "O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "9780544003415")

if __name__ == "__main__":
    main()
