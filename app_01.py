import requests

def fetch_page(url):
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    #PREÇO DE UM TABLETE
    url = "https://shopee.com.br/Rel%C3%B3gio-Com-Cord%C3%A3o-De-Folhas-Rel%C3%B3gios-Femininos-Pulseiras-Com-Diamantes-i.1025667949.23892777482"
    page_content = fetch_page(url)
    print(page_content)