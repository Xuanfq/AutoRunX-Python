import sys
import os
import json
import shutil


def update_single_doc_readme_append_node_name(doc_root):
    config_path = os.path.join(doc_root, 'config.json')
    readme_path = os.path.join(doc_root, 'README.md')
    if os.path.exists(config_path):
        with open(config_path,encoding='utf-8') as fp:
            config = json.load(fp)
            node_name = config['node_name']
            with open(readme_path, '+a',encoding='utf-8') as f:
                f.writelines("**Node ID**: {}\n\n".format(node_name))


def update_lib_doc_readme_append_node_name(doc_lib_root):
    for type in os.listdir(doc_lib_root):
        type_root = os.path.join(doc_lib_root, type)
        for node_name in os.listdir(type_root):
            node_doc_root = os.path.join(type_root, node_name)
            update_single_doc_readme_append_node_name(node_doc_root)


def update_single_doc(node_type, node_name, node_root, doc_root, lang):
    if not os.path.exists(doc_root):
        os.mkdir(doc_root)
    # copy source code: node_name.py and node_name_attachment_dir
    entry_script = os.path.join(node_root, node_name+'.py')
    entry_script_attachment = os.path.join(node_root, node_name)
    if os.path.exists(entry_script):
        shutil.copy(entry_script, doc_root)
    if os.path.exists(entry_script_attachment):
        entry_script_attachment_dest = os.path.join(doc_root, node_name)
        if os.path.exists(entry_script_attachment_dest):
            shutil.rmtree(entry_script_attachment_dest)
        shutil.copytree(entry_script_attachment, entry_script_attachment_dest)
    # create config.json file
    config_path = os.path.join(doc_root, 'config.json')
    if not os.path.exists(config_path):
        with open(os.path.join(sys.path[0], __file__.replace(".py", ''), 'config.json')) as f:
            config = json.load(f)
        config['node_name'] = node_name
        config['node_type'] = node_type
        with open(config_path, '+a') as f:
            f.write(json.dumps(config, ensure_ascii=False))
    # create README.md file
    readme_path = os.path.join(doc_root, 'README.md')
    if not os.path.exists(readme_path):
        shutil.copy(os.path.join(sys.path[0], __file__.replace(
            ".py", ''), 'README-{}.md'.format(lang)), readme_path)


def updata_doc_lib(lib_root, doc_lib_root, lang):
    for type in os.listdir(lib_root):
        node_root = os.path.join(lib_root, type)
        for node_file in os.listdir(node_root):
            if os.path.isfile(os.path.join(node_root, node_file)) and node_file != '__init__.py':
                node_name = node_file.replace('.py', '')
                update_single_doc(node_name.split('-')[0], node_name, node_root,
                                  os.path.join(doc_lib_root, type, node_name), lang=lang)


if __name__ == '__main__':
    # update doc lib
    updata_doc_lib(os.path.join(
        sys.path[0], "../../lib"), os.path.join(sys.path[0], "../../doc/zh/lib"), 'zh')
    updata_doc_lib(os.path.join(
        sys.path[0], "../../lib"), os.path.join(sys.path[0], "../../doc/en/lib"), 'en')

    # doc README.md append node_name
    # update_lib_doc_readme_append_node_name(
    #     os.path.join(sys.path[0], "../../doc/zh/lib"))
    # update_lib_doc_readme_append_node_name(
    #     os.path.join(sys.path[0], "../../doc/en/lib"))
    
    pass