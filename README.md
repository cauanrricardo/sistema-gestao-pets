# 🐶 Sistema de Gestão de Pets

Aplicação desenvolvida para a disciplina **Fundamentos de Banco de Dados** da UFC - Campus Quixadá.

---

## 📌 Objetivo

Criar um sistema que facilite a gestão de clínicas veterinárias, com foco no acompanhamento clínico dos pets e na organização das informações dos tutores, profissionais e consultas.

---

## ⚙️ Tecnologias Utilizadas

- **Python + FastAPI**
- **PostgreSQL**
- **PgAdmin**
- **SQL** (DDL, DML, Views, Controle de Acesso)

---

## 📁 Funcionalidades

- CRUD de **Tutor**
- CRUD de **Pet**
- **GET** e **POST** de **Consultas**
- **Visões SQL** para facilitar relatórios clínicos e administrativos
- **Controle de acesso** com usuários:
  - `administrador_vet`
  - `analista_vet`

---

## 🧩 Organização do Projeto

- `main.py`: inicializa a aplicação FastAPI
- `models/`: modelos de dados (Pydantic)
- `database/`: conexão com PostgreSQL
- `routes/`: endpoints da API
- `crud_*.py`: operações com o banco
- `etapa4.sql`: comandos SQL das visões e permissões
- `db.py`: integração com o PostgreSQL (usar variáveis de ambiente para dados sensíveis)

