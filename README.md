# Api de Doação de Livros

Essa é uma API simples feita com Flask e SQLite3 para fins de estudo da escola Vai Na Web, ela permite cadastrar e listar doados.

## Como rodar o projeto

1. Faça o clone do repositório:
```bash
git clone <URL_DO_REPOSITORIO>
cd nome-do-projeto
```

2. Crie um ambiente virtual (obrigatorio):
```bash
python -m venv venv
source venv/Scripts/activate
```
3. Instala as dependências
```bash
pip install -r requirements.txt
```

4. Inicie o servidor?
```bash
python app.py
```
> A api está disponivem em http: http://127.0.0.1:5000/

## Endpoints 

### POST /doar

Endpoin para cadastrar um novo livro

**Formato de envio dos dados**
```json
{
    "titulo":"Ainda estou devendo aqui",
    "categoria":"Finanças",
    "autor":"Fernanda Polia",
    "image_url":"https://exemplo.com"
}
```

**Resposta 201 (Created)**:
```json
{
    "mensagem":"Livro cadastrado com sucesso!"
}
```

---

### GET /livros

Retorna todos os livros cadastrados em nossa API.

**Resposta 200**:
```json
{
    "id":"1",
    "titulo":"Ainda estou devendo aqui",
    "categoria":"Finanças",
    "autor":"Fernanda Polia",
    "image_url":"https://exemplo.com"
}
```