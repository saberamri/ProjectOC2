import pandas as pd
import wget
import csv

from books.bookinf import export_data
from books.nextlinks import next_load
from books.catload import href_load

def main():
    """find all books urls from a category link"""

    url = "http://books.toscrape.com/catalogue/category/books_1/index.html"
    cat = href_load(url)
    result = []

    for lim in cat[:]:
        obj = next_load(lim)
        for lm in obj:
            li = export_data(lm)
            result.append(li)
            print(result)
    

    """export all category data in a single csv and all books images. 
    """
    clst = result[0].keys()
    with open('export/All.csv', 'w', newline='') as data_output:
        csv_output = csv.DictWriter(data_output, fieldnames = clst, delimiter=';')
        csv_output.writeheader()
        for row in result:
            image_filename = wget.download(row["image_url"], out = "export/images")
            print('Image Successfully Downloaded: ', image_filename)
        csv_output.writerows(result)


    """export all category data each category in a csv file
    """
    df_from_dict = pd.DataFrame.from_dict(result)
    df_grouped = df_from_dict.groupby("category")
    for k, gr in df_grouped:
        gr.to_csv('export/{}.csv'.format(k), sep=';', index=False, encoding='utf-8-sig')


if __name__ == "__main__":
    main()
