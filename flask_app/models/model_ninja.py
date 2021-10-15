from flask_app.config.mysqlconnection import connectToMySQL# model the class after the friend table from our database
DATABASE = 'dojos_and_ninjas_db'
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        ninjas = []
        # Iterate over the db results and create instances of friends with cls.
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas ( first_name , last_name , age , dojo_id, created_at , updated_at ) VALUES ( %(fname)s , %(lname)s , %(age)s , %(dojo_id)s, NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )