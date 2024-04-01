import requests
from bs4 import BeautifulSoup

product_url = "https://www.amazon.co.uk/LATERN-Rectangular-Breathable-Thickened-Vegetables/dp/B09MRSZLSD/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=iT9L9&content-id=amzn1.sym.6aea875e-359f-49f3-864f-cff62d586b6a%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=6aea875e-359f-49f3-864f-cff62d586b6a&pf_rd_r=G65KE96H44G4F1N9HEV9&pd_rd_wg=tvYyf&pd_rd_r=671e1b4e-1167-4537-bcaa-5cb5f1dd6ab7&pd_rd_i=B09MRSZLSD"

headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
}

response = requests.get(product_url, headers=headers).text
soup = BeautifulSoup(response, "html.parser")
price_tags = soup.find_all(name="span", class_="a-price-whole")
prices = [int(price.getText().replace('\xa0', '').strip(",")) for price in price_tags]
print(prices)




