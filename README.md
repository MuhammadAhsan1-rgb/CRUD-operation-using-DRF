# CRUD-operation-using-DRF

![Python](https://img.shields.io/badge/Python-3.9-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-REST_Framework-092E20?style=flat&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/Database-MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)

A secured RESTful CRUD API built with **Django REST Framework**, managing **Employee** and **Department** resources on top of a **MySQL** database. Built as part of the Progree Backend Development Internship (Task 2).

## 🚀 Features

- Full CRUD support (Create, Read, Update, Delete) for both Employee and Department resources
- Relational data model — each Employee belongs to a Department via a foreign key
- Request validation via DRF ModelSerializers
- Partial updates supported through PATCH, full updates through PUT
- Database credentials kept out of source control using environment variables

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** Django, Django REST Framework
- **Database:** MySQL
- **Config management:** python-decouple (`.env` file)

## 📁 Project Structure

```
Project 2/
├── Project/
│   └── api/              # Main app: models, serializers, views, urls
├── Project_1/             # Django project config (settings, asgi, wsgi, urls)
├── manage.py
├── requirements.txt
└── .env                   # Local environment variables (not committed)
```

## ⚙️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/MuhammadAhsan1-rgb/CRUD-operation-using-DRF.git
cd CRUD-operation-using-DRF
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the project root:
```
DB_NAME=mydatabase
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=3306
```

### 5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the development server
```bash
python manage.py runserver
```

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| 🟢 GET | `/get/` | List all employees and departments |
| 🔵 POST | `/create-department/` | Create a new department |
| 🔵 POST | `/create-employee/` | Create a new employee |
| 🟡 PUT / PATCH | `/update-department/<id>` | Update a department |
| 🟡 PUT / PATCH | `/update-employee/<id>` | Update an employee |
| 🔴 DELETE | `/delete-department/<id>` | Delete a department |
| 🔴 DELETE | `/delete-employee/<id>` | Delete an employee |

## 👤 Author

Muhammad Ahsan
