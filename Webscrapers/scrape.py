from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import pandas as pd

new_world = "https://www.newworld.co.nz/shop/category/fresh-foods-and-bakery?pg=2"

def source_html(url):
    dr = webdriver.Chrome()
    dr.get(url)
    return dr.page_source

source = source_html(new_world)

soup = BeautifulSoup(source, 'lxml')

csv_file = open('scrape_data.csv','w', newline='') 

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'dollars','cents'])


for match in soup.find_all('div', class_="_1afq4wy0"):

    title = match.find('p', class_='_1afq4wy7 w6tzb3l w6tzb31r').text.strip()
    dollars = match.find('p', class_='whm0tf1 _1xxz4ve0 _1xxz4ve2').text.strip()
    cents = match.find('p', class_='whm0tf3 _1xxz4ve4 _1xxz4ve6').text.strip()

    price = int(dollars + cents) / 100

    img = match.find('img', class_='_14gbuuw2')
    img_src = img['src']

    link_a = match.find('a', class_="_1afq4wy2")
    link_to_product = link_a['href']

    csv_writer.writerow([title, dollars, cents] )

    # print(f"Product Name: {title}\n Price: ${dollars}.{cents} ({price})\n Image Source: {img_src}\n Link to Find: {link_to_product}")

csv_file.close()

reader = csv.DictReader(open('scrape_data.csv'))
for row in reader:
    print(row)