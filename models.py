from peewee import *

db = PostgresqlDatabase(
    'countries',
    host = 'localhost',
    port = '5432',
    user = 'milka',
    password = '123'
)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Countries(BaseModel):
    name = CharField(null = False)
    official_name = CharField(null = False)
    capital = CharField( null = False)
    region =  CharField( null = False)
    subregion = CharField( null = False)
    population = IntegerField(null = False)
    continents = CharField( null = False)
    timezones = CharField( null = False)
    
   





db.create_tables([Countries])