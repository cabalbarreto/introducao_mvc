class Livro:
    def __init__(self, id, titulo, autor, ano_publicacao, isbn):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.isbn = isbn

    def __str__(self):
        return f"Livro(ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}, ISBN: {self.isbn})"
