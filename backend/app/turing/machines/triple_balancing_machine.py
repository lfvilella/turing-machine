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
                self.set_transitions(key='q0->q1', value='a,A,R')

            elif self._current_state == 'q1' and symbol_at_head == 'a':
                self._tape.set_value('a')
                self._tape.move_to_right()
                self._current_state = 'q1'
                self.set_transitions(key='q1->q1', value='a,a,R')

            elif self._current_state == 'q1' and symbol_at_head == 'B':
                self._tape.set_value('B')
                self._tape.move_to_right()
                self._current_state = 'q1'
                self.set_transitions(key='q1->q1', value='B,B,R')

            elif self._current_state == 'q1' and symbol_at_head == 'b':
                self._tape.set_value('B')
                self._tape.move_to_right()
                self._current_state = 'q2'
                self.set_transitions(key='q1->q2', value='b,B,R')

            elif self._current_state == 'q2' and symbol_at_head == 'b':
                self._tape.set_value('b')
                self._tape.move_to_right()
                self._current_state = 'q2'
                self.set_transitions(key='q2->q2', value='b,b,R')

            elif self._current_state == 'q2' and symbol_at_head == 'C':
                self._tape.set_value('C')
                self._tape.move_to_right()
                self._current_state = 'q2'
                self.set_transitions(key='q2->q2', value='C,C,R')

            elif self._current_state == 'q2' and symbol_at_head == 'c':
                self._tape.set_value('C')
                self._tape.move_to_left()
                self._current_state = 'q3'
                self.set_transitions(key='q2->q3', value='c,C,L')

            elif self._current_state == 'q3' and symbol_at_head == 'b':
                self._tape.set_value('b')
                self._tape.move_to_left()
                self._current_state = 'q3'
                self.set_transitions(key='q3->q3', value='b,b,L')

            elif self._current_state == 'q3' and symbol_at_head == 'C':
                self._tape.set_value('C')
                self._tape.move_to_left()
                self._current_state = 'q3'
                self.set_transitions(key='q3->q3', value='C,C,L')

            elif self._current_state == 'q3' and symbol_at_head == 'B':
                self._tape.set_value('B')
                self._tape.move_to_left()
                self._current_state = 'q4'
                self.set_transitions(key='q3->q4', value='B,B,L')

            elif self._current_state == 'q4' and symbol_at_head == 'a':
                self._tape.set_value('a')
                self._tape.move_to_left()
                self._current_state = 'q4'
                self.set_transitions(key='q4->q4', value='a,a,L')

            elif self._current_state == 'q4' and symbol_at_head == 'B':
                self._tape.set_value('B')
                self._tape.move_to_left()
                self._current_state = 'q4'
                self.set_transitions(key='q4->q4', value='B,B,L')

            elif self._current_state == 'q4' and symbol_at_head == 'A':
                self._tape.set_value('A')
                self._tape.move_to_right()
                self._current_state = 'q0'
                self.set_transitions(key='q4->q0', value='A,A,R')

            elif self._current_state == 'q0' and symbol_at_head == 'B':
                self._tape.set_value('B')
                self._tape.move_to_right()
                self._current_state = 'q5'
                self.set_transitions(key='q0->q5', value='B,B,R')

            elif self._current_state == 'q5' and symbol_at_head == 'B':
                self._tape.set_value('B')
                self._tape.move_to_right()
                self._current_state = 'q5'
                self.set_transitions(key='q5->q5', value='B,B,R')

            elif self._current_state == 'q5' and symbol_at_head == 'C':
                self._tape.set_value('C')
                self._tape.move_to_right()
                self._current_state = 'q6'
                self.set_transitions(key='q5->q6', value='C,C,R')

            elif self._current_state == 'q6' and symbol_at_head == 'C':
                self._tape.set_value('C')
                self._tape.move_to_right()
                self._current_state = 'q6'
                self.set_transitions(key='q6->q6', value='C,C,R')

            elif (
                self._current_state == 'q6'
                and symbol_at_head == self._tape._blank_symbol
            ):
                self._tape.move_to_right()
                self._current_state = 'qf'
                self.set_transitions(key='q6->qf', value='#,#,R')

            else:
                self.set_transitions(key='fail', value='*,*,*')
                return {
                    'tape': str(self._tape),
                    'message': 'Ops... Is not a triple balancing.',
                    'output': 'Rejected',
                    'transitions': self._transitions,
                }

        return {
            'tape': str(self._tape),
            'message': 'Work done!',
            'output': 'Accepted',
            'transitions': self._transitions,
        }
