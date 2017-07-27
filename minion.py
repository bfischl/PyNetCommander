#!/usr/bin/env python3
import json
import platform
import requests
from uuid import getnode
import minion_lib


def load_settings(filename):
    """
    :param filename:
    :return:
    """
    with open(filename, encoding='utf-8') as f:
        tmp_settings = json.load(f)
    return tmp_settings


def get_mac():
    return hex(getnode())

class minion:
    def __init__(self, mac, platform, settings):
        self.mac = mac
        self.platform = platform
        self.settings = settings
        self.hashcode = None
        self.available_commands = []

    def register(self):
        """ Connects to Master and registers, receives hashcode
        :return: 0 on success
        """
        if settings['https'] == 1:
            url = "https://"
        else:
            url = "http://"
        url += settings['master_ip'] + ':' + str(settings['master_port']) + settings['register']
        print(url)
        payload = {"platform": self.platform, "mac": str(self.mac), "available": str(self.available_commands)}
        try:
            r = requests.post(url, json=payload)
            if r.status_code == 201:
                self.hashcode = r.json()['hashcode']
                print('HASHCODE:\t%s' % self.hashcode)
        except requests.ConnectionError as e:
            print("FAIL TO CONNECT")



    def get_tasks(self):
        # Implement retrieve tasks from master
        pass

    def schedule_task(self):
        # Implement
        pass


if __name__ == "__main__" :
    settings = load_settings('minion_settings.json')
    me = minion(get_mac(), platform.platform(), settings)
    me.available_commands.append(a for a in dir(minion_lib) if not a.startswith('__'))
    me.register()
