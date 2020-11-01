## API For Ecom

___
### Required
    python3.6 or above


## installation

### local
    pip3 install -r requiremnts.txt
    python3 app.py


### DOCKER
    `sudo docker build --tag flask-api . `
    `sudo docker run flask-api:latest `

## Avalible Endpoints
- `/products`  - ["GET"]
- `/addproduct` - ["POST"]
- `/deleteproduct`  - ["DELETE"]
- `/updateproduct` - ["PATCH"]


## ENDPOINTS payloads -

`/products` - GET

    No need payload its just a GET request

____
`/addproduct` - POST



```curl
curl --location --request POST 'http://localhost:5000/addproduct' \
--header 'Content-Type: application/json' \
--data-raw '{"name": "new product 01",
"brand_name": "john lewis & partners",
"regular_price_value": 99,
"offer_price_value": 99,
"currency": "GBP",
"classification_l1": "women",
"classification_l2": "women'\''s knitwear",
"classification_l3": "",
"classification_l4": "",
"image_url": "https://johnlewis.scene7.com/is/image/JohnLewis/004193458?"
}'
```
_____
`/updateproduct` -PATCH

```curl
curl --location --request PATCH 'http://localhost:5000/updateproduct' \
--header 'Content-Type: application/json' \
--data-raw '{"which":{"name": "0012"},
"new":{"name":"updated name"}
}'
```
___
`/deleteproduct` - DELETE
### It takes id of product
```curl
curl --location --request DELETE 'http://localhost:5000/deleteproduct' \
--header 'Content-Type: application/json' \
--data-raw '{"id":"5f7ecc5cb42497611c6f090b"}'
```






___
# Payload Sample For post request
# (classification l1 , l2 , l3 , l4  `optionals` )and others are `required`
___
```json
{
"name": "0012",
"brand_name": "jellycat",
"regular_price_value": 12,
"offer_price_value": 12,
"currency": "GBP",
"classification_l1": "baby & child",
"classification_l2": "soft toys",
"classification_l3": "",
"classification_l4": "",
"image_url": "https://johnlewis.scene7.com/is/image/JohnLewis/237070760?"
}

```

