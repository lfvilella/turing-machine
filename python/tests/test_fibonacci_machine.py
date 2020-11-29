from turing.machines import fibonacci_machine


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
        }
        assert expected_result == result
