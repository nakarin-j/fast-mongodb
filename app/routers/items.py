from fastapi import APIRouter
from schemas.item import InputItem, Item, UpdateItem
from typing import List

import app.services.item_service as ItemService

router = APIRouter(prefix='/items')

@router.get('/', response_model=List[Item])
async def get_items_list():
    resp = ItemService.get_items()
    return resp


@router.post('/')
async def create_item(item: InputItem):
    ItemService.create_item(item)
    return {"success": True}
    

@router.put('/{item_id}')
async def update_item(item_id: str, update_payload: UpdateItem):
    ItemService.update_item(item_id, update_payload)
    return {"success": True}
    

@router.delete('/{item_id}')
async def delete_item(item_id: int):
    ItemService.delete_item(item_id)
    return {"success": True}