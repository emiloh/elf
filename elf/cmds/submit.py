from argparse import ArgumentParser, Namespace
from configparser import ConfigParser
from pathlib import Path
import requests

AOC_URL = 'https://adventofcode.com'

def submit_solution(ns: Namespace, config: ConfigParser):
    part = 2 if ns.p2 else 1
    year = config['general']['year'] if ns.year is None else ns.year
    path_to_solution = Path(config.get('general', 'workdir')) / '.solution' / year / f'sol_p{part}_day{int(ns.day):02}.txt'

    if not path_to_solution.exists():
        print('Answer not found. Try running the "run" command')
        return
    
    with open(path_to_solution, "r") as f:
        answer = f.read()
    
    endpoint = f'/{year}/day/{ns.day}/answer'
    data = {'level': str(part), 'answer': answer}



    response = requests.post(AOC_URL + endpoint, cookies={'session': config.get('aoc', 'token')}, data=data)
    if 'not the right answer' in response.text:
        if 'too low' in response.text:
            print('Result: WRONG (too low)')
        elif 'too high' in response.text:
            print('Result: WRONG (too high)')
        else:
            print('Result: WRONG')
    elif 'gave an answer too recently' in response.text:
        print('Too many request. Wait a minute.')
    elif 'solving the right level' in response.text:
        print('You have already solved this part.')
    else:
        print("Result: CORRECT!")

def add_submit_parser(subparser: ArgumentParser):
    submit_parser = subparser.add_parser('submit', help="Submit solution to given day")
    submit_parser.add_argument('-p1', help='Indicates that it is part 1 you want to submit', action='store_true')
    submit_parser.add_argument('-p2', help='Indicates that it is part 2 you want to submit', action='store_true')
    submit_parser.add_argument('--day', '-d', help="Specifies the given day")
    submit_parser.add_argument('--year', '-y', help="Specifies the given year. Defaults to year in coniguration file")
    submit_parser.set_defaults(func=submit_solution)

    