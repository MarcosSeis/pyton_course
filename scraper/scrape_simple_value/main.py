from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import gmtime, strftime
import time

def get_driver():
    #Opciones para hacerlo mas facil la navegacion
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximazed')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')
    options.add_argument('--headless')
    # Configura el navegador con el servicio
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('http://automated.pythonanywhere.com')
    return driver

def date_moment():
    fecha_str = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    return fecha_str

def clean_text(text):
    # ''''''extract temperature''''''    
    output = float(text.split(": ")[1])
    return output

def create_file():
    name = date_moment()
    f = open(name + ".txt", "x")
    return f

def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    date = clean_text(element.text)
    file = create_file()
    file.write(str(date))
    return file

#Ciclo para repetir la funcion cada ciertos segundos
while True :
    main()
    time.sleep(5)