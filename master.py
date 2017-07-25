#!/usr/bin/env python3
import json
from flask import Flask, jsonify

app = Flask(__name__)
tasks = [{

    'id': 1

}]


def load_settings():
    with open('settings.json') as f:
        settings = json.load(f)
    return settings


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    settings = load_settings
    app.run(settings['host'], settings['port'])
