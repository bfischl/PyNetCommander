import hashlib

# TODO implement proper database


def register_minion(ip,mac,platform):
    """
    :param ip:
    :param mac:
    :param platform:
    :return: returns valid md5 hash on success or negative value on failure
    """
    return 0


def query_tasks(hash):
    """Queries the attached database for tasks given a specific hashcode"""
    return {"TASK" : "TEST1"}


def update_status(task_id, status, results):
    return {str(task_id) : "UPDATED"}