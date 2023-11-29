from argparse import ArgumentParser, Namespace
from configparser import ConfigParser
from pathlib import Path
from http import client
import requests


AOC_URL = 'https://adventofcode.com'

def get_input(ns: Namespace, config: ConfigParser):
    year = config['general']['year'] if ns.year is None else ns.year
    path_to_input = Path(config.get('general', 'workdir')) / '.input' / year / f'day{int(ns.day):02}.txt'

    if not path_to_input.parent.exists():
        path_to_input.parent.mkdir(parents=True, exist_ok=True)

    if path_to_input.exists():
        print(f'The input file for this day has already been downloaded.')
        print(f'It can be found at:')
        print(f'{str(path_to_input)}')
        return
    
    endpoint = f'/{year}/day/{ns.day}/input'

    response = requests.get(AOC_URL + endpoint, cookies={'session': config.get('aoc', 'token')})
    
    with open(path_to_input, "w+") as input_file:
        input_file.write(response.text)
    


def add_get_parser(subparser: ArgumentParser):
    get_parser = subparser.add_parser('get', description='Download input from given day on given year')
    get_parser.add_argument('--day', '-d', help='Specify the day')
    get_parser.add_argument('--year', '-y', help='Specify the year. Will defualt to year in your configuration file.')
    get_parser.set_defaults(func=get_input)