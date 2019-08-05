import feedparser
import requests

result = requests.get('https://www.toutless.com/app.php/feed').text

d = feedparser.parse(result)

for entry in d.entries:
  print(entry.id)