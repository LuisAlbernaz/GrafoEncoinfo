import json
import requests
from bs4 import BeautifulSoup
from keyword_extract import extrair_palavra_chave

with open('artigos_encoinfo_com_link.json', 'r', encoding='utf-8') as f:
    artigos = json.load(f)

artigos_atualizados = [] 

for artigo in artigos:
    url = artigo['Link']
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        h4_resumo = soup.find('h4', string="Resumo")
        
        resumo = ""
        if h4_resumo:
            for sibling in h4_resumo.find_next_siblings():
                if sibling.name == 'p':
                    resumo += sibling.text.strip() + " "
                else:
                    break 

        if len(resumo) > 1:
            print(f"Resumo encontrado: {resumo[:100]}...")  
        else:
            print("Resumo não encontrado. Usando o título para extrair a palavra-chave.")
            resumo = artigo['Título']
        palavra_chave = extrair_palavra_chave(resumo)
        print(f"Palavra-chave extraída: {palavra_chave}")

        artigo['Palavra-chave'] = palavra_chave
        artigos_atualizados.append(artigo)

with open('artigos_encoinfo_com_kw.json', 'w', encoding='utf-8') as f:
    json.dump(artigos_atualizados, f, ensure_ascii=False, indent=4)
