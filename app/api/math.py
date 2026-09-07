from typing import Annotated

from fastapi import APIRouter, Path

from app.schemas.math import DoubleResult

router = APIRouter(prefix="/math", tags=["math"])


@router.get("/double/{value}")
def double(value: Annotated[int, Path(description="The integer to double")]) -> DoubleResult:
    return DoubleResult(result=value * 2)
