🧩 CRUD com FastAPI, PostgreSQL, SQLAlchemy e Docker

Projeto desenvolvido como parte do meu portfólio de aprendizado e da minha transição para a área de Engenharia de Dados.

Este projeto consiste na construção de uma aplicação CRUD completa, utilizando Python, FastAPI, SQLAlchemy, Pydantic, PostgreSQL e Docker.

O projeto foi desenvolvido durante meus estudos na Jornada de Dados, do Luciano Galvão (Luciano do Jornada de Dados), como exercício prático para consolidar conceitos de desenvolvimento de APIs, persistência de dados, containers e comunicação entre aplicações e bancos de dados.

Contexto de aprendizado: este projeto tem como objetivo demonstrar minha evolução prática em Python e fundamentos que fazem parte do ecossistema de Engenharia de Dados. A implementação segue os conceitos estudados durante a formação e serve como base para projetos mais voltados a pipelines, ETL/ELT, orquestração e plataformas de dados.

🎯 Objetivos

Praticar desenvolvimento de APIs REST com Python.

Entender a comunicação entre uma aplicação e um banco de dados relacional.

Trabalhar com ORM utilizando SQLAlchemy.

Validar dados utilizando Pydantic.

Implementar operações CRUD.

Containerizar a aplicação com Docker.

Utilizar Docker Compose para orquestrar backend, frontend e PostgreSQL.

Consolidar fundamentos que serão utilizados em projetos posteriores de Engenharia de Dados.

🏗️ Arquitetura

A aplicação é composta por três serviços principais:

                    ┌─────────────────┐
                    │    Frontend     │
                    │   Streamlit     │
                    └────────┬────────┘
                             │
                             │ HTTP
                             ▼
                    ┌─────────────────┐
                    │     Backend     │
                    │     FastAPI     │
                    │   SQLAlchemy    │
                    │     Pydantic    │
                    └────────┬────────┘
                             │
                             │ SQL
                             ▼
                    ┌─────────────────┐
                    │   PostgreSQL    │
                    │    Database     │
                    └─────────────────┘

                       Docker Compose

Os serviços são executados em uma rede Docker compartilhada, permitindo a comunicação entre os containers.

🛠️ Tecnologias utilizadas

Tecnologia

Utilização

Python

Linguagem principal

FastAPI

Desenvolvimento da API REST

Uvicorn

Servidor ASGI

SQLAlchemy

ORM e comunicação com o banco

Pydantic

Validação e definição dos schemas

PostgreSQL

Banco de dados relacional

Streamlit

Interface frontend

Requests

Consumo da API pelo frontend

Pandas

Manipulação de dados no frontend

Docker

Containerização

Docker Compose

Orquestração dos serviços

Poetry

Gerenciamento de dependências e ambiente Python

📁 Estrutura do projeto

CRUD/
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

O backend é responsável por disponibilizar a API e fazer a comunicação entre o frontend e o PostgreSQL.

FastAPI

O FastAPI é utilizado para construir a API REST em Python. Ele permite definir endpoints, receber requisições, validar dados e retornar respostas estruturadas.

Uvicorn

O Uvicorn é o servidor ASGI utilizado para executar a aplicação FastAPI.

SQLAlchemy

O SQLAlchemy é utilizado como ORM para realizar a comunicação entre Python e PostgreSQL.

A utilização do ORM permite representar tabelas do banco através de classes Python e executar operações de persistência utilizando a camada de abstração do SQLAlchemy.

Pydantic

O Pydantic é utilizado para definir os schemas da API e realizar a validação dos dados recebidos e retornados pelos endpoints.

🗄️ Banco de dados

O projeto utiliza PostgreSQL executado em um container Docker.

As configurações do banco são fornecidas por variáveis de ambiente:

POSTGRES_DB=mydatabase
POSTGRES_USER=user
POSTGRES_PASSWORD=password

A aplicação utiliza a variável DATABASE_URL para estabelecer a conexão com o banco:

postgresql://user:password@postgres:5432/mydatabase

O hostname postgres corresponde ao nome do serviço do PostgreSQL definido no Docker Compose.

Também é utilizado um volume Docker para manter os dados do PostgreSQL mesmo quando os containers são reiniciados.

🔄 Operações CRUD

O backend implementa as operações fundamentais de CRUD:

Create — criação de registros

Read — consulta de registros

Update — atualização de registros

Delete — remoção de registros

A separação das responsabilidades é feita entre diferentes arquivos:

database.py

Responsável pela configuração da conexão com o banco, criação da engine e gerenciamento das sessões do SQLAlchemy.

models.py

Define os modelos ORM que representam as tabelas do banco de dados.

schemas.py

Define os schemas Pydantic utilizados para entrada, validação e resposta da API.

crud.py

Concentra as operações de criação, consulta, atualização e remoção dos registros.

router.py

Define as rotas e endpoints da API.

main.py

Inicializa a aplicação FastAPI e registra os componentes necessários.

🐳 Docker

O projeto utiliza Docker para criar ambientes isolados para os serviços da aplicação.

O docker-compose.yml reúne:

PostgreSQL

Backend

Frontend

Os serviços são conectados através de uma rede Docker personalizada.

Subindo o projeto

Com o Docker Desktop em execução, na raiz do projeto:

docker compose up --build

Para executar em segundo plano:

docker compose up --build -d

Para encerrar os containers:

docker compose down

Para verificar os serviços:

docker compose ps

🌐 Acessando a aplicação

Backend

A API fica disponível em:

http://localhost:8000

Documentação da API

O FastAPI disponibiliza documentação interativa:

http://localhost:8000/docs

A interface permite visualizar e testar os endpoints da API diretamente pelo navegador.

Frontend

O frontend Streamlit fica disponível em:

http://localhost:8501

📚 Aprendizados

Durante o desenvolvimento deste projeto, pratiquei conceitos importantes como:

Desenvolvimento de APIs REST com Python.

Estruturação de aplicações FastAPI.

HTTP e endpoints.

ORM e SQLAlchemy.

Modelagem de tabelas.

Sessões e conexão com banco de dados.

Validação de dados com Pydantic.

Operações CRUD.

PostgreSQL.

Variáveis de ambiente.

Comunicação entre containers.

Docker e Docker Compose.

Gerenciamento de dependências com Poetry.

Separação de responsabilidades em uma aplicação Python.

🚀 Relação com minha transição para Engenharia de Dados

Este projeto faz parte da construção do meu portfólio durante minha transição profissional para Engenharia de Dados.

Apesar de o foco principal aqui ser o desenvolvimento de uma aplicação CRUD, os conhecimentos praticados são relevantes para projetos de dados, especialmente:

Python
   ↓
APIs
   ↓
Banco de Dados
   ↓
SQL
   ↓
Docker
   ↓
Integração de Dados

A partir dessa base, pretendo evoluir meus projetos para cenários mais próximos do dia a dia de Engenharia de Dados, trabalhando com:

ETL e ELT

Airflow

dbt

Data Quality

Modelagem de dados

Processamento com PySpark

Data Lakes

Cloud

Pipelines de dados

Monitoramento e observabilidade

📈 Próximos passos

Este projeto representa uma etapa do meu processo de aprendizado. Entre as possíveis evoluções estão:

Adicionar testes automatizados.

Melhorar tratamento de erros.

Implementar autenticação.

Adicionar migrations com Alembic.

Melhorar a documentação da API.

Implementar CI/CD.

Integrar o projeto a um pipeline de dados.

Utilizar Airflow para orquestração.

Integrar processos de transformação com dbt.

Evoluir a arquitetura para um cenário de Engenharia de Dados.

👨‍💻 Sobre o projeto

Este repositório faz parte do meu portfólio de estudos em Engenharia de Dados e registra minha evolução prática durante a transição de uma carreira voltada à automação e sistemas industriais para a área de Dados.

O projeto teve como referência os conteúdos e ensinamentos do Luciano Galvão, da Jornada de Dados, especialmente os estudos relacionados a Python avançado para dados, APIs, FastAPI, SQLAlchemy, PostgreSQL e Docker.

A ideia é utilizar os fundamentos aprendidos como base para desenvolver projetos próprios cada vez mais próximos de problemas reais de Engenharia de Dados.

🔗 Links

Jornada de Dados: https://www.jornadadedados.com.br/

GitHub: https://github.com/Dev-PPrado

LinkedIn: https://www.linkedin.com/in/pedro-prado-34369a1b5

📌 Status

Concluído — projeto de aprendizado e portfólio.

Novas melhorias poderão ser incorporadas conforme avanço nos estudos de Engenharia de Dados.