from utils import parser


def cli():
    (p, conf) = parser.create_parser()

    args = p.parse_args()

    if args.command is not None:
        args.func(args, conf)

    

if __name__ == "__main__":
    cli()