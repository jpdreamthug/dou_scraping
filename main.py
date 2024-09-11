from scraper.parse import scrape_all_vacancies, scrape_detail_vacancy
from scraper.csv_writer import save_vacancies_to_csv
from scraper.utils import get_webdriver, HOME_URL
from tqdm import tqdm


def main() -> None:
    driver = get_webdriver()

    try:
        print("Scraping vacancy links...")
        vacancy_links = scrape_all_vacancies(driver, HOME_URL)
    except Exception as err:
        print(f"Error during scraping vacancy links: {err}")
        return

    print(f"Found {len(vacancy_links)} vacancies. Scraping details...")

    vacancies = []
    for link in tqdm(vacancy_links, desc="Scraping vacancies", unit="vacancy"):
        try:
            vacancy = scrape_detail_vacancy(driver, link)
            vacancies.append(vacancy)
        except ValueError as ve:
            print(f"Data parsing error for vacancy {link}: {ve}")
        except AttributeError as ae:
            print(f"Element not found error in {link}: {ae}")
        except TimeoutError as te:
            print(f"Timeout scraping vacancy {link}: {te}")

    save_vacancies_to_csv(vacancies, "vacancies_with_keywords.csv")
    driver.quit()


if __name__ == "__main__":
    main()
