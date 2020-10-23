from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

hoteis = [
        {
        'hotel_id': '"alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
        },
         {
        'hotel_id': '"bravo',
        'nome': 'Brevo Hotel',
        'estrelas': 4.4,
        'diaria': 480.90, 
        'cidade': 'Santa Catarina'
        },
        {
        'hotel_id': '"charlie',
        'nome': 'Charlie Hotel',
        'estrelas': 3.9,
        'diaria': 320.20,    
        'cidade': 'Salvador'
        }
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

api.add_resource(Hoteis, '/hoteis')


if __name__ == '__main__':
    app.run(debug=True)