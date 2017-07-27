import json
import requests
from platform import platform
from uuid import getnode

from minion_lib import Task
from minion_lib import Base

# Add more libraries at will inside minion_lib


def get_mac():
    return hex(getnode())


class Minion:
    def __init__(self, settings):
        self.mac = hex(getnode())
        self.platform = platform()
        self.settings = settings
        try:
            self.hashcode = settings['hashcode']
        except KeyError:
            self.hashcode = None
        self.available_commands = []

    def register(self):
        """ Connects to master_lib and registers, receives hashcode
        :return: 0 on success
        """
        if self.settings['https'] == 1:
            url = "https://"
        else:
            url = "http://"
        url += self.settings['master_ip'] + ':' + str(self.settings['master_port']) + self.settings['register']
        payload = {"platform": self.platform, "mac": str(self.mac), "available": json.dumps(self.available_commands)}
        if self.hashcode is not None:
            payload["hashcode"] = self.hashcode
        try:
            r = requests.post(url, json=payload)
            if r.status_code == 201:
                # If Server accepts it...
                self.hashcode = r.json()['hashcode']
        except requests.ConnectionError as e:
            print("Connection Error:\t%s" % e.response)
            return 1
        return 0

    def get_tasks(self):
        """Connects to the Tasking Server and returns JSON of tasks
        :return: dict JSON of tasks
        """
        if self.settings['https'] == 1:
            url = "https://"
        else:
            url = "http://"
        url += self.settings['master_ip'] + ':' + str(self.settings['master_port']) \
               + self.settings['tasks'] + '/' + str(self.hashcode)
        try:
            r = requests.get(url)
            # TODO parse r.text as JSON
            print(r.text)
        except requests.ConnectionError as e:
            print(e.response)

    def schedule_task(self):
        # TODO Implement Scheduling
        pass

    def execute_task(self,task):
        # TODO Implement Task Execution
        print(task.cmd)

    def update_results(self,task,results):
        # TODO Update server with Command Execution
        task.results = results