# 🛒 Product CRUD API

API REST para gerenciamento de produtos, desenvolvida como projeto de estudo durante minha jornada de transição para a área de **Engenharia de Dados**.

O projeto utiliza **Python, FastAPI, SQLAlchemy, PostgreSQL e Docker**, com uma arquitetura separando a API, a camada de acesso aos dados e o banco de dados.

O desenvolvimento foi realizado durante meus estudos na **Jornada de Dados**, do **Luciano Galvão**, utilizando os conteúdos da formação como base para colocar em prática conceitos de Python, APIs, bancos de dados e Docker.

---

## 🏗️ Arquitetura

Fluxo principal da aplicação:

```text
┌─────────────────┐
│    Frontend     │
│    Streamlit    │
└────────┬────────┘
         │
         │ HTTP
         ▼
┌─────────────────┐
│     Backend     │
│     FastAPI     │
│    Pydantic     │
│    SQLAlchemy   │
└────────┬────────┘
         │
         │ SQL
         ▼
┌─────────────────┐
│    PostgreSQL   │
│     Database    │
└─────────────────┘

      Docker Compose

Os serviços são executados em containers Docker e se comunicam através de uma rede interna criada pelo Docker Compose.

🛠️ Tecnologias
* **Python**
* **FastAPI**
* **Uvicorn**
* **SQLAlchemy**
* **Pydantic**
* **PostgreSQL**
* **Streamlit**
* **Requests**
* **Pandas**
* **Docker / Docker Compose**
* **Poetry**

🎯 Objetivo

Praticar conceitos de desenvolvimento com Python e construir uma aplicação capaz de realizar operações de CRUD sobre dados armazenados em um banco PostgreSQL.

O projeto também faz parte da construção do meu portfólio durante a transição para Engenharia de Dados, servindo como base para projetos futuros envolvendo APIs, integração de dados e pipelines.

🔄 Operações CRUD

A API permite realizar as principais operações sobre os produtos:

* Create

Criação de um novo produto:

POST /products/

* Read

Listagem dos produtos:

GET /products/

* Consulta de um produto específico:

GET /products/{product_id}
Update

* Atualização de um produto:

PUT /products/{product_id}

* Delete

Exclusão de um produto:

DELETE /products/{product_id}


📂 Estrutura

├── backend/
│   ├── Dockerfile
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
│   ├── router.py
│   └── schemas.py
├── frontend/
│   ├── Dockerfile
│   └── ...
├── docker-compose.yml
├── pyproject.toml
├── poetry.lock
└── README.md

🔙 Backend

O backend é responsável pela implementação da API e comunicação com o PostgreSQL.

* FastAPI

Utilizado para construção da API REST e definição dos endpoints responsáveis pelas operações de CRUD.

* SQLAlchemy

Utilizado como ORM para realizar a comunicação entre a aplicação Python e o PostgreSQL.

* Pydantic

Utilizado para validação dos dados recebidos pela API e definição dos schemas de entrada e saída.

* Uvicorn

Servidor ASGI utilizado para executar a aplicação FastAPI.

🗄️ Banco de Dados

O projeto utiliza PostgreSQL executado em um container Docker.

A conexão com o banco é realizada através da variável de ambiente:

DATABASE_URL=postgresql://user:password@postgres:5432/mydatabase

O banco utiliza um volume Docker para permitir a persistência dos dados entre reinicializações dos containers.

🐳 Docker

O projeto utiliza Docker Compose para executar e integrar os serviços da aplicação:

PostgreSQL
    │
    ├── Backend
    │
    └── Frontend

Os serviços são executados em containers e conectados através de uma rede Docker compartilhada.

🚀 Como Executar:

Pré-requisitos:

Docker Desktop
Git
1. Clone o repositório
git clone https://github.com/Dev-PPrado/product-crud-api.git
2. Acesse o projeto
cd product-crud-api
3. Inicie os containers
docker compose up --build

Para executar em segundo plano:

docker compose up --build -d

4. Verifique os containers
docker compose ps
5. Para encerrar a aplicação
docker compose down

🌐 Acessando a aplicação

Após iniciar os containers:

API
http://localhost:8000

Documentação da API

O FastAPI disponibiliza automaticamente a documentação interativa através do Swagger:

http://localhost:8000/docs

Através da interface é possível visualizar e testar os endpoints da API.

Frontend
http://localhost:8501

📚 Aprendizados

Durante o desenvolvimento deste projeto, pratiquei:

Desenvolvimento de APIs REST com Python
FastAPI
CRUD
SQLAlchemy ORM
PostgreSQL
Pydantic
Modelagem e persistência de dados
Comunicação entre aplicação e banco de dados
Docker e Docker Compose
Variáveis de ambiente
Gerenciamento de dependências com Poetry
Organização e separação de responsabilidades em uma aplicação Python.

🚀 Relação com Engenharia de Dados

Este projeto representa uma das etapas do meu processo de transição para Engenharia de Dados.

A construção de uma API integrada a um banco de dados permitiu praticar conceitos importantes relacionados à integração, armazenamento e disponibilização de dados.

A partir dessa base, meus próximos projetos serão direcionados para cenários mais próximos do dia a dia de Engenharia de Dados:

API
 │
 ▼
Python
 │
 ▼
PostgreSQL
 │
 ▼
ETL / ELT
 │
 ▼
Airflow / dbt
 │
 ▼
Data Lake / Data Warehouse

🗺️ Roadmap

✅ Implementado
* [x] API REST com FastAPI
* [x] Operações CRUD
* [x] SQLAlchemy
* [x] PostgreSQL
* [x] Pydantic
* [x] Frontend com Streamlit
* [x] Docker
* [x] Docker Compose
* [x] Gerenciamento de dependências com Poetry

🔜 Próximos Updates
* [ ] Testes automatizados
* [ ] Testes de integração
* [ ] Migrations com Alembic
* [ ] Melhorias no tratamento de erros
* [ ] CI/CD
* [ ] Integração com pipeline de dados
* [ ] Orquestração com Apache Airflow
* [ ] Transformações com dbt
* [ ] Processamento com PySpark
* [ ] Integração com Cloud
* [ ] Evolução para uma arquitetura de Engenharia de Dados

🎓 Referência de aprendizado

Este projeto foi desenvolvido durante meus estudos na Jornada de Dados, do Luciano Galvão, utilizando como base os conteúdos relacionados a:

Python
FastAPI
SQLAlchemy
PostgreSQL
Docker
Desenvolvimento de APIs

A implementação faz parte do meu processo de aprendizado e da construção de um portfólio prático voltado para Engenharia de Dados.

👨‍💻 Autor

Pedro Henrique de Souza Prado

Engenheiro de Controle e Automação em transição para Engenharia de Dados.

Atualmente desenvolvendo projetos práticos para aprofundar conhecimentos em:

Python • SQL • PostgreSQL • ETL/ELT • Docker • Airflow • dbt • Engenharia de Dados

🔗 Links

GitHub:
https://github.com/Dev-PPrado

LinkedIn:
www.linkedin.com/in/pedro-hsprado-dataengineer

Jornada de Dados:
https://www.jornadadedados.com.br/

⭐ Projeto desenvolvido para fins de estudo, aprendizado e construção de portfólio em Engenharia de Dados.
