import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://books.toscrape.com/catalogue/page-"
all_books = []

# Loop through the first 5 pages
for page in range(1, 6):
    url = f"{base_url}{page}.html"
    print(f"Scraping {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text.strip()
        availability = book.find('p', class_='instock availability').text.strip()

        all_books.append({
            'title': title,
            'price': price,
            'availability': availability
        })

# Save to CSV
with open('books_dataset.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'price', 'availability'])
    writer.writeheader()
    writer.writerows(all_books)

print("✅ Dataset saved as books_dataset.csv")
