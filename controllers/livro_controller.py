from app.models.livro import Livro
from app.views.livro_view import LivroView

class LivroController:
    def __init__(self):
        self.view = LivroView()

    def adicionar_livro(self, id, titulo, autor, ano_publicacao, isbn):
        livro = Livro(id, titulo, autor, ano_publicacao, isbn)
        self.view.mostrar_livro(livro)

    def listar_livros(self, livros):
        self.view.mostrar_livros(livros)
