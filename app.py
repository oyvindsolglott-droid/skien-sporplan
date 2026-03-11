from flask import Flask, jsonify, send_from_directory
import requests
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__, static_folder=".", static_url_path="")

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/api/balise-vehicles")
def balise():
    # foreløpig testdata
    data = {
        "802": ["75", "75"],
        "804": ["75", "75"],
        "2470": ["69"],
        "2472": ["69"]
    }

    return jsonify({
        "ok": True,
        "updatedAt": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "trains": data
    })

if __name__ == "__main__":
    app.run()
