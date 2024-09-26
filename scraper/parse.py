import logging
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from scraper.utils import KEYWORDS, Vacancy, load_more_items


# Setup logging
logging.basicConfig(level=logging.INFO)


def scrape_all_vacancies(driver, url: str) -> list[str]:
    driver.get(url)

    while load_more_items(driver):
        pass

    vacancy_elements = driver.find_elements(
        By.CSS_SELECTOR, "#vacancyListId > ul > li > div.title > a"
    )

    vacancy_links = []
    for element in vacancy_elements:
        link = element.get_attribute("href")
        vacancy_links.append(link)

    return vacancy_links


def scrape_detail_vacancy(driver, url: str) -> Vacancy:
    driver.get(url)

    try:
        title = driver.find_element(By.CSS_SELECTOR, "h1").text
    except NoSuchElementException:
        title = None
        logging.warning(f"Title not found for vacancy {url}")

    try:
        description = driver.find_element(
            By.CSS_SELECTOR, "div.b-typo.vacancy-section"
        ).text
    except NoSuchElementException:
        description = ""
        logging.warning(f"Description not found for vacancy {url}")

    try:
        company_name = driver.find_element(
            By.CSS_SELECTOR, "div.b-compinfo > div > div.l-n > a:nth-child(1)"
        ).text
    except NoSuchElementException:
        company_name = None
        logging.warning(f"Company name not found for vacancy {url}")

    try:
        date = driver.find_element(By.CSS_SELECTOR, "div.date").text
    except NoSuchElementException:
        date = None
        logging.warning(f"Date not found for vacancy {url}")

    try:
        location_element = driver.find_elements(By.CSS_SELECTOR, "div.sh-info > span")
        location = location_element[0].text.split(", ") if location_element else None
    except NoSuchElementException:
        location = None
        logging.warning(f"Location not found for vacancy {url}")

    try:
        salary = (
            driver.find_element(By.CSS_SELECTOR, "span.salary").text
            if driver.find_elements(By.CSS_SELECTOR, "span.salary")
            else None
        )
    except NoSuchElementException:
        salary = None
        logging.warning(f"Salary not found for vacancy {url}")

    # Use set intersection for faster keyword search
    keywords_found = list(set(KEYWORDS).intersection(set(description.lower().split())))

    return Vacancy(
        title=title,
        company_name=company_name,
        date=date,
        location=location,
        salary=salary,
        keywords_found=keywords_found,
    )
