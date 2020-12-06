"""Odd Machine

This machine change all number to odd. If not odd overwrites to 1.

For example:
  tape = [1, 2, 3, 77, 10]
  result = [1, 1, 3, 77, 1]
"""

from .. import universal_machine


class OddMachine(universal_machine.UniversalTuringMachine):
    def run(self):
        state_counter = 0

        symbol_at_head = self._tape.get_value()
        while symbol_at_head != self._tape._blank_symbol:
            try:
                symbol = (
                    '1' if int(symbol_at_head) % 2 == 0 else symbol_at_head
                )
            except ValueError:
                self.set_transitions(key='fail', value='*,*,*')
                return {
                    'tape': str(self._tape),
                    'message': 'Hey Human, I just accept numbers.',
                    'output': 'Rejected',
                    'transitions': self._transitions,
                }

            self._tape.set_value(symbol)
            self._tape.move_to_right()

            previous_state = state_counter
            state_counter += 1
            self.set_transitions(
                key=f'q{previous_state}->q{state_counter}',
                value=f'{symbol_at_head},{symbol},R',
            )

            symbol_at_head = self._tape.get_value()

        self.set_transitions(  # set final transition
            key=f'q{state_counter}->qf', value='#,#,R',
        )
        return {
            'tape': str(self._tape),
            'message': 'Work done!',
            'output': 'Accepted',
            'transitions': self._transitions,
        }
