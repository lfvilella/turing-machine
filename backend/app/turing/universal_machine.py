"""Universal Turing Machine

This module is about the UTM.

All machines what use this generic class is
  forced to implement the programing function.
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
        self._transitions = []

    @abc.abstractclassmethod
    def run(self):
        pass

    def set_transitions(self, key, value):
        self._transitions.append({key: value})
