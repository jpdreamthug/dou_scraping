import dataclasses
from urllib.parse import urljoin

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from seleniumwire import webdriver


BASE_URL = "https://jobs.dou.ua/"
HOME_URL = urljoin(BASE_URL, "vacancies/?category=Analyst")

KEYWORDS = [
    "Python",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Seaborn",
    "Scikit-learn",
    " R ",
    "SQL",
    "Java",
    "Scala",
    "Tableau",
    "Power BI",
    "Excel",
    "Google Sheets",
    "NoSQL",
    "PostgreSQL",
    "MongoDB",
    "Hadoop",
    "TensorFlow",
    "Keras",
    "PyTorch",
    "XGBoost",
    "Spark",
    "Kafka",
    "AWS",
    "Azure",
    "GCP",
]


@dataclasses.dataclass
class Vacancy:
    title: str
    company_name: str
    date: str
    location: list[str]
    keywords_found: list[str]
    salary: str | None = None


def interceptor(request):
    del request.headers["user-agent"]
    del request.headers["sec-ch-ua"]
    del request.headers["referer"]
    request.headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    request.headers["sec-ch-ua"] = (
        '"Chromium";v="128", "Google Chrome";v="128"'
    )
    request.headers["referer"] = "https://www.google.com"


def get_webdriver() -> webdriver.Chrome:
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.request_interceptor = interceptor
    return driver


def load_more_items(driver) -> bool:
    try:
        more_button = driver.find_element(
            By.CSS_SELECTOR, "#vacancyListId > div.more-btn > a"
        )
        wait = WebDriverWait(driver, 10)
        more_button = wait.until(ec.element_to_be_clickable(more_button))
        more_button.click()
        return True
    except Exception:
        return False
