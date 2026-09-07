from typing import Annotated

from fastapi import APIRouter, Path

from app.schemas.strings import ConcatResult

router = APIRouter(prefix="/str", tags=["strings"])


@router.get("/{value}")
def concat(
    value: Annotated[str, Path(description="The string to concatenate with 'X'")],
) -> ConcatResult:
    return ConcatResult(result=value + "X")
