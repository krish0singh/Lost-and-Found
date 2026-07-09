# Lost & Found Portal

**Developed by:** Krish Singh
**Course:** BSc Computer Science — Semester 5 Mini Project

A web application that helps students and employees...
A web application that helps students and employees of a college or
organization report **lost items** and post **found items**, so that
belongings can be reunited with their owners quickly.

Built as a BSc Computer Science Semester 5 Mini Project.

---

## Features

- **User Authentication** — Register, Login, Logout (passwords hashed with Werkzeug)
- **Home Page** — Welcome banner + latest lost and found items
- **Lost Item Module** — Add / View / Edit / Delete your own lost item reports
- **Found Item Module** — Add a found item, view all found items reported by anyone
- **Search** — Search across lost and found items by item name and/or category
- **Dashboard** — Total lost items, total found items, and your own total posts
- **Responsive UI** — Built with Bootstrap 5, works on mobile and desktop
- **Form validation** — Both client-side (Bootstrap) and server-side
- **Flash messages** — Clear success / error feedback on every action

---

## Technology Stack

| Layer      | Technology                          |
|------------|--------------------------------------|
| Backend    | Python 3, Flask                      |
| Database   | SQLite, accessed via Flask-SQLAlchemy|
| Frontend   | HTML5, CSS3, Bootstrap 5, JavaScript |
| Auth       | Flask sessions + Werkzeug password hashing |

---

## Project Structure

```
lost-found-portal/
│
├── app.py                  # Application entry point (app factory, blueprints)
├── extensions.py           # Shared SQLAlchemy `db` instance
├── requirements.txt        # Python dependencies
├── README.md
├── database.db             # Created automatically on first run (SQLite)
│
├── templates/               # Jinja2 HTML templates
│   ├── base.html            # Layout: navbar, flash messages, footer
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_lost.html
│   ├── add_found.html
│   ├── edit_lost.html
│   ├── view_lost.html
│   ├── view_found.html
│   ├── search_results.html
│   ├── _item_form_fields.html  # Shared partial for item forms
│   ├── 404.html
│   └── 403.html
│
├── static/
│   ├── css/style.css        # Custom theme (on top of Bootstrap 5)
│   ├── js/script.js         # Form validation, delete confirmation, alerts
│   └── images/
│
├── models/                  # SQLAlchemy models
│   ├── __init__.py          # Re-exports db + models
│   ├── user.py               # User table
│   ├── lost_item.py          # LostItems table
│   └── found_item.py         # FoundItems table
│
├── routes/                  # Flask Blueprints (one file per feature)
│   ├── __init__.py
│   ├── auth.py                # Register / Login / Logout
│   ├── lost.py                 # Lost item CRUD
│   ├── found.py                # Found item add/view
│   ├── dashboard.py            # Dashboard stats
│   └── search.py               # Search
│
└── utils/                   # Small helper modules
    ├── __init__.py
    ├── decorators.py          # @login_required
    └── validators.py          # Server-side form validation helpers
```

---

## Database Schema

**Users**
| Column   | Type         |
|----------|--------------|
| id       | Integer (PK) |
| username | String, unique |
| email    | String, unique |
| password | String (hashed) |

**LostItems**
| Column      | Type |
|-------------|------|
| id          | Integer (PK) |
| user_id     | Integer (FK -> Users.id) |
| item_name   | String |
| category    | String |
| description | Text |
| location    | String |
| date        | Date |
| contact     | String |

**FoundItems**
| Column      | Type |
|-------------|------|
| id          | Integer (PK) |
| user_id     | Integer (FK -> Users.id) |
| item_name   | String |
| category    | String |
| description | Text |
| location    | String |
| date        | Date |
| contact     | String |

---

## Setup & Installation

### 1. Prerequisites
- Python 3.9 or newer installed on your machine
- `pip` (comes with Python)

### 2. Get the project
```bash
git clone <your-repository-url>
cd lost-found-portal
```
(or simply download/extract the project folder)

### 3. Create a virtual environment (recommended)
```bash
python -m venv venv

# Activate it:
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the application
```bash
python app.py
```

The app will start at **http://127.0.0.1:5000**. On the very first
run, `database.db` (SQLite) is created automatically along with all
required tables — no manual database setup needed.

### 6. Using the app
1. Open the site and click **Register** to create an account.
2. **Login** with your new credentials.
3. Use the navbar dropdown to **Report Lost Item** or **Report Found Item**.
4. View your lost items under **My Lost Items** (edit/delete available there).
5. View everyone's found items under **Found Items**.
6. Use **Search** to look for an item by name or category.
7. Check your **Dashboard** for stats on lost/found counts and your total posts.

---

## Notes for Evaluators / Developers

- The project follows Flask's **application factory** pattern (`create_app()` in `app.py`) and organizes routes into **Blueprints**, keeping each module (auth, lost items, found items, dashboard, search) in its own file — this is the modular structure requested for the mini project.
- Passwords are hashed using `werkzeug.security.generate_password_hash` — plain-text passwords are never stored.
- All forms are validated on both the client (HTML5 + Bootstrap `needs-validation`) and the server (`utils/validators.py`), and every action shows a flash message (success/error).
- Only the user who created a lost item can edit or delete it (`utils/decorators.py` + ownership checks in `routes/lost.py`), returning a 403 page otherwise.
- To reset the database, simply stop the server and delete `database.db`; it will be recreated automatically the next time you run `python app.py`.

---

## Possible Future Enhancements

- Image upload for lost/found items
- Email notifications when a matching item is posted
- Admin panel to moderate/resolve reports
- Mark an item as "Resolved/Returned"
- Pagination for large item lists

---

## License

This project was created for academic purposes as part of a BSc
Computer Science Semester 5 Mini Project. Free to use and modify for
learning purposes.
