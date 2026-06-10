import random
import sqlite3
from flask import Flask, render_template
import os
import pandas as pd
app = Flask(__name__)
_HERE = os.path.dirname(os.path.realpath(__file__))

@app.route('/')
def w209():
    file='about9.jpg'
    return render_template('w209.html',file=file)

@app.route("/map")
def map_page():
    return render_template("map.html")

@app.route("/api")
def api():
    return {"x": random.randint(2,100)}

@app.route("/players/count")
def players_count():
    con = sqlite3.connect("players_20.db")
    cursor = con.cursor()
    cursor.execute("SELECT COUNT(*) FROM players")
    count = cursor.fetchone()[0]
    con.close()
    return {"count": count}

@app.route("/getData/<int:year>")
def getData(year):
    revenue = pd.read_csv(os.path.join(_HERE, "static", "data", "1_Revenues.csv"))
    if year < 1942 or year > 2008:
        return "Error in the year range"
    filtered = revenue[revenue["Year4"] == year][
        ["Name", "Year4", "Total Revenue", "Population (000)"]
    ]
    return filtered.to_json(orient="records")

if __name__ == '__main__':
    app.run()
