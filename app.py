from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

BACKEND_URL = 'https://tuxts-backend.herokuapp.com/'

@app.route('/texts', methods=['GET'])
def get_texts():
    date = request.args.get('date', '')
    r = requests.get(BACKEND_URL + 'texts.json', params={'date': date})
    texts = [replace_url(text) for text in r.json()]
    return jsonify(texts)

@app.route('/texts', methods=['POST'])
def post_text():
    r = requests.post(BACKEND_URL + 'texts.json', json=request.json)
    text = replace_url(r.json())
    return jsonify(text)

@app.route('/texts/<int:id>', methods=['GET'])
def get_text(id):
    r = requests.get(BACKEND_URL + 'texts/{}.json'.format(id))
    text = replace_url(r.json())
    return jsonify(text)

@app.route('/texts/<int:id>', methods=['PUT'])
def put_text(id):
    r = requests.put(BACKEND_URL + 'texts/{}.json'.format(id), json=request.json)
    text = replace_url(r.json())
    return jsonify(text)

@app.route('/texts/<int:id>', methods=['DELETE'])
def delete_text(id):
    r = requests.delete(BACKEND_URL + 'texts/{}.json'.format(id))
    return '', 204

def replace_url(text):
    text['url'] = request.host_url + 'texts/{}'.format(text['id'])
    return text
