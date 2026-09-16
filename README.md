# 🛒 Product CRUD API

API REST para gerenciamento de produtos, desenvolvida com **Python e FastAPI**, utilizando **PostgreSQL** como banco de dados e **Docker** para containerização da aplicação.

Este projeto faz parte do meu **portfólio de aprendizado durante minha transição para a área de Engenharia de Dados**.

---

## 📌 Sobre o projeto

O projeto consiste em uma aplicação CRUD completa para gerenciamento de produtos, permitindo realizar operações de:

- ➕ Criação de produtos
- 🔎 Consulta de produtos
- ✏️ Atualização de produtos
- 🗑️ Exclusão de produtos

A aplicação foi desenvolvida utilizando uma arquitetura separando as responsabilidades entre **API, regras de acesso aos dados e banco de dados**.

O projeto foi desenvolvido durante meus estudos na **Jornada de Dados**, do **Luciano Galvão**, como forma de colocar em prática conceitos de Python, APIs, bancos de dados e Docker.

> Este é um projeto de aprendizado. A implementação teve como referência os conteúdos estudados na Jornada de Dados e faz parte da minha evolução prática na construção de projetos para o portfólio de Engenharia de Dados.

---

## 🏗️ Arquitetura

```text
                  ┌────────────────────┐
                  │      Frontend      │
                  │     Streamlit      │
                  └─────────┬──────────┘
                            │
                            │ HTTP
                            ▼
                  ┌────────────────────┐
                  │      Backend       │
                  │      FastAPI       │
                  │     Pydantic       │
                  │     SQLAlchemy     │
                  └─────────┬──────────┘
                            │
                            │ SQL
                            ▼
                  ┌────────────────────┐
                  │     PostgreSQL     │
                  │      Database      │
                  └────────────────────┘

                       Docker Compose

Os serviços são executados em containers Docker e se comunicam através de uma rede interna criada pelo Docker Compose.

🛠️ Tecnologias utilizadas

🐍 Python	Desenvolvimento da aplicação
⚡ FastAPI	Construção da API REST
🚀 Uvicorn	Servidor ASGI
🗄️ PostgreSQL	Banco de dados relacional
🔗 SQLAlchemy	ORM e comunicação com o banco
✅ Pydantic	Validação e schemas dos dados
🎨 Streamlit	Interface frontend
🌐 Requests	Comunicação com a API
📊 Pandas	Manipulação de dados
🐳 Docker	Containerização
🔧 Docker Compose	Orquestração dos serviços
📦 Poetry	Gerenciamento de dependências
📂 Estrutura do projeto
product-crud-api/
│
├── README.md
├── docker-compose.yml
├── pyproject.toml
├── poetry.lock
│
├── backend/
│   ├── Dockerfile
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
│   ├── router.py
│   └── schemas.py
│
└── frontend/
    ├── Dockerfile
    └── ...
🔙 Backend

O backend é responsável por disponibilizar a API e realizar a comunicação com o banco de dados PostgreSQL.

FastAPI

Utilizado para construção da API REST e definição dos endpoints responsáveis pelas operações de CRUD.

SQLAlchemy

Utilizado como ORM para realizar a comunicação entre a aplicação Python e o PostgreSQL.

Pydantic

Utilizado para validação dos dados recebidos pela API e definição dos schemas de entrada e saída.

Uvicorn

Servidor ASGI utilizado para executar a aplicação FastAPI.

🗄️ Banco de dados

O projeto utiliza PostgreSQL, executado através de um container Docker.

A conexão com o banco é configurada através da variável de ambiente:

DATABASE_URL

Exemplo:

postgresql://user:password@postgres:5432/mydatabase

O PostgreSQL utiliza um volume Docker para permitir a persistência dos dados mesmo após a reinicialização dos containers.

🔄 Operações CRUD

A API disponibiliza as operações básicas de gerenciamento de produtos:

Create

Criação de novos produtos através de:

POST /products/
Read

Listagem de produtos:

GET /products/

Consulta de um produto específico:

GET /products/{product_id}
Update

Atualização de um produto:

PUT /products/{product_id}
Delete

Exclusão de um produto:

DELETE /products/{product_id}
🐳 Executando com Docker
Pré-requisitos

Para executar o projeto, é necessário ter instalado:

Docker Desktop
Git

Clone o repositório:

git clone https://github.com/Dev-PPrado/product-crud-api.git

Entre na pasta:

cd product-crud-api

Execute os serviços:

docker compose up --build

Para executar em segundo plano:

docker compose up --build -d

Para verificar os containers:

docker compose ps

Para encerrar os serviços:

docker compose down
🌐 Acessando a aplicação

Após iniciar os containers:

API
http://localhost:8000
Documentação interativa

O FastAPI disponibiliza automaticamente a documentação da API através do Swagger:

http://localhost:8000/docs

Através dela é possível visualizar e testar os endpoints da aplicação.

Frontend
http://localhost:8501
📚 Principais aprendizados

Durante o desenvolvimento deste projeto, pratiquei conceitos como:

Desenvolvimento de APIs REST com Python
FastAPI
HTTP e endpoints
CRUD
SQLAlchemy ORM
PostgreSQL
Modelagem de dados
Pydantic e validação de dados
Sessões e conexão com banco de dados
Variáveis de ambiente
Docker
Docker Compose
Comunicação entre containers
Gerenciamento de dependências com Poetry
Organização e separação de responsabilidades em uma aplicação Python
🚀 Relação com Engenharia de Dados

Este projeto representa uma etapa do meu processo de transição profissional para Engenharia de Dados.

Embora o objetivo principal seja desenvolver uma API CRUD, o projeto me permitiu trabalhar com componentes que fazem parte do ecossistema de dados:

              API
               │
               ▼
             Python
               │
               ▼
           PostgreSQL
               │
               ▼
          Dados persistidos
               │
               ▼
       Integração com pipelines

A partir dessa base, meu objetivo é evoluir os projetos do portfólio para cenários cada vez mais próximos de Engenharia de Dados, trabalhando com:

ETL e ELT
SQL
Airflow
dbt
Data Quality
Modelagem de dados
PySpark
Data Lakes
Docker
Cloud
Orquestração de pipelines
📈 Próximos passos

Algumas evoluções planejadas para este projeto ou para projetos futuros:

 Adicionar testes automatizados
 Implementar migrations com Alembic
 Melhorar tratamento de erros
 Implementar autenticação
 Adicionar testes de integração
 Implementar CI/CD
 Integrar a API com um pipeline de dados
 Utilizar Airflow para orquestração
 Integrar dbt para transformação dos dados
 Evoluir a arquitetura para um projeto de Engenharia de Dados
🎓 Referência de aprendizado

Este projeto foi desenvolvido como parte dos meus estudos na Jornada de Dados, do Luciano Galvão, utilizando como base os conhecimentos apresentados nos conteúdos relacionados a Python, FastAPI, SQLAlchemy, PostgreSQL e Docker.

A implementação faz parte do meu processo de aprendizado e construção de um portfólio voltado para Engenharia de Dados.

👨‍💻 Sobre mim

Sou formado em Engenharia de Controle e Automação e atualmente trabalho com suporte e sistemas em ambiente industrial.

Estou realizando uma transição de carreira para a área de Dados, com foco em Engenharia de Dados, desenvolvendo projetos práticos para consolidar conhecimentos em Python, SQL, bancos de dados, ETL/ELT, Docker, Airflow, dbt e processamento de dados.

Este repositório faz parte dessa jornada.

🔗 Links

GitHub:
https://github.com/Dev-PPrado

LinkedIn:
https://www.linkedin.com/in/pedro-prado-34369a1b5

Jornada de Dados:
https://www.jornadadedados.com.br/
