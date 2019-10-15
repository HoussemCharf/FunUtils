from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


# assign your desired site link to scrape on the url variable 
url = 'https://bandera.inquirer.net/balita/' 

request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
source = urlopen(request).read()

soup = BeautifulSoup(source, 'lxml')

div_id_with_news_links = 'landing-main-default'
div = soup.find('div', {'id': div_id_with_news_links})

news_links = {}

for h2 in div.find_all('h2'):
    a = h2.find('a')
    print(a['href'])
    news_links[a.text] = a['href'] # Saving each links to a dictionary named 'news_links'


    # Below, I'm exporting the content of the news
    # Creating individual file for each news

    news_request = Request(a['href'], headers={'User-Agent': 'Mozilla/5.0'})
    news_source = urlopen(news_request).read()
    news_soup = BeautifulSoup(news_source, 'lxml')
    news_title = news_soup.h1.text

    p_content = ""

    for paragraph in news_soup.find_all('p'):
        p_content += paragraph.text + "\n"

    news_file = open(a.text+".txt", "w+")
    news_file.write('Title: ' + news_title +'\n')
    news_file.write('Content: ' + p_content +'\n')
    news_file.close()

""" Just in case you only need the links,
        I saved them in a dictionary.
        {'title': 'link'}
"""
print("\nDictionary of Links: \n")
print(news_links)
