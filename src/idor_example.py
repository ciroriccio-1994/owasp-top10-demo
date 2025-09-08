# idor_example.py
# Insecure Direct Object Reference (IDOR) demo using Flask

from flask import Flask, request

app = Flask(__name__)

# Fake "database"
users = {
    "1": {"id": 1, "name": "Alice", "email": "alice@example.com"},
    "2": {"id": 2, "name": "Bob", "email": "bob@example.com"},
}

@app.route("/profile")
def profile():
    # ❌ Vulnerable: user can directly request any ID without authorization
    user_id = request.args.get("id")
    if user_id in users:
        return users[user_id]
    return {"error": "User not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)
