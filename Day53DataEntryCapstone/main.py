import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)
soup = BeautifulSoup(response.text, "html.parser")

link_tags = soup.find_all('a', class_="property-card-link")
links = [a_tag['href'] for a_tag in link_tags]
print(f"There are {len(links)} links to individual listings in total: \n")
print(links)

# price_tags = soup.find_all('span', class_="PropertyCardWrapper__StyledPriceLine")
# prices = [a_tag.text.replace('+/mo', '').replace('/mo','').replace('+ 1 bd', '').replace('+ 1bd', '') for a_tag in price_tags]

all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")
print(all_prices)

# adress_tags = soup.find_all('address')
# addresses = [a_tag.text.replace('\n', '') for a_tag in adress_tags]
# print(addresses)

all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]
print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")
print(all_addresses)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScaF_DU2szYiMEJlOPBCd2_iD3QsZL2hhUjdbTKt56lSQFgdw/viewform?usp=sf_link")
    time.sleep(2)
    address = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(links[n])
    submit_button.click()

