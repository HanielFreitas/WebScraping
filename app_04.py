import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def fetch_page():
    #PREÇO DE UMA TV
    url = "https://www.mercadolivre.com.br/smart-tv-dled-32-hd-multi-essencial-roku-wi-fi/p/MLB46561061?pdp_filters=item_id%3AMLB5304821036#polycard_client=offers&wid=MLB5304821036&sid=offers&deal_print_id=dc8922be-8b16-4a90-a847-dee00a89cc0c&tracking_id=20546646-3073-4c35-b13f-8ea48eb2c9ef&position=1"
    response = requests.get(url)
    return response.text

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find('h1',class_='ui-pdp-title').get_text()
    prices = soup.find_all('span', class_='andes-money-amount__fraction')
    old_price: int = int(prices[0].get_text().replace('.', '').replace(',', ''))
    new_price: int = int(prices[1].get_text().replace('.', '').replace(',', ''))
    installments_price: int = int(prices[2].get_text().replace('.', '').replace(',', ''))
    
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

    return {
        'product_name': product_name,
        'old_price': old_price,
        'new_price': new_price,
        'installments_price': installments_price,
        'timestamp': timestamp
    }

def save_to_dataframe(product_info,df):
    new_row = pd.DataFrame([product_info])
    df = pd.concat([df,new_row], ignore_index=True)
    return df

if __name__ == "__main__":

    df = pd.DataFrame()

    while True:
        page_content = fetch_page()
        product_info = parse_page(page_content)
        df = save_to_dataframe(product_info,df)
        print(df)
        time.sleep(10)
