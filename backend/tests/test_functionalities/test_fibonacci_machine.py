from app.turing.machines import fibonacci_machine


class TestTripleBalancingMachine:
    def _build_machine(
        self,
        initial_state='q0',
        final_state='qf',
        tape_data=None,
        blank_symbol='#',
    ):
        return fibonacci_machine.FibonacciMachine(
            initial_state=initial_state,
            final_state=final_state,
            blank_symbol=blank_symbol,
            tape_data=tape_data,
        )

    def test_accept_right_sequence(self):
        tape_data = '1|2|3|5|8|13|21'

        machine = self._build_machine(tape_data=tape_data)
        result = machine.run()
        expected_result = {
            'tape': '1|2|3|5|8|13|21|#',
            'message': 'Work done! Is fibonacci.',
            'output': 'Accepted',
            'transitions': [
                {'q0->q1': '1,1,R'},
                {'q1->q2': '2,2,R'},
                {'q2->q3': '3,3,R'},
                {'q3->q4': '5,5,R'},
                {'q4->q5': '8,8,R'},
                {'q5->q6': '13,13,R'},
                {'q6->q7': '21,21,R'},
                {'q7->qf': '#,#,R'},
            ],
        }
        assert expected_result == result

    def test_2_accept_right_sequence(self):
        tape_data = '1|2|3|5|8|13|21|34|55'

        machine = self._build_machine(tape_data=tape_data)
        result = machine.run()
        expected_result = {
            'tape': '1|2|3|5|8|13|21|34|55|#',
            'message': 'Work done! Is fibonacci.',
            'output': 'Accepted',
            'transitions': [
                {'q0->q1': '1,1,R'},
                {'q1->q2': '2,2,R'},
                {'q2->q3': '3,3,R'},
                {'q3->q4': '5,5,R'},
                {'q4->q5': '8,8,R'},
                {'q5->q6': '13,13,R'},
                {'q6->q7': '21,21,R'},
                {'q7->q8': '34,34,R'},
                {'q8->q9': '55,55,R'},
                {'q9->qf': '#,#,R'},
            ],
        }
        assert expected_result == result

    def test_reject_invalid_sequence(self):
        tape_data = '1|2|3|5|7|13'

        machine = self._build_machine(tape_data=tape_data)
        result = machine.run()
        expected_result = {
            'tape': '1|2|3|5|7|13|#',
            'message': 'Is it not fibonacci',
            'output': 'Rejected',
            'transitions': [
                {'q0->q1': '1,1,R'},
                {'q1->q2': '2,2,R'},
                {'q2->q3': '3,3,R'},
                {'q3->q4': '5,5,R'},
                {'fail': '*,*,*'},
            ],
        }
        assert expected_result == result

    def test_2_reject_invalid_sequence(self):
        tape_data = '2|3|13'

        machine = self._build_machine(tape_data=tape_data)
        result = machine.run()
        expected_result = {
            'tape': '2|3|13|#',
            'message': 'Is it not fibonacci',
            'output': 'Rejected',
            'transitions': [{'fail': '*,*,*'}],
        }
        assert expected_result == result

    def test_3_reject_invalid_sequence(self):
        tape_data = '1|3|5|7|13'

        machine = self._build_machine(tape_data=tape_data)
        result = machine.run()
        expected_result = {
            'tape': '1|3|5|7|13|#',
            'message': 'Is it not fibonacci',
            'output': 'Rejected',
            'transitions': [
                {'q0->q1': '1,1,R'},
                {'q1->q2': '3,3,R'},
                {'fail': '*,*,*'},
            ],
        }
        assert expected_result == result

    def test_reject_char_sequence(self):
        tape_data = '1|2|A|B'

        machine = self._build_machine(tape_data=tape_data)
        result = machine.run()
        expected_result = {
            'tape': '1|2|A|B|#',
            'message': 'Hey Human, I just accept numbers.',
            'output': 'Rejected',
            'transitions': [
                {'q0->q1': '1,1,R'},
                {'q1->q2': '2,2,R'},
                {'fail': '*,*,*'},
            ],
        }
        assert expected_result == result
