from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from flask_pymongo import PyMongo

from database_fn import database
db = database()



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://greendeck:wFiLryTvunPBa6sx@mustaffa-app.ddqdx.mongodb.net/testdb_4_green_deck?retryWrites=true&w=majority"
mongo = PyMongo(app)
api = Api(app)

#Configuring collection name we are going to work with
#db_operations = mongo.db.<COLLECTION_NAME>
greendeck_data = mongo.db.greendeck_data 

class TodoSimple(Resource):
    def get(self):
        return {"todo_id": "hello mustaffa - tell me how it feels"}

    # def put(self, todo_id):
    #     todos[todo_id] = request.form['data']
    #     return {todo_id: todos[todo_id]}



#crud operations
#create
create_parser = reqparse.RequestParser()
create_parser.add_argument('task')

class create_entry(Resource):
    def put(self):
        data = create_parser.parse_args()

        result={"test":"inserted successfully "}
        return (result)









#routes are mentioned here 
api.add_resource(TodoSimple, '/test')

if __name__ == '__main__':
    app.run(debug=True, port=5001)