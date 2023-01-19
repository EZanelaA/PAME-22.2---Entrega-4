from flask import Blueprint
from .controller import UserController, UserDetails, ProductController, ProductDetails

user_api = Blueprint("user_api", __name__)

user_api.add_url_rule(
    "/users",
    view_func = UserController.as_view("users_controller"),
    methods = ["GET"]
)

user_api.add_url_rule(
    "/users/<int:id>",
    view_func = UserDetails.as_view("users_details"),
    methods = ["GET"]
)

user_api.add_url_rule(
    "/products",
    view_func = ProductController.as_view("products_controller"),
    methods = ["GET"]
)

user_api.add_url_rule(
    "/products/<int:id>",
    view_func = ProductDetails.as_view("products_details"),
    methods = ["GET"]
)
