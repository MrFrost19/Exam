import requests
import lxml
from bs4 import BeautifulSoup

session = requests.Session()
header = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36"}

class Exam:

    def page_checker_txt_printer(self):
        for page in range(1, 7):
            self.url = f"https://cash-backer.club/shops?page={page}"

            self.response = session.get(self.url, headers=header)
            self.soup = BeautifulSoup(self.response.text, "lxml")

            self.all_shop = self.soup.find("div", class_="row col-lg-9 col-md-9 col-12")
            self.shop = self.all_shop.find_all("div", class_="col-lg-2 col-md-3 shop-list-card pseudo-link no-link")

            for elem in self.shop:
                logo_text = elem.find("div", class_="shop-title").text
                logo_text1 = logo_text[logo_text.find(":")+1:logo_text.find("%")]
                cashback_text = elem.find("div", class_="shop-rate").text
                cashback_text1 = cashback_text[cashback_text.find(":")++1:logo_text.find("%")]
                with open("cashbacker.txt", "a", encoding="utf-8") as file:
                    file.write(f"{logo_text} ---->>>> {cashback_text} of cashback\n")

cashbacker = Exam()
cashbacker.page_checker_txt_printer()