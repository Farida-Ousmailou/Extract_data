import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.gov.uk/search/news-and-communications"

page = requests.get(url)
page_content = page.content
print("Statut code:", page.status_code)
soup = BeautifulSoup(page_content,"html.parser")
print(soup.title.string)
class_name = "govuk-link"

titres = soup.find_all("a", class_=class_name)
descriptions = soup.find("p", class_="gem-c-document-list__item-description")
print(descriptions.string)

titres_textes = []
for titre in titres:
    titres_textes.append(titre.string)
print(titres_textes)


descriptions_textes = []
for description in descriptions:
    descriptions_textes.append(description.string)
print(descriptions_textes)


en_tete = ["titre", "description"]
with open("data.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(en_tete)
    for titre, description in zip(titres_textes, descriptions_textes):
        writer.writerow([titre, description])



