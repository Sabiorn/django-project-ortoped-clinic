import requests
from bs4 import BeautifulSoup





# soup = BeautifulSoup(r.text, "lxml")
# print(r.status_code)

response = requests.get('https://frankmayer.ru/')  # Замените URL на нужный вам

if response.status_code == 200:
    with open('testt.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
else:
    raise Exception(f"HTTP request failed with status code {response.status_code}")
