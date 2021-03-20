from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup as BS
from scraper import get_trending_coin_data

app = Flask("__init__")


@app.route("/")
def home():
    return "<h1>Hello world</h1>"


@app.route("/trending-coin")
def trending_coin():

    trending_coin_data = get_trending_coin_data()

    return jsonify({
        "trending": trending_coin_data
    })


if __name__ == "__main__":
    app.run(debug=True)
