from flask import jsonify, request
from flask_restful import Resource


class NER(Resource):
    def __init__(self, **kwargs):
        # Guardamos el modelo de spacy
        self.nlp = kwargs["nlp"]

    def post(self):
        # Obtenemos las oraciones
        data = request.get_json()
        sentences = data["oraciones"]

        response = {"resultado": []}
        for s in sentences:
            doc = self.nlp(s)

            # Extraemos las entidades nombradas con sus respectivas etiquetas para cada oración
            entities = {}
            for ent in doc.ents:
                entities[ent.text] = ent.label_
            
            response["resultado"].append(
                {
                    "oración": s,
                    "entidades": entities
                }
            )

        return jsonify(response)