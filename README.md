# 🚀 Pipeline DevOps – API Flask com Docker, Swagger, JWT e CI/CD

Este projeto demonstra uma API desenvolvida em **Flask**, containerizada com **Docker**, documentada com **Swagger**, protegida com **JWT**, testada com **unittest** e integrada a um pipeline de **CI/CD** via GitHub Actions.  
A aplicação roda na porta **1313**.

---


## 🔧 Desenvolvimento da API

A API foi criada usando Flask e possui rotas básicas, rotas protegidas por JWT e integração com Swagger para documentação.

Instalação das dependências:

```bash
pip install -r requirements.txt
```

---

## 🐳 Dockerização

### Criar imagem
```bash
docker build -t api-flask .
```

### Executar container
```bash
docker run -p 1313:1313 api-flask
```

### Docker Compose
```bash
docker-compose up --build
```

Acesse:

👉 http://localhost:1313  
👉 http://localhost:1313/swagger

---

## 🔐 Autenticação JWT

### Gerar token
POST:
```
http://localhost:1313/login
```

### Acessar rota protegida
Header:
```
Authorization: Bearer <token>
```

---

## 🧪 Testes

Testes automáticos com unittest:

```bash
python -m unittest discover
```

---

## 🔄 Pipeline CI/CD (GitHub Actions)

A pipeline executa automaticamente:

1. **Test** → Roda os testes unittest  
2. **Build** → Constrói a imagem Docker  
3. **Deploy** → Publica/roda a imagem (dependendo da configuração)

Exemplo de deploy automático:

```bash
docker run -d -p 1313:1313 usuario/api-flask:latest
```

---

## ▶️ Como rodar o projeto

```bash
git clone https://github.com/ErikPaulino87/Pipeline-Devops.git
cd Pipeline-Devops
docker-compose up --build
```

A aplicação estará funcionando na porta **1313**.

---
