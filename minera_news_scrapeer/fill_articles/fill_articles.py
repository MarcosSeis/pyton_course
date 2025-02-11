import requests
from bs4 import BeautifulSoup
import json
import os

def get_article_content(article):
    """Extrae el contenido del artículo desde su enlace."""
    url = article["link"]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"No se pudo acceder a {url}")
        return ""
    
    soup = BeautifulSoup(response.content, "html.parser")
    content_element = soup.find(class_="article-content")
    
    return content_element.get_text(strip=True) if content_element else "Contenido no disponible"

def update_articles_with_content(json_filename="articles.json"):
    """Lee el JSON de artículos, extrae el contenido y actualiza el archivo."""
    if not os.path.exists(json_filename):
        print("El archivo JSON no existe.")
        return
    
    with open(json_filename, "r", encoding="utf-8") as file:
        articles = json.load(file)
    
    for article in articles:
        article["content"] = get_article_content(article)
    
    with open(json_filename, "w", encoding="utf-8") as file:
        json.dump(articles, file, indent=4, ensure_ascii=False)


    print("El archivo JSON ha sido actualizado con el contenido de los artículos.")

    return articles

if __name__ == "__main__":
    update_articles_with_content()
