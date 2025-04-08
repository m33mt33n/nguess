# -*- coding: utf-8 -*-

from argparse import ArgumentParser, ArgumentTypeError
from nguess import MagicGuess


def columns(arg):
  """validate number of columns"""
  try:
    arg = int(arg)
    if arg < 5 or arg > 15:
      raise ArgumentTypeError('value must be an integer in range 5 to 15!')
  except ValueError:
    raise ArgumentTypeError('value must be an integer!')
  return arg


def guessed_number(arg):
  """validate guessed number"""
  try:
    arg = int(arg)
    if arg < 1:
      raise ArgumentTypeError('value must a non-zero positive integer!')
  except ValueError:
    raise ArgumentTypeError('value must be an integer!')
  return arg


def main():
  """main procedure"""
  parser = ArgumentParser(
    description='Simulation of a schooltime number guess game.', prog='nguess'
  )
  parser.add_argument(
    '-c', metavar='INT', dest='columns', type=columns, default=5,
    help="number of columns to be used when printing tabular data (default: 5)."
  )
  parser.add_argument(
    '-u', metavar='INT', dest='upper_limit', type=guessed_number, default=50,
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
