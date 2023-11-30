from argparse import ArgumentParser, Namespace
from configparser import ConfigParser
from pathlib import Path
import sys, subprocess

def run_day(ns: Namespace, config: ConfigParser):
    part = 2 if ns.p2 else 1
    year = config['general']['year'] if ns.year is None else ns.year

    path_to_code = Path(config.get('general', 'workdir')) / year / f'day{int(ns.day):02}' / f'p{part}.py'
    path_to_solutions = Path(config.get('general', 'workdir')) / '.solution' / year / f'sol_p{part}_day{int(ns.day):02}.txt'
    path_to_input = Path(config.get('general', 'workdir')) / '.input' / year /f'day{int(ns.day):02}.txt'
    python = sys.executable

    with open(path_to_solutions, "wt") as solution_file:
        output = subprocess.check_output([python, str(path_to_code), str(path_to_input)]).decode("UTF-8")
        solution_file.write(str(output).strip())
    
    print('Answer:')
    print(str(output).strip())
    




    

def add_run_parser(subparser: ArgumentParser):
    run_parser = subparser.add_parser('run', help='Run specific part on given day. Answer saved to file used for submit.')
    run_parser.add_argument('-p1', help='Indicates that it is part 1 you want to submit', action='store_true')
    run_parser.add_argument('-p2', help='Indicates that it is part 2 you want to submit', action='store_true')
    run_parser.add_argument('--day', '-d', help="Specify the given day")
    run_parser.add_argument('--year', '-y', help="Specify the given year. Defaults to the year in your configuration file")
    run_parser.set_defaults(func=run_day)