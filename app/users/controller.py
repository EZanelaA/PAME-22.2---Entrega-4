from flask import request
from flask.views import MethodView
from .models import users, products
from .schemas import UserSchemas, ProductSchemas

def getLastId(list):
    lastUser = list[-1]
    return lastUser["id"]

class UserController(MethodView):
    def get(self):
        schema = UserSchemas()
        return schema.dump(users, many = True), 200

class UserDetails(MethodView):
    def get(self, id):
        schema = UserSchemas()
        for user in users:
            if user["id"] == id:
                return schema.dump(user), 200
        return {}, 404

class ProductController(MethodView):
    def get(self):
        schema = ProductSchemas()
        return schema.dump(products, many = True), 200

class ProductDetails(MethodView):
    def get(self, id):
        schema = ProductSchemas()
        for product in products:
            if product["id"] == id:
                return schema.dump(product), 200
        return {}, 404