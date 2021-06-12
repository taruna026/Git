from flask import Flask, request, json
import os
from service import getPersonInfo, updatePersonById

app = Flask(__name__)


@app.route('/person', methods=['GET','PUT'])
def func():
    print('===============')
    if request.method=='GET':
        return getPersonInfo(request)
    elif request.method=='PUT':
        return updatePersonById(request.args.get('id'), json.loads(request.data))

@app.route('/webhook', methods=['GET', 'POST'])
def service():
    print('===shakndka', json.loads(request.data))
    return json.loads(request.data))

    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port = port)