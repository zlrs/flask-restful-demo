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
    'District': fields.Raw,
}
# {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x0000025D3393B0F0>,
# 'ID': 1, 'District': 'Kabol', 'Name': 'Kabul', 'Population': 1780000, 'CountryCode': 'AFG'}


class Cities(Resource):
    @marshal_with(city_fields)
    def get(self):
        session = DBSession()
        cities = session.query(City).limit(20).all()  # list
        cities_dict = [e.__dict__ for e in cities]    # list
        print(cities[0])
        print(dir(cities[0]))
        print(cities_dict[0])
        return cities_dict


api.add_resource(Cities, '/Cities')

if __name__ == '__main__':
    app.run()
