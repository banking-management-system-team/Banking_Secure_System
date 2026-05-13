# 🏦 Banking Management System API

A scalable and enterprise-level Banking Management System backend built using **FastAPI**, **Supabase PostgreSQL**, **SQLAlchemy ORM**, and **JWT Authentication**.

This project is designed using a modular architecture to support large-scale banking operations including authentication, account management, transactions, loan services, and administrative controls.

The system follows industry-standard backend development practices with clean folder structure, secure authentication, database abstraction, and RESTful API design.

---

# 🚀 Project Modules

The complete system contains 5 major modules:

| Module | Description |
|---|---|
| Authentication Module | User registration, login, JWT authentication |
| Accounts Module | Bank account creation and management |
| Transactions Module | Deposit, withdrawal, transfer, transaction history |
| Loan Module | Loan applications, EMI tracking, approvals |
| Admin Module | Manage users, accounts, reports, analytics |

---

# 📌 Total API Routers

| Module | Routes |
|---|---|
| Authentication | 5 |
| Accounts | 5 |
| Transactions | 5 |
| Loans | 5 |
| Admin | 5 |

✅ Total APIs: **25 Routes**

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| FastAPI | Backend Framework |
| PostgreSQL | Relational Database |
| Supabase | Cloud PostgreSQL Provider |
| SQLAlchemy | ORM |
| JWT | Secure Authentication |
| bcrypt | Password Hashing |
| Pydantic | Data Validation |
| Uvicorn | ASGI Server |
| Python | Core Programming Language |

---

# 🏗️ System Architecture

```text id="1fhqaj"
Frontend / Client
        ↓
FastAPI Routers
        ↓
Service Layer
        ↓
SQLAlchemy ORM
        ↓
Supabase PostgreSQL Database

📁 Project Structure
banking_system/
│
├── app/
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── dependencies.py
│   │
│   ├── models/
│   │   ├── user_model.py
│   │   ├── account_model.py
│   │   ├── transaction_model.py
│   │   ├── loan_model.py
│   │   ├── emi_model.py
│   │
│   ├── schemas/
│   │   ├── auth_schema.py
│   │   ├── account_schema.py
│   │   ├── transaction_schema.py
│   │   ├── loan_schema.py
│   │   ├── admin_schema.py
│   │
│   ├── routers/
│   │   ├── auth_router.py
│   │   ├── account_router.py
│   │   ├── transaction_router.py
│   │   ├── loan_router.py
│   │   ├── admin_router.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── account_service.py
│   │   ├── transaction_service.py
│   │   ├── loan_service.py
│   │   ├── admin_service.py
│   │
│   ├── repositories/
│   │   ├── auth_repository.py
│   │   ├── account_repository.py
│   │   ├── transaction_repository.py
│   │   ├── loan_repository.py
│   │   ├── admin_repository.py
│   │
│   ├── utils/
│   │   ├── password.py
│   │   ├── jwt_handler.py
│   │
│   ├── __init__.py
│   └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md

🔐 Authentication Flow
User Registration
        ↓
Password Hashing using bcrypt
        ↓
Store User in PostgreSQL
        ↓
User Login
        ↓
Password Verification
        ↓
JWT Token Generation
        ↓
Access Protected APIs

⚙️ Environment Variables

Create a .env file in project root:
DATABASE_URL=postgresql://YOUR_USERNAME:YOUR_PASSWORD@YOUR_SUPABASE_URL:6543/postgres

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

📦 Installation Guide
1️⃣ Clone Repository
git clone https://github.com/your-username/banking-system.git
2️⃣ Navigate to Project
cd banking-system
3️⃣ Create Virtual Environment
Windows
python -m venv venv
4️⃣ Activate Virtual Environment
Windows
venv\Scripts\activate
5️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Run FastAPI Server
python -m uvicorn app.main:app --reload
🌐 API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc UI:

http://127.0.0.1:8000/redoc

📚 API Endpoints

🔐 Authentication Routes
Method	Endpoint	Description
POST	/auth/register	Register User
POST	/auth/login	Login User
POST	/auth/logout	Logout User
GET	/auth/profile	Get User Profile
PUT	/auth/profile/update	Update Profile

🏦 Account Routes
Method	Endpoint	Description
POST	/accounts/create	Create Bank Account
GET	/accounts/details/{id}	Get Account Details
GET	/accounts/balance/{id}	Check Balance
PUT	/accounts/update/{id}	Update Account
DELETE	/accounts/delete/{id}	Delete Account

💸 Transaction Routes
Method	Endpoint	Description
POST	/transactions/deposit	Deposit Money
POST	/transactions/withdraw	Withdraw Money
POST	/transactions/transfer	Transfer Money
GET	/transactions/history/{id}	Transaction History
GET	/transactions/{id}	Transaction Details

🏦 Loan Routes
Method	Endpoint	Description
POST	/loans/apply	Apply for Loan
GET	/loans/status/{id}	Loan Status
GET	/loans/history/{id}	Loan History
PUT	/loans/update/{id}	Update Loan
DELETE	/loans/cancel/{id}	Cancel Loan

👨‍💼 Admin Routes
Method	Endpoint	Description
GET	/admin/users	View All Users
GET	/admin/accounts	View All Accounts
GET	/admin/transactions	View Transactions
GET	/admin/loans	View Loans
GET	/admin/reports	Generate Reports

🗄️ Database Tables
Table Name	Purpose
users	Store user details
accounts	Bank account details
transactions	Deposit/withdrawal history
loans	Loan records
emis	EMI tracking

🔒 Security Features

✅ JWT Authentication
✅ bcrypt Password Hashing
✅ SQLAlchemy ORM Protection
✅ Input Validation using Pydantic
✅ Environment Variable Protection
✅ Secure API Design
✅ Role-Based Access Control
✅ Secure Database Connection

👥 Team Distribution
Team Member	Responsibility
Member 1	Authentication Module
Member 2	Accounts Module
Member 3	Transactions Module
Member 4	Loans Module
Member 5	Admin Module

📈 Future Enhancements
Redis Caching
Docker Deployment
Kubernetes Scaling
Rate Limiting
Fraud Detection
Email Notifications
SMS Alerts
CI/CD Pipeline
API Gateway
Microservices Architecture
🧠 Learning Outcomes

This project demonstrates:

✅ Enterprise Backend Architecture
✅ REST API Development
✅ ORM Integration
✅ Authentication & Authorization
✅ Cloud Database Integration
✅ Team Collaboration Workflow
✅ Scalable FastAPI Design

👨‍💻 Author
Vasant Naik & Team

FastAPI | PostgreSQL | Backend Development

⭐ Support

If you like this project:

⭐ Star the repository
🍴 Fork the repository
📢 Share with others

📜 License

This project is licensed under the MIT License.