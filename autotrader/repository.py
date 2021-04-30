import requests
import json
import os

def getQuote(symbol):
    url = 'https://api.tdameritrade.com/v1/marketdata/$SPX.X/quotes'
    res = requests.get(url, headers = {'Authorization': 'Bearer {}'.format(os.environ.get("ACCESS_TOKEN"))})

    print(res.status_code, res.content)
    return json.loads(res.content)
    