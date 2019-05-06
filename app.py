from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with
from models import City, DBSession

app = Flask(__name__)
api = Api(app, prefix='')


city_fields = {
    'ID': fields.Raw,
    'Name': fields.Raw,
    'Population': fields.Raw,
    'CountryCode': fields.Raw,
    # 'District': fields.Raw,
}


class Cities(Resource):
    @marshal_with(city_fields)
    def get(self):
        session = DBSession()
        cities = session.query(City).all()
        cities_dict = [e.__dict__ for e in cities]
        return cities_dict


api.add_resource(Cities, '/Cities')

if __name__ == '__main__':
    app.run()
