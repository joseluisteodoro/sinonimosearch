import requests
from bs4 import BeautifulSoup

def buscarporpalavra(palavra):
    url = f"https://www.sinonimos.com.br/{palavra}"
    # headers = {"User-Agent": "Mozilla/5.0"}
    session = requests.Session()
    resposta = session.get(url)

    if resposta.status_code != 200:
        return ["Erro ao tentar acessar o site: {resposta.status_code}"]

    sopa = BeautifulSoup(resposta.text,'html.parser')

    bloco = sopa.find('p',class_='syn-list syn-list-1')

    if not bloco:
        return[f"Nenhum sinonimo encontrado para palavra {palavra}"]
    
    sinonimos_tags = bloco.find_all('a', class_='sinonimo')
    sinonimos = [tag.text.strip() for tag in sinonimos_tags]

    print(f"Sinônimos encontrados para: {palavra}")
    print("-"*40)
    for s in sinonimos:
        print(f"\t• {s}")
    print("-"*40 + f"\n Total encontrados: {len(sinonimos)}\n")
    
    
