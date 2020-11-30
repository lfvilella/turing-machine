import pydantic


class TapeInput(pydantic.BaseModel):
    tape: str


class MachineResponse(pydantic.BaseModel):
    tape: str
    message: str
    output: str
