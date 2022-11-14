from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd

companies = ['Apple', 
             'Microsoft', 
             'Google', 
             'Amazon',
             'Berkshire Hathaway',
             'Tesla',
             'United Health',
             'Exxon Mobil',
             'Johnson & Johnson',
             'Visa',
             'NVIDIA',
             'JPMorgan Chase',
             'Walmart',
             'Chevron',
             'Eli Lilly'
             'Procter & Gamble',
             'Mastercard',
             'Home Depot',
             'Bank of America',
             'Meta']

start_date = '11/1/2021'
end_date = '11/31/2021'
# googlenews = GoogleNews(start=start_date, end=end_date, lang='en', region='US')
googlenews = GoogleNews(period='1month', lang='en', region='US')

def clean_results(res, name, keys):
    for d in res:
        d['text'] = d['title']+'. '+d['desc']
        d['query'] = name
        d['source'] = 'googlenews'
        d['date'] = [d['date'], d['datetime']]
        for k in keys:
            del d[k]
    return res

data = []
del_keys = ['media', 'link', 'img', 'datetime', 'title', 'desc']
# for name in companies:
#     print(f"Searching for '{name}' query")
#     googlenews.search(name)
#     for i in range(10):
#         print(f"Page No{i+1}")
#         result = googlenews.page_at(i+1)
#         data.extend(clean_results(result, 'Apple', del_keys))
#     googlenews.clear()

# df = pd.DataFrame(data)
# df.to_excel('news.xlsx')
# df.to_csv(index=False)