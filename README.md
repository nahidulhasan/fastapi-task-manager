📘 FastAPI Task Manager API

A simple, secure, and production-ready Task Manager REST API built with FastAPI, JWT Authentication, Argon2 Password Hashing, and SQLAlchemy ORM.
This project is perfect for learning backend development, FastAPI, authentication, and CRUD APIs.

🚀 Features

User Registration & Login (JWT Authentication)

Secure password hashing using Argon2

Create, read, update, delete tasks (CRUD)

SQLite database (easy to run locally)

Protected routes using OAuth2 Bearer Tokens

Pydantic models for validation

Auto-generated API documentation (Swagger UI)

Clean, modular project structure



📦 Tech Stack

FastAPI

SQLAlchemy ORM

Pydantic

Argon2 (argon2-cffi)

SQLite

Python-Jose (JWT)

Uvicorn


⚙️ Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/nahidulhasan/fastapi-task-manager.git

cd fastapi-task-manager

2️⃣ Create & activate virtual environment

python3 -m venv .venv

source .venv/bin/activate

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Run the API

uvicorn app.main:app --reload

API will be available at:
http://127.0.0.1:8000

Interactive API docs (Swagger UI):
http://127.0.0.1:8000/docs

🔐 Authentication Flow

1️⃣ Register a user

POST /auth/register

Body:

{
  "email": "test@example.com",
  "password": "123456"
}

2️⃣ Login to get JWT token

POST /auth/token

Form-data:

username=test@example.com
password=123456


Response:

{

  "access_token": "<JWT_TOKEN>",

  "token_type": "bearer"

}


Use this token for all protected routes:

Authorization: Bearer <token>

📝 Task Endpoints

➕ Create a Task

POST /tasks/
Requires authentication.

Example:

{

  "title": "Buy groceries",

  "description": "Milk, eggs, bread",

  "priority": "HIGH",

  "due_date": "2025-01-31T10:00:00"
}

📖 Get All Tasks

GET /tasks/


🔍 Get Single Task

GET /tasks/{task_id}

✏️ Update Task

PUT /tasks/{task_id}

Example:

{

  "title": "Updated title",

  "completed": true

}

🗑 Delete Task

DELETE 

/tasks/{task_id}

🗄 Database

SQLite is used by default:

app/tasks.db


❤️ Contributing

Pull requests are welcome!
Feel free to open issues or suggest new features.

📜 License

MIT License.
