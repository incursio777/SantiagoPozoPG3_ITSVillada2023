import requests
import json

def todos():
    if __name__ == "__main__":
        url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
        responce = requests.get(url)
        if responce.status_code == 200:
            contenido = (responce.content)
            file = open("obtener texto", "wb")
            file.write(contenido)
            file.close()

def mago_oscuro():
    if __name__ == "__main__":
        url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?name=Dark Magician"
        responce = requests.get(url)
        if responce.status_code == 200:
            contenido = (responce.content)
            file = open("obtener texto", "wb")
            file.write(contenido)
            file.close()

def atributos_2():
    if __name__ == "__main__":
        url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?level=7&attribute=DARK"
        responce = requests.get(url)
        if responce.status_code == 200:
            contenido = (responce.content)
            file = open("obtener texto", "wb")
            file.write(contenido)
            file.close()
def ordenamiento():
    if __name__ == "__main__":
        url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?attribute=dark&sort=level"
        responce = requests.get(url)
        if responce.status_code == 200:
            contenido = (responce.content)
            file = open("obtener texto", "wb")
            file.write(contenido)
            file.close()


def post():
    if __name__ == "__main__":
        url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
        payload = {
            "name": "botozo",
        }
        responce = requests.post(url, json=payload)
        if responce.status_code == 200:
            contenido = (responce.content)
            file = open("obtener texto", "wb")
            file.write(contenido)
            file.close()

dato = int(input("Dime un numero: "))  
if dato == 1:
    todos()
elif dato == 2:
    mago_oscuro()
elif dato == 3:
    atributos_2()
elif dato == 4:
    ordenamiento()
elif dato == 5:
    post()