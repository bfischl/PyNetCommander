import hashlib

def register_minion(id,ip,mac,platform):
    """
    :param id:
    :param ip:
    :param mac:
    :param platform:
    :return: returns valid md5 hash on success or negative value on failure
    """
    return hashlib.md5()


def get_next_id():
    """Queries the attached database"""
    return 1


def query_tasks(hash):
    """Queries the attached database for tasks given a specific hashcode"""
    return {"TASK" : "TEST1"}