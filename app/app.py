import json

import jsonpickle as jsonpickle
from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api
from deepparse.parser import AddressParser, FormattedParsedAddress

app = Flask(__name__)
api = Api(app)
address_parser = AddressParser(model_type='best', device='cpu')


def main():
    app.run(host='0.0.0.0', port=5000)


class ErrorResponse:
    def __init__(self, error):
        self.error = error

    def toJson(self):
        return jsonpickle.encode(self, unpicklable=False)


def parseAddress(addr, with_probability):
    fpa = address_parser(addr, with_prob=with_probability)
    return ParsedAddress(fpa.raw_address, fpa.to_dict(), fpa.address_parsed_components, with_probability)


def jsonResponse(response, status):
    return Response(response, status=status, mimetype='application/json')


class ParsedAddress:
    def __init__(self, raw_address, parsed_address, parsed_address_components, with_probability):
        self.raw_address = raw_address
        self.parsed_address = parsed_address
        self.parsed_address_components = []
        if with_probability:
            for tpl in parsed_address_components:
                value = tpl[0]
                component = tpl[1][0]
                probability = tpl[1][1]
                self.parsed_address_components.append(AddressComponent(component, value, probability))
        else:
            for tpl in parsed_address_components:
                value = tpl[0]
                component = tpl[1]
                self.parsed_address_components.append(AddressComponent(component, value, None))

    def toJson(self):
        return jsonpickle.encode(self, unpicklable=False)


class AddressComponent:
    def __init__(self, component, value, probability):
        self.name = component
        self.value = value
        self.probability = probability

    def toJson(self):
        return jsonpickle.encode(self, unpicklable=False)


@app.route('/parse-address', methods=['POST'])
def parse_address():
    try:
        req_data = json.loads(request.data)
        address_to_parse = req_data['address']
        probability = req_data.get('probability')
    except:
        error_response = ErrorResponse("Cannot read address from request")
        return jsonResponse(error_response.toJson(), 400)

    with_probability = False

    if not (probability is None):
        with_probability = probability

    try:
        parsed_address = parseAddress(address_to_parse, with_probability)
        return jsonResponse(parsed_address.toJson(), status=200)
    except:
        error_response = ErrorResponse("Cannot parse address")
        return jsonResponse(error_response.toJson(), 400)
