# 🚀 Pipeline DevOps – API Flask 

Este repositório contém uma API em **Flask** com **Docker**, **Swagger**, **JWT**, testes com **unittest** e pipeline **CI/CD**.  
A aplicação pode ser acessada **localmente** ou pelo **deploy na nuvem (Vercel)**.

---

## 🌐 Acesso na nuvem (deploy)

A versão publicada está disponível em:

- API: **https://pipeline-devops-pi.vercel.app**  
- Swagger: **https://pipeline-devops-pi.vercel.app/swagger**

---

## ▶️ Acesso local (desenvolvimento)

### 🔹 Rodar localmente (Python)
```bash
pip install -r requirements.txt
python app.py
```

Acesse:
- API: http://localhost:1313
- Swagger: http://localhost:1313/swagger

---

### 🔹 Rodar com Docker
```bash
docker build -t api-flask .
docker run -p 1313:1313 api-flask
```

### 🔹 Docker Compose
```bash
docker-compose up --build
```

Acesse:
- API: http://localhost:1313
- Swagger: http://localhost:1313/swagger

---

## 🔐 Autenticação JWT

### Gerar token  
POST:
```
Local:  http://localhost:1313/login
Nuvem:  https://pipeline-devops-pi.vercel.app/login
```

### Acessar rota protegida  
Header:
```
Authorization: Bearer <token>
```

---

## 🧪 Testes

Executar testes:
```bash
python -m unittest discover
```

---

## 🔄 Pipeline CI/CD (GitHub Actions)

A pipeline executa automaticamente:

1. **Test** – Executa os testes automatizados  
2. **Build** – Constrói a imagem Docker  
3. **Deploy** – Publica/atualiza a aplicação na nuvem  

---

## ▶️ Como iniciar rapidamente

```bash
git clone https://github.com/ErikPaulino87/Pipeline-Devops.git
cd Pipeline-Devops
docker-compose up --build
```

A aplicação estará disponível em:

👉 Local: http://localhost:1313  
👉 Nuvem: https://pipeline-devops-pi.vercel.app

---
