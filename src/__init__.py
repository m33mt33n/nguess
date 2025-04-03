# -*- coding: utf-8 -*-

import re
from copy import deepcopy
from tabulate import tabulate


class MagicGuess:
  def __init__(self, upper_limit=30, columns=5, colors=True):
    "init method"
    self.upper_limit = upper_limit
    self.columns = columns
    self._set_colors(colors)

  def _set_colors(self, colors=True):
    """set colors for formatting"""
    global A0, A1, C1, C2
    if colors:
      import colored as c
      A0 = c.attr(0)  # reset
      A1 = c.attr(1)  # bold
      C1 = c.fg(6)    # cyan
      C2 = c.fg(33)   # blue
    else:
      A0 = A1 = C1 = C2 = ""

  def make_cards(self):
    """generate magic cards"""
    binary_str = lambda x: str(bin(x)[2:])
    num_of_cards = len(binary_str(self.upper_limit))
    cards = {str(n): [] for n in range(1, num_of_cards + 1)}
    for num in range(1, self.upper_limit + 1):
      binary_num = binary_str(num)
      for index, char in enumerate(reversed(binary_num), 1):
        if char == '1':
          cards[str(index)].append(num)
    return cards

  def make_table(self, card):
    """add formatting for pretty printing"""
    table = []
    columns = self.columns
    max_iterations = len(card) / columns
    iterations = 0
    while iterations < max_iterations:
      iterations += 1
      row = card[:columns]
      while len(row) < columns:
        row.append(" ")
      table.append(row)
      del(card[:columns])
    table = tabulate(table, tablefmt="grid")
    table = re.sub("(\d+)", fr"{C1}\1{A0}", table, flags=re.MULTILINE)
    return table

  def ask(self, message="Are you sure you want to continue?", default=True):
    """ask yes/no question"""
    yes, no = ("Y", "n") if default else ("y", "N")
    answer = input(f"{message}  [{yes}/{no}] ").strip().lower()
    while answer not in ["y", "n", ""]:
      answer = input(f"Invalid input, please enter again. [{yes}/{no}] ").strip().lower()
    return {"y": True, "n": False, "": default}[answer]

  def guess(self, print_result=False):
    """start play"""
    print(
      f"Please pick a number between 1 to {self.upper_limit},",
      "and answer the questions as they printed:\n",
    )
    cards = self.make_cards()
    answers = []
    for index, card in enumerate(deepcopy(cards).values(), 1):
      print(f"{self.make_table(card)}")
      if self.ask(message="Above list contains your number?", default=True):
        answers.append(index)
      print()
    guessed_num = 0
    for table_num in answers:
      guessed_num += cards[str(table_num)][0]
    if print_result:
      print(f"You've picked: {C1}{guessed_num}{A0}")
    else:
      return guessed_num
