from lxml import html
import requests


url = "https://boardgamegeek.com"
data = requests.get(url)
page = html.fromstring(data.text)
xpath = '//*[@class="media-module__body relative"]//h2//a'
foundElements = page.xpath(xpath)
print(foundElements)
for element in foundElements :

   #print(element.tag, element.keys())
   for name, value in sorted(element.items()):
       print('%r' % (value))