import tweepy
import datetime
import time
consumer_key = "imwrWfsSa6ClKDtco1m5aamlL"
consumer_secret = "Ee1l74nk8Sx9a3lgYRGRtIMsA9w9CJp6UWS5o5Hujaktb9FUgh"
bearer_token = "AAAAAAAAAAAAAAAAAAAAANxGjQEAAAAAJRz42cJaTM0Vjftlj5qBXZbFUoQ%3Ds6sj59WRac4zF8fAn973cVazbok2TMSfcsryTIfBXVF4NERfXg"

access_token = "1591903520805961728-idXQZQJ5ETnqmTxG1MrKepmW1pWT5Z"
access_token_secret = "oaa6utpuNwrTFfryWg2M5BQvrSN3FoKxa3XxfqIC7Z1nB"

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

# api = tweepy.API(auth)
client = tweepy.Client(bearer_token=bearer_token)

companies = ['Apple', 
             'Microsoft', 
             'Google', 
             'Amazon',
             'Berkshire Hathaway',
             'Tesla',
             '\"United Health\"',
             '"Exxon Mobil"',
             '\"Johnson & Johnson\"',
             'Visa',
             'NVIDIA',
             '\"JPMorgan Chase\"',
             'Walmart',
             'Chevron',
             '\"Eli Lilly\"'
             '\"Procter & Gamble\"',
             'Mastercard',
             '\"Home Depot\"',
             '\"Bank of America\"',
             'Meta']

stock_names = ["AAPL",
                "MSFT",
                "GOOG",
                "AMZN",
                "BRK-B",
                "TSLA",
                "UNH",
                "XOM",
                "JNJ",
                "V",
                "NVDA",
                "JPM",
                "WMT",
                "CVX",
                "LLY",
                "PG",
                "MA",
                "HD",
                "BAC",
                "META"]

responses = []
for company, stock_name in zip(companies, stock_names):
    time.sleep(2)
    print ("(stock #" + stock_name + ") OR (stock " + company + ") lang:en -is:retweet -links -https")
    responses.append(client.search_all_tweets("(stock #" + stock_name + ") OR (stock " + company + ") lang:en -is:retweet -links -https", max_results=10))

for response in responses:
    tweets = response.data
    for tweet in tweets:
        print(tweet.text)
    