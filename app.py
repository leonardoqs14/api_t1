from flask import Flask,request,jsonify  # Importamos a classe Flask do módulo flask para criar nosso aplicativo web
from flask_cors import CORS
import sqlite3
app=Flask(__name__)
CORS(app)

def init_db():
    #Crie o nosso banco de dados com um arquivo "database.db" e conecte a variavel conn (Connection)
    with sqlite3.connect("database.db") as conn:
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS LIVROS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    image_url TEXT NOT NULL
                )
            """
        )

init_db()

@app.route("/")
def home():
    return jsonify(f"Bem vindo a API Livros")


@app.route("/doar", methods=["POST"])
def doar():

    dados = request.get_json()

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("image_url")

    if not titulo or not categoria or not autor or not  image_url:
        return jsonify({"erro":"Todos os campos são obrigatorios"}),400
    
    with sqlite3.connect("database.db") as conn:
        conn.execute(f"""
        INSERT INTO LIVROS(titulo, categoria, autor, image_url)
        VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
        """)
    
        conn.commit()

        return jsonify({"Mensagem": "Livro cadastrado com sucesso"}), 201



@app.route("/livros", methods=["GET"])
def listar_livros():

    with sqlite3.connect("database.db") as conn:
        livros = conn.execute("SELECT * FROM LIVROS").fetchall()

        livros_formatados = []

        for item in livros:
            dicionario_livros = {
                "id": item[0],
                "titulo":item[1],
                "categoria":item[2],
                "autor":item[3],
                "image_url":item[4]
            }
            livros_formatados.append(dicionario_livros)

    return jsonify(livros_formatados)







# Aqui verificamos se o script está sendo executado diretamente e não importado como módulo
if __name__ == "__main__":
    # Inicia o servidor Flask no modo de depuração (nesse modo nossa API responde automaticamente a qualquer atualização que fizermos no código)
    app.run(debug=True)