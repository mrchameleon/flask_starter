from flask import Blueprint, render_template, request, jsonify

from models import User

route_blueprint = Blueprint('route', __name__,)


@route_blueprint.route('/', methods=['GET'])
def home():
    users = User.query.all()
    return render_template("index.html", app_name="Flask Starter", users=users)

@route_blueprint.route('/ping', methods=['GET'])
def ping():
    return jsonify(
        {"status": "success", "detail": "pong!"}
    )


@route_blueprint.route('/post', methods=['POST'])
def post():
    # the post endpoint just returns back exactly what was sent to it.
    data = request.json
    return jsonify(
        data
    )
