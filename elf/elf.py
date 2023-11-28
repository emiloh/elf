from utils import parser

def cli():
    p = parser.create_parser()

    args = p.parse_args()
    

if __name__ == "__main__":
    cli()