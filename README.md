
# Foxxe Frey Labs

Welcome to **Foxxe Frey Labs** — a Django-powered web platform for creative innovation, showcasing a blend of interactive surveys, games, and author information. This project demonstrates rapid, modern Django development with a clean UI, modular architecture, and W3.CSS for styling.

## 🚀 Features

- ✨ **Lunar Lander**: A playable Lunar Lander game (pure HTML/JS/CSS) on `/lander/`
- 📝 **Surveys & Quizzes**: Foundation for interactive surveys (Quiz, Programmer Survey, Reader Survey coming soon)
- 📃 **About**: Media-rich author page with project background
- 🌈 **Modern UI**: Responsive layout using [W3.CSS](https://www.w3schools.com/w3css/)
- ⚡ **Fast Deploy**: Ready for deployment on [Railway](https://railway.app/) or any modern Django host

---

## 🏗️ Project Structure

```
yourproject/
├── pages/                  # App for static/info pages (home, about, lander)
│   ├── templates/pages/
│   │   ├── home.html
│   │   ├── about.html
│   │   └── lander.html
│   └── static/pages/
│       └── ... (optional)
├── surveys/                # Survey, Quiz, and future Reader Survey logic
├── static/
│   ├── css/
│   │   └── base.css        # Custom global styles (optional)
│   ├── js/
│   │   └── base.js         # Custom global JS (optional)
│   └── images/
│       └── FoxxeFreyLabs.png
├── templates/
│   └── base.html           # Site-wide base template (W3.CSS)
├── manage.py
└── requirements.txt
```

---

## 🚦 Quickstart

### 1. **Clone and Setup**

```bash
git clone https://github.com/yourusername/foxxe-frey-labs.git
cd foxxe-frey-labs
python3 -m venv hubEnv
source hubEnv/bin/activate
pip install -r requirements.txt
```

### 2. **Apply Migrations and Run**

```bash
python manage.py migrate
python manage.py runserver
```
Visit [http://localhost:8000](http://localhost:8000) in your browser.

---

### 3. **Static Files**

- Global static files go in `/static/`
- App-specific static files go in `yourapp/static/yourapp/`
- Run `python manage.py collectstatic` before deploying to production.

---

## 🛠️ Customization

- **Styling:** Easily themed by editing `base.html` and using W3.CSS utility classes.
- **Pages:** Add new pages in the `pages` app.
- **Surveys:** Expand the `surveys` app for more forms and data collection.

---

## 🌍 Deployment

Ready for Railway, Heroku, or any modern Django host.
- Set environment variables for `DEBUG`, `SECRET_KEY`, and database settings.
- For Railway, connect your repo, set up your environment, and deploy.

---

## 🤝 Credits

- [W3.CSS](https://www.w3schools.com/w3css/) for fast, mobile-first UI
- [Django](https://www.djangoproject.com/) for robust backend
- [Todd McCaffrey](https://toddmccaffrey.com/) — project creator & inspiration

---

## 📢 License

MIT — see [LICENSE](LICENSE) for details.

---

**Questions, suggestions, or PRs welcome!**
