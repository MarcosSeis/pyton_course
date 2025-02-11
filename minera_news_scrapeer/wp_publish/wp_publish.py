import os
from dotenv import load_dotenv
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def publicar_noticias_en_wordpress(noticias):
    """
    Publica una lista de noticias como posts en WordPress.

    Parámetros:
        noticias (list): Lista de diccionarios con las noticias.

    Retorna:
        list: Lista de IDs de los posts publicados.
    """
    # Obtener credenciales de WordPress desde las variables de entorno
    wp_site_xmlrpc = os.getenv("WP_WEB")
    wp_user = os.getenv("WP_USER")
    wp_password = os.getenv("WP_PASSWORD")

    # Conectar a WordPress
    wp = Client(wp_site_xmlrpc, wp_user, wp_password)
    ids_publicados = []

    # Iterar sobre cada noticia y publicarla como un post
    for noticia in noticias:
        post = WordPressPost()

        # Asignar título, contenido y otros campos
        post.title = noticia["title"]
        post.post_type = "noticia"  

        # Agregar campos personalizados de ACF (si es necesario)
        post.custom_fields = [
            {"key": "titulo", "value": noticia["title"]},  # Campo ACF para la titulo
            {"key": "contenido", "value": noticia["content"]}  # Campo ACF para el contenido
        ]

        # Estado de la publicación (draft o publish)
        post.post_status = "publish"  # Cambia a "draft" si prefieres guardar como borrador

        # Crear la entrada
        try:
            new_id = int(wp.call(NewPost(post)))
            ids_publicados.append(new_id)
            print(f'Post publicado con éxito. ID: {new_id}, Título: {noticia["title"]}')
        except Exception as e:
            print(f'Error al publicar el post: {noticia["title"]}. Error: {e}')

    return ids_publicados