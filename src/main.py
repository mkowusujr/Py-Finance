import repo
import cli
import argparse
from controller import handle_args


def main():
    repo.setup_db()
    parser: argparse.ArgumentParser() = cli.setup_parser()
    args = parser.parse_args()
    # print(args)
    handle_args(args)


main()
