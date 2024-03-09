from config import app,db
from flask import request
from model import Product
#uri --> http://localhost:5000/api/v1/product/  -- GET

import json
@app.route('/api/v1/product/',methods=['GET'])
def get_list_of_products():
    #fetch list of products from db -- thru sqlalchemy
    product_list = Product.query.all()

    #if no products in db -- return -- simple message --
    if not product_list:
        return json.dumps({"ERROR" : "No Products...!"})

    final_product_list = []
    #iterate one by and prepare dict -
    for prod in product_list:
        prod_dict = {}
        prod_dict['PRODUCT_ID'] = prod.id
        prod_dict['PRODUCT_NAME'] = prod.name
        prod_dict['PRODUCT_PRICE'] = prod.price
        prod_dict['PRODUCT_QTY'] = prod.qty
        prod_dict['PRODUCT_VENDOR'] = prod.vendor
        prod_dict['PRODUCT_CATEGORY'] = prod.category

        #add that dict every time inside final list
        final_product_list.append(prod_dict)

    if final_product_list:
        return json.dumps(final_product_list)





#http://localhost:5000/api/v1/product/  -- POST

@app.route('/api/v1/product/',methods=['POST'])
def save_product():

    print(dir(request))