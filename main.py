from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "./chromedriver"

# create a Service object for the ChromeDriver
service = Service(chrome_driver_path)

# start the ChromeDriver service
service.start()

# create a Chrome web driver with the Service object
driver = webdriver.Chrome(service=service)

website_url = "https://www.linkedin.com/jobs/search"

def scrape_linkedin_jobs():
    # ------------------- Step 1 -----------------------
    # go to the web page using selenium
    driver.get(website_url)

    print(driver.title)

    # ------------------- Step 2 ------------------------
    # get jobs -- main element

    # search by class/id or any other field you can find
    jobs = driver.find_elements(
        value="base-card__full-link",
        by=By.CLASS_NAME
    )

    # -------------------- Step 3 -----------------------
    # get job info
    for job in jobs:
        print(job)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scrape_linkedin_jobs()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
