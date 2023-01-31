from bs4 import BeautifulSoup
import requests
from inflection import titleize

# daily_url = 'http://www.dailysmarty.com/topics/python'
# r = requests.get(daily_url)
# soup = BeautifulSoup(r.content)

# names = [titleize(i.contents[0].contents[0].get('href').split('/')[-1]) for i in soup.find_all("div", {"class": "post-link-title"})]

def title_generator(links):
    titles = []

    def post_formatter(url):
        if 'posts' in url:
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            url = titleize(url)
            titles.append(url)

# UPDATED CODE
    for link in links:
        if link.get('href') == None:
            continue
        else:
            post_formatter(link.get("href"))
# UPDATED CODE

    return titles


r = requests.get('http://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('a')
titles = title_generator(links)

for title in titles:
    print(title)
print('')