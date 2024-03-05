import requests
import lxml 
from bs4 import BeautifulSoup
import smtplib


USERAGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
ACCEPTLANGUAGE = "en-US,en;q=0.9"
URL= "https://www.hanes.com/ex101-586nsb.html"

YOUR_SMTP_ADDRESS = "smtp.gmail.com"
#Enter your email/password to recive alert:
YOUR_EMAIL= "ENTER YOUR EMAIL"
YOUR_PASSWORD = "ENTER YOUR PASSWORD"

BUY_PRICE = 100


headers = {
  "User-Agent": USERAGENT,
  "Accept-Language": ACCEPTLANGUAGE,
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_='bfx-price').get_text()

price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(class_="base").get_text()
print(title)

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )

