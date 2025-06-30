from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

def connect_db():
    return psycopg2.connect(os.environ['DATABASE_URL'])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def signup():
    email = request.form["email"]
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO waitlist (email) VALUES (%s);", (email,))
    conn.commit()
    cur.close()
    conn.close()
    return "Thanks for signing up!"
