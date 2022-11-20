import json
import urllib.request

htmltext = urllib.request.urlopen('http://www.bloomberg.com/markets/watchlist/recent-ticker/AAPL:US')
data = json.load(htmltext)

print(data)