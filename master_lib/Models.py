def register_minion(id,ip,mac,platform):
    """
    :param id:
    :param ip:
    :param mac:
    :param platform:
    :return: returns valid md5 hash on success or negative value on failure
    """
    return 0


def get_next_id():
    return 1


def query_tasks(hash):
    return {"TASK":"TEST1"}