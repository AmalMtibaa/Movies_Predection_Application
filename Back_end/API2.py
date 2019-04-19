from flask_jsonpify import jsonify
from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
import sys
from io import StringIO
import contextlib
from All_algorithms import *
from Predection import *


app = Flask(__name__)
api = Api(app)
app.debug = True
CORS(app)

@app.route('/', methods=['POST'])
def predict():
    if request.method == "POST":
        content = request.get_json()
        algo_id=int(content["algorithme_id"])
        del content["algorithme_id"]
        print("content", content)
        p=PrepareDataForPredection(algo_id,content)
        predection=""
        if p==0:
            predection="Flop"
        if p==1:
            predection="Average"
        if p==2:
            predection="Hit"
        if p==3:
            predection="Super-Hit"
        if p==4:
            predection="BlockBuster"
        return jsonify({'predection': predection})


@app.route('/evaluation/<id>', methods=['GET'])
def errorrange(id):
    if request.method == "GET":
        id=int(id)
        error=str(errorRange(id))
        if(id==0):
            return jsonify({'error_value': error})
        if (id == 1):
            return jsonify({'error_value': error})
        if (id == 2):
            return jsonify({'error_value': error})
        if (id == 3):
            return jsonify({'error_value': error})
        else:
            return jsonify({'some_message': "Error !"})

@app.route('/getFirstFiveLines', methods=['GET'])
def getFirstFive():
    if request.method == "GET":
        print(dataset1[:5].values.tolist())
        return jsonify({'firstFive': dataset1[:5].values.tolist()})



@app.route('/example/<id>', methods=['GET'])
def predictExemple(id):
    if request.method == "GET":
        from sklearn.ensemble import RandomForestClassifier
        nb2=RandomForestClassifier(n_estimators=20, max_depth=4, bootstrap=True, random_state=0)
        nb2.fit(X_train[5:], y_train[5:])
        P = nb2.predict(X_train[:5])
        p=P.item(int(id))
        trueValues=y_train[:5]
        predection = ""
        if p == 0:
            predection = "Flop"
        if p == 1:
            predection = "Average"
        if p == 2:
            predection = "Hit"
        if p == 3:
            predection = "Super-Hit"
        if p == 4:
            predection = "BlockBuster"
        isTrue=False
        if p==trueValues[int(id)]:
            isTrue=True
        return jsonify({'predection': predection,'isTrue':isTrue})


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


if __name__ == '__main__':
     app.run(port=5002)