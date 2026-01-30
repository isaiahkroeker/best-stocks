import requests, os, json

# The stocks we want to check
symbols = ['AAPL', 'NVDA', 'TSLA', 'MSFT', 'AMZN', 'GOOGL', 'META', 'AMD', 'NFLX']
api_key = os.getenv('FINNHUB_KEY')
results = []

for s in symbols:
    url = f'https://finnhub.io/api/v1/stock/recommendation?symbol={s}&token={api_key}'
    data = requests.get(url).json()
    if data:
        # Score = (Strong Buy * 2) + Buy - Sell
        top = data[0]
        score = (top['strongBuy'] * 2) + top['buy'] - top['sell']
        results.append({"symbol": s, "score": score})

# Sort so the highest score is at the top
results.sort(key=lambda x: x['score'], reverse=True)

with open('data.json', 'w') as f:
    json.dump(results, f)
