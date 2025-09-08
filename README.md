# OWASP Top 10 Demo

This repository contains simple examples of common vulnerabilities from the OWASP Top 10, with insecure code and secure fixes.

## Vulnerabilities Included
- SQL Injection (SQLi)
- Cross-Site Scripting (XSS)
- Insecure Direct Object Reference (IDOR)

## Repository Structure
- src/sql_injection.py: vulnerable SQL query
- src/sql_injection_fixed.py: fixed SQL query (parameterized)
- src/xss_example.py: vulnerable XSS example
- src/xss_example_fixed.py: fixed XSS example (escaped input)
- src/idor_example.py: vulnerable access control
- src/idor_example_fixed.py: fixed access control

## Learning Outcomes
- Identify common application security issues
- Reproduce them in code
- Apply secure coding practices to mitigate risks

---

## SQL Injection (SQLi)

### Files
- src/sql_injection.py: vulnerable version (string concatenation)
- src/sql_injection_fixed.py: fixed version (parameterized query)

### How to Test
python src/sql_injection.py

Input:
Username: alice
Password: ' OR '1'='1 --

Result:
Login bypassed.

---

## Cross-Site Scripting (XSS)

### Files
- src/xss_example.py: vulnerable version (direct render of input)
- src/xss_example_fixed.py: fixed version (escaping user input)

### How to Test
python src/xss_example.py

Visit in browser:
http://127.0.0.1:5000/?name=<script>alert('XSS')</script>

Result:
JavaScript executes in the browser.

---

## Insecure Direct Object Reference (IDOR)

### Files
- src/idor_example.py: vulnerable version (no authorization checks)
- src/idor_example_fixed.py: fixed version (enforces access control)

### How to Test
python src/idor_example.py

Visit in browser:
http://127.0.0.1:5000/profile?id=2

Result:
Even if the logged-in user is ID 1, you can directly access user 2’s data.

## Setup & Run
pip install -r requirements.txt
python src/sql_injection.py
python src/xss_example.py
python src/idor_example.py



