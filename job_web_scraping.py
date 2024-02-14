import requests
from bs4 import BeautifulSoup
import csv


class JobScraper:
    def __init__(self, offer_link):
        """
        Initializes an instance of JobScraper with the job offer URL.

        Args:
            offer_link (str): The URL of the job offer.
        """
        self.offer_link = offer_link

    def get_web_html(self):
        """
        Retrieves the HTML content of the job offer web page.

        Returns:
            str: The HTML content of the page.
        """
        response = requests.get(self.offer_link)
        if response.status_code == 200:
            html = response.text
            with open("job.html", "w") as f:
                f.write(html)
            return html
        else:
            return None
    def get_job_info(self, soup):
        """
        Extracts job information from a BeautifulSoup object.

        Args:
            soup (BeautifulSoup): The BeautifulSoup object containing the HTML code of the page.

        Returns:
            tuple: A tuple containing job data and column names.
        """
        job_title = soup.title.string
        tags = soup.find("div", {"class": "row permalink-infos d-flex align-items-center px-3"})
        job_tags = tags.string
        description = soup.find("p", {"class": "permalink-description"})
        job_description = description.text.replace(",", " ")
        return [job_title, job_tags, job_description], ["job_title", "tags", "description"]

    def csv_add_line(self, job_data, column_names, csv_path):
        """
        Adds a new line to the CSV file with the provided data.

        Args:
            job_data (list): List of job data.
            column_names (list): List of column names for the CSV file.
            csv_path (str): Path of the CSV file.
        """
        with open(csv_path, "a", encoding="utf-8", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=";")
            if csv_file.tell() == 0:
                writer.writerow(column_names)
            writer.writerow(job_data)

    def scrape_data_from_job_offer(self, job_offers_csv_path):
        """
        Scrapes job offer information and saves it to a CSV file.

        Args:
            job_offers_csv_path (str): Path of the CSV file.
        """
        web_page_html = self.get_web_html()
        if web_page_html:
            soup = BeautifulSoup(web_page_html, "lxml")
            job_data, columns_names = self.get_job_info(soup)
            self.csv_add_line(job_data, columns_names, job_offers_csv_path)


# Parameters
offer_link = "https://www.jobijoba.com/fr/annonce/54/26e1c6007076b02ca4ca43b4d7d3f51b"
job_scraper = JobScraper(offer_link)
job_scraper.scrape_data_from_job_offer("job_offers.csv")
