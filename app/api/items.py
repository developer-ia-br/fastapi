from typing import Annotated

from fastapi import APIRouter, HTTPException, Path

from app.schemas.item import Item

router = APIRouter(prefix="/items", tags=["items"])

_ITEMS: dict[int, Item] = {
    1: Item(id=1, name="Widget", price=9.99),
}


@router.get("/{item_id}")
def get_item(item_id: Annotated[int, Path(ge=1, description="The item ID")]) -> Item:
    if item_id not in _ITEMS:
        raise HTTPException(status_code=404, detail="Item not found")
    return _ITEMS[item_id]
