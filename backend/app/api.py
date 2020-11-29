import fastapi

from . import schemas, services

_VERSION = '/api/v.1'


app = fastapi.FastAPI(
    openapi_url=_VERSION + '/openapi.json', docs_url=_VERSION + '/docs',
)


@app.post(
    _VERSION + '/machine/triple_balancing',
    status_code=200,
    response_model=schemas.MachineResponse,
)
def triple_balancing_machine(tape_input: schemas.TapeInput):
    return services.run_triple_balancing_machine(
        tape_input=schemas.TapeInput(**tape_input.dict())
    )


@app.post(
    _VERSION + '/machine/fibonacci',
    status_code=200,
    response_model=schemas.MachineResponse,
)
def fibonacci_machine(tape_input: schemas.TapeInput):
    return services.run_fibonacci_machine(
        tape_input=schemas.TapeInput(**tape_input.dict())
    )


@app.post(
    _VERSION + '/machine/odd',
    status_code=200,
    response_model=schemas.MachineResponse,
)
def odd_machine(tape_input: schemas.TapeInput):
    return services.run_odd_machine(
        tape_input=schemas.TapeInput(**tape_input.dict())
    )
