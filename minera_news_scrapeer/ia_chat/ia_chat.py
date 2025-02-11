import openai
import os
import json

from dotenv import load_dotenv 

load_dotenv()

def chat(prompt, text):
    try:
        api_key = os.getenv("OPENAI_API_KEY")  
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": text},
            ],
        )
        return response.choices[0].message.content
    except Exception as err:
        print("Error al conectar con OpenAI:", err)
        return "ERROR"
    

def process_items(items, prompt):
    results = []
    articulos_publish = []
    
    for item in items:
        text = f"Title: {item['title']}\nDate: {item['date']}\nLink: {item['link']}\nContent: {item['content']}"
        response = chat(prompt, text)
        
        try:
            # Intentar convertir la respuesta en JSON
            response_json = json.loads(response)
        except json.JSONDecodeError:
            print(f"Error al decodificar la respuesta de OpenAI para el artículo: {item['title']}")
            response_json = {"error": "Respuesta inválida de OpenAI", "raw_response": response}
        
        # Guardar el artículo con la respuesta formateada
        articulo = {
            "title": response_json.get("title", item["title"]),  # Usar el título generado o el original
            "date": response_json.get("date", item["date"]),    # Usar la fecha generada o la original
            "link": item["link"],
            "content": response_json.get("content", item["content"]),  # Usar el contenido generado o el original
        }
        articulos_publish.append(articulo)
        results.append(response_json)
    
    # Guardar los artículos en JSON
    with open("articulos_publish.json", "w", encoding="utf-8") as f:
        json.dump(articulos_publish, f, ensure_ascii=False, indent=4)
    
    return results
