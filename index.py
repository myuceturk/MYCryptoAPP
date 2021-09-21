"""import requests
from bs4 import BeautifulSoup

html = requests.get("https://coinmarketcap.com/")

soup = BeautifulSoup(html.content)

tagBtc = soup.findAll("a",{"href":"/currencies/bitcoin/markets/"})

for btc in tagBtc:
    yaziBtc = btc.text
    print(yaziBtc)"""

from flask import Flask, render_template,redirect,url_for
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

app = Flask(__name__)
app.secret_key = "ccappKey"   

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
headers = {
'Accepts': 'application/json',
'X-CMC_PRO_API_KEY': '07a1656e-a5e3-4229-a864-7b7de02c72b1',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url)
    data = json.loads(response.text)
    print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)   

@app.template_filter()
def currencyFormat(value):
    value = float(value)
    return "$ {:,.2f}".format(value)

@app.route("/")
def index():
    return render_template("index.html", data = data)     


if __name__ == "__main__":
    app.run(debug=True)    