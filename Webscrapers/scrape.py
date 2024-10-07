from bs4 import BeautifulSoup
from selenium import webdriver

new_world = "https://www.newworld.co.nz/shop/category/fresh-foods-and-bakery?pg=2"

def source_html(url):
    dr = webdriver.Chrome()
    dr.get(url)
    return dr.page_source

source = source_html(new_world)

soup = BeautifulSoup(source, 'lxml')

for match in soup.find_all('p', class_='_1afq4wy7 w6tzb3l w6tzb31r'):
    title = match.text
    print(title)

