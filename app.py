from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# ── Database setup ──────────────────────────────────────
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registrations (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT    NOT NULL,
            email     TEXT    NOT NULL,
            phone     TEXT    NOT NULL,
            event     TEXT    NOT NULL,
            college   TEXT    NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# ── Routes ───────────────────────────────────────────────
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    full_name = request.form['full_name']
    email     = request.form['email']
    phone     = request.form['phone']
    event     = request.form['event']
    college   = request.form['college']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO registrations (full_name, email, phone, event, college) VALUES (?, ?, ?, ?, ?)',
        (full_name, email, phone, event, college)
    )
    conn.commit()
    conn.close()

    return redirect(url_for('success', name=full_name, event=event))


@app.route('/success')
def success():
    name  = request.args.get('name')
    event = request.args.get('event')
    return render_template('success.html', name=name, event=event)


@app.route('/registrations')
def view_registrations():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM registrations ORDER BY timestamp DESC')
    rows = cursor.fetchall()
    conn.close()
    return render_template('registrations.html', registrations=rows)


# ── Start ────────────────────────────────────────────────
if __name__ == '__main__':
    init_db()
    app.run(debug=True)