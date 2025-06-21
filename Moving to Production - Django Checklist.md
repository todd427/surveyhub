**Great move!** Here’s a concise checklist (with details if you want them) for taking your Django site from **development to production**—especially if you’re deploying on Railway or any modern PaaS.

---

# 🚀 Moving to Production: Django Checklist

## 1. **Set `DEBUG = False`**

* In `settings.py`:

  ```python
  DEBUG = False
  ```
* Add your production domain(s) to `ALLOWED_HOSTS`:

  ```python
  ALLOWED_HOSTS = ["your-production-domain.com", "your-app-on-railway.app"]
  ```

---

## 2. **Configure Static & Media Files**

* Collect static files:

  ```bash
  python manage.py collectstatic
  ```
* In production, make sure static files are served correctly. On Railway, you may need to use [WhiteNoise](https://whitenoise.evans.io/) or let your PaaS handle static files.

  * **Add WhiteNoise:**
    `pip install whitenoise`
    In `settings.py`, add to `MIDDLEWARE` *after* SecurityMiddleware:

    ```python
    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
        # ...
    ]
    ```

    And set:

    ```python
    STATIC_ROOT = BASE_DIR / "staticfiles"
    STATIC_URL = "/static/"
    ```

    (You already have `STATICFILES_DIRS` for dev.)

---

## 3. **Database Settings**

* Use a production database (e.g., Railway Postgres, not SQLite).
* Set your database URL in Railway's environment variables or in `settings.py`:

  ```python
  import os
  DATABASES = {
      "default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))
  }
  ```

  * (Use `dj-database-url` if you want easy env var parsing.)

---

## 4. **Set SECRET\_KEY Securely**

* Never use your dev/test `SECRET_KEY` in production.
* In Railway, add `SECRET_KEY` as a private environment variable and load it in `settings.py`:

  ```python
  SECRET_KEY = os.environ.get("SECRET_KEY")
  ```

---

## 5. **Security Settings**

* **CSRF and session cookies:**

  ```python
  CSRF_COOKIE_SECURE = True
  SESSION_COOKIE_SECURE = True
  ```
* **Use HTTPS** (Railway serves HTTPS by default)
* **Set `SECURE_HSTS_SECONDS`**, `SECURE_SSL_REDIRECT`, etc., for best practice.

---

## 6. **Allowed Hosts & CORS**

* Confirm `ALLOWED_HOSTS` matches your production domain(s).
* If using AJAX or APIs, configure CORS appropriately.

---

## 7. **Email Settings**

* For password resets, notifications, etc., use a real email backend (SMTP, SendGrid, etc.), not console backend.

---

## 8. **Run Migrations on Production**

* After deployment, run:

  ```bash
  python manage.py migrate
  ```

---

## 9. **(Optional) Admin Hardening**

* Restrict `/admin` to superusers.
* Change admin URL (e.g., to `/my-secret-admin/`).

---

## 10. **Monitoring & Logging**

* Set up error reporting and logging (e.g., Sentry, Railway logs).
* Make sure you have access to Railway logs for troubleshooting.

---

## 11. **Test Everything!**

* Visit the live app on its Railway URL (or custom domain).
* Check static files, forms, login, survey submission, and the admin.

---

# **Railway-Specific Steps**

1. **Connect your GitHub repo to Railway.**
2. **Set environment variables** in Railway's dashboard for `SECRET_KEY`, `DATABASE_URL`, etc.
3. **Deploy!** (Railway will build and collect static files.)
4. **Run migrations** from Railway's “Shell”/“Run” tool.
5. **Point your custom domain** (optional) and update `ALLOWED_HOSTS`.

---

## 🏁 You’re live!

**Let me know if you want step-by-step code, a sample `settings.py` for production, or if you hit any snags!**
Happy to help review your Railway deployment config or environment.
