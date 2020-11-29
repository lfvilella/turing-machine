from turing.machines import odd_machine


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
        }
        assert expected_result == result

    def test_odd_numbers_result_any_change(self):
        tape_data = '1|3|5|7|11'

        machine = self._build_machine(tape_data=tape_data)
        result = machine.run()

        expected_result = {
            'tape': f'{tape_data}|#',
            'message': 'Work done!',
            'output': 'Accepted',
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
        }
        assert expected_result == result