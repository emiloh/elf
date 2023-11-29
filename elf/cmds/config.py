from configparser import ConfigParser
from argparse import ArgumentParser, Namespace
from pathlib import Path
import os

HOME_DIR = Path.home()

CONFIG_FILE_PATH = HOME_DIR / '.aoc' / 'config.ini'
DEFAULT_YEAR = 2015

def init_config(token: str, workdir: Path, year: int = DEFAULT_YEAR) -> ConfigParser:
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
        confingfile.close()

def add_config_parser(subparser: ArgumentParser):
    config_parser = subparser.add_parser('config', description="Modify your config file")
    config_parser.add_argument('--token', '-t', help='Your session token')
    config_parser.add_argument('--workdir', '-wd', help="Your working directory for advent of code solutions")
    config_parser.add_argument('--year', '-y', help='Year you are currently working on. Default is 2015')
    config_parser.set_defaults(func=update_config)

def update_config(ns: Namespace, config: ConfigParser):
    if ns.token is not None:
        config.set('aoc', 'token', ns.token)    
    if ns.workdir is not None:
        config.set('general', 'workdir', ns.workdir) 
    if ns.year is not None:
        config.set('general', 'year', ns.year) 
    
    with open(CONFIG_FILE_PATH, "w+") as confingfile:
        config.write(confingfile)
        confingfile.close()
    