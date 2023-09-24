
import sys,os
import json


def get_node_list_config(module_root):
    result=[]
    for item in os.listdir(module_root):
        config_path=os.path.join(module_root,item,"config.json")
        if os.path.exists(config_path):
            with open(config_path,"r",encoding="utf-8") as f:
                config=json.load(f)
                result.append(config)
    return result


def generate_node_list_config_for_web(doc_root):
    node_data=[{
        'type':'dtio',
        'name':'输入输出节点',
        'nodeList':get_node_list_config(os.path.join(doc_root,"dataio"))
    },{
        'type':'dtpc',
        'name':'输入输出节点',
        'nodeList':get_node_list_config(os.path.join(doc_root,"dataprocess"))
    },{
        'type':'ctrl',
        'name':'输入输出节点',
        'nodeList':get_node_list_config(os.path.join(doc_root,"flowcontrol"))
    },{
        'type':'func',
        'name':'输入输出节点',
        'nodeList':get_node_list_config(os.path.join(doc_root,"flowfunction"))
    }]  
    with open(os.path.join(sys.path[0],'nodeData.json'),'w',encoding='utf-8') as f:
        f.write(json.dumps(node_data,ensure_ascii=False))
    return node_data


if __name__=='__main__':
    generate_node_list_config_for_web(os.path.join(sys.path[0],"../../doc/"))
























