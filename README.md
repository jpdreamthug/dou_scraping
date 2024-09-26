# dou_scraping

## Project Overview
**dou_scraping** is a web scraping and data analysis project designed to extract job postings from the [DOU](https://jobs.dou.ua/) job board. The primary goal is to analyze the collected data to identify trends and demands in the Ukrainian IT job market, such as the most sought-after technologies, programming languages, and tools.

## Features
- **Automated Data Collection**: Utilizes Selenium to interact with dynamic web pages and scrape up-to-date job postings from DOU.
- **Detailed Data Extraction**: Gathers essential information including job titles, company names, required skills, salaries, locations, and job descriptions.
- **Data Storage**: Saves the scraped data into CSV files for easy access and further analysis.
- **Data Analysis**: Performs basic data analysis using Jupyter Notebook to uncover trends and insights in the IT job market.
- **Progress Tracking**: Implements progress bars using `tqdm` to monitor the scraping process.
- **Logging**: Maintains comprehensive logs to track the scraping process and handle errors effectively.

## Technologies Used
- **Selenium**: For automating web browser interactions and scraping dynamic content from DOU.
- **Python**: The primary programming language used for developing scraping scripts and data analysis tools.
- **Pandas**: For efficient data manipulation and analysis.
- **Tqdm**: For displaying progress bars during the scraping process.
- **Logging**: For tracking the scraping process and handling errors.
- **Jupyter Notebook**: For conducting and presenting data analysis.


## Setup and Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/jpdreamthug/dou_scraping.git
    cd dou_scraping
    ```

2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Scraper**
    ```bash
    python main.py
    ```

5. **Analyze the Data**
    - Open the Jupyter Notebook located in the `analysis` directory to perform data analysis.
    ```bash
    jupyter notebook analysis/data_analysis.ipynb
    ```

## Usage
- **Scraping Jobs**
    Execute the `main.py` script to collect the latest job postings from DOU. The script will log the scraping process and save the data to `data/vacancies_with_keywords.csv`.
- **Analyzing Data**
    Use the Jupyter Notebook in the `analysis` folder to perform and visualize data analysis on the scraped data.
- **Monitoring Progress**
    Progress bars provided by `tqdm` will display the scraping progress in the console. Detailed logs are maintained in `logs/scraping.log`.

## Key Components

### main.py
The entry point of the project. It initializes the WebDriver, scrapes vacancy links, retrieves detailed information for each vacancy, handles exceptions, and saves the data to a CSV file.

### scraper/parse.py
Contains functions to scrape all vacancy links and scrape detailed information for each vacancy using Selenium.

### scraper/csv_writer.py
Handles saving the scraped vacancy data to a CSV file.

### scraper/utils.py
Includes utility functions and constants such as the WebDriver setup, home URL, and keywords for filtering vacancies.

### analysis/data_analysis.ipynb
A Jupyter Notebook that performs basic data analysis on the scraped data, including identifying the most demanded technologies and visualizing trends.

## Logging
The scraping process is logged to `logs/scraping.log`, capturing information, warnings, errors, and critical issues to aid in debugging and monitoring.

## Contact
For any questions or suggestions, feel free to reach out at [ykondrattsev@gmail.com](mailto:ykondrattsev@gmail.com).

