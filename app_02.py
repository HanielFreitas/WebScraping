import requests
from bs4 import BeautifulSoup

def fetch_page():
    url = "https://www.mercadolivre.com.br/tablet-samsung-galaxy-tab-s6-lite-wi-fi-64gb-4gb-ram-tela-104-cinza-sm-p620nzadzto/p/MLB35330751?pdp_filters=deal%3AMLB779362-1#polycard_client=homes-korribanSearchTodayPromotions&searchVariation=MLB35330751&wid=MLB5041324376&position=2&search_layout=grid&type=product&tracking_id=dbdb5e2f-1cb8-435a-bc41-35ada47761b7&sid=search&c_id=/home/today-promotions-recommendations/element&c_uid=c7b15147-6bc7-4505-8e0d-932441e11765"
    response = requests.get(url)
    return response.text

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find('h1',class_='ui-pdp-title').get_text()
    prices = soup.find_all('span', class_='andes-money-amount__fraction')
    old_price: int = int(prices[0].get_text().replace('.', '').replace(',', ''))
    new_price: int = int(prices[1].get_text().replace('.', '').replace(',', ''))
    installments_price: int = int(prices[2].get_text().replace('.', '').replace(',', ''))
    
    return {
        'product_name': product_name,
        'old_price': old_price,
        'new_price': new_price,
        'installments_price': installments_price
    }

if __name__ == "__main__":
    page_content = fetch_page()
    product_info = parse_page(page_content)
    print(product_info)
