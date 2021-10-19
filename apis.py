import requests

# The api keys in this code are publicly available and free, available from
# alphavantage.co/query and newsapi.org and have therefore not been redacted

# alphavantage.co API---------------------
AV_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_NAME = "Tesla"
STICK_SYMBOL = "TSLA"


alphavantage_stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STICK_SYMBOL,
    "apikey": "ZVV5B9A4FZ6WDIQA",
}

av_response = requests.get(AV_ENDPOINT, params=alphavantage_stock_params)

av_response.raise_for_status()
stock_price = av_response.json()
yday_close_data = stock_price["Time Series (Daily)"]
# turning data to list to avoid hardcoded dates:
yday_close_data_list = [value for (key, value) in yday_close_data.items()]
yday_data = yday_close_data_list[0]
yday_closing_price = yday_data['4. close']

day_before_data = yday_close_data_list[1]
day_before_closing_price = day_before_data['4. close']



# ----------------------------------------


# newsapi.org API
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

newsapi_params = {
    "qInTitle": STICK_SYMBOL,
    "sortBy": "publishedAt",
    "apiKey": "2309c90d0e6a481590fed6cbc6c9da15"
    }

news_response = requests.get(NEWS_ENDPOINT, params=newsapi_params)
articles = news_response.json()['articles']
article_one = articles[0]['title'], articles[0][f'url']
article_two = articles[1]['title'], articles[1][f'url']
article_three = articles[2]['title'], articles[2]['url']

#------------------------
