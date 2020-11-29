"""Triple Balancing Machine

This machine change solved triple balancing problem.

For example: 'a|a|a|b|b|b|c|c|c'
"""

from .. import universal_machine


class TripleBalancingMachine(universal_machine.UniversalTuringMachine):
    def run(self):
        while self._current_state != self._final_state:
            symbol_at_head = self._tape.get_value()

            if self._current_state == 'q0' and symbol_at_head == 'a':
                self._tape.set_value('A')
                self._tape.move_to_right()
                self._current_state = 'q1'

            elif self._current_state == 'q1' and symbol_at_head == 'a':
                self._tape.set_value('a')
                self._tape.move_to_right()
                self._current_state = 'q1'

            elif self._current_state == 'q1' and symbol_at_head == 'B':
                self._tape.set_value('B')
                self._tape.move_to_right()
                self._current_state = 'q1'

            elif self._current_state == 'q1' and symbol_at_head == 'b':
                self._tape.set_value('B')
                self._tape.move_to_right()
                self._current_state = 'q2'

            elif self._current_state == 'q2' and symbol_at_head == 'b':
                self._tape.set_value('b')
                self._tape.move_to_right()
                self._current_state = 'q2'

            elif self._current_state == 'q2' and symbol_at_head == 'C':
                self._tape.set_value('C')
                self._tape.move_to_right()
                self._current_state = 'q2'

            elif self._current_state == 'q2' and symbol_at_head == 'c':
                self._tape.set_value('C')
                self._tape.move_to_left()
                self._current_state = 'q3'

            elif self._current_state == 'q3' and symbol_at_head == 'b':
                self._tape.set_value('b')
                self._tape.move_to_left()
                self._current_state = 'q3'

            elif self._current_state == 'q3' and symbol_at_head == 'C':
                self._tape.set_value('C')
                self._tape.move_to_left()
                self._current_state = 'q3'

            elif self._current_state == 'q3' and symbol_at_head == 'B':
                self._tape.set_value('B')
                self._tape.move_to_left()
                self._current_state = 'q4'

            elif self._current_state == 'q4' and symbol_at_head == 'a':
                self._tape.set_value('a')
                self._tape.move_to_left()
                self._current_state = 'q4'

            elif self._current_state == 'q4' and symbol_at_head == 'B':
                self._tape.set_value('B')
                self._tape.move_to_left()
                self._current_state = 'q4'

            elif self._current_state == 'q4' and symbol_at_head == 'A':
                self._tape.set_value('A')
                self._tape.move_to_right()
                self._current_state = 'q0'

            elif self._current_state == 'q0' and symbol_at_head == 'B':
                self._tape.set_value('B')
                self._tape.move_to_right()
                self._current_state = 'q5'

            elif self._current_state == 'q5' and symbol_at_head == 'B':
                self._tape.set_value('B')
                self._tape.move_to_right()
                self._current_state = 'q5'

            elif self._current_state == 'q5' and symbol_at_head == 'C':
                self._tape.set_value('C')
                self._tape.move_to_right()
                self._current_state = 'q6'

            elif self._current_state == 'q6' and symbol_at_head == 'C':
                self._tape.set_value('C')
                self._tape.move_to_right()
                self._current_state = 'q6'

            elif (
                self._current_state == 'q6'
                and symbol_at_head == self._tape._blank_symbol
            ):
                self._tape.move_to_right()
                self._current_state = 'qf'

            else:
                return {
                    'tape': str(self._tape),
                    'message': 'Ops something is not OK',
                    'output': 'Rejected',
                }

        return {
            'tape': str(self._tape),
            'message': 'Work done!',
            'output': 'Accepted',
        }
