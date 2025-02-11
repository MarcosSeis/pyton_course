import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def get_articles():
    URL = "https://www.juniorminingnetwork.com/mining-topics/topic/mexico.html"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    today = datetime.today().date().isoformat()
    articles = []
    
    for article in soup.find_all(class_="article-title"):
        title = article.a.text.strip()
        link = "https://www.juniorminingnetwork.com" + article.a["href"]
        
        date_element = article.find_previous_sibling(class_="article-date")
        date_str = date_element.text.strip() if date_element else "Fecha no disponible"
        
        try:
            date = datetime.strptime(date_str, "%B %d, %Y").date().isoformat()
        except ValueError:
            date = "Fecha no disponible"
        
        if date == today:
            articles.append({"title": title, "date": date, "link": link})
    
    return articles

def save_to_json(data, filename="articles.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    articles = get_articles()
    save_to_json(articles)
    print(f"Archivo 'articles.json' creado con éxito. Se encontraron {len(articles)} artículos de hoy.")
