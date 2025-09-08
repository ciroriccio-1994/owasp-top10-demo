# idor_example_fixed.py
# Fixed Insecure Direct Object Reference (IDOR) demo with access control

from flask import Flask, request

app = Flask(__name__)

# Fake "database"
users = {
    "1": {"id": 1, "name": "Alice", "email": "alice@example.com"},
    "2": {"id": 2, "name": "Bob", "email": "bob@example.com"},
}

# Fake session (simulating "Alice" logged in)
current_user_id = "1"

@app.route("/profile")
def profile():
    user_id = request.args.get("id")

    # Secure: only allow access to the current user's own profile
    if user_id == current_user_id and user_id in users:
        return users[user_id]
    return {"error": "Unauthorized"}, 403

if __name__ == "__main__":
    app.run(debug=True)
