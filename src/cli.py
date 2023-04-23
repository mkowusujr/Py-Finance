import argparse


def setup_parser() -> argparse.ArgumentParser:
    # Setup Parser
    parser = argparse.ArgumentParser(
        prog='money-py',
        description='simple budget tracking in your terminal'
    )

    # Cli Cmds
    parser.add_argument('-disp', '-display', '-dp',
                        choices=['entries'], dest='display')
    parser.add_argument('-rec', '-record', action='store_true', dest='record')

    # Item Related
    parser.add_argument('-b', '-budget', type=str, nargs='?', dest='budget')
    parser.add_argument('-e', '-expense', type=str,
                        nargs='?', dest='expense')
    parser.add_argument('-s', '-seller', type=str, nargs='?', dest='seller')
    parser.add_argument('-a', '-amount', type=float, nargs='?', dest='amount')
    parser.add_argument('-d', '-date', type=str, nargs='?', dest='date')
    parser.add_argument('-c', '-category', type=str,
                        nargs='?', dest='category')
    
    # Aggregate Cmds
    parser.add_argument('--sum', action='store_true', dest='sum')

    return parser
