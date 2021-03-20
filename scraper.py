from bs4 import BeautifulSoup as BS
import requests


def get_trending_coin_data():
    url = "https://coinmarketcap.com/trending-cryptocurrencies/"
    response = requests.get(url)
    soup = BS(response.content, "html.parser")
    rows = soup.select("tbody tr")

    data = []

    for row in rows:
        name = row.select('td p')[1].text
        price = float(row.select('td')[3].text.replace("$", ""))
        change_in_24h = float(row.select('td')[4].text.replace("%", ""))
        change_in_7d = float(row.select('td')[5].text.replace("%", ""))
        market_cap = row.select('td')[7].text.replace(
            ",", "").replace("$", "").replace("--", "")
        market_cap = float(market_cap) if market_cap else ""
        volume = float(row.select('td')[8].text.replace(
            ",", "").replace("$", ""))

        d = {
            "name": name,
            "price": price,
            "24h": change_in_24h,
            "7d": change_in_7d,
            "market_cap": market_cap,
            "volume": volume
        }

        print(d)
        data.append(d)

    return data
