
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://www.nytimes.com/books/best-sellers/")
driver.maximize_window()


driver.find_element(By.XPATH, "(//button[@type='button'])[4]").click()
driver.find_element(By.XPATH, "(//a[@class='css-114t425'][normalize-space()='Amazon'])[2]").click()

# switching with two tab
driver.switch_to.window(driver.window_handles[1])


# landing on amazon page and adding book to cart. then check cart
driver.find_element(By.ID, "add-to-cart-button").click()
driver.find_element(By.XPATH, "//span[@id='nav-cart-count']").click()


# Check if add to cart flow was successful
bookTitle = driver.find_element(By.CLASS_NAME, "a-truncate-cut").text
print("Book Title: " + bookTitle)
assert "fourth wing (the empyrean, 1)" in bookTitle.lower()
print("TEST PASSED : ADD TO CART FLOW SUCCESSFUL")

driver.quit()