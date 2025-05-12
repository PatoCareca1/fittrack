
# FitTrack

Sistema Web para gerenciamento de treino, dieta e progresso físico, desenvolvido com Django e Django REST Framework, com suporte adicional a GraphQL e autenticação via JWT. O objetivo é oferecer uma interface simples e funcional para praticantes de musculação acompanharem sua rotina de forma eficiente.

 O projeto foi desenvolvido para as atividades AT1, AT2 e AT3 da disciplina de **Desenvolvimento Web (2ª Unidade)**.

## 📚 Descrição Geral

O FitTrack permite:
- Cadastrar treinos, exercícios e refeições
- Acompanhar evolução corporal (progresso físico)
- Persistir dados em banco relacional (SQLite) e arquivo JSON (workouts.json)
- Usar API REST e GraphQL (Queries e Mutations)
- Proteger rotas com autenticação JWT
- Gerenciar dados via front-end (HTML + JS puro + Tailwind CSS)

## 🚀 Tecnologias Utilizadas

- Python 3.13
- Django 5.2.1
- Django REST Framework
- Graphene-Django (GraphQL)
- SimpleJWT (autenticação JWT)
- SQLite (banco relacional)
- Tailwind CSS (CDN)
- HTML + JavaScript puro (fetch API)


## 📁 Estrutura do Projeto

```
fittrack/
├── core/
│   ├── models.py            # Models (Workout, Exercise, Meal, Progress, etc.)
│   ├── serializers.py       # Serializers DRF
│   ├── views/
│   │   ├── rest_views.py    # ViewSets da API REST (banco relacional)
│   │   └── json_views.py    # CRUD com persistência em arquivo JSON
│   ├── schema.py            # Queries e Mutations do GraphQL
│   └── urls.py              # Rotas REST e JSON
├── data/
│   └── workouts.json        # Persistência local (JSON)
├── fittrack/
│   ├── settings.py          # Configurações globais (JWT, CORS, apps)
│   ├── urls.py              # Inclusão de rotas REST e GraphQL
│   └── asgi.py / wsgi.py    # Servidores ASGI/WSGI
├── frontend/
│   └── index.html           # Interface web (CRUD completo)
├── manage.py                # Entrada principal Django
├── requirements.txt         # Dependências do projeto
└── README.md
```

> 🧠 REST e GraphQL compartilham o mesmo back-end. A separação é lógica e não exige múltiplas pastas específicas. Toda a autenticação, models e banco de dados são únicos.

---

## 🔐 Autenticação com JWT

### 1. Gerar token:

```
POST /api/token/
```

**Body (JSON):**
```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

### 2. Usar token:

Nas requisições autenticadas, envie o header:
```
Authorization: Bearer SEU_TOKEN
```

---

## 🔗 Endpoints REST principais

- `POST /api/token/` — gerar token
- `GET /api/workouts/` — listar treinos do usuário
- `POST /api/workouts/` — criar treino
- `PUT /api/workouts/{id}/` — editar
- `DELETE /api/workouts/{id}/` — remover

## Para JSON

- GET /api/json/workouts/
- POST /api/json/workouts/
- PUT /api/json/workouts/{id}/
- DELETE /api/json/workouts/{id}/

## 🔎 GraphQL

### Endpoint:
```
http://localhost:8000/graphql/
```
### Importante:

Header de autenticação:
´´´
{
  "Authorization": "Bearer SEU_TOKEN"
}
´´´
### Query de listagem:

```graphql
query {
  allWorkouts {
    id
    name
    date
  }
}
```

### Mutation de criação:

```graphql
mutation {
  createWorkout(name: "Treino GraphQL", date: "2025-05-12") {
    workout {
      id
      name
      date
    }
  }
}
```

> Autenticação por JWT também é exigida no GraphQL.

### Mutation de exclusão:

mutation {
  deleteWorkout(id: 1) { ok }
}

## 🧪 Como rodar localmente

1. Clone o repositório:
```bash
git clone https://github.com/PatoCareca1/fittrack
cd fittrack
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Aplique as migrações e crie superusuário:
```bash
python manage.py migrate
python manage.py createsuperuser
```

5. Rode o servidor:
```bash
python manage.py runserver
```

6. Acesse:
- API REST: `http://localhost:8000/api/workouts/`
- GraphQL: `http://localhost:8000/graphql/`
- Front-end: abra `frontend/index.html` no navegador

## ✅ O que foi entregue:

| ATIVIDADE | FUNCIONALIDADES INCLUÍDAS                                      |
|-----------|---------------------------------------------------------------|
| **AT1**   | API REST completa + Front-end funcional + JWT + GraphQL extra |
| **AT2**   | CRUD completo com persistência em arquivo JSON (via API e Front) |
| **AT3**   | Banco relacional (SQLite) + segurança JWT + GraphQL integrado |

## 📽️ Vídeo de Apresentação

> https://youtu.be/ZbWQWiZfR9I

