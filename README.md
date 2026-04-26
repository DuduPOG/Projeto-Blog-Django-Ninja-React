# Projeto-Blog-Django-Ninja-React

Repositório para prática de Django Ninja e React para os contribuidores terem condições de ganhar dinheiro com desenvolvimento de software

## 🚀 Bootcamp Fullstack — Diário Pessoal (Django Ninja + React)

Este repositório é a base de um bootcamp prático onde cada participante irá desenvolver um **blog/diário pessoal** utilizando:

* 🐍 Django + Django Ninja (backend)
* ⚛️ React (frontend)

O objetivo é aprender **fullstack na prática**, construindo uma aplicação real passo a passo.

---

## 📌 📖 Sobre o Projeto

A aplicação será um **diário pessoal com posts organizados por tópicos**:

* 📝 Criar postagens
* 🗂️ Criar tópicos (categorias)
* 📚 Sidebar com tópicos
* 📄 Feed vertical de posts

---

## 🧱 Estrutura do Projeto

```bash
meu-bootcamp/
│
├── backend/        # Django + Ninja
├── frontend/       # React
└── README.md
```

---

## ⚙️ 🔧 Setup Inicial (OBRIGATÓRIO)

### 1. Clonar o repositório

```bash
git clone https://github.com/DuduPOG/Projeto-Comercio-Eletronico-Django-Ninja.git
```

---

## 🐍 BACKEND — Django Ninja

### 2. Criar ambiente virtual Python

```bash
python -m venv {'nome do ambiente'}
```

### Ativar ambiente

* **Linux/macOS**

```bash
source venv/bin/activate
```

* **Windows**

```bash
venv\Scripts\activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Rodar servidor backend

```bash
python manage.py runserver
```

A API estará disponível em:
👉 [http://localhost:8000/api/](http://localhost:8000/api/)

---

## ⚛️ FRONTEND — React

### 5. Instalar dependências

```bash
cd frontend
npm install
```

---

### 6. Rodar frontend

```bash
npm run dev
```

O frontend estará em:
👉 [http://localhost:5173](http://localhost:5173)

---

## 🔗 Integração

O React irá consumir a API do Django em:

```bash
http://localhost:8000/api/
```

---

## 📋 📚 Regras do Bootcamp

Para manter organização e aprendizado:

* ✅ Commits pequenos e frequentes
* ✅ Cada funcionalidade deve funcionar antes de avançar
* ✅ Reunião todo final de semana para apresentar a evoução individual
* ❌ Não pular etapas
* ❌ Não copiar código sem entender

---

## 📈 Roadmap de Desenvolvimento

### 🟢 Etapa 1 — Base

* Criar tela no Figma (opcional)
* Listar posts
* Criar posts
* Layout simples

---

### 🟡 Etapa 2 — Tópicos

* Criar tópicos
* Filtrar posts por tópico
* Sidebar funcional

---

### 🟠 Etapa 3 — CRUD completo

* Editar post
* Deletar post

---

### 🔵 Etapa 4 — Melhorias

* Loading
* Feedback de erro
* Melhorar UI

---

### 🔴 Etapa 5 — Avançado (opcional)

* Login (autenticação)
* Usuários
* Posts privados

---

## 💡 Dicas Importantes

* Sempre verifique o console do navegador (F12)
* Use o Django Admin para testar dados
* Teste endpoints antes de integrar com o React

---

## 🧪 Testando a API

Acesse no navegador:

👉 [http://localhost:8000/api/docs](http://localhost:8000/api/docs)

---

## 🆘 Problemas Comuns

### CORS error

→ Verificar `django-cors-headers`

### API não responde

→ Backend não está rodando

### Mudança não aparece

→ Reiniciar servidor

---

## 🎯 Objetivo Final

Cada participante terá um:

* Projeto fullstack funcional
* Entendimento de APIs REST
* Experiência com React + Django

---

## 🚀 Bora codar

Se travar, pergunte, investigue e tente entender — isso faz parte do processo.
