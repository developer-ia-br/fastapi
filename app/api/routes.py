from fastapi import APIRouter, HTTPException

from app.schemas.item import Item

router = APIRouter()

_ITEMS: dict[int, Item] = {
    1: Item(id=1, name="Widget", price=9.99),
}


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id not in _ITEMS:
        raise HTTPException(status_code=404, detail="Item not found")
    return _ITEMS[item_id]
