"""Universal Turing Machine

This module is about the UTM

TODO: describe more about it...
"""

import abc

from . import tape, transition


class UniversalTuringMachine(metaclass=abc.ABCMeta):
    def __init__(
        self,
        initial_state=None,
        accepting_states=None,
        blank_symbol=None,
        tape_data='',
        transition_data=None,
    ):
        self._current_state = initial_state
        self._accepting_states = accepting_states if accepting_states else []
        self._tape = tape.Tape(tape_data, blank_symbol)
        self._transitions = transition.TransitionTable()

        if transition_data:
            for transition_string in transition_data:
                self._transitions.add_transition(
                    transition.Transition.from_data_string(transition_string)
                )

    @abc.abstractclassmethod
    def run(self):
        pass
