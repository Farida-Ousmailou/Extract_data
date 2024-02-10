import requests
from bs4 import BeautifulSoup

# type GET request
r = requests.get("https://www.jobijoba.com/fr/annonce/54/26e1c6007076b02ca4ca43b4d7d3f51b")
# content of r
page_html = r.text
print(page_html)

# initialize a BS object
soup = BeautifulSoup(page_html, "lxml")

# getting title
job_title= soup.title.text
print(job_title)

# getting mainly tag
tags = soup.find("div", {"class": "row permalink-infos d-flex align-items-center px-3"})
print(tags.text)

# job offer text
description = soup.find("p", {"class": "permalink-description"})
print(description.text)
#print((soup.find("div", {"class": "permalink-subtitle" })).text)