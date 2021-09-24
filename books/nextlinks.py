#! /usr/bin/env python3
# coding: utf-8

from urllib.parse import urljoin
from io import BytesIO
from lxml import etree
import requests

from books.bookurl import data_cat


def next_links(url):
    """Cette fonction affiche le lien de la page next suivante"""

    response = requests.get(url)
    if response.ok:
        tree = etree.parse(BytesIO(response.content), etree.HTMLParser())
        next = tree.xpath("//li[@class= 'next']/a")
        if len(next) > 0:
            next = urljoin(url, next[0].get("href"))
        else:
            next = None
    return(next)


def next_load(url):
    links = []
    
    """Cette fonction donne tous les liens des livres à partir d'une catégorie"""
    while url is not None:
        links.extend(data_cat(url))
        url = next_links(url)
    return(links)


if __name__ == "__main__":
    url = "http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
    object = next_load(url)
    print(object)