import tweepy
import datetime
api_key = "ENW9TBrKZ0iKYCb2dI0Ps6ebh"
api_secret_key = "UjggX3y0t3yfEtkvKpFLH5FtLEF1d0WMHwsvDIDEQN8ja7R85C"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAO8hjQEAAAAAZCNfPEW5vnhPdIv8%2F%2Fa2mCl3D8w%3D3Wbj4uQvXs4uFnCxwMd3YV1wznVAspi1R2lUx6OBmwk2XLUAZW"

access_token = "1591903520805961728-qDdU56zonWnFvwJ1rGUmg4WD3iVp8x"
access_token_secret = "uThL1Jm06bd7aEbxRrAZ7p0MlH682GzN0FbObzdROfBQE"


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
    print ("(stock #" + stock_name + ") OR (stock " + company + ") lang:en -is:retweet -links -https")
    responses.append(client.search_recent_tweets("(stock #" + stock_name + ") OR (stock " + company + ") lang:en -is:retweet -links -https", max_results=10))

for response in responses:
    tweets = response.data
    for tweet in tweets:
        print(tweet.text)
    