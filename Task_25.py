from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium import webdriver

class imdb:
    # Setup WebDriver path and options
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    wait = WebDriverWait(driver, 15) # Use WebDriverWait to wait for elements to be present

    def __init__(self, web_url):
        self.url = web_url

    def imdb_form(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)

            # # Navigate to the IMDb Advanced Name Search page

            scroll_to = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[1]/ul/li[1]/span")))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to)
            self.driver.implicitly_wait(10)

            # Fill in the input boxes and select boxes
            # For example, filling in the name box
            Collapse = self.wait.until(EC.presence_of_element_located((By.XPATH,'//span[text()="Expand all"]'))).click()

            name_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[1]/div[2]/div/div/div/div/div/div/input"))).send_keys("vignesh")
            print("Name is entered into the form")
            scroll_to_Birth_date = self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Birth date"]')))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_Birth_date)

            DB_startdate = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name="birth-year-month-start-input"]'))).send_keys("2020-02")
            DB_todate = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name="birth-year-month-end-input"]'))).send_keys("2024-02")
            print("date is entered into the form")

            scroll_to_Birthday = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Birthday']")))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_Birthday)
            BD_Input = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@name="birthday-input"]'))).send_keys("12-02")
            print("Birthday is entered into the form")
            scroll_to_Awards = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Awards & recognition']")))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_Awards)
            Award_select = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Best Director-Nominated']")))
            print("Award option is selected in the form")
            # initialize ActionChain object

            actions = ActionChains(self.driver)
            actions.move_to_element(Award_select)
            actions.click(Award_select)
            actions.perform()
            scroll_to_Page_topics = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Page topics']")))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_Page_topics)
            page_topic = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Place of birth']")))
            # initialize ActionChain object
            actions = ActionChains(self.driver) # initialize ActionChain object
            actions.move_to_element(page_topic)
            actions.click(page_topic)
            actions.perform()
            scroll_to_Trivia = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Trivia']")))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_Trivia)
            topic = self.wait.until(EC.presence_of_element_located((By.XPATH, '//select[@class="ipc-select__input"]')))
            dropdown = Select(topic)
            dropdown.select_by_index(2)
            dropdown_option = self.wait.until(EC.element_to_be_clickable((By.ID,'text-input__5'))).send_keys("India")
            scroll_to_Gender_identity = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Gender identity']")))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_Gender_identity)
            # initialize ActionChain object
            actions = ActionChains(self.driver)# initialize ActionChain object
            credit = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@class="sc-cb8b4fe5-0 hbbOwa react-autosuggest__input"]'))).send_keys("Holiday")
            actions.pause(2)
            actions.send_keys(Keys.ARROW_DOWN)
            actions.pause(1)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            scroll_to_Credits = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Credits']")))
            print("credit is entered into th form")
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_Credits)
            # initialize ActionChain object
            actions = ActionChains(self.driver)
            Adult_name = self.wait.until(EC.presence_of_element_located((By.ID,"include-adult-names")))
            actions.move_to_element(Adult_name)
            actions.click(Adult_name)
            actions.perform()
            result = self.wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='See results']"))).click()
            print("Search performed successfully.")
        except (NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException) as e:
            print(e)
        finally:
            self.driver.quit()


if __name__ == "__main__":
    url = "https://www.imdb.com/search/name/"
    imdb1 = imdb(url)
    imdb1.imdb_form()