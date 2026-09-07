from pydantic import BaseModel


class DoubleResult(BaseModel):
    result: int
