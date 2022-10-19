# Tuto : https://medium.com/@belen.sanchez27/5-steps-to-get-started-with-web-scraping-using-beautiful-soup-8d954a406627
# Tuto 2 video : https://www.youtube.com/watch?v=ng2o98k983k&ab_channel=CoreySchafer
from bs4 import BeautifulSoup
import requests
import csv

# Target web page
url = 'https://www.nuoobox.com/blogs/conseils/cheveux-poreux-que-faire'

# Connection to web page
response = requests.get(url)
# If 200 --> All good !
# print(response.status_code)

# Convert the response HTLM string into a python string
# html = response.text

soup = BeautifulSoup(response.content, 'lxml')

# Let's print the html code with indentation
# print(soup.prettify())

# Save in csv ('w' = write)
csv_file = open('test_webscraping.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Titre de la page', 'H1', 'H2', 'Texte d\'intro', 'Texte'])

title_page = soup.title.text
print(title_page)

h1_title = soup.h1.text
print(h1_title)

h2_title = soup.find_all('h2')

for all_h2 in h2_title:
    print(all_h2.get_text())

intro = soup.find('div', id='1630673005239').text
print(intro)

summary = soup.find_all('p', class_='text--1627545557198')
for all_text in summary:
    print(all_text.get_text())

csv_writer.writerow([title_page, h1_title, h2_title, intro, summary])
csv_file.close()
