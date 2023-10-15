
import sys
import os
import json


def get_node_list_config(module_root):
    result = []
    for item in os.listdir(module_root):
        config_path = os.path.join(module_root, item, "config.json")
        if os.path.exists(config_path):
            with open(config_path, "r", encoding="utf-8") as f:
                config = json.load(f)
                result.append(config)
    return result


def generate_node_list_config_for_web(doc_root, result_path="", lang='zh'):
    node_data = [{
        'type': 'dtio',
        'name': '输入输出节点' if lang == 'zh' else 'Input/Output Node',
        'nodeList': get_node_list_config(os.path.join(doc_root, "dataio"))
    }, {
        'type': 'dtpc',
        'name': '数据处理节点' if lang == 'zh' else 'Data Processing Node',
        'nodeList': get_node_list_config(os.path.join(doc_root, "dataprocess"))
    }, {
        'type': 'ctrl',
        'name': '程序控制节点' if lang == 'zh' else 'Program Control Node',
        'nodeList': get_node_list_config(os.path.join(doc_root, "flowcontrol"))
    }, {
        'type': 'func',
        'name': '程序功能节点' if lang == 'zh' else 'Program Function Node',
        'nodeList': get_node_list_config(os.path.join(doc_root, "flowfunction"))
    }, {
        'type': 'evrx',
        'name': '事件发生节点' if lang == 'zh' else 'Event Start Node',
        'nodeList': get_node_list_config(os.path.join(doc_root, "eventreceive"))
    }, {
        'type': 'evtx',
        'name': '事件触发节点' if lang == 'zh' else 'Event Emit Node',
        'nodeList': get_node_list_config(os.path.join(doc_root, "eventtransmit"))
    }]
    node_data_dir = os.path.join(
        sys.path[0], __file__.replace('.py', ''), result_path)
    if not os.path.exists(node_data_dir):
        os.mkdir(node_data_dir)
    with open(os.path.join(sys.path[0], '{}/nodeData.json'.format(node_data_dir)), 'w', encoding='utf-8') as f:
        f.write(json.dumps(node_data, ensure_ascii=False))
    return node_data


if __name__ == '__main__':
    generate_node_list_config_for_web(os.path.join(
        sys.path[0], "../../doc/zh/lib"), 'zh', 'zh')
    generate_node_list_config_for_web(os.path.join(
        sys.path[0], "../../doc/en/lib"), 'en', 'en')
