from flask import Blueprint


blueprint = Blueprint("controllers", __name__)


@blueprint.route("/paraphrase")
def paraphrase():
    return {"hello": "world!"}
