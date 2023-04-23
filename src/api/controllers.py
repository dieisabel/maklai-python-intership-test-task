from flask import Blueprint
from flask import request
from nltk.tree import Tree

from api.schemas import TreeSchema
from services.paraphrase import paraphrase

blueprint = Blueprint("controllers", __name__)


@blueprint.route("/paraphrase", methods=["GET"])
def paraphrase_controller():
    limit = int(request.args.get("limit", 20))
    treebank = request.args.get("tree", None)
    if not treebank:
        error_message = {"error": {"message": "tree argument is required"}}
        return error_message, 400

    tree = Tree.fromstring(treebank)
    paraphrases = paraphrase(tree, limit)
    schema = TreeSchema()
    response = {
        "paraphrases": [schema.dump(tree) for tree in paraphrases],
    }
    return response, 200
