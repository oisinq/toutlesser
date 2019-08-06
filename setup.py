import feedparser
import requests
import time
import pync
import random

idSet = set()
count = 1

while True:
  print(f"Request No.{count}...")
  result = requests.get('https://www.toutless.com/app.php/feed').text
  d = feedparser.parse(result)

  for entry in d.entries:
    if 'Electric Picnic' in entry.title and ':forsale:' in entry.content[0].value and not entry.id in idSet:
      print(entry.content)
      idSet.add(entry.id)
      print("New one: ")
      print(entry.id)
      pync.notify('EP ticket found!', open=entry.id)
    else:
      print("nope...")
  
  count += 1
  time.sleep(random.uniform(55, 65))