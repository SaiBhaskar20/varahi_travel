from flask import Flask, render_template, request
import psycopg2
import math
import os
app = Flask(__name__)

# LOCAL PostgreSQL connection
conn = psycopg2.connect(
    dbname=os.environ.get("DB_NAME"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    host=os.environ.get("DB_HOST"),
    port=os.environ.get("DB_PORT")
)
cur = conn.cursor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/book", methods=["GET", "POST"])
def book():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        arrival_time = request.form["arrival_time"]
        members = int(request.form["members"])

        trips = math.ceil(members / 2)
        total_cost = trips * 25

        cur.execute("""
            INSERT INTO bookings (name, phone, arrival_time, members, trips, total_cost)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, phone, arrival_time, members, trips, total_cost))
        conn.commit()

        booking = {
            "name": name,
            "phone": phone,
            "arrival_time": arrival_time,
            "members": members,
            "trips": trips,
            "total_cost": total_cost
        }

        return render_template("confirmation.html", booking=booking)

    # 👇 GET request (NO booking here)
    return render_template("book.html")



@app.route("/admin")
def admin():
    cur.execute("SELECT * FROM bookings ORDER BY created_at DESC")
    bookings = cur.fetchall()
    return render_template("admin.html", bookings=bookings)

if __name__ == "__main__":
    app.run(debug=True)
