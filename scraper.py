from bs4 import BeautifulSoup as BS
import requests


def check_for_negative(element_style, number):

    if "down-color" in element_style:
        return -abs(number)
    else:
        return number


def get_trending_coin_data():
    url = "https://coinmarketcap.com/trending-cryptocurrencies/"
    response = requests.get(url)
    soup = BS(response.content, "html.parser")
    rows = soup.select("tbody tr")

    data = []

    for row in rows:
        name = row.select('td p')[1].text
        symbol = row.select_one('.coin-item-symbol').text
        price = float(row.select('td')[3].text.replace(
            "$", "").replace("<", "").replace(",", ""))

        change_in_24h_styles = row.select(
            'td')[4].select_one("span").get("style")

        change_in_24h = float(row.select(
            'td')[4].text.replace("%", "").replace(",", ""))

        change_in_24h = check_for_negative(change_in_24h_styles, change_in_24h)

        change_in_7d_styles = row.select(
            'td')[5].select_one("span").get("style")

        change_in_7d = float(row.select(
            'td')[5].text.replace("%", "").replace(",", ""))

        change_in_7d = check_for_negative(change_in_7d_styles, change_in_7d)
        market_cap = row.select('td')[7].text.replace(
            ",", "").replace("$", "").replace("--", "").replace(",", "")
        market_cap = float(market_cap) if market_cap else ""
        volume = float(row.select('td')[8].text.replace(
            ",", "").replace("$", "").replace(",", ""))

        d = {
            "name": name,
            "symbol": symbol,
            "price": price,
            "24h": change_in_24h,
            "7d": change_in_7d,
            "market_cap": market_cap,
            "volume": volume
        }

        print(d)
        data.append(d)

    return data
