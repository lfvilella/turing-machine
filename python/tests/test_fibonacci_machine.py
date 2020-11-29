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
        tape_data = '1|2|3|5|7|13|21'

        machine = self._build_machine(tape_data=tape_data)
        result = machine.run()
        expected_result = {
            'tape': '1|2|3|5|7|13|21|#',
            'message': 'Work done!',
            'output': 'Accepted',
        }
        breakpoint()
        assert expected_result == result
