from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://www.speedcubedb.com/a/3x3/PLL")

time.sleep(2)

buttons = driver.find_elements(By.CLASS_NAME, "more-algs")

driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buttons[-1])
time.sleep(5)

for button in buttons:
# Scroll to the button using JavaScript before clicking
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)

    # Add a slight delay to let the scroll complete (adjust the time if necessary)
    time.sleep(1)

    # Click the button
    button.click()

    # Add a delay after clicking to wait for the content to load
    time.sleep(1)

# Additional delay before closing the browser
time.sleep(2)

elements = driver.find_elements(By.CLASS_NAME, "singlealgorithm")

for element in elements:
    id = element.get_attribute("data-alg")
    standard_alg = element.find_element(By.CLASS_NAME, "scdb-panel").text

    algorithms = []

    algorithmList = element.find_elements(By.CLASS_NAME, "list-group-item")

    for algorithm in algorithmList:
        algorithms.append(algorithm.text)

    print(f"PLL ID: {id}")
    print(f"Standard Algorithm: {standard_alg}")
    print("Additional Algorithms:")
    for algorithm in algorithms:
        print(algorithm)

    with open("pll.txt", "a") as file:
        file.write(f"pLL ID: {id}\n")
        file.write(f"Standard Algorithm: {standard_alg}\n")
        file.write("Additional Algorithms:\n")
        for algorithm in algorithms:
            file.write(algorithm + "\n")
        file.write("\n")

driver.quit()
