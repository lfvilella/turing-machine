from .turing.machines import (
    fibonacci_machine,
    odd_machine,
    triple_balancing_machine,
)


def run_triple_balancing_machine(tape_input: str):
    machine = triple_balancing_machine.TripleBalancingMachine(
        initial_state='q0',
        final_state='qf',
        tape_data=tape_input.tape,
        blank_symbol='#',
    )
    return machine.run()


def run_fibonacci_machine(tape_input: str):
    machine = fibonacci_machine.FibonacciMachine(
        initial_state='q0',
        final_state='qf',
        tape_data=tape_input.tape,
        blank_symbol='#',
    )
    return machine.run()


def run_odd_machine(tape_input: str):
    machine = odd_machine.OddMachine(
        initial_state='q0',
        final_state='qf',
        tape_data=tape_input.tape,
        blank_symbol='#',
    )
    return machine.run()
