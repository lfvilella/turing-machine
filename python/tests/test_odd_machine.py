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

        expected_tape_result = '1|1|3|77|1|#'
        assert expected_tape_result == result['tape']

    def test_odd_numbers_result_any_change(self):
        tape_data = '1|3|5|7|11'

        machine = self._build_machine(tape_data=tape_data)
        result = machine.run()

        expected_tape_result = f'{tape_data}|#'
        assert expected_tape_result == result['tape']

    def test_char_raises(self):
        tape_data = '1|3|E|7|A'

        machine = self._build_machine(tape_data=tape_data)
        result = machine.run()

        expected_tape_result = {'error': 'Hey Human, I just accept numbers.'}
        assert expected_tape_result == result
