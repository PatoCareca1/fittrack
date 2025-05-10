
# FitTrack

Sistema Web para gerenciamento de treino, dieta e progresso físico, desenvolvido com Django e Django REST Framework, com suporte adicional a GraphQL e autenticação via JWT. O objetivo é oferecer uma interface simples e funcional para praticantes de musculação acompanharem sua rotina de forma eficiente.

---

## 📚 Descrição Geral

O FitTrack permite:

- Cadastrar treinos e exercícios
- Registrar refeições com dados nutricionais
- Acompanhar a evolução corporal (peso, medidas)
- Usar tanto API REST quanto API GraphQL
- Proteger rotas com autenticação JWT
- Interagir com a API via front-end HTML + JS puro

---

## 🚀 Tecnologias Utilizadas

- Python 3.13
- Django 5.2.1
- Django REST Framework
- Graphene-Django (GraphQL)
- SimpleJWT (autenticação)
- Tailwind CSS (via CDN)
- HTML + JavaScript (fetch)

---

## 📁 Estrutura do Projeto

```
fittrack/
├── core/
│   ├── models.py            # Models principais
│   ├── views.py             # ViewSets da API REST
│   ├── serializers.py       # Serializers DRF
│   ├── schema.py            # Queries e mutations GraphQL
│   └── urls.py              # Rotas REST
├── frontend/
│   └── index.html           # Interface web
├── manage.py
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

(semelhante para `/meals/`, `/progress/`, etc.)

---

## 🔎 GraphQL

### URL:
```
http://localhost:8000/graphql/
```

### Exemplo de query:

```graphql
query {
  allWorkouts {
    id
    name
    date
  }
}
```

### Exemplo de mutation:

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

---

## 🧪 Como rodar localmente

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/fittrack.git
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

---

## 👨‍🏫 Observações Finais

- Projeto desenvolvido para a disciplina de Desenvolvimento Web (AT1)
- Integra REST e GraphQL em um único backend Django
- Autenticação segura via JWT
- Front-end leve e funcional com Tailwind
- Cumpre todos os critérios da AT1 com +2 pontos extras por GraphQL

---

## 📽️ Vídeo de Apresentação

> [INSIRA AQUI O LINK PARA O YOUTUBE]

---
