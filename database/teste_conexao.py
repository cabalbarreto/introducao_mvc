import psycopg2

try:
    conn = psycopg2.connect(
        dbname="intro_mvc",
        user="postgres",
        password="geleira@1",
        host="127.0.0.1", # tive muito problema de conexão quando localhost, mudei para o endereço ip
        port="5433",  # ou "5433"
        options='-c client_encoding=utf8'
    )
    print("Conexão bem-sucedida!")
    conn.close()
except Exception as e:
    print(f"Erro ao conectar: {e}")