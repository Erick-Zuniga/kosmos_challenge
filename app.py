import spacy
from flask import Flask
from flask_restful import Api
from ner import NER

app = Flask(__name__)
api = Api(app)

# Haciendo carga del modelo aquí para no tener que cargarlo cada vez que se necesite
nlp = spacy.load("es_core_news_sm")

# Ruta para el post. De paso se le pasa al modelo de Spacy a la clase
api.add_resource(NER, '/ner', resource_class_kwargs={"nlp": nlp})

if __name__ == '__main__':
    app.run(debug=True)
