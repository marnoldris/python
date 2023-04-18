#!/usr/bin/python

import requests, bs4

response = requests.get('https://scrolller.com/volcanic-temple-2-by-scott-richard-avykqa0tal')
response.raise_for_status()

soup = bs4.BeautifulSoup(response.content, 'html.parser')


scraped_data = soup.select_one('img[src$=".jpg"]')
image_url = scraped_data['src']

# Download the file by url as binary
image_bin = requests.get(image_url).content
with open('scraped_image.jpg', 'wb') as f:
    f.write(image_bin)
