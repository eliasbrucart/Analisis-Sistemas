import requests

def obtener_datos_api(url):
    try:
        respone = requests.get(url, timeout=10)
        if respone.status_code == 200:
            return respone.json()
    except requests.exceptions.RequestException as e:
        return None