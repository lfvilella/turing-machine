from turing.machines import triple_balancing


class TestTripleBalancing:
    def _build_machine(
        self,
        initial_state='q0',
        final_state='qf',
        tape_data=None,
        blank_symbol='#',
    ):
        return triple_balancing.TripleBalancing(
            initial_state=initial_state,
            final_state=final_state,
            blank_symbol=blank_symbol,
            tape_data=tape_data,
        )

    def test_accept_aaabbbccc(self):
        tape_data = 'a|a|a|b|b|b|c|c|c'

        machine = self._build_machine(tape_data=tape_data)
        result = machine.run()
        expected_result = {
            'tape': 'A|A|A|B|B|B|C|C|C|#',
            'message': 'Work done!',
            'output': 'Accepted',
        }
        assert expected_result == result

    def test_accept_aaaaaabbbbbbcccccc(self):
        tape_data = 'a|a|a|a|a|a|b|b|b|b|b|b|c|c|c|c|c|c'

        machine = self._build_machine(tape_data=tape_data)
        result = machine.run()
        expected_result = {
            'tape': 'A|A|A|A|A|A|B|B|B|B|B|B|C|C|C|C|C|C|#',
            'message': 'Work done!',
            'output': 'Accepted',
        }
        assert expected_result == result

    def test_reject_aabbccc(self):
        tape_data = 'a|a|b|b|c|c|c'

        machine = self._build_machine(tape_data=tape_data)
        result = machine.run()
        expected_result = {
            'tape': 'A|A|B|B|C|C|c|#',
            'message': 'Ops something is not OK',
            'output': 'Rejected',
        }
        assert expected_result == result

    def test_reject_abbbccc(self):
        tape_data = 'a|b|b|b|c|c|c'

        machine = self._build_machine(tape_data=tape_data)
        result = machine.run()
        expected_result = {
            'tape': 'A|B|b|b|C|c|c|#',
            'message': 'Ops something is not OK',
            'output': 'Rejected',
        }
        assert expected_result == result

    def test_reject_aacc(self):
        tape_data = 'a|a|c|c'

        machine = self._build_machine(tape_data=tape_data)
        result = machine.run()
        expected_result = {
            'tape': 'A|a|c|c|#',
            'message': 'Ops something is not OK',
            'output': 'Rejected',
        }
        assert expected_result == result
