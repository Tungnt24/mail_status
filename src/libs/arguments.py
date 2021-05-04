import argparse

parser = argparse.ArgumentParser()
arg = parser.add_mutually_exclusive_group()
arg.add_argument(
    "-c",
    "--count",
    type=str,
    nargs='+',
    help="total number of messages in a folder",
)

arg.add_argument(
    "-s",
    "--status",
    type=str,
    help="check mail status",
)

args = parser.parse_args()
