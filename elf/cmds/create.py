from argparse import ArgumentParser, Namespace
from configparser import ConfigParser
from pathlib import Path

def create_day(ns: Namespace, config: ConfigParser):
    

def add_create_parser(subparser: ArgumentParser):
    create_parser = subparser.add_parser('create', help='Create folder and files for a day')
    create_parser.add_argument('--day', '-d', help="Specify the given day")
    create_parser.add_argument('--year', '-y', help="Specify the given year. Defaults to the year in your configuration file")
    create_parser.set_defaults(func=create_day)
