from ..extensions import ma
from marshmallow import Schema, fields, validate

class UserSchema(ma.Schema):
    id = fields.String(dump_only=True)
    name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True, load_only=True)
    role = fields.String(
        load_default="user",
        validate=validate.Oneof(["admin", "user"])
    )
