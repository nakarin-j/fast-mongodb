from db import db
from datetime import datetime
from typing import List
from bson.objectid import ObjectId
from schemas.item import InputItem, UpdateItem

def get_items():
    data = db['items'].find()
    return [i for i in data]


def get_item_by_id(item_id: str) -> dict:
    return db['items'].find_one({'_id': ObjectId(item_id)})


def create_item(item: InputItem) -> None:
    db['items'].insert(item.dict())


def update_item(item_id: int, input_item: UpdateItem) -> None:
    db['items'].update_one({"_id": ObjectId(item_id)}, {"$set": input_item.dict()})


def delete_item(item_id: int):
    db['items'].delete_one({"_id": ObjectId(item_id)})