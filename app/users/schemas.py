from app.extensions import ma

class UserSchemas(ma.Schema):
    id = ma.Integer(dump_only = True)
    username = ma.String(required = True)
    status = ma.String(required = True)

class ProductSchemas(ma.Schema):
    id = ma.Integer(dump_only = True)
    item = ma.String(required = True)
    price = ma.Integer(required = True)
    size = ma.String(required = True)
    quantity = ma.Integer(required = True)