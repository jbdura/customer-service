# API

This is the API for the customer service web app.

# Getting Started

These instructions will help you set up and run the project on your local machine. 

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.9 or higher
- `virtualenv` 

### Installation



1. Navigate to the project directory:

  ```bash
    cd api
  ```

2. Create a virtual environment (recommended):

  ```bash
  virtualenv .env
  source .env/bin/activate  # On Windows, use 'venv\Scripts\activate'
  ```

3. Install project dependencies:

  ```bash
  pip install -r requirements.txt
  ```

4. Apply database migrations:

  ```bash
  python manage.py migrate
  ```

### Running the Development Server
Start the Django development server:

  ```bash
  python manage.py runserver
  ```
  You can access the API at http://localhost:8000

# API Documentation
The project includes Swagger documentation for the API. You can access the API documentation by visiting http://localhost:8000/api/docs/ in your web browser.

### Authentication
By default, the project uses token-based authentication. To obtain an authentication token, you can use the built-in /api/token/ endpoint. See the API documentation for more details.
