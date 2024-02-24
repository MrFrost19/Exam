import requests
import lxml
from bs4 import BeautifulSoup

session = requests.Session()
header = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36"}

for page in range(1, 7):
    url = f"https://cash-backer.club/shops?page={page}"

    response = session.get(url, headers=header)
    soup = BeautifulSoup(response.text, "lxml")

    all_shop = soup.find("div", class_="row col-lg-9 col-md-9 col-12")
    shop = all_shop.find_all("div", class_="col-lg-2 col-md-3 shop-list-card pseudo-link no-link")
    shop_body = shop.find_all("div", class_="card-body")

    for elem in all_shop:
        logo_text = elem.find("div", class_="shop-title").text
        logo_text1 = logo_text[logo_text.find(":")+1:logo_text.find("%")]
        cashback_text = elem.find("div", class_="shop-rate").text
        cashback_text1 = cashback_text[cashback_text.find(":")++1:logo_text.find("%")]
        with open("cashbacker.txt", "a", encoding="utf-8") as file:
            file.write(f"{logo_text} ---->>>> {cashback_text}\n")