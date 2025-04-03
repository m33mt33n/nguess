# -*- coding: utf-8 -*-

import argparse
from nguess import MagicGuess


def main():
  """main procedure"""
  parser = argparse.ArgumentParser(
    description='A number guess game based on an old school algorithm.', prog='nguess'
  )
  parser.add_argument(
    '-c', metavar='INT', dest='columns', type=int, default=5,
    help="number of columns to be used when printing tabular data (default: 5)."
  )
  parser.add_argument(
    '-u', metavar='INT', dest='upper_limit', type=int, default=50,
    help="upper limit of 'to be guessed' number (default: 50), bigger the set number greater will be the "
      "count of the questions asked by the script and longer will will be the length of data printed, "
      "usage of numbers upto 100 is recommended."
  )
  parser.add_argument(
    "-N", "--no-colors", dest="no_colors", action="store_true",
    help="don't use colors."
  )
  a = parser.parse_args()

  m = MagicGuess(upper_limit=a.upper_limit, columns=a.columns, colors=(not a.no_colors))
  try:
    m.guess(print_result=True)
  except KeyboardInterrupt:
    print("\nCancelled by user!")


if __name__ == '__main__':
  main()
