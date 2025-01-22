import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Crear el archivo (sobrescribiendo si ya existe)
def create_file():
    name = "nombres"
    return open(name + ".txt", "w")  # Modo "w" para sobrescribir

# Extraer los nombres de los <h3>
def names():
    return [name.text for name in soup.find_all('h3')]  # Retorna una lista de nombres

# Guardar los nombres en el archivo
def main():
    nombres = names()  # Lista de nombres
    file = create_file()
    for nombre in nombres:
        file.write(nombre + "\n")  # Escribir cada nombre en una línea nueva
    file.close()  # Cerrar el archivo después de escribir
    print(f"Archivo 'nombres.txt' creado con éxito.")

if __name__ == "__main__":
    main()
