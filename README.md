# Inventory Management System API

## Overview

The **Inventory Management System API** is a comprehensive backend application built with **Django Rest Framework (DRF)**. It facilitates efficient management of inventory items, supporting full CRUD (Create, Read, Update, Delete) operations. The system leverages **PostgreSQL** for robust database management, **Redis** for caching frequently accessed data to enhance performance, and **JWT (JSON Web Tokens)** for secure authentication. Configuration management is handled securely using **python-decouple**, allowing for easy management of environment variables. Additionally, the application incorporates **logging** for monitoring and **unit tests** to ensure reliability and functionality.

## Features

- **User Authentication**
  - User registration and login with JWT-based authentication.
  
- **CRUD Operations**
  - Create, Read, Update, and Delete inventory items with detailed attributes.
  
- **Caching**
  - Utilizes Redis to cache frequently accessed items, improving performance.
  
- **Configuration Management**
  - Uses `python-decouple` to manage environment variables securely.
  
- **Logging**
  - Comprehensive logging for debugging and monitoring API usage.
  
- **Testing**
  - Unit tests to verify the functionality of all API endpoints.

## Technologies Used

- **Django**
- **Django Rest Framework**
- **PostgreSQL**
- **Redis**
- **JWT Authentication**
- **Python-Decouple**
- **Python Logging**
- **Unit Testing with Django's Test Framework**

## Getting Started

Follow these instructions to set up and run the Inventory Management System API on your local machine.

### Prerequisites

- **Python 3.8+**
- **PostgreSQL**
- **Redis**

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/inventory_management.git
cd inventory_management
```

#### 2. Create a Virtual Environment
  It's recommended to use a virtual environment to manage project dependencies.

```bash
git clone https://github.com/yourusername/inventory_management.git
cd inventory_management
```


#### 3. Install Dependencies
Install the required Python packages using `pip`.

```bash
pip install -r requirements.txt
```

#### 4. Configure Environment Variables
The project uses python-decouple to manage configuration via environment variables. Create a `.env` file in the root directory of the project with the following content:

```bash
SECRET_KEY=your-very-secure-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DB_NAME=your_db_name
DB_USER=your-db-username
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=port

# Redis Configuration
REDIS_URL=redis://127.0.0.1:6379/1
```
**Important:** Replace the placeholder values (e.g., your-very-secure-secret-key, your-db-password) with your actual configuration details.


#### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5. Start Redis Server
Ensure Redis is installed and running on `localhost:6379`.


#### 5. Run the Development Server

```bash
python manage.py runserver
```
Access the API at `http://127.0.0.1:8000/api/`


## API Documentation















