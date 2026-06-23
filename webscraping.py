import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.scrapethissite.com/pages/simple/"

response=requests.get(url)

soup=BeautifulSop(response.text,"html.sparser")

countries_capital={}
countries=soup.find_all("div",class_="country")

for country in countries:
    name=country.find("h3",class_="country-name").text.strip()
    capital=country.find("span",class_="country-capital").text.strip()

    countries_capital[name]=capital

print(countries_capital)
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

countries_capital = {}

countries = soup.find_all("div", class_="country")

for country in countries:
    name = country.find("h3", class_="country-name").text.strip()
    capital = country.find("span", class_="country-capital").text.strip()

    countries_capital[name] = capital

# Convert dictionary to DataFrame
df = pd.DataFrame(
    list(countries_capital.items()),
    columns=["Country", "Capital"]
)

print(df.head())