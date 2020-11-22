"""Tape

This module is about the turing machine Tape

TODO: describe more about it...
"""


class Tape:
    DIRECTION_CHOICES = {'L': 'Left', 'R': 'Right', 'S': 'Stop'}

    def __init__(self, _input: str, blank_symbol: str):
        self._blank_symbol = blank_symbol
        self._position = 0
        self._tape = {index: item for index, item in enumerate(_input)}

    def __str__(self):
        return ''.join([item for item in self._tape.values()])

    @staticmethod
    def is_valid_direction(direction: str):
        return direction in Tape.DIRECTION_CHOICES.keys()

    def move_to_left(self):
        self._position -= 1

    def move_to_right(self):
        self._position += 1

    def get_value(self):
        """Get Value From Current Position"""
        if self._position not in self._tape.keys():
            return self._blank_symbol

        return self._tape[self._position]

    def set_value(self, value):
        """Set Value From Current Position"""
        self._tape[self._position] = value
