
import sys
import os
import globals
import imp
from threading import Lock

user_node_set = set()

"""
key: node id
value: node
"""
node_dict = {}
node_dict_lock = Lock()


def init(**kwargs):
    # init user_node_set
    global user_node_set
    import os
    lib_root = os.path.join(os.path.dirname(__file__), "../lib/")
    node_class_paths = [os.path.join(lib_root, type) for type in [
        'dataio', 'dataprocess', 'flowcontrol', 'flowfunction', 'eventreceive', 'eventtransmit']]
    for node_root in node_class_paths:
        for node_name in os.listdir(node_root):
            if os.path.isfile(os.path.join(node_root, node_name)) and node_name != '__init__.py':
                user_node_set.add(node_name.replace('.py', ''))
    return None


def put(key, value, **kwargs):
    with node_dict_lock:
        node_dict[key] = value


def get(key, **kwargs):
    ret = None
    with node_dict_lock:
        ret = node_dict[key]
    return ret


def has(key, **kwargs):
    ret = False
    with node_dict_lock:
        ret = key in node_dict
    return ret


def generate(key, **kwargs):
    """
    key: node_name, node's filename but bot include extension, module name
    """
    if key in user_node_set:
        return imp.reload(globals.import_module(key))
    else:
        raise Exception('No "{}" module or node'.format(key))


def get_or_generate(id, node_name, **kwargs):
    """
    id: node_id or node_name, typically this is the node_id
    node_name: node_name, node's filename but bot include extension, also called the module name
    """
    ret = None
    with node_dict_lock:
        if id in node_dict:
            ret = node_dict[id]
    if ret is None:
        ret = generate(node_name)
    return ret


def get_or_generate_put(id, node_name, **kwargs):
    """
    id: node_id or node_name, typically this is the node_id
    node_name: node_name, node's filename but bot include extension, also called the module name
    """
    ret = None
    with node_dict_lock:
        if id in node_dict:
            ret = node_dict[id]
        else:
            ret = generate(node_name)
            node_dict[id] = ret
    return ret
