# xss_example_fixed.py
# Fixed Cross-Site Scripting (XSS) demo using Flask + escape()

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def home():
    # Secure: escaping user input prevents XSS
    name = request.args.get("name", "guest")
    return f"<h1>Hello {escape(name)}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
