# Projeto de Extração e Normalização de Dados para um Grafo de Conhecimento

Este projeto consiste em um conjunto de scripts Python para extrair dados de artigos de uma conferência, normalizar palavras-chave e construir um grafo de conhecimento utilizando o banco de dados Neo4j. Os principais passos incluem:

1. **Extrair Artigos da Conferência**: O script `extract_articles.py` faz a extração de artigos de uma conferência específica a partir de seus anais disponíveis online.

2. **Extração de Palavras-Chave**: O script `keyword_extract.py` utiliza a biblioteca NLTK para extrair palavras-chave relevantes a partir dos resumos dos artigos.

3. **Normalização de Palavras-Chave**: O script `normalizar_keywords.py` normaliza as palavras-chave extraídas para um formato padronizado, removendo acentos e convertendo para letras maiúsculas.

4. **Construção do Grafo de Conhecimento**: O script `grafos.py` utiliza a biblioteca Neo4j para criar um banco de dados de grafo que representa a relação entre artigos, participantes e palavras-chave.

## Instruções de Uso

1. **Instalação de Dependências**:
   - Certifique-se de ter o Python instalado no seu ambiente.
   - Instale as bibliotecas necessárias executando `pip install -r requirements.txt`.

2. **Execução dos Scripts**:
   - Execute o script `extract_articles.py` para extrair os artigos da conferência e salvar em um arquivo JSON.
   - Em seguida, execute `keyword_extract.py` para extrair e salvar as palavras-chave dos resumos dos artigos.
   - Utilize o script `normalizar_keywords.py` para normalizar as palavras-chave extraídas.

3. **Configuração do Banco de Dados**:
   - Certifique-se de ter o Neo4j instalado e em execução.
   - No script `grafos.py`, substitua `suaUri`, `seuUser` e `suaSenha` pelas informações do seu banco de dados Neo4j.
   - Execute o script `grafos.py` para criar o grafo de conhecimento no Neo4j.

## Estrutura dos Arquivos

- `extract_articles.py`: Script para extrair artigos da conferência.
- `keyword_extract.py`: Script para extrair palavras-chave dos resumos dos artigos.
- `normalizar_keywords.py`: Script para normalizar as palavras-chave extraídas.
- `grafos.py`: Script para construir o grafo de conhecimento no Neo4j.
- `requirements.txt`: Arquivo contendo as dependências do projeto.
- `artigos_encoinfo_com_link.json`: Arquivo JSON com os artigos e seus links.
- `artigos_encoinfo_com_kw.json`: Arquivo JSON com os artigos e suas palavras-chave extraídas.
- `artigos_encoinfo_com_kw_normalizadas.json`: Arquivo JSON com os artigos e suas palavras-chave normalizadas.

## Observações

- Certifique-se de configurar corretamente os parâmetros de conexão com o Neo4j no script `grafos.py`.
- Os scripts foram desenvolvidos e testados em ambiente Python 3.11.