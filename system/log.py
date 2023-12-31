
import sys
import os
import globals

import datetime


COMMON_LOG_FILE = "log/common.log"      # common log, all(log) in one.
LOG_FILE = "log/log.log"        # pure log, func log output


def init(**kwargs):
    global LOG_FILE, COMMON_LOG_FILE
    if "COMMON_LOG_FILE" in kwargs:
        COMMON_LOG_FILE = kwargs['COMMON_LOG_FILE']
    else:
        COMMON_LOG_FILE = os.path.join(globals.ENV_WORK_DIR, COMMON_LOG_FILE)
    if "LOG_FILE" in kwargs:
        LOG_FILE = kwargs['LOG_FILE']
    else:
        LOG_FILE = os.path.join(globals.ENV_WORK_DIR, LOG_FILE)
    for filefullpath in [COMMON_LOG_FILE, LOG_FILE]:
        if len(filefullpath.split('/')) > 1:
            [path, filename] = os.path.split(filefullpath)
            # print(path,filename)
            if not os.path.exists(path):
                os.makedirs(path)


def common_log(**kwargs):
    msg = kwargs['msg']
    # common log
    with open(COMMON_LOG_FILE, "+a", encoding="utf-8") as f:
        f.write(msg)
        # print(msg,end="")


def log(**kwargs):
    """
    kw:
    - msg: must, log message
    - is_new_line: True, optional, default True
    - timestamp: True, optional, default True
    - end: '\n', optional, default '\n'
    - second_log_file: optional
    """
    is_new_line = True
    timestamp = True
    end = ''
    msg = kwargs['msg']
    if 'is_new_line' in kwargs:
        is_new_line = kwargs['is_new_line']
    if 'timestamp' in kwargs:
        timestamp = kwargs['timestamp']
    if 'end' in kwargs:
        end = kwargs['end']
    if timestamp:
        msg = "[{}]: {}".format(datetime.datetime.now(), msg)
    if is_new_line:
        msg = "\n{}{}".format(msg, end)
    else:
        msg = "{}{}".format(msg, end)
    print(msg, end="", flush=True)
    # func log
    with open(LOG_FILE, "+a", encoding="utf-8") as f:
        f.write(msg)
    # common log
    common_log(msg=msg)
    # second log file
    if "second_log_file" in kwargs:
        if len(kwargs['second_log_file'].split('/')) > 1:
            [path, filename] = os.path.split(kwargs['second_log_file'])
            if not os.path.exists(path):
                os.makedirs(path)
        with open(kwargs['second_log_file'], "+a", encoding="utf-8") as f:
            f.write(msg)


# init(COMMON_LOG_FILE="log/common-log.log")
# log(msg="hello func!")
