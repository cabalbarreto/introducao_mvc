from database.db import Database
from models.livro import Livro
from views.livro_views import LivroView

class LivroController:
    def __init__(self, db_config):
        self.db = Database(
            db_config["dbname"],
            db_config["user"],
            db_config["password"],
            db_config["host"],
            db_config["port"]
        )
        self.create_table_if_not_exists()
        self.view = LivroView()

    def create_table_if_not_exists(self):
        conn = self.db.connect()
        if conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS livros (
                    id SERIAL PRIMARY KEY,
                    titulo VARCHAR(255) NOT NULL,
                    autor VARCHAR(255) NOT NULL,
                    ano INTEGER,
                    isbn VARCHAR(20)
                );
            """)
            conn.commit()
            cur.close()
            conn.close()

    def adicionar_livro(self, id, titulo, autor, ano, isbn):
        conn = self.db.connect()
        if conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO livros (id, titulo, autor, ano, isbn) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING;",
                (id, titulo, autor, ano, isbn)
            )
            conn.commit()
            cur.close()
            conn.close()
            print("Livro adicionado com sucesso!")
        else:
            print("Erro ao conectar ao banco de dados.")

    def listar_livros(self, livros):
        self.view.mostrar_livros(livros)
