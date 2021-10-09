import os

import requests
from bs4 import BeautifulSoup

os.chdir('D:\Work\Avtaar\ML Assignment 2')

movies = []
with open('top5movies.txt') as file:
    movies = file.read().split('\n')

# print(data)

link = 'https://en.wikipedia.org/wiki/'


url = link + movies[0].title().replace(' ', '_')

r = requests.get(url)


soup = BeautifulSoup(r.text, 'html5lib')

infobox = soup.find('table', {'class': 'infobox'})

title = infobox.findAll('tr')[0].text
print(title)

director = infobox.findAll('tr')[2].a.text
print(director)

#release_year = infobox.findAll('tr')[11].li.text.replace(u'\xa0', ' ').split(' ')[2]
release_year = infobox.find('div', text='Release date').find_next(
    'li').text.replace(u'\xa0', ' ').split(' ')[2]
print(release_year)

""" overall_gross_earning = infobox.findAll('tr')[-1].td
overall_gross_earning = overall_gross_earning.text.replace(overall_gross_earning.a.text, '') """
overall_gross_earning = infobox.find(
    'th', text='Box office').find_next('td').text
print(overall_gross_earning)

""" cast = infobox.findAll('tr')[5].findAll('a')
cast = [x.text for x in cast] """
cast = infobox.find('th', text='Starring').findNext('td')
print(cast)
