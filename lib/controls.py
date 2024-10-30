import sqlite3

from lib.models import Todo, User


def load_users() -> list[User]:
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    users = [User(*user) for user in users]
    print(users)
    for user in users:
        cursor.execute("SELECT * FROM todos WHERE user_id = ?", (user.identificator,))
        todos = cursor.fetchall()
        user.todos = [Todo(*todo[2:]) for todo in todos]

    conn.close()
    return users


def save_users(users: list[User]):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Update algh to update or avoid dublicates
    cursor.execute("DELETE FROM todos")
    cursor.execute("DELETE FROM users")
    conn.commit()

    for user in users:
        cursor.execute(
            "INSERT INTO users VALUES (?, ?)",
            (user.identificator, user.name),
        )
        conn.commit()
        for todo in user.todos:
            cursor.execute(
                "INSERT INTO todos (user_id, title, description, completed) VALUES (?, ?, ?, ?)",
                (user.identificator, todo.title, todo.description, todo.completed),
            )
            conn.commit()

    conn.close()


def create_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE users (
            identificator TEXT PRIMARY KEY,
            name TEXT
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            title TEXT,
            description TEXT,
            completed  TEXT
        )
        """
    )

    conn.commit()

    conn.close()
