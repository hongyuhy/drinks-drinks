from flask import Flask
import flask
from flask_mysqldb import MySQL
import services.get_drinks_from_db
import services.add_drink_to_db

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)

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
    return services.get_drinks_from_db()

@app.route("/api/add_drinks", methods=['POST'])
def add_drinks():
    body = flask.request.get_json(force=True)
    name = body["name"]
    price = body["price"]
    services.add_drink_to_db(name, price)
    # TODO: some response
    return


@app.route("/api/complete_order", methods=['POST'])
def complete_order():
    #TODO
    return


@app.route("/test")
def test():
    cur = mysql.connection.cursor()
    # cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
    # cur.execute("")
    mysql.connection.commit()
    cur.close()
    return



if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    # app.run("0.0.0.0", port=80)
    app.run()

