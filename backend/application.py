from flask import Flask
import flask
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)

@app.route("/api/create_order", methods=['POST'])
def create_order():
    body = flask.request.get_json(force=True)
    venue = body["venue"]
    time = body["time"]
    orders = body["order"]
    return 0


@app.route("/api/get_menu", methods=['GET'])
def get_menu():
    return {
        "id": "drink_id",
        "drink_name": "milo",
        "price": 1.0
    }

@app.route("/api/get_orders", methods=['GET'])
def get_orders():
    return {
        "order": {
            "id": "drink_id",
            "drink_name": "milo",
            "price": 1.0,
            "status": "DElIVERED" # "UNDELIVERED"
        }
    }



if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    # app.run("0.0.0.0", port=80)
    app.run()

