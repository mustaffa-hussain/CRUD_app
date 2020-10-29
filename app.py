#Add Flask-PyMongo to our app
from flask import Flask, jsonify, request, redirect
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://greendeck:wFiLryTvunPBa6sx@mustaffa-app.ddqdx.mongodb.net/testdb_4_green_deck?retryWrites=true&w=majority"
mongo = PyMongo(app)

#Configuring collection name we are going to work with
#db_operations = mongo.db.<COLLECTION_NAME>
db_operations = mongo.db.greendeck_data 


@app.route('/test')
def home():
    '''
    initail test route fn
    '''
    print("hello mustaffa, lets get coding now")
    result={"returned output":"all went well"}
    return result


@app.route('/create/<int:year>/<int:month>/<title>')
def create():
    new_user = {'Name' : 'xyz', 'Age' : 20}
    db_operations.insert_one(new_user)
    #print(user['Name'],'Created successfully')
    result = {'result' : 'Created successfully'}
    return jsonify(result)
    # return result



#CRUD Operations

#Create

@app.route('/create')
def create():
    new_user = {'Name' : 'xyz', 'Age' : 20}
    db_operations.insert_one(new_user)
    #print(user['Name'],'Created successfully')
    result = {'result' : 'Created successfully'}
    return jsonify(result)
    # return result


@app.route('/create-many')
def create_many():
    new_user_1 = {'Name' : 'xyz1', 'Age' : 10}
    new_user_2 = {'Name' : 'xyz2', 'Age' : 20}
    new_user_3 = {'Name' : 'xyz3', 'Age' : 30}
    new_users = [new_user_1, new_user_2, new_user_3]
    db_operations.insert_many(new_users)
    result = {'result' : 'Created successfully'}
    return result

#Read

@app.route('/read')
def read_all():
    '''
    the funtion return all the documents in the collection.
    input: None
    output: dict 
    '''
    users = db_operations.find()
    output = [{'Name' : user['name'], 'Brand_name' : user['brand_name']} for user in users]
    #print(output)
    return jsonify(output)

@app.route('/read-with-filter')
def read_with_filter():
    filt = {'Name' : 'xyz'}
    users = db_operations.find(filt)
    output = [{'Name' : user['Name'], 'Age' : user['Age']} for user in users]
    #print(output)
    return jsonify(output)

@app.route('/read-one')
def read_one():
    filt = {'Name' : 'xyz'}
    user = db_operations.find_one(filt)
    output = {'Name' : user['Name'], 'Age' : user['Age']}
    #print(output)
    return jsonify(output)

#Update

@app.route('/update')
def update():
    updated_user = {"$set": {'Age' : 30}}
    filt = {'Name' : 'xyz'}
    db_operations.update_one(filt, updated_user)
    result = {'result' : 'Updated successfully'}
    return result

@app.route('/update-many')
def update_many():
    updated_user = {"$set": {'Age' : 30}}
    filt = {'Name' : 'xyz'}
    db_operations.update_many(filt, updated_user)
    result = {'result' : 'Updated successfully'}
    return result

@app.route('/update-if-exist-or-insert')
def update_if_exist_or_insert():
    updated_user = {"$set": {'Age' : 30}}
    filt = {'Name' : 'xyz'}
    db_operations.update_one(filt, updated_user, upsert=True)
    result = {'result' : 'Done successfully'}
    return result

#Delete

@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    filt = {'Name' : 'xyz'}
    db_operations.delete_one(filt)
    result = {'result' : 'Deleted successfully'}
    return result

@app.route('/delete-many')
def delete_many():
    filt = {'Name' : 'xyz'}
    db_operations.delete_many(filt)
    result = {'result' : 'Deleted successfully'}
    return result

#Saving and retrieving files



@app.route('/save-file', methods=['POST'])
def save_file():
    if 'new_file' in request.files:
        new_file = request.files['new_file']
        mongo.save_file(new_file.filename, new_file)
        data = {'Name' : request.values.get('name'), 'File Name' : new_file.filename}
        db_operations.insert(data)
    return redirect('/')

@app.route('/retrieve-file/<name>')
def retrieve_file(name):
    filt = {'Name' : name}
    f = db_operations.find_one(filt)
    file_name = f['File Name']
    return mongo.send_file(file_name)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

