from neo4j import GraphDatabase
import json

class GraphDB:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_participant(self, participant_name):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_and_return_participant, participant_name)
            return result

    def create_article(self, article_title, year, keyword):
        with self.driver.session() as session:
            result = session.write_transaction(self._create_and_return_article, article_title, year, keyword)
            return result

    def create_relationship(self, participant_name, article_title):
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_relationship, participant_name, article_title)

    @staticmethod
    def _create_and_return_participant(tx, participant_name):
        query = (
            "MERGE (p:Participant {name: $participant_name}) "
            "RETURN p"
        )
        result = tx.run(query, participant_name=participant_name)
        return result.single()[0]

    @staticmethod
    def _create_and_return_article(tx, article_title, year, keyword):
        query = (
            "CREATE (a:Article {title: $article_title, year: $year, keyword: $keyword}) "
            "RETURN a"
        )
        result = tx.run(query, article_title=article_title, year=year, keyword=keyword)
        return result.single()[0]

    @staticmethod
    def _create_and_return_relationship(tx, participant_name, article_title):
        query = (
            "MATCH (p:Participant {name: $participant_name}), "
            "(a:Article {title: $article_title}) "
            "MERGE (p)-[:CONTRIBUTED_TO]->(a)"
        )
        tx.run(query, participant_name=participant_name, article_title=article_title)


# Configurações do banco de dados
uri = "suaUri"
user = "seuUser"
password = "suaSenha"

db = GraphDB(uri, user, password)

with open('artigos_encoinfo_com_kw_normalizadas.json', 'r', encoding='utf-8') as file:
    articles_data = json.load(file)

for article in articles_data:
    title = article['Título']
    year = article['Ano']
    keyword = article['Palavra-chave']
    db.create_article(title, year, keyword)
    for participant_name in article['Membros']:
        db.create_participant(participant_name)
        db.create_relationship(participant_name, title)

db.close()