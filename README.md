# StellarBlog

A fully-featured Django blog app with user authentication, post creation, comments, and attractive design.  
Built with Django, Python, MySQL, HTML, CSS, and JavaScript.

## Features
- Register, login, logout
- Create/view posts (with images)
- Add comments
- Secure user permissions
- Animated UI and glassmorphism theme
- Admin dashboard for post/user management

## Tech Stack
- Django 5.2.7
- MySQL (Workbench)
- Python 3.13
- HTML/CSS/JS
- VS Code, Git, GitHub

## Running Locally

1. Clone the repository:
    ```
    git clone https://github.com/SAIMOULIs/stellarblog.git
    ```
2. Create a Python virtual environment and activate it.
3. Install requirements:
    ```
    pip install -r requirements.txt
    ```
4. Configure your MySQL database in `settings.py`.
5. Run migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Create a superuser:
    ```
    python manage.py createsuperuser
    ```
7. Run the local server:
    ```
    python manage.py runserver
    ```
8. Visit `http://127.0.0.1:8000`
9. Done!

## Screenshots
*(Add your homepage, login, admin, and post screenshots)*

## Authors
- [Your Name] (your email)

## License
MIT
