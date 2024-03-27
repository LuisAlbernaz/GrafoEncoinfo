import requests
from bs4 import BeautifulSoup
import json

base_url = "https://ulbra-to.br/encoinfo/edicoes/{}/anais/"

artigos = []

for ano in range(1999, 2024):  # Loop pelos anos de 1999 a 2023
    url = base_url.format(ano)
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for artigo in soup.select('ul.list-unstyled > li'):
            titulo = artigo.select_one('h6.titulo-link').text.strip()
            link_artigo = artigo.select_one('a')['href']  # Extraindo o link do artigo
            membros_str = artigo.select_one('p.text-muted').text.strip()
            membros_lista = [membro.strip() for membro in membros_str.split(',')]
            
            artigos.append({
                'Título': titulo,
                'Membros': membros_lista,
                'Ano': ano,
                'Link': link_artigo 
            })

with open('artigos_encoinfo_com_link.json', 'w', encoding='utf-8') as f:
    json.dump(artigos, f, ensure_ascii=False, indent=4)
