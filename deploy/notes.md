# Deployment Notes

## 1. Environment Setup

- Clone repository and navigate to project folder.
- Create and activate virtual environment:
    - Windows: `python -m venv env && .\env\Scripts\activate`
    - Linux/Mac: `python3 -m venv env && source env/bin/activate`
- Install requirements:

    ```
    pip install -r requirements.txt
    ```

## 2. Environment Variables

- Copy `.env.example` to `.env`.
- Edit `.env`:
    - Set `SECRET_KEY`
    - Set `DEBUG`
    - Set `ALLOWED_HOSTS`
    - Set `DATABASE_URL` (e.g. for production: `postgres://...`)

## 3. Database Migration

- Apply migrations:

    ```
    python manage.py migrate
    ```

## 4. Create Superuser

- Create an admin user for access to /admin:

    ```
    python manage.py createsuperuser
    ```

## 5. Static Files

- Collect static assets:

    ```
    python manage.py collectstatic
    ```
- Ensure `STATIC_ROOT` is correctly set in `settings.py`.

## 6. Running the Server

- For development:

    ```
    python manage.py runserver
    ```
- For production (Linux):
    ```
    gunicorn librarybox.wsgi:application --bind 0.0.0.0:8000
    ``` 
    *(For Windows, use Waitress instead of Gunicorn.)*

## 7. Deployment Tips

- Set `DEBUG=False` for production.
- Use strong secrets in `.env`.
- Make sure `.env` and `db.sqlite3` are in `.gitignore`.
- Consider Nginx proxy for production static/media files & HTTPS.

## 8. Troubleshooting

- Activate virtual environment before running any Django commands.
- Look for missing migrations, incorrect environment variables, or static file errors.

---

## File Structure Example

    libraryboxd/
    ├─ core/
    │  ├─ __pycache__/
    │  ├─ migrations/
    │  │  ├─ __pycache__/
    │  │  ├─ __init__.py
    │  ├─ __init__.py
    │  ├─ admin.py
    │  ├─ apps.py
    │  ├─ models.py
    │  ├─ tests.py
    │  ├─ urls.py
    │  ├─ views.py
    ├─ deploy/
    │  ├─ deploy.sh
    │  ├─ notes.md*
    ├─ dockerfile/
    ├─ env/
    │  ├─ Include/
    │  ├─ Lib \ site-packages/
    │  ├─ Scripts/
    │  ├─ .gitignore
    │  ├─ pyvenv.cfg
    ├─ libraryboxd/
    │  ├─ __pycache__/
    │  ├─ __init__.py
    │  ├─ .env
    │  ├─ asgi.py
    │  ├─ settings.py
    │  ├─ urls.py
    │  ├─ wsgi.py
    ├─ staticfiles \ admin/
    │  ├─ css/
    │  ├─ img/
    │  ├─ js/
    ├─ .env.example
    ├─ .gitignore
    ├─ manage.py
    ├─ db.sqlite3
    ├─ README.md
    ├─ requirements.txt
