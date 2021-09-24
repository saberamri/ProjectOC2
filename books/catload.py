from io import BytesIO
from lxml import etree
import requests
from urllib.parse import urljoin


def href_load(url):
    """trouver tous les liens des catégories dans une page"""
    
    response = requests.get(url)
    if response.ok:
        tree = etree.parse(BytesIO(response.content), etree.HTMLParser())
        cat = tree.xpath("//div[@class= 'side_categories']/ul/li/ul/li/a")
        links = []
        for elem in list(cat):
            li = urljoin(url, elem.get("href"))
            links.append(li)
    return links


if __name__ == "__main__":

    url = "http://books.toscrape.com/catalogue/category/books_1/index.html"
    cat = href_load(url)
    print(cat)
