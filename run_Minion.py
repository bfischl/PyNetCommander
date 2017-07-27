#!/usr/bin/env python3
import json
from minion_lib.Minion import Minion


def load_settings(filename):
    """
    :param filename: JSON encoded settings file
    :return: dict of settings
    """
    with open(filename, encoding='utf-8') as f:
        tmp_settings = json.load(f)
    return tmp_settings

if __name__ == "__main__" :
    settings = load_settings('minion_settings.json')
    me = Minion(settings)
    me.register()
    tasks = me.get_tasks()
    for task in tasks:
        me.schedule_task(task)
