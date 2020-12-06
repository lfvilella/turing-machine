from app.turing.machines import odd_machine


class TestOddMachine:
    def _build_machine(
        self,
        initial_state='q0',
        final_state='qf',
        tape_data=None,
        blank_symbol='#',
    ):
        return odd_machine.OddMachine(
            initial_state=initial_state,
            final_state=final_state,
            blank_symbol=blank_symbol,
            tape_data=tape_data,
        )

    def test_convert_pair_numbers_to_one(self):
        tape_data = '1|2|3|77|10'

        machine = self._build_machine(tape_data=tape_data)
        result = machine.run()

        expected_result = {
            'tape': '1|1|3|77|1|#',
            'message': 'Work done!',
            'output': 'Accepted',
            'transitions': [
                {'q0->q1': '1,1,R'},
                {'q1->q2': '2,1,R'},
                {'q2->q3': '3,3,R'},
                {'q3->q4': '77,77,R'},
                {'q4->q5': '10,1,R'},
            ],
        }
        assert expected_result == result

    def test_odd_numbers_result_any_change(self):
        tape_data = '1|3|5|7|11'

        machine = self._build_machine(tape_data=tape_data)
        result = machine.run()

        expected_result = {
            'tape': '1|3|5|7|11|#',
            'message': 'Work done!',
            'output': 'Accepted',
            'transitions': [
                {'q0->q1': '1,1,R'},
                {'q1->q2': '3,3,R'},
                {'q2->q3': '5,5,R'},
                {'q3->q4': '7,7,R'},
                {'q4->q5': '11,11,R'},
            ],
        }
        assert expected_result == result

    def test_char_raises(self):
        tape_data = '1|3|E|7|A'

        machine = self._build_machine(tape_data=tape_data)
        result = machine.run()

        expected_result = {
            'tape': '1|3|E|7|A|#',
            'message': 'Hey Human, I just accept numbers.',
            'output': 'Rejected',
            'transitions': [
                {'q0->q1': '1,1,R'},
                {'q1->q2': '3,3,R'},
                {'fail': '*,*,*'},
            ],
        }
        assert expected_result == result
