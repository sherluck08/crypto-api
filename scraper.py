from bs4 import BeautifulSoup as BS
import requests
import json
from pprint import pprint


def check_for_negative(element_style, number):

    if "down-color" in element_style:
        return -abs(number)
    else:
        return number


def get_page_source_code(url):

    header = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.3"}
    response = requests.get(url, headers=header)
    soup = BS(response.content, "html.parser")
    return soup


def convert_script_tag_to_json(script_tag):

    data = str(script_tag).replace(
        "</script>", "").replace('<script id="__NEXT_DATA__" type="application/json">', "")
    json_data = json.loads(data)

    return json_data


def get_trending_coin_data():

    url = "https://coinmarketcap.com/trending-cryptocurrencies/"
    soup = get_page_source_code(url)
    script_tag = soup.select_one("script#__NEXT_DATA__")
    json_data = convert_script_tag_to_json(script_tag)
    trending_coins = json_data["props"]["initialState"]["cryptocurrency"]["trendingCoins"]["data"]

    trending_coin_data = []

    for coin in trending_coins:

        name = coin['name']
        symbol = coin['symbol']
        price = coin['priceChange']['price']
        price_change_in_7d = coin['priceChange']['priceChange7d']
        price_change_in_24h = coin['priceChange']['priceChange24h']
        market_cap = coin['marketCap']
        volume_24h = coin['priceChange']['volume24h']

        d = {
            "name": name,
            "symbol": symbol,
            "price": price,
            "price_change_24h": price_change_in_24h,
            "price_change_7d": price_change_in_7d,
            "market_cap": market_cap,
            "volume_24h": volume_24h
        }

        print(d)
        trending_coin_data.append(d)

    return trending_coin_data


def get_top_coins():

    url = "https://coinmarketcap.com/"
    soup = get_page_source_code(url)
    script_tag = soup.select_one("script#__NEXT_DATA__")
    json_data = convert_script_tag_to_json(script_tag)
    top_coins = json_data["props"]["initialState"]["cryptocurrency"]["listingLatest"]["data"]

    top_coin_data = []

    for coin in top_coins:

        name = coin['name']
        symbol = coin['symbol']
        price = coin['quote']['USD']['price']
        change_in_7d = coin['quote']['USD']['percentChange7d']
        change_in_24h = coin['quote']['USD']['percentChange24h']
        market_cap = coin['quote']['USD']['marketCap']
        volume_24h = coin['quote']['USD']['volume24h']

        d = {
            "name": name,
            "symbol": symbol,
            "price": price,
            "change_24h": change_in_24h,
            "change_7d": change_in_7d,
            "market_cap": market_cap,
            "volume_24h": volume_24h
        }

        print(d)
        top_coin_data.append(d)

    return top_coin_data
