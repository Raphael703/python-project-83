import requests


def get_status_code(url):
    try:
        response = requests.head(url)
        return response.status_code
    except requests.RequestException:
        return None
