from fastapi.middleware.cors import CORSMiddleware
import fastapi

from . import schemas, services

_VERSION = '/api/v.1'


app = fastapi.FastAPI(
    openapi_url=_VERSION + '/openapi.json', docs_url=_VERSION + '/docs',
)

origins = [
    'http://localhost',
    'http://localhost:3000',
]

app.add_middleware(  # to able frontend
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
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
