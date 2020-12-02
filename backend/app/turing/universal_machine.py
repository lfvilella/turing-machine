"""Universal Turing Machine

This module is about the UTM

TODO: describe more about it...
"""

import abc

from . import tape


class UniversalTuringMachine(metaclass=abc.ABCMeta):
    def __init__(
        self,
        initial_state='q0',
        final_state='qf',
        blank_symbol='#',
        tape_data='',
    ):
        self._tape = tape.Tape(tape_data, blank_symbol)
        self._current_state = initial_state
        self._final_state = final_state

    @abc.abstractclassmethod
    def run(self):
        pass