# API Connect

## Objetivo

A **API Connect** é uma API REST desenvolvida como Produto Mínimo Viável (MVP) para realizar o cadastro, consulta, atualização e exclusão de usuários.

A aplicação permite trabalhar com dados de usuários contendo **ID, nome e e-mail**, utilizando uma estrutura de persistência em memória para fins de prototipação.

## Tecnologias utilizadas

* Python
* Flask
* REST API
* HTTP
* JSON
* Git e GitHub
* Visual Studio Code

## Estrutura do projeto

text
API CONNECT/
│
├── app.py
├── routes/
│   └── api_routes.py
├── controllers/
│   └── api_controller.py
├── data/
│   └── database.py
├── venv/
├── .gitignore
└── requirements.txt


## Como executar localmente

### 1. Clonar o projeto

bash
git clone URL_DO_REPOSITORIO


### 2. Acessar a pasta

bash
cd API-Connect


### 3. Criar o ambiente virtual

bash
python -m venv venv


### 4. Ativar o ambiente virtual

No Windows:

bash
venv\Scripts\activate


### 5. Instalar as dependências

bash
pip install -r requirements.txt


### 6. Executar a aplicação

bash
python app.py


A API ficará disponível em:

text
http://127.0.0.1:5000


## Endpoints

| Método | Endpoint         | Descrição                   | Status de sucesso |
| ------ | ---------------- | --------------------------- | ----------------- |
| POST   | `/usuarios`      | Cadastra um novo usuário    | 201 Created       |
| GET    | `/usuarios`      | Lista todos os usuários     | 200 OK            |
| GET    | `/usuarios/<id>` | Consulta um usuário pelo ID | 200 OK            |
| PUT    | `/usuarios/<id>` | Atualiza um usuário         | 200 OK            |
| DELETE | `/usuarios/<id>` | Remove um usuário           | 204 No Content    |

## Exemplos de requisições

### Criar usuário

**POST** `/usuarios`

json
{
    "nome": "João Silva",
    "email": "joao@email.com"
}


### Listar usuários

**GET** `/usuarios`

Retorna a lista de usuários cadastrados.

### Buscar usuário

**GET** `/usuarios/1`

Retorna o usuário correspondente ao ID informado.

### Atualizar usuário

**PUT** `/usuarios/1`

json
{
    "nome": "João Santos",
    "email": "joao.santos@email.com"
}


### Excluir usuário

**DELETE** `/usuarios/1`

Remove o usuário correspondente ao ID informado.

## Validação e tratamento de erros

A API realiza validações nos dados recebidos nas operações de cadastro e atualização.

Quando os campos obrigatórios não são informados, a API retorna:

json
{
    "error": "O campo 'email' é obrigatório."
}


com o status:

text
400 Bad Request


Quando um usuário não é encontrado, a API retorna:

json
{
    "error": "Usuário não encontrado"
}


com o status:


404 Not Found




Durante o desenvolvimento do MVP, os usuários são armazenados em uma lista em memória no arquivo `data/database.py`.

Essa abordagem foi escolhida para simplificar a implementação inicial. Em uma evolução futura do projeto, essa estrutura poderá ser substituída por um banco de dados real.



Projeto desenvolvido como atividade prática de desenvolvimento de API REST utilizando Python e Flask.
