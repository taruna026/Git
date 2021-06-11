from flask import Flask, request
from service import getPersonInfo

app = Flask(__name__)



@app.route('/person/find', methods=['GET'])
def func():
    return getPersonInfo(request)

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 105)