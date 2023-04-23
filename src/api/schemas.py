from marshmallow import Schema
from marshmallow import fields


class TreeSchema(Schema):
    tree = fields.Function(lambda tree: ' '.join(str(tree).split()))
