"""Odd Machine

This machine change all number to odd. If not odd overwrites to 1.

For example:
  tape = [1, 2, 3, 77, 10]
  result = [1, 1, 3, 77, 1]
"""

from .. import universal_machine


class OddMachine(universal_machine.UniversalTuringMachine):
    def run(self):
        while self._current_state != self._final_state:
            symbol_at_head = self._tape.get_value()

            if symbol_at_head == self._tape._blank_symbol:
                self._current_state = self._final_state
                continue

            try:
                symbol_at_head = (
                    '1' if int(symbol_at_head) % 2 == 0 else symbol_at_head
                )
            except ValueError:
                return {'error': 'Hey Human, I just accept numbers.'}

            self._tape.set_value(symbol_at_head)
            self._tape.move_to_right()

        return {'tape': str(self._tape), 'message': 'Work done!'}
