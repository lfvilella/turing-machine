"""Fibonacci Machine

This machine solve fibonacci problem.

For example: '1|2|3|5|7|13|21'
"""

from .. import universal_machine


class FibonacciMachine(universal_machine.UniversalTuringMachine):
    def _is_fibonacci(self, number: int, memory_1: int, memory_2: int):
        return number == (memory_1 + memory_2)

    def run(self):
        symbol_at_head = self._tape.get_value()
        if symbol_at_head != '1':
            self.set_transitions(key='fail', value='*,*,*')
            return {
                'tape': str(self._tape),
                'message': 'Is it not fibonacci',
                'output': 'Rejected',
                'transitions': self._transitions,
            }

        state_counter, memory_1, memory_2 = 0, 0, 0
        while symbol_at_head != self._tape._blank_symbol:
            try:
                number = int(symbol_at_head)
            except ValueError:
                self.set_transitions(key='fail', value='*,*,*')
                return {
                    'tape': str(self._tape),
                    'message': 'Hey Human, I just accept numbers.',
                    'output': 'Rejected',
                    'transitions': self._transitions,
                }

            if self._tape._position > 1:
                self._tape.move_to_left()
                memory_1 = int(self._tape.get_value())

                self._tape.move_to_left()
                memory_2 = int(self._tape.get_value())

                self._tape.move_to_right()
                self._tape.move_to_right()
            else:
                memory_1 = number
                memory_2 = number

            if (
                not self._is_fibonacci(number, memory_1, memory_2)
                and self._tape._position > 1
            ):
                self.set_transitions(key='fail', value='*,*,*')
                return {
                    'tape': str(self._tape),
                    'message': 'Is it not fibonacci',
                    'output': 'Rejected',
                    'transitions': self._transitions,
                }

            self._tape.move_to_right()

            previous_state = state_counter
            state_counter += 1
            self.set_transitions(
                key=f'q{previous_state}->q{state_counter}',
                value=f'{symbol_at_head},{number},R',
            )

            symbol_at_head = self._tape.get_value()

        self.set_transitions(  # set final transition
            key=f'q{state_counter}->qf', value='#,#,R',
        )
        return {
            'tape': str(self._tape),
            'message': 'Work done! Is fibonacci.',
            'output': 'Accepted',
            'transitions': self._transitions,
        }
