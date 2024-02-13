import requests
from bs4 import BeautifulSoup
import csv

def get_web_html (offer_link:str) -> str :
    """
    Sends an http get request to the specified URL, retrieves
    the textual content of the response and returns it as a string.


    Args:
        url(str): the url to send the request to

    Returns:
        str: The text content of the http response
    """
    # type GET request
    response = requests.get(offer_link)
    # Check if the HTTP request was successful (status code 200)
    if response.status_code == 200:
        html = response.text
        with open("job.html", "w") as f:
            # Write the HTML content to the "job.html" file
            f.write(html)

    # content of response
    page_html = response.text
    return page_html

def get_job_info(soup:BeautifulSoup,)->list:
    """
    obtain information relating to the job offer

    :param soup: the soup object obtained
    :param offer_link: used the offer link

    :return: job_data, column_names
    """
    # getting title
    job_title = soup.title.text
    print(job_title)

    # getting mainly tag
    tags = soup.find("div", {"class": "row permalink-infos d-flex align-items-center px-3"})
    job_tags = tags.text
    print(job_tags)

    # job offer description
    description = soup.find("p", {"class": "permalink-description"})
    job_description = description.text.replace(",", " ")
    print(job_description)

    # organizing data into a list
    job_data = [job_title, job_tags, job_description]
    # organizing columns_names into a list
    column_names = ["job_title", "tags", "description"]
    return job_data, column_names

def csv_add_line (job_data: list , column_names: list, csv_path: str)->str:
    """
    Writes a new line in csv format to the specified file path.

    :param new_line: A list of values to add as a new row
    :param columns: A list of columns names for the csv file
    :param csv_path: The file path of the csv file to write

    If the csv file does not exist, this function will
    create it and write the columns names before adding
    the new line. If already exists, this function will
    append the new line to the end of file.

    :return: None
    """
    with open("job_offers.csv", "w", encoding="utf-8", newline="") as csv_file:
        # create a writer object
        writer = csv.writer(csv_file, delimiter=";")
        # add a line with columns
        if csv_file.tell() == 0:
            writer.writerow(column_names)
        # add data for the offer
        writer.writerow(job_data)
        # close automatically the file

def scrape_data_from_job_offer(offer_link:str, job_offers_csv_path: str )-> str:
    """
    scrapes information from a job offer webpage and saves it to a csv file.

    :param offer_link (str): URL of job offer web page
    :param job_offers_csv_path (str): The path of the csv file
    :return:
    """
    # Get the html code with the page
    web_page_html = get_web_html(offer_link)

    # initialize a BS object
    soup = BeautifulSoup(web_page_html, "lxml")

    # accessing different elements on the page
    job_data, columns_names = get_job_info(soup)

    # save the results to csv file
    csv_add_line(job_data, columns_names, job_offers_csv_path)

# parameters
offer_link = "https://www.jobijoba.com/fr/annonce/54/26e1c6007076b02ca4ca43b4d7d3f51b"
scrape_data_from_job_offer(offer_link, "job_offers.csv")