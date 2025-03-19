from flask import Flask,request,jsonify  # Importamos a classe Flask do módulo flask para criar nosso aplicativo web

import sqlite3
app=Flask(__name__)

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
















# Aqui verificamos se o script está sendo executado diretamente e não importado como módulo
if __name__ == "__main__":
    # Inicia o servidor Flask no modo de depuração (nesse modo nossa API responde automaticamente a qualquer atualização que fizermos no código)
    app.run(debug=True)