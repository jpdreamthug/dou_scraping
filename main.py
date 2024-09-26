import logging
from scraper.parse import scrape_all_vacancies, scrape_detail_vacancy
from scraper.csv_writer import save_vacancies_to_csv
from scraper.utils import get_webdriver, HOME_URL
from tqdm import tqdm


# Configure logging
logging.basicConfig(level=logging.INFO, filename="scraping.log", filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")


def main() -> None:
    driver = get_webdriver()

    try:
        logging.info("Scraping vacancy links...")
        vacancy_links = scrape_all_vacancies(driver, HOME_URL)

        if not vacancy_links:
            logging.warning("No vacancy links found. Exiting...")
            return

        logging.info(f"Found {len(vacancy_links)} vacancies. Scraping details...")

        vacancies = []
        for link in tqdm(vacancy_links, desc="Scraping vacancies", unit="vacancy"):
            try:
                vacancy = scrape_detail_vacancy(driver, link)
                vacancies.append(vacancy)
            except ValueError as ve:
                logging.error(f"Data parsing error for vacancy {link}: {ve}")
            except AttributeError as ae:
                logging.error(f"Element not found error in {link}: {ae}")
            except TimeoutError as te:
                logging.error(f"Timeout scraping vacancy {link}: {te}")
    except Exception as err:
        logging.critical(f"Error during scraping vacancy links: {err}")
    finally:
        driver.quit()

    save_vacancies_to_csv(vacancies, "vacancies_with_keywords.csv")


if __name__ == "__main__":
    main()
