# Hello World Django Project

## Description
This project is a simple Django application that displays "Hello, World!" or a personalized greeting if a name is specified as a query parameter.



### Prerequisites
- Python installed on your machine.
- Django installed (`pip install django`).

### Project Setup and Run Instructions
1. download the project files.
2. Navigate to the project directory.
   ```sh
   cd myproject
3. Install dependencies
`pip install -r requirements.txt`
4. Create the database 
`python manage.py migrate`
5. Start the server
`python manage.py runserver`
6. Access the application in your web browser
`http://localhost:8000/hello/`
or `http://127.0.0.1:8000/hello/?name=Roger`

### Additional Notes
The `hello_world` endpoint is configured in `urls.py` and `views.py`.