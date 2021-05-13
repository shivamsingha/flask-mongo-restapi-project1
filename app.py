from models import db, AddressBook
from flask import Flask, jsonify, request
from mongoengine.queryset.visitor import Q

app = Flask(__name__)
app.config.from_object(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": "test123"}
app.config["TESTING"] = True
app.config["SECRET_KEY"] = "secret"

db.init_app(app)

@app.route("/", methods=['GET', 'POST', 'PATCH', 'DELETE'])
def crud():
    if request.method == 'POST':
        if request.is_json:
            req = request.get_json()
            data=AddressBook(**req).save()
            return jsonify(data), 200
        else:
            return "Request was not JSON", 400
    
    if request.method == 'DELETE':
        if request.is_json:
            req = request.get_json()
            if 'id' in req:
                data=AddressBook.objects(id=req['id']).delete()
                return '', 200
            else:
                return 'Not Found', 404
        else:
            return "Request was not JSON", 400
    
    if request.method == 'GET':
        args=request.args
        if 'q' in args:
            q=args['q']
            return jsonify(AddressBook.objects(Q(name__icontains=q)|Q(address__icontains=q)|Q(city__icontains=q)|Q(state__icontains=q)|Q(country__icontains=q)))
        else:
            return jsonify(AddressBook.objects(**args))
    
    if request.method == 'PATCH':
        if request.is_json:
            req = request.get_json()
            if 'id' in req:
                AddressBook.objects(id=req['id']).update_one(**req)
                data=AddressBook.objects(id=req['id'])
                return jsonify(data), 200
            else:
                return 'Not Found', 404
        else:
            return "Request was not JSON", 400

    return '', 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
