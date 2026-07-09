"""
extensions.py
-------------
Flask extensions (like SQLAlchemy) are created here, in a file that
has no dependency on the rest of the app. This is the standard trick
to avoid circular imports:

    app.py        -> imports db from extensions, calls db.init_app(app)
    models/*.py   -> import db from extensions, define db.Model classes
    routes/*.py   -> import db and the models they need

Nobody has to import app.py, so there are no circular import problems.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
