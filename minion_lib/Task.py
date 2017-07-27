class Task:
    def __init__(self,time,params,cmd):
        self.time = time
        self.params = params
        self.cmd = cmd
        self.status = "NEW"
        self.results = None

    def get_status(self):
        return self.status
