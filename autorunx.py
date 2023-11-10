
import sys
import os
import argparse
import globals
import json


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', required=False, type=str,
                    help="specifies the configuration file to run")
parser.add_argument('-v', '--version', action='version', version='1.1.1',
                    help="checking version information"
                    )


def main():
    args = parser.parse_args()
    if args.config is not None:
        config_path = args.config
        if not os.path.exists(config_path):
            print("Invalid parameter: {}".format(config_path))
            return
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
            globals.init(**config)
            globals.start()
        return
    else:
        parser.print_help()


def run(config):
    with open(config, "r", encoding="utf-8") as f:
        config = json.load(f)
        globals.init(**config)
        globals.start()


if __name__ == '__main__':
    main()
