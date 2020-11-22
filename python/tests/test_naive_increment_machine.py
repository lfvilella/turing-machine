import pytest
from turing.machines import naive_increment_machine


class TestNaiveIncrementMachine:
    def _build_machine(
        self,
        initial_state='q0',
        accepting_states=['qf'],
        tape_data=None,
        blank_symbol='#',
        transition_data=[],
    ):
        return naive_increment_machine.NaiveIncrementMachine(
            initial_state=initial_state,
            accepting_states=accepting_states,
            tape_data=tape_data,
            blank_symbol=blank_symbol,
            transition_data=transition_data,
        )

    def test_increment_9_in_tape_111(self):
        tape_data = '111'
        blank_symbol = 'B'
        element_to_increment = '9'

        utm = self._build_machine(
            initial_state='q0',
            accepting_states=['qf'],
            tape_data=tape_data,
            blank_symbol=blank_symbol,
            transition_data=[
                'q0 1 q0 1 R',
                f'q0 {blank_symbol} qf {element_to_increment} S',
            ],
        )
        result = utm.run()
        assert result == (tape_data + element_to_increment)  # '1119'
