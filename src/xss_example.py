# xss_example.py
# Simple Cross-Site Scripting (XSS) demo using Flask

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    # ❌ Vulnerable: directly renders user input without sanitization
    name = request.args.get("name", "guest")
    return f"<h1>Hello {name}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
