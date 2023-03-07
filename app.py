# -*- coding: utf-8 -*-
import os
from flask import Flask, request, Response
from flask_cors import CORS 
import yaml
import json

with open('config/dev.yaml', 'r',encoding="utf-8") as f:
    config = yaml.load(f, Loader=yaml.Loader)


app = Flask(__name__, static_folder='static')
cors = CORS(app) 


@app.route('/sample', methods=['GET', 'POST'])
def sample_func():

    res = {
        'code': 200,
        'msg': 'success'
    }
    return Response(response=json.dumps(res, indent = 4), status=200, content_type='application/json')




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
