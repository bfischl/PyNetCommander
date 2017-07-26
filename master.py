#!/usr/bin/env python3
import json
from flask import Flask, jsonify, make_response

app = Flask(__name__)


def load_settings():
    with open('settings.json') as f:
        settings = json.load(f)
    return settings


def load_tasks():
    tasks = [{

        'id': 1

    }]
    return tasks


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)


@app.route('/sheep/1/tasks/<int:sheep_id>', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/sheep/1/register', methods=['POST'])
def register_new():
    pass


if __name__ == '__main__':
    settings = load_settings
    tasks = load_tasks()
    app.run(settings['host'], settings['port'])
