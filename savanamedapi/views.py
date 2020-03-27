import json

from flask import jsonify, request, abort, make_response
from flask_restful import Resource, Api

from savanamedapi import app

api_savana = Api(app)

lst_terms = [
                {
                    "descriptions": ["accidente cerebrovascular", "infarto cerebral"],
                    "parents": ["enfermedad cerebrovascular"],
                    "name": "ictus",
                    "id": 1
                },
                {
                    "descriptions": ["procedimiento quirurgico", "intervencion quirurgica"],
                    "parents": ["procedimiento"],
                    "name": "cirugia",
                    "id": 2
                },
                {
                    "descriptions": ["operacion en el corazon", "cardiocirugia"],
                    "parents": ["procedimiento en el corazon",
                                "procedimiento quirurgico cardiovascular"],
                    "name": "cirugia cardiaca",
                    "id": 3
                },
                {
                    "descriptions": ["embarazo en curso", "gestacion"],
                    "parents": ["hallazgo relacionado con el embarazo"],
                    "name": "embarazo",
                    "id": 4
                }
            ]


def get_terms_from_name(word_to_find):

    """
    Get all terms related to word_to_find(which name contains word_to_find)
    :param word_to_find: term to find which is contained in name key
    :return: list of terms which name has the word_to_find
    """

    terms = [{'name': term['name'], 'id': term['id']} for term in lst_terms if
             word_to_find in term['name']]
    return terms


def get_terms_from_id(term_id):

    """
    Get all terms which term id match with term_id
    :param term_id: term id
    :return: list of terms which id match with the term_id
    """

    detail_term = [term for term in lst_terms if term["id"] == term_id]
    return detail_term


@app.errorhandler(400)
def bad_request(error='Bad request'):
    return make_response(jsonify({'message': error.description}), 400)


@app.errorhandler(404)
def not_found(error={'description': 'Not found'}):
    return make_response(jsonify({'message': error.description}), 404)


class SavanaMedListAPI(Resource):
    """
    Class to manage all related to list query endpoint
    """
    @staticmethod
    def get():

        params = request.args
        if 'search' not in params:
            abort(400, {"description": "Search key not found in parameters"})
        else:
            terms = get_terms_from_name(params["search"])
            return jsonify({'terms': terms})
        terms = get_terms_from_name(params)

        return jsonify({'terms': terms})

    @staticmethod
    def post():

        data = request.get_data()
        json_data = json.loads(data)
        if 'search' not in json_data:
            abort(400, "Search key not found")
        else:
            terms = get_terms_from_name(json_data["search"])
            return jsonify({'terms': terms})


class SavanaMedDetailAPI(Resource):
    """
    Class to manage all related to detail endpoint
    """
    @staticmethod
    def get():
        params = request.args
        if 'id' not in params:
            abort(400, "Id key not found in parameters")
        else:
            detail_term = get_terms_from_id(int(params["id"]))

            return jsonify({'detail_term': detail_term})

    @staticmethod
    def post():
        data = request.get_data()
        json_data = json.loads(data)
        if 'id' not in json_data:
            abort(400, "Id key not found in parameters")
        else:
            terms = get_terms_from_id(json_data["id"])
            return jsonify({'detail_term': terms})


api_savana.add_resource(SavanaMedListAPI, '/savanamed/api/get_terms', endpoint='/search')


api_savana.add_resource(SavanaMedDetailAPI, '/savanamed/api/get_details', endpoint='/detail')

