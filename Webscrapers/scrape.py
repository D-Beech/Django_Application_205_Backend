from bs4 import BeautifulSoup
from selenium import webdriver

new_world = "https://www.newworld.co.nz/shop/category/fresh-foods-and-bakery?pg=2"

def source_html(url):
    dr = webdriver.Chrome()
    dr.get(url)
    return dr.page_source

source = source_html(new_world)

soup = BeautifulSoup(source, 'lxml')

# for match in soup.find_all('p', class_='_1afq4wy7 w6tzb3l w6tzb31r'):
#     title = match.text
#     print(title)

for match in soup.find_all('div', class_="_1afq4wy0"):
    title = match.find('p', class_='_1afq4wy7 w6tzb3l w6tzb31r').text
    dollars = match.find('p', class_='whm0tf1 _1xxz4ve0 _1xxz4ve2').text
    cents = match.find('p', class_='whm0tf3 _1xxz4ve4 _1xxz4ve6').text
    print(f"Product Name: {title}\n Price: ${dollars}.{cents}")