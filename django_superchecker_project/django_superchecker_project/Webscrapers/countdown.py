from bs4 import BeautifulSoup
from selenium import webdriver
import csv
from models import Product

woolworths = "https://www.woolworths.co.nz/shop/browse"

categories = ["/fruit-veg",
"/meat-poultry",
"/fish-seafood",
"/fridge-deli",
"/bakery",
"/frozen",
"/pantry",
"/beer-wine",
"/drinks",
"/health-body",
"/household",
"/baby-child",
"/pet"]

#Start of Beautiful Soup House Keeping
def source_html(url):
    dr = webdriver.Chrome()
    dr.get(url)
    return dr.page_source

def cook_soup(url):
    return BeautifulSoup(source_html(url), 'lxml')
#End of Beautiful Soup House Keeping

#This function returns the max for number of pages for a catergory by finding the final a tag value for the page nav
def last_page(soup):
    num = 1
    for match in soup.find_all('a', class_="ng-star-inserted"):
        try:
            num = int(match.text)
        except:
            continue
    return num

def page_number_ranges():
    ranges = []
    for c in categories:
        url = woolworths + c 
        source = source_html(url)
        soup = BeautifulSoup(source, 'lxml')
        max = last_page(soup)
        ranges.append(max)
    return ranges

#This function writes all page urls in csv file
def update_woolworths_urls():
    ranges = page_number_ranges()

    urls_file = open('woolworths_urls.csv','w', newline='')
    csv_writer = csv.writer(urls_file)

    for i in range(len(ranges)):
        for page in range(1, ranges[i]):
            url = woolworths + categories[i] + "?page=" + str(page)
            print(url)
            csv_writer.writerow([url])

    urls_file.close()
#End of url update automation



soup = cook_soup("https://www.woolworths.co.nz/shop/browse/fish-seafood?page=1")

for match in soup.find_all('div', class_='product-entry product-cup ng-star-inserted'):
    try:
        title = match.find('h3', 'ng-star-inserted').text.strip()
        price_data = match.find('span').text.strip().split()
        price, price_unit = price_data[0], price_data[2]
        img_src = match.find('img')['src']
        link = match.find('a', class_="productImage-container")['href']
        print(title)
        item = Product(name="title", )
    except:
        print("could not extract")
        continue





# ranges = page_number_ranges()
# for x in range(len(ranges)):
#     t = categories[x] + str(ranges[x])
#     print(t)

update_woolworths_urls()