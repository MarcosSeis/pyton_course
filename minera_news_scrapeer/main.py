from junior_minning_scrapper.junior_minning_scrapper import get_articles, save_to_json
from fill_articles.fill_articles import update_articles_with_content
from ia_chat.ia_chat import process_items


def main():
    # Paso 1: Extraer artículos y guardarlos en JSON
    articles = get_articles()
    save_to_json(articles)
    print("Artículos extraídos y guardados en 'articles.json'.")

    # Paso 2: Actualizar los artículos con su contenido
    artcles_full = update_articles_with_content()
    print("Contenido de los artículos agregado a 'articles.json'.")

    #Paso 3: Usar la IA
    prompt = "Eres un editor de textos de una pagina web de noticias llamada mineria news, a continuacion te voy a pasar un texto en inglés, con title, date, link y content, todo en ingles, quiero que me devuelvas un objeto con title, date y content, en español en el valor pero que las llaves las conserves igual, el value de contenent en formato de nota para el sitio web mineria news, esto con el fin de generar una nota que sera publicada, trata de ser claro, formal pero informativo y si puedes complementar la nota con datos sobre lo que se habla hazlo, es iimportante que me regreses un objeto como te lo pedi, title, date y content."

    process_items(artcles_full, prompt)

if __name__ == "__main__":
    main()
