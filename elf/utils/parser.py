from argparse import ArgumentParser
from configparser import ConfigParser
from cmds import config, get, submit, create, run



def create_parser() -> (ArgumentParser, ConfigParser):
    parser = ArgumentParser('elf')
    #parser.description('A happy christmas elf ready to help you interact with Advent of Code!')
    
    # Add different parsers
    subparser = parser.add_subparsers(dest='command')
    config.add_config_parser(subparser)
    conf = config.init_config("insert token here", "insert working directory here")

    get.add_get_parser(subparser)
    submit.add_submit_parser(subparser)
    create.add_create_parser(subparser)
    run.add_run_parser(subparser)

    return (parser, conf)


