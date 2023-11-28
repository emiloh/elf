from configparser import ConfigParser
from argparse import ArgumentParser
from pathlib import Path
import os

HOME_DIR = Path.home()

CONFIG_FILE_PATH = HOME_DIR / '.aoc' / 'config.ini'
DEFAULT_YEAR = 2015

def init_config(token: str, workdir: Path, year: int = 2015) -> ConfigParser:
    config = ConfigParser()

    if not CONFIG_FILE_PATH.parent.exists():
        CONFIG_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
        
    if CONFIG_FILE_PATH.exists():
        config.read(CONFIG_FILE_PATH)
        return config
            
    config['aoc'] = {'token': token}
    config['general'] = {'workdir': str(workdir), 'year': year}
    
    with open(CONFIG_FILE_PATH, "w+") as confingfile:
        config.write(confingfile)

def add_config_parser(parser: ArgumentParser):
    subparser = parser.add_subparsers()
    config_parser = subparser.add_parser('config', description="Modify your config file")
    config_parser.add_argument('--token', '-t', help='Your session token', nargs=1)
    config_parser.add_argument('--workdir', '-wd', help="Your working directory for advent of code solutions",
                               nargs=1)
    config_parser.add_argument('--year', '-y', help='Year you are currently working on. Default is 2015', 
                               nargs=1, default=DEFAULT_YEAR)


def update_config():
    pass
    