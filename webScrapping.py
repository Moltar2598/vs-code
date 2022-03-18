from bs4 import BeautifulSoup
import requests
import selenium as sm
import pandas as pd

alibaba_url = "https://federemote.en.alibaba.com/productlist.html?spm=a2700.shop_index.88.17"
response = requests.get(alibaba_url)

soup = BeautifulSoup(response.text,'html.parser')

ul_class = "next-menu-content"
prod_detail = soup.find('ul',attrs={'class':ul_class})

for i in prod_detail:

    a_class = "menu-link"
    prod = i.find('a',attrs={'class':a_class})
    st = str(prod)
    ttl = st.split("<")
    cat = ttl[1].split(">")
    print(cat[1])
/html/body/div[4]/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div/ul
/html/body/div[4]/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div/ul/li[3]
/html/body/div[4]/div[3]/div[2]/div[1]/div[3]/div/div/div[2]/div/ul/li[11]

#print(prod_detail)
#print(soup)