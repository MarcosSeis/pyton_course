from junior_minning_scrapper.junior_minning_scrapper import get_articles, save_to_json
from fill_articles.fill_articles import update_articles_with_content

def main():
    # Paso 1: Extraer artículos y guardarlos en JSON
    articles = get_articles()
    save_to_json(articles)
    print("Artículos extraídos y guardados en 'articles.json'.")

    # Paso 2: Actualizar los artículos con su contenido
    update_articles_with_content()
    print("Contenido de los artículos agregado a 'articles.json'.")

if __name__ == "__main__":
    main()
