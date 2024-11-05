from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Connecting to Scraping Browser...")

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Initialize ChromeDriver with full path to chromedriver.exe
    service = Service('C:/Users/sarka/AI_WEB_SCRAPPER/chromedriver-win64/chromedriver.exe')
    
    try:
        # Initialize the driver
        with webdriver.Chrome(service=service, options=chrome_options) as driver:
            driver.get(website)
            print("Waiting for CAPTCHA to solve manually if present...")

            # Get page content
            html = driver.page_source
            print("Navigated! Scraping page content...")
            return html
    except WebDriverException as e:
        print(f"An error occurred while scraping the website: {e}")
        return None


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get text or further process the content
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
