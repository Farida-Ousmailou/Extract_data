import requests
from bs4 import BeautifulSoup

# type GET request
r = requests.get("https://www.jobijoba.com/fr/annonce/54/18adbb3d68f9217048763ca416deb342")
# content of r
page_html = r.text
print(page_html)

# initialize a BS object
soup = BeautifulSoup(page_html, "lxml")

# getting title
print(soup.title.text)

# getting mainly tag
print((soup.find("div", {"class": "row permalink-infos d-flex align-items-center px-3"})).text)
