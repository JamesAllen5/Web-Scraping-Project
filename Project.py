from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


webpage = 'https://coinmarketcap.com/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)

table_rows = soup.findAll("tr")

for row in table_rows[1:5]:
    td=row.findAll("td")

    name=td[2].text
    current_price=int(td[3].text.replace(',',''))
    percent_change=int(td[9].text.replace(',',''))
    old_price=current_price/percent_change

    print(f"Name:{name}")
    print(f"Current Price:{current_price}")
    print(f"Percent Change:{percent_change}")
    print(f"Yesterdays Price::{old_price}")
