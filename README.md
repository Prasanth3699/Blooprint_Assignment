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

### Using Postman

 1. **Register a New User**

    - Set the request type to POST and the URL to `http://127.0.0.1:8000/api/register/`.
    - In the Body tab, select raw and JSON format.
    - Enter the JSON data:
      
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
    - Click Send.

  Authenticate with the API to receive a JWT access token, which is required for subsequent authenticated requests.

2. **Login to Obtain JWT Tokens:**
   - Set the request type to `POST` and the URL to `http://127.0.0.1:8000/api/login/`.
   - In the Body tab, select `raw` and `JSON` format.
   - Enter the JSON data:
     
    ```json
     {
       "username": "your_username",
       "password": "your_password"
     }
     ```
    - Click Send.
    - Copy the `access` token from the response for authenticated requests.

    
3. **Create a New Item:**
   - Set the request type to `POST` and the URL to `http://127.0.0.1:8000/api/items/`.
   - In the Headers tab, add:
     - `Content-Type: application/json`
     - `Authorization: Bearer <your_access_token>`
   - In the Body tab, select raw and `JSON` format.
   - Enter the JSON data:
     
    ```json
     {
    "name": "Item Name",
    "description": "Item Description",
    "quantity": 100,
    "price": 29.99,
    "category": "electronics"
    }
     ```
   - Click Send.
     
4. **Read an Item:**
   - Set the request type to `GET` and the URL to `http://127.0.0.1:8000/api/items/1/`.
   - In the Headers tab, add:
      - `Authorization: Bearer <your_access_token>`
   - Click Send.

5. **Update an Item:**

   - Set the request type to `PUT` and the URL to `http://127.0.0.1:8000/api/items/1/update/`.
   - In the Headers tab, add:
      - `Content-Type: application/json`
      - `Authorization: Bearer <your_access_token>`
   - In the Body tab, select raw and JSON format.
   - Enter the JSON data:
     
    ```json
     {
    "name": "Updated Name",
    "description": "Updated Description",
    "quantity": 150,
    "price": 39.99,
    "category": "furniture"
      }
     ```
   - Click Send.
      
6. **Delete an Item:**

   - Set the request type to `DELETE` and the URL to `http://127.0.0.1:8000/api/items/1/delete/`.
   - In the Headers tab, add:
      - `Authorization: Bearer <your_access_token>`
   - Click Send.

---

## Notes

- Replace `<your_access_token>` with the actual JWT access token obtained from the login response.
- Ensure that the API server is running at `http://127.0.0.1:8000/`.
- Replace item IDs in the URLs with the actual IDs of the items you wish to interact with.
- Use tools like [Postman](https://www.postman.com/) or [cURL](https://curl.se/) to send HTTP requests.

---

## Troubleshooting

- **Invalid Credentials:** Ensure that the username and password provided during login are correct.
- **Expired Token:** If the access token has expired, perform the login process again to obtain a new token.
- **Permission Denied:** Verify that the authenticated user has the necessary permissions to perform the requested operation.
- **Server Errors:** Check the server logs for detailed error messages and ensure that the API server is running without issues.

---

## License

**This is an assignment demo project. Please do not misuse or distribute this repository. It is intended solely for educational and demonstration purposes. Unauthorized use is prohibited.**
---






