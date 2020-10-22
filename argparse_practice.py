# import argparse
# parser = argparse.ArgumentParser()
# parser.parse_args()

# ----positional argument----
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("echo")
# args = parser.parse_args()

# print(args.echo)

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number", type=int)
args = parser.parse_args()

print(args.square**2)