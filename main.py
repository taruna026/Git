from flask import Flask, request
import os
from service import getPersonInfo

app = Flask(__name__)



@app.route('/person/find', methods=['GET'])
def func():
    return getPersonInfo(request)

    

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port = port)