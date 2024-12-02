import requests

def site_acessivel(url):
    try:
        requests.get(url, verify=False)
    except requests.exceptions.RequestException:
        print(f'O site Pudim não está acessível no momento.')
    else:
        print('Consegui acessar o site Pudim com sucesso!')
