from argparse import ArgumentParser, Namespace
from configparser import ConfigParser
from pathlib import Path

PATH_TO_TEMPLATE = Path.home() / '.aoc' / 'template.py'

def create_day(ns: Namespace, config: ConfigParser):
    year = config['general']['year'] if ns.year is None else ns.year
    path_to_code = Path(config.get('general', 'workdir')) / year / f'day{int(ns.day):02}'
    part1 = path_to_code / 'p1.py'
    part2 = path_to_code / 'p2.py'

    if not path_to_code.exists():
        path_to_code.mkdir(parents=True, exist_ok=True)
    
    with open(PATH_TO_TEMPLATE, "rt") as template_file:
        with open(part1, "wt") as part1_file:
            part1_file.write(template_file.read())
    with open(PATH_TO_TEMPLATE, "rt") as template_file:
        with open(part2, "wt") as part2_file:
            part2_file.write(template_file.read())

def add_create_parser(subparser: ArgumentParser):
    create_parser = subparser.add_parser('create', help='Create folder and files for a day')
    create_parser.add_argument('--day', '-d', help="Specify the given day")
    create_parser.add_argument('--year', '-y', help="Specify the given year. Defaults to the year in your configuration file")
    create_parser.set_defaults(func=create_day)
