import requests
from bs4 import BeautifulSoup
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
#html_code = page.text
page_content = page.content
soup = BeautifulSoup(page_content,"html.parser")
print(soup.title.string)
class_name = "govuk-link"
titres = soup.find_all("a", class_=class_name)
#print(titres)
descriptions = soup.find("p", class_="gem-c-document-list__item-description")
#print(descriptions)
titres_textes = []
for titre in titres:
    titres_textes.append(titre.string)
print(titres_textes)

descriptions_textes = []
for description in descriptions:
    descriptions_textes.append(description.string)
print(descriptions_textes)