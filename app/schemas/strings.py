from pydantic import BaseModel


class ConcatResult(BaseModel):
    result: str
