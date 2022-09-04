import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

base_url = 'https://habr.com/ru/all/'
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'разработчика', 'Телеграм', 'МГЛУ']
headers = Headers().generate()
response = requests.get(base_url, headers=headers).text
soup = BeautifulSoup(response, 'html.parser')
posts = soup.find_all('div', class_="tm-article-snippet")
def main():
    for post in posts:
        for keyword in KEYWORDS:
            if keyword in post.text:
                date_time = post.find('span', class_='tm-article-snippet__datetime-published').text
                title = post.find(class_="tm-article-snippet__title-link").text
                href = post.find('a', class_="tm-article-snippet__title-link").attrs['href']
                link = base_url + href
                print(f"<{date_time}>-<{title}>-<{link}>")

if __name__ == '__main__':
    main()

