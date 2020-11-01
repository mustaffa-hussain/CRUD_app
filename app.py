#librarires
from flask import Flask,jsonify,request,Response
from bson import json_util
import json

#custom scripts
from db_functions import database         #db functions script

app = Flask(__name__)

db = database()                           #gets the db connection object



@app.route('/products',methods=["GET"])
def root():
    '''
    Function to get the results from DB.
    Only 'GET' method is needed as only fetching is happeneing.

    '''
    try:
        _data = db.get()

        return Response(
            json_util.dumps(_data).replace("NaN", "null"),
            mimetype='application/json'
        )

    except Exception as e:
        return jsonify({"error": str(e)}),500



# create new product
@app.route("/addproduct",methods = ["POST"])
def insertProduct():
    '''
    Function to add entry to DB.
    Only 'POST' used as whole object is entered.

    '''

    payload = request.get_json()

    try:
        name = payload["name"]
        brand_name = payload["brand_name"]
        regular_price_value = payload["regular_price_value"]
        offer_price_value = payload["offer_price_value"]
        currency = payload["currency"]

        image_url = payload["image_url"]

        classification_l1 = payload.get("classification_l1", "")
        classification_l2 = payload.get("classification_l2", "")
        classification_l3 = payload.get("classification_l3", "")
        classification_l4 = payload.get("classification_l4", "")
    except KeyError:
        return jsonify({"error":"make sure all params are given"})

    insert_query = {
            "name":name,
            "brand_name":brand_name,
            "regular_price_value": regular_price_value,
            "offer_price_value":offer_price_value,
            "currency":currency,
            "image_url":image_url,
            "classification_l1":classification_l1,
            "classification_l2":classification_l2,
            "classification_l3":classification_l3,
            "classification_l4":classification_l4
            }
    res = db.insert(insert_query)
    print(res.inserted_id)

    return jsonify({"status": "success", "id": str(res.inserted_id)})


@app.route("/deleteproduct", methods= ["DELETE"])
def delete_product():
    '''
    Function to delete an entry from DB.
    only 'DELETE' method used to delete whole entry from db.
    '''
    _data = request.get_json()
    try:
        _delid = _data["id"]

    except KeyError:
        return jsonify({"error":"provide id to delete it"})
    # print(db.find_one(_delid))

    delete_result = db.find_one_and_delete(_delid)

    if delete_result:
        return Response(
            json_util.dumps({"status": "success", "data": delete_result}).replace("NaN", "null"),
            mimetype='application/json'
        )

    else:

        return jsonify({"status": "denied", "reason": "product not found"})


@app.route("/updateproduct", methods=["PATCH"])
def update_product():
    '''
    Function to update a an entry from DB.
    Method Patch used as partial update/complete update both are possible.
    '''
    _json_data = request.get_json()
    try:

        old_data  = _json_data["which"]
        new_data   = _json_data["new"]
    except KeyError:

        return jsonify({"status":"denied","reason":"required value not provied"})

    updated_result  = db.find_one_and_update(old_data,new_data)
    if updated_result:
        return Response(
            json_util.dumps({"status": "success", "data": updated_result}).replace(
                "NaN", "null"),
            mimetype='application/json'
        )

    else:

        return jsonify({"status": "denied", "reason": "product not found"})






app.run(debug=True,port=5010)



