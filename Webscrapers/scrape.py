from bs4 import BeautifulSoup
from selenium import webdriver
import csv

new_world = "https://www.newworld.co.nz/shop/category"

categories = ["/fresh-foods-and-bakery",
 "/chilled-frozen-and-desserts",
  "/pantry",
   "/drinks",
    "/beer-cider-and-wine",
     "/personal-care",
      "/baby-toddler-and-kids",
       "/pets",
        "/kitchen-dining-and-household",
         "/quick-and-easy-meals" ]



#Beautiful Soup House Keeping
def source_html(url):
    dr = webdriver.Chrome()
    dr.get(url)
    return dr.page_source

def cook_soup(url):
    return BeautifulSoup(source_html(url), 'lxml')


#Workhorse Function, currently writing rows to CVC file, need to refactor
def messy_function(url):
    soup = cook_soup(url)

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


#This function returns the max for number of pages for a catergory by finding the final a tag value for the page nav
#It is not always accurate (sometimes returns value less than actual max, maybe 10%-20% of the time)
def last_page(soup):
    num = 0
    for match in soup.find_all('a', class_='_10vhnom2 _10vhnom1'):
        num = int(match.find('p').text)
    return num

#This function returns a list of page numbers for upper range limit, 
def page_number_ranges():
    ranges = []
    for c in categories:
        url = new_world + c 
        source = source_html(url)
        soup = BeautifulSoup(source, 'lxml')
        max = last_page(soup)
        ranges.append(max)
    return ranges


#Testing Code is Below
ranges = page_number_ranges()

csv_file = open('scrape_data.csv','w', newline='') 
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'dollars','cents'])


for i in range(len(ranges)):
    for page in range(0, ranges[i]):
        url = new_world + categories[i] + "?pg=" + str(page)
        print(url)
        messy_function(url)

csv_file.close()

# reader = csv.DictReader(open('scrape_data.csv'))
# for row in reader:
#     print(row)

    




























