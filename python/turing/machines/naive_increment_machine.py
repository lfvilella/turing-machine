"""Naive Increment Machine

This machine just acept 1 on input.

This rep inspire me: https://github.com/jwoschitz/turing-python
"""

from .. import universal_machine


class NaiveIncrementMachine(universal_machine.UniversalTuringMachine):
    """This machine just increment an element on last position Tape"""

    def run(self):
        while self._current_state not in self._accepting_states:
            symbol_at_head = self._tape.get_value()

            _transition = self._transitions.get_transition_for(
                self._current_state, symbol_at_head
            )

            self._tape.set_value(_transition.symbol_next)

            if _transition.tape_motion == 'R':
                self._tape.move_to_right()

            elif _transition.tape_motion == 'L':
                self._tape.move_to_left()

            self._current_state = _transition.state_next

        return str(self._tape)
