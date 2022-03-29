from splinter import Browser
from bs4 import BeautifulSoup as bs
import re
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():
    # Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://redplanetscience.com/'
browser.visit(url)

time.sleep(1)
# Scrape page into Soup
html = browser.html
soup = bs(html, "html.parser")

#scrape new_title and news_p
news_title = soup.find('div', class_='content_title')
news_p= soup.find('div', class_= 'article_teaser_body')
#print without extras
news_title.text
#print without extras
news_p.text

browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, 'html.parser')

    items = soup.find_all('div', class_='item')

     # Mars facts
url = 'https://galaxyfacts-mars.com/'
browser.visit(url) 
time.sleep(1)

dfs = pd.read_html(url)
for df in dfs:
    try:
        df = df.rename(columns={0: "Description", 1: "Value"})
        df = df.set_index("Description")
        marsfacts_html = df.to_html().replace('\n', '')
        

# Mars Hemispheres

url = 'https://marshemispheres.com/'


browser.visit(url)
time.sleep(1)
html = browser.html
soup = bs(html, 'html.parser')

items = soup.find_all('div', class_='item')
urls = []
titles = []
for item in items:
    urls.append(url + item.find('a')['href'])
    titles.append(item.find('h3').text.strip())

img_urls = []
for oneurl in urls:
browser.visit(oneurl)
html = browser.html
soup = bs(html, 'html.parser')
# savetofile(textfilename,soup.prettify())
oneurl = url+soup.find('img',class_='wide-image')['src']
img_urls.append(oneurl)
img_urls
hemisphere_image_urls = []
    for i in range(len(titles)):
    hemisphere_image_urls.append({'title':titles[i],'img_url':img_urls[i]})


    
marspage = {}
marspage["news_title"] = news_title
marspage["news_p"] = news_p
marspage["featured_image_url"] = featured_image_url
marspage["mars_facts"] = marsfacts_html
marspage["hemisphere_image_urls"] = hemisphere_image_urls

return marspage