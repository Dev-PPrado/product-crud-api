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
