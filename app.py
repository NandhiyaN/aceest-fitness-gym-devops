from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from functools import wraps

app = Flask(__name__)
app.config["SECRET_KEY"] = "aceest-devops-assignment-key"
DB_NAME = "aceest_fitness.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            age INTEGER,
            height REAL,
            weight REAL,
            program TEXT,
            membership_status TEXT,
            membership_end TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT NOT NULL,
            workout_date TEXT NOT NULL,
            workout_type TEXT NOT NULL,
            duration INTEGER,
            notes TEXT
        )
    """)

    existing_user = cursor.execute(
        "SELECT username FROM users WHERE username = ?",
        ("admin@aceest.com",)
    ).fetchone()

    if not existing_user:
        cursor.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            ("admin@aceest.com", "Admin@123", "Admin")
        )

    conn.commit()
    conn.close()


def login_required(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("login"))
        return route_function(*args, **kwargs)
    return wrapper


@app.route("/")
def home():
    if "username" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        conn = get_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        ).fetchone()
        conn.close()

        if user:
            session["username"] = user["username"]
            session["role"] = user["role"]
            flash("Login successful.", "success")
            return redirect(url_for("dashboard"))

        flash("Invalid username or password.", "error")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/dashboard")
@login_required
def dashboard():
    conn = get_connection()
    client_count = conn.execute("SELECT COUNT(*) AS total FROM clients").fetchone()["total"]
    conn.close()

    return render_template(
        "dashboard.html",
        username=session.get("username"),
        role=session.get("role"),
        client_count=client_count
    )


@app.route("/clients")
@login_required
def clients():
    conn = get_connection()
    client_list = conn.execute(
        "SELECT * FROM clients ORDER BY name"
    ).fetchall()
    conn.close()

    return render_template("clients.html", clients=client_list)


@app.route("/clients/add", methods=["GET", "POST"])
@login_required
def add_client():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        age = request.form.get("age", "").strip()
        height = request.form.get("height", "").strip()
        weight = request.form.get("weight", "").strip()
        membership_status = request.form.get("membership_status", "").strip()
        membership_end = request.form.get("membership_end", "").strip()

        if not name:
            flash("Client name is required.", "error")
            return redirect(url_for("add_client"))

        conn = get_connection()
        try:
            conn.execute("""
                INSERT INTO clients (name, age, height, weight, membership_status, membership_end)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                name,
                age if age else None,
                height if height else None,
                weight if weight else None,
                membership_status if membership_status else None,
                membership_end if membership_end else None
            ))
            conn.commit()
            flash("Client added successfully.", "success")
        except sqlite3.IntegrityError:
            flash("Client already exists.", "error")
        finally:
            conn.close()

        return redirect(url_for("clients"))

    return render_template("add_client.html")


@app.route("/logout")
@login_required
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("login"))


@app.route("/health")
def health():
    return {"status": "UP", "application": "ACEest Fitness & Gym Management"}


if __name__ == "__main__":
    initialize_database()
    app.run(host="0.0.0.0", port=5000, debug=True)