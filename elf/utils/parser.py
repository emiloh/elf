from argparse import ArgumentParser
from configparser import ConfigParser
from cmds import config



def create_parser() -> (ArgumentParser, ConfigParser):
    parser = ArgumentParser('elf')
    #parser.description('A happy christmas elf ready to help you interact with Advent of Code!')
    
    # Add different parsers
    config.add_config_parser(parser)
    conf = config.init_config("insert token here", "insert working directory here")

    return (parser, conf)


