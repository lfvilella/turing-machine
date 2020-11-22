"""Transition

This module is about the turing machine Transition

TODO: describe more about it...
"""

from . import tape


class TransitionException(Exception):
    """Transition Exception"""

    pass


class NotFound(TransitionException):
    """Transition Not Found"""

    pass


class ParseError(TransitionException):
    """Transition Parse Error"""

    pass


class Transition:
    def __init__(
        self,
        state_current,
        symbol_current,
        state_next,
        symbol_next,
        tape_motion,
    ):
        self.expected_state_symbol_pair = (state_current, symbol_current)
        self.state_next = state_next
        self.symbol_next = symbol_next
        self.tape_motion = tape_motion

    @staticmethod
    def from_data_string(transition_as_string):
        splitted = transition_as_string.split()
        if len(splitted) != 5:
            raise ParseError(
                f'Transition "{transition_as_string}" '
                'has incorrect number of arguments'
            )

        if not tape.Tape.is_valid_direction(splitted[-1]):
            raise ParseError(
                f'Transition "{transition_as_string}" '
                f'has invalid tape motion "{splitted[-1]}"'
            )
        return Transition(
            splitted[0], splitted[1], splitted[2], splitted[3], splitted[4]
        )


class TransitionTable(object):
    def __init__(self):
        self._transitions = {}

    def add_transition(self, transition):
        self._transitions[transition.expected_state_symbol_pair] = transition

    def get_transition_for(self, state_current, symbol_current):
        current_state_symbol_pair = (state_current, symbol_current)

        if current_state_symbol_pair not in self._transitions:
            raise NotFound(
                'No transition found for state '
                f'{state_current} and symbol {symbol_current}'
            )

        return self._transitions[current_state_symbol_pair]
