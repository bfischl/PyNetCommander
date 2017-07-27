#!/usr/bin/env python3
import json
from flask import Flask, jsonify, make_response, request, abort
from master_lib.Models import *
# TODO Implement Database


app = Flask(__name__)


class local_minion:
    """
    This is just a temporary object for the master to view. It doesn't do anything but calculate a hash
    """
    def __init__(self, id, ip, mac, platform):
        self.sheep_id = id
        self.ip = ip
        self.mac = mac
        self.platform = platform
        self.hashcode = None

    def gethash(self):
        if self.hashcode:
            return self.hashcode
        else:
            # TODO Implement hashing function
            self.hashcode="test"
            return self.hashcode


def load_settings(filename):
    with open(filename, encoding='utf-8') as f:
        tmp_settings = json.load(f)
    return tmp_settings


def load_tasks():
    tasks = [{
        "task_id": 1,
        "sheep_id": 1
    }]
    return tasks


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)


@app.route('/api/1/tasks/<int:sheep_hash>', methods=['GET'])
def get_tasks(sheep_hash):
    return jsonify(query_tasks(sheep_hash))


@app.route('/api/1/register', methods=['POST'])
def register_new():
    if not request.json:
        abort(400)
    tmp_hash = register_minion(get_next_id(), request.remote_addr, request.json["mac"], request.json["platform"])
    if tmp_hash < 0:
        return abort(500)
    else:
        return jsonify({"hashcode":tmp_hash}), 201


if __name__ == '__main__':
    settings = load_settings('master_settings.json')
    tasks = load_tasks()
    app.run(settings['host'], settings['port'])
