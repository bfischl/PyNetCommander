#!/usr/bin/env python3
import json
from flask import Flask, jsonify, make_response, request, abort
from master_lib.Models import *


app = Flask(__name__)


def load_settings(filename):
    with open(filename, encoding='utf-8') as f:
        tmp_settings = json.load(f)
    return tmp_settings


def load_tasks_from_file(filename):
    tasks = [{
        "task_id": 1,
        "sheep_id": 1
    }]
    return tasks


@app.errorhandler(401)
def unauthorized(error):
    # TODO add IP to bad boy list
    return make_response(jsonify({'error':'Not authorized'}),401)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)


@app.route('/api/1/tasks/<int:minion_hash>', methods=['GET'])
def get_tasks(minion_hash):
    return jsonify(query_tasks(minion_hash))


@app.route('/api/1/tasks/<int:task_id>', methods=['POST'])
def post_status(task_id):
    return jsonify(update_status(task_id,request.json["status"], request.json["results"]))


@app.route('/api/1/register', methods=['POST'])
def register_new():
    if not request.json:
        abort(400)
    tmp_hash = register_minion(request.remote_addr, request.json["mac"], request.json["platform"])
    if tmp_hash < 0:
        return abort(500)
    else:
        return jsonify({"hashcode":tmp_hash}), 201


if __name__ == '__main__':
    settings = load_settings('master_settings.json')
    tasks = load_tasks_from_file(settings['tasks.json'])
    app.run(settings['host'], settings['port'])
