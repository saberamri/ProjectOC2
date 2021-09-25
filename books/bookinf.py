from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


def export_data(url):
    """scrapping a single data  book's from a given url"""
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'lxml')
        dict_rate = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        title = soup.find('h1').get_text()
        UPC = soup.find("th", text='UPC')
        product_type = soup.find("th", text='Product Type')
        price_exc = soup.find("th", text='Price (excl. tax)')
        priceinc = soup.find("th", text='Price (incl. tax)')
        cat = soup.find('ul', {'class': 'breadcrumb'}).find_all('li')
        number_available = soup.find_all('tr')[5].find('td').text
        image_url = soup.find_all('img')[0]
        rate = soup.select_one('.star-rating').attrs.get('class')[1]
        desc = soup.find('article', {'class': 'product_page'}).findAll('p')

        return {
            "product_page_url": url,
            "universal_ product_code (upc)": UPC.next_sibling.text,
            "title": title,
            "product_type": product_type.next_sibling.text,
            "price_excluding_tax": price_exc.next_sibling.text,
            "price_including_tax": priceinc.next_sibling.text,
            "number_available": number_available,
            "Product_Description": str(desc[3].text),
            "category": cat[2].text.strip(),
            "review_rating": dict_rate[rate],
            "image_url": urljoin(url, image_url["src"])
        }


if __name__ == "__main__":
    url = "http://books.toscrape.com/catalogue/a-year-in-provence-provence-1_421/index.html"
    object = export_data(url)
    print(object)
