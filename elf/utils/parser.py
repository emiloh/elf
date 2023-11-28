from argparse import ArgumentParser
from cmds import config



def create_parser() -> ArgumentParser:
    parser = ArgumentParser('elf')
    #parser.description('A happy christmas elf ready to help you interact with Advent of Code!')
    
    # Add different parsers
    config.add_config_parser(parser)
    config.init_config("test", "test")

    return parser


