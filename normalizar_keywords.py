import json
from unidecode import unidecode

def normalizar_palavra_chave(palavra):
    return unidecode(palavra).upper()

with open('artigos_encoinfo_com_kw.json', 'r', encoding='utf-8') as f:
    artigos = json.load(f)

for artigo in artigos:
    artigo['Palavra-chave'] = normalizar_palavra_chave(artigo['Palavra-chave'])

with open('artigos_encoinfo_com_kw_normalizadas.json', 'w', encoding='utf-8') as f:
    json.dump(artigos, f, ensure_ascii=False, indent=4)
