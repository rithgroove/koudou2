import argparse
import configparser
import json
from src.UI.view import View
from src.UI.controller import Controller
#from src.utils.parser import load_parameters
# from controller import Controller
# from os.path import join

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", dest='use_view', action='store_true', help="Use UI")
    parser.add_argument("-c", dest='config', help="Configuration File")
    args = parser.parse_args()

    config_file = args.config
    if config_file is None:
        config_file = "config.ini"

    config = read_config(config_file)

    if args.use_view:
        view = View()
        controller = Controller()
        view.set_controller(controller)
        view.main_loop()


def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    print(config.sections())
    for x in config.sections():
        for key in config[x]:
            print(f"{key} = {config[x][key]}")
    return config

if __name__ == "__main__":
    main()
