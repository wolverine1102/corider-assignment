from ..extensions import ma
from marshmallow import Schema, fields, validate

class UserSchema(ma.Schema):
    id = fields.String(dump_only=True)
    name = fields.String()
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True)
    role = fields.String(
        load_default="user",
        validate=validate.OneOf(["admin", "user"])
    )

user_schema = UserSchema()
users_schema = UserSchema(many=True)