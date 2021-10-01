import argparse
import configparser

def input_arguments():
    my_parser = argparse.ArgumentParser()
    
    my_parser.add_argument(
        '-c',
        '--config',
        type=str,
        action='store',
        help="This option allows you to specify a config file.",
        required=False
    )
    
    my_parser.add_argument(
        '-a',
        '--avar',
        type=int,
        action='store',
        help="This is an integer and all I'm going to do is print it.",
        required=False
    )

    my_parser.add_argument(
        '-b',
        '--bvar',
        action='store',
        help="This is a string I'm going to print.",
        required=False
    )

    my_args = my_parser.parse_args()
    
    return my_args
    
my_args = input_arguments()
config_filename = my_args.config

config = configparser.ConfigParser()
config.read(config_filename)

print(config['FILES']['input'])
