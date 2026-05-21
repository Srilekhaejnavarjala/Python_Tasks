# ============================================================
# Import Required Modules
# ============================================================
from flask import Flask, render_template, request, redirect

# ============================================================
# Create Flask Application
# ============================================================
app = Flask(__name__)

# ============================================================
# Temporary TODO Storage
# ============================================================
tasks = [
    {
        "id": 1,
        "title": "Complete Flask Project",
        "status": "Pending"
    },
    {
        "id": 2,
        "title": "Practice CRUD Operations",
        "status": "Completed"
    }
]

# ============================================================
# Home Route
# ============================================================
@app.route("/")
def home():

    return render_template("home.html")


# ============================================================
# Add Task Page
# ============================================================
@app.route("/add-task")
def add_task_page():

    return render_template(
        "add_task.html",
        tasks=tasks
    )


# ============================================================
# Dashboard Page
# ============================================================
@app.route("/dashboard")
def dashboard():

    total_tasks = len(tasks)

    completed_tasks = len([
        task for task in tasks
        if task["status"] == "Completed"
    ])

    pending_tasks = len([
        task for task in tasks
        if task["status"] == "Pending"
    ])

    return render_template(
        "dashboard.html",
        total=total_tasks,
        completed=completed_tasks,
        pending=pending_tasks
    )


# ============================================================
# Add Task Logic
# ============================================================
@app.route("/add", methods=["POST"])
def add_task():

    title = request.form.get("title")

    if title:

        new_task = {
            "id": len(tasks) + 1,
            "title": title,
            "status": "Pending"
        }

        tasks.append(new_task)

    return redirect("/add-task")


# ============================================================
# Update Task Logic
# ============================================================
@app.route("/update/<int:task_id>")
def update_task(task_id):

    for task in tasks:

        if task["id"] == task_id:

            if task["status"] == "Pending":
                task["status"] = "Completed"

            else:
                task["status"] = "Pending"

    return redirect("/add-task")


# ============================================================
# Delete Task Logic
# ============================================================
@app.route("/delete/<int:task_id>")
def delete_task(task_id):

    global tasks

    tasks = [
        task for task in tasks
        if task["id"] != task_id
    ]

    return redirect("/add-task")


# ============================================================
# Run Flask Application
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)