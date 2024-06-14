import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_page(url):
    response=requests.get(url)
    if response.status_code==200:
        return response.content
    else:
        raise Exception (f"Failed to fetch page:{url}")
def parse_product(product) :
    title=product.find("a",class_="title").text.strip()
    description=product.find("p",class_="description").text.strip()
    price=product.find("h4",class_="price").text.strip()
    return {
        "title":title,
        "description":description,
        "price":price
    }
    
def scrape(url):
    page_content=fetch_page(url)
    soup=BeautifulSoup(page_content,"html.parser")
    products=soup.find_all("div", class_="thumbnail")   
    
    products_data=[]
    for product in products:
        product_info=parse_product(product)
        products_data.append(product_info)
        
    print(products_data)
    return pd.DataFrame(products_data)

base_url="https://webscraper.io/test-sites/e-commerce/allinone"

df=scrape(base_url)

print(df)

df.to_csv("../data/raw/products1.csv", index=False, mode='a', header=False)  
    