from flask import Flask, render_template, request, redirect, session
from cs50 import SQL
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = "this-is-a-random-secret-key-change-me"
db = SQL("sqlite:///planner.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user_id" not in session:
       return redirect("/login")
    if request.method == "POST":
       task = request.form.get("task")
       db.execute(
           "INSERT INTO tasks (user_id, task) VALUES (?, ?)",
           session["user_id"],
           task
        )
    tasks = db.execute(
           "SELECT * FROM tasks WHERE user_id = ?",
           session["user_id"]
    )
    return render_template("dashboard.html", tasks=tasks)

@app.route("/add")
def add():
    return render_template("add-task.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        rows = db.execute(
        "SELECT * FROM users WHERE username = ?",
             username
        )
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
           return "Invalid username or password"
        
        session["user_id"] = rows[0]["id"]
        return redirect("/dashboard")

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        pw_hash = generate_password_hash(password)

        db.execute(
            "INSERT INTO users (username, email, hash) VALUES (?, ?, ?)",
             username,
             email,
             pw_hash
      )
        return "Registered Successfully"
    return render_template("register.html")

@app.route("/delete", methods=["POST"])
def delete():
    task_id = request.form.get("id")

    db.execute(
        "DELETE FROM tasks WHERE id = ?",
        task_id
    )

    return redirect("/dashboard")

if __name__ == "__main__":
    app.run(debug=True)
    app.secret_key = "change_this_to_a_random_secret_key"