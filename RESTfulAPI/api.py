from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello API World!"

@app.route('/developer/api/v1.0/pattern', methods=['GET'])
def getcheck():
    newget = loadfile()
    if request.method == 'GET':
        results = newget
    return results

@app.route('/developer/api/v1.0/pattern', methods=['POST'])
def uploadNew():
    return "upload success"


@app.errorhandler(404)
def not_found(error)
    return "Not Found"

def loadfile():
    db = open("jsonContent.json", encoding='utf-8')
    content = json.load(db)
    return content




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

