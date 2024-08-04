"""This module  handles the scraping of Divar using selenium and scrapy.
First it runs links.py to get all the links saved into urls.csv.
Then it runs the spider to scrape required data from each link.

local import:
    links
 """

import os

import links

cities = [
        "tehran",
        "tabriz",
        "mashhad",
        "isfahan",
        "karaj",
        "shiraz",
        "qom",
        "ahvaz",
        "kermanshah",
]
groups = [
    "apartment",
    "villa",
    "old-house",
]
for city in cities:
    for group in groups:
        links.get_links(city, group)
        os.system("scrapy crawl divar_real_estate")


# ToDo-----------------------------------------------------------------
# 1. Fix the problem gettng blocked with scrapy(add proxy and delaytime).
# 2. Write to mysql database.(using selenium pipelines?)
