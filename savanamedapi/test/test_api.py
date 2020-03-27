from unittest import TestCase
import json


from savanamedapi import app


class TestApi(TestCase):

    def setUp(self):
        self.test_client = app.test_client(self)

    def test_list_api_cancer(self):

        param_to_sent = {"search": "cancer"}

        resp = self.test_client.post("/savanamed/api/get_terms", data=json.dumps(param_to_sent))
        data = json.loads(resp.data.decode())

        self.assertEqual(len(data["terms"]), 0)

        resp = self.test_client.get("/savanamed/api/get_terms", query_string=param_to_sent)
        data = json.loads(resp.data.decode())

        self.assertEqual(len(data["terms"]), 0)

    def test_list_api_embarazo(self):

        param_to_sent = {"search": "embarazo"}

        resp = self.test_client.post("/savanamed/api/get_terms", data=json.dumps(param_to_sent))
        data = json.loads(resp.data.decode())

        self.assertEqual(len(data["terms"]), 1)

        self.assertEqual(data['terms'][0]['name'], 'embarazo')
        self.assertEqual(data['terms'][0]['id'], 4)

        resp = self.test_client.get("/savanamed/api/get_terms", query_string=param_to_sent)
        data = json.loads(resp.data.decode())

        self.assertEqual(len(data["terms"]), 1)

        self.assertEqual(data['terms'][0]['name'], 'embarazo')
        self.assertEqual(data['terms'][0]['id'], 4)

    def test_list_api_cirugia(self):

        param_to_sent = {"search": "cirugia"}

        resp = self.test_client.post("/savanamed/api/get_terms", data=json.dumps(param_to_sent))
        data = json.loads(resp.data.decode())

        self.assertEqual(len(data["terms"]), 2)

        self.assertEqual(data['terms'][0]['name'], 'cirugia')
        self.assertEqual(data['terms'][0]['id'], 2)
        self.assertEqual(data['terms'][1]['name'], 'cirugia cardiaca')
        self.assertEqual(data['terms'][1]['id'], 3)

        resp = self.test_client.get("/savanamed/api/get_terms", query_string=param_to_sent)
        data = json.loads(resp.data.decode())

        self.assertEqual(len(data["terms"]), 2)

        self.assertEqual(data['terms'][0]['name'], 'cirugia')
        self.assertEqual(data['terms'][0]['id'], 2)
        self.assertEqual(data['terms'][1]['name'], 'cirugia cardiaca')
        self.assertEqual(data['terms'][1]['id'], 3)

    def test_list_api_param_wrong(self):
        param_to_sent = {"searching": "cancer"}

        resp = self.test_client.post("/savanamed/api/get_terms", data=json.dumps(param_to_sent))
        data = json.loads(resp.data.decode())

        self.assertEqual(data["message"], "Search key not found")

    def test_detail_api(self):

        param_to_sent = {"id": 1}

        resp = self.test_client.post("/savanamed/api/get_details", data=json.dumps(param_to_sent))
        data = json.loads(resp.data.decode())

        self.assertEqual(data['detail_term'][0]['name'], 'ictus')
        self.assertEqual(len(data['detail_term'][0]['descriptions']), 2)

        resp = self.test_client.get("/savanamed/api/get_details", query_string=param_to_sent)
        data = json.loads(resp.data.decode())

        self.assertEqual(data['detail_term'][0]['name'], 'ictus')
        self.assertEqual(len(data['detail_term'][0]['descriptions']), 2)

    def test_detail_api_param_wrong(self):
        param_to_sent = {"ident": 1}

        resp = self.test_client.post("/savanamed/api/get_details", data=json.dumps(param_to_sent))
        data = json.loads(resp.data.decode())

        self.assertEqual(data["message"], "Id key not found in parameters")

    def test_detail_api_id_not_found(self):
        param_to_sent = {"id": 7}

        resp = self.test_client.post("/savanamed/api/get_details", data=json.dumps(param_to_sent))
        data = json.loads(resp.data.decode())
        self.assertEqual(len(data['detail_term']), 0)

    def test_endpoint_not_exist(self):
        param_to_sent = {"id": 1}

        resp = self.test_client.post("/savanamed/api/get_descriptions", data=json.dumps(param_to_sent))
        data = json.loads(resp.data.decode())
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(data['message'],
                         "The requested URL was not found on the server. If you entered the URL "
                         "manually please check your spelling and try again.")
