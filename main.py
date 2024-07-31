from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import csv
import pandas as pd

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'INR'
}

with open('api.json') as f:
    config = json.load(f)
api_key = config['api_key']

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': api_key,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)

  # print(data)
  df = pd.DataFrame(data['data'])
  df.to_csv('coinmarketcap_data.csv', index=False)

  with open('coinmarketcap_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    print(f"Row 17: {reader[1][17]}")
    # for row in reader:
      
      # if row[17]:  # Check if the 18th column is not empty
      #   try:
      #     json_data = json.loads(row[17])
      #     price = json_data.get('INR', {}).get('price')
      #     if price:
      #       print(f"Bitcoin price in INR: {price}")
      #     else:
      #       print("Price not found")
      #   except json.JSONDecodeError:
      #     print("Invalid JSON data")
      # else:
      #   print("No JSON data found in this row")

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)