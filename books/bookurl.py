#! /usr/bin/env python3
# coding: utf-8

"""
trouver tous les url des livres de lien actuel à partir d'un lien de catégorie
"""
from urllib.parse import urljoin
from io import BytesIO
from lxml import etree
import requests


def data_cat(url):
    response = requests.get(url) 
    if response.ok:
        tree = etree.parse(BytesIO(response.content), etree.HTMLParser())
        product_page_url = tree.xpath("//article[@class= 'product_pod']/h3/a")
        links = []
        for elem in list(product_page_url):
            li = urljoin(url, elem.get("href"))
            links.append(li)
    return(links)


if __name__ == "__main__":
    url = "http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-4.html"
    object = data_cat(url)
    print(object)
