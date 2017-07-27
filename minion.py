import json, os, socket, fcntl, struct, platform, requests
from uuid import getnode
import minion_lib

def load_settings(filename):
    with open(filename,'rb') as f:
        tmp_settings = json.load(f)
    return tmp_settings

def get_mac():
    return hex(getnode())

class sheep:
    def __init__(self, mac, platform, settings):
        self.mac = mac
        self.platform = platform
        self.settings = settings
        self.hashcode = None
        self.available_commands = []
    def register(self):
        if settings['https'] == 1:
            url = "https://"
        else:
            url = "http://"
        url += settings['master_ip'] + ':' + str(settings['master_port']) + settings['register']
        print(url)
        payload = {"platform": self.platform, "mac": self.mac, "available": self.available_commands}
        r = requests.post(url, json=payload)
        if r.status_code == 201:
            self.hashcode = r.json()['hashcode']
            print('HASHCODE:\t%s', self.hashcode)

    def get_tasks(self):
        # Implement retrieve tasks from master
        pass

    def schedule_task(self):
        # Implement
        pass


if __name__ == "__main__" :
    settings = load_settings('minion_settings.json')
    me = sheep(get_mac(), platform.platform(), settings)
    me.available_commands.append(a for a in dir(minion_lib) if not a.startswith('__'))
    me.register()
