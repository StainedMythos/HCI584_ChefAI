
import sqlite3
from flask import current_app, g

def get_db():
    """
    Get a database connection.
    """
    if 'db' not in g:
        # Connect to the SQLite database
        g.db = sqlite3.connect(
            'database.db',
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # Return rows as dictionaries
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    """
    Close the database connection.
    """
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db(app):
    """
    Initialize the database with the application context.
    """
    with app.app_context():
        db = get_db()
        with current_app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8'))
    # Register the close_db function to be called when the app context ends
    app.teardown_appcontext(close_db)
