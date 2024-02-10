import requests
from bs4 import BeautifulSoup
import csv

# type GET request
r = requests.get("https://www.jobijoba.com/fr/annonce/54/26e1c6007076b02ca4ca43b4d7d3f51b")
# content of r
page_html = r.text
print(page_html)

# initialize a BS object
soup = BeautifulSoup(page_html, "lxml")

# getting title
job_title = soup.title.text
print(job_title)

# getting mainly tag
tags = soup.find("div", {"class": "row permalink-infos d-flex align-items-center px-3"})
job_tags = tags.text
print(job_tags)

# job offer text
description = soup.find("p", {"class": "permalink-description"})
job_description= description.text
print(job_description)

#print((soup.find("div", {"class": "permalink-subtitle" })).text)

column_names = ["job_title", "tags", "description"]
job_data = [job_title, job_tags, job_description]

with open("job_offers.csv", "w", encoding="utf-8", newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    if csv_file.tell == 0:
        writer.writerow(column_names)
    writer.writerow(job_data)