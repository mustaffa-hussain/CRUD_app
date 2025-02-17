## API For Ecom

___
### Required
    python3.6 or above


## installation

### local
    pip3 install -r requiremnts.txt
    python3 app.py


### DOCKER
    `sudo docker build --tag crudapp . `
    `sudo docker run crudapp:latest`

## Avalible Endpoints
- `/products`  - ["GET"]
- `/addproduct` - ["POST"]
- `/deleteproduct`  - ["DELETE"]
- `/updateproduct` - ["PATCH"]

## Document schema (keys) in DB

```json
{
"name": "str",
"brand_name": "str",
"regular_price_value": "float",
"offer_price_value": "float",
"currency": "str",
"classification_l1": "str",
"classification_l2": "str",
"classification_l3": "str",
"classification_l4": "str",
"image_url": "str"
}

```


## Data to be send with the requests -

`/products` - GET <br>
    The endpoint to retrive data from DB.<br>
    It send all the product data. the functionality can further be improved to send specific data.

____
`/addproduct` - POST <br>
    The endpoint to add entry to DB.<br>
    You can add document to MongoDB. Send in the JSON in the body of the request.
    Note: these are necessary keys. If not send, the end point returns an error. other keys can be added along with these keys.
    
    An example json : 
    {"name": "mustaffa test",
      "brand_name": "mustaffa test 1",
      "regular_price_value": 99,
      "offer_price_value": 99,
      "currency": "INR",
      "classification_l1": "men",
      "image_url": "https://mustaffa-hussain.github.io/Portfolio/"
      }


_____
`/updateproduct` -PATCH <br>
    The endpoint to update entry in DB.<br>
    You can update the entries in db by sending. Send the JSON of 'which' and 'new' in the body of request. <br>
    Key -> which is used to identify the document in db that is to be updated.<br>
    key -> new is used to update the entry
    
    An example json : 
    {"which":{"name": "mustaffa test"},
      "new":{"name":"mustaffa name updated"}
      }

____

`/deleteproduct` - DELETE <br>
    The endpoint to delete an entry from DB. It take the id to delete the document.
    Send the JSOn in the body.
    
    An example json : 
    {"id":"5f9ec0ffc675c3202c31656f"}

___

## Screenshots are in `Screenshots` folder. check them out for working samples.

