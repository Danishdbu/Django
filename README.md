# Django Setup Notes

This guide outlines the steps to set up a Django project, including the folder and file structure.

## Prerequisites
- Python 3.8+ installed
- pip (Python package manager)
- virtualenv (recommended for isolated environments)

## Setup Steps

1. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Django**
   ```bash
   pip install django
   ```

3. **Start a New Django Project**
   ```bash
   django-admin startproject myproject
   cd myproject
   ```

4. **Create a Django App**
   ```bash
   python manage.py startapp myapp
   ```

5. **Configure Settings**
   - Open `myproject/settings.py`
   - Add `'myapp'` to `INSTALLED_APPS`:
     ```python
     INSTALLED_APPS = [
         ...
         'myapp',
     ]
     ```

6. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Start Development Server**
   ```bash
   python manage.py runserver
   ```
   - Access at `http://127.0.0.1:8000/`

## Folder and File Structure

Below is the typical structure of a Django project after setting up a project named `myproject` and an app named `myapp`.

```
myproject/
│
├── myproject/
│   ├── __init__.py           # Marks directory as Python package
│   ├── asgi.py              # ASGI config for async deployment
│   ├── settings.py          # Project settings (database, apps, etc.)
│   ├── urls.py              # Root URL configurations
│   └── wsgi.py              # WSGI config for deployment
│
├── myapp/
│   ├── __init__.py           # Marks directory as Python package
│   ├── admin.py             # Admin panel customizations
│   ├── apps.py              # App configuration
│   ├── migrations/          # Database migration files
│   │   ├── __init__.py
│   │   └── 0001_initial.py  # Example migration file
│   ├── models.py            # Database models
│   ├── tests.py             # Test cases
│   ├── urls.py              # App-specific URL configurations
│   └── views.py             # View functions or classes
│
├── venv/                    # Virtual environment folder
│   ├── bin/                 # Scripts (activate, pip, python)
│   ├── lib/                 # Python libraries
│   └── pyvenv.cfg           # Virtual env config
│
├── manage.py                # Django command-line utility
├── requirements.txt         # Project dependencies (optional, create with `pip freeze > requirements.txt`)
└── .gitignore               # Git ignore file (optional, for version control)
```

## Example `.gitignore`
```
# .gitignore
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.sqlite3
```

## Notes
- **Project vs. App**: The project (`myproject`) is the overall container, while apps (`myapp`) are modular components.
- **Database**: Default is SQLite (`db.sqlite3`). Modify `settings.py` for PostgreSQL, MySQL, etc.
- **Static Files**: Add a `static/` folder in the app or project for CSS/JS/images.
- **Templates**: Create a `templates/` folder in the app for HTML files.
- **Next Steps**: Define models in `myapp/models.py`, create views in `myapp/views.py`, and map URLs in `myapp/urls.py`.

## Example `requirements.txt`
```
django==5.1
```

## Useful Commands
- Create superuser: `python manage.py createsuperuser`
- Collect static files: `python manage.py collectstatic`
- Run tests: `python manage.py test`

This setup provides a foundation for building a Django application.
