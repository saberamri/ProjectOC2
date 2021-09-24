#! /usr/bin/env python3
# coding: utf-8

"""trouver tous les url des livres à partir d'un lien de catégorie"""

import pandas as pd
import wget


from books.bookinf import export_data
from books.nextlinks import next_load
from books.catload import href_load
from books.bookurl import data_cat


url = "http://books.toscrape.com/catalogue/category/books_1/index.html"
cat = href_load(url)
result = []

for lim in cat[:]:
    obj = next_load(lim)

    for lm in obj:
        li = export_data(lm)
        result.append(li)
        print(result)

"""export data
"""
df_from_dict = pd.DataFrame.from_dict(result)
df_grouped = df_from_dict.groupby("category")
for k, gr in df_grouped:
    gr.to_csv('export/{}.csv'.format(k), sep=';', index=False)

"""
export images
"""
for elem in result:
    image_filename = wget.download(elem["image_url"])
    print('Image Successfully Downloaded', image_filename)