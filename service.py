from flask import Flask, request, json
import requests

PIPERDRIVE_BASE_URL='https://api.pipedrive.com/v1/persons/'
API_KEY='243772d23c4e2c22e4fcd63a487190f5b3823f06'

def getPersonInfo(request):
    if request.args.get('id'):
        return getPersonInfoById(request.args.get('id'))
    elif request.args.get('name'):
        return getPersonInfoByName(request.args.get('name'))
    else:
        return 'Enter correct query params'


def getPersonInfoById(id):
    data = requests.get(f"{PIPERDRIVE_BASE_URL}{id}?api_token={API_KEY}")
    return json.loads(data.content)


def getPersonInfoByName(name):
    data = requests.get(f"{PIPERDRIVE_BASE_URL}find?term={name}&api_token={API_KEY}")
    return json.loads(data.content)