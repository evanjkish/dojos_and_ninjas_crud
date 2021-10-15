from flask_app.config.mysqlconnection import connectToMySQL# model the class after the friend table from our database
from flask_app.models.model_ninja import Ninja
DATABASE = 'dojos_and_ninjas_db'
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos ( name , created_at , updated_at ) \
        VALUES ( %(dname)s , NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )

    @classmethod
    def get_dojo_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id \
        WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db( query, data )
        dojo = cls(results[0])
        for ninja in results:
            dojo.ninjas.append(Ninja(ninja))

        return dojo
