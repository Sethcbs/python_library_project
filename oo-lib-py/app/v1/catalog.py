
from .items import Item

class Catalog():
    def __init__(self): 
        self._items = {}

    def add(self, item: Item) -> None:
        if item.id.value not in self._items:
            self._items[item.id.value] = item
        else:
            raise ValueError(f"An item with key '{item.id.value}' is already in the catalog.")

    def get_item_details(self, item_ids):
        cataloged_item = self._items[item_ids]
        detail_string = (f"ID: {cataloged_item.id.value}, Title: {cataloged_item.title}, Days Allowed: ({str(cataloged_item.days_allowed())} days)")
                
        return detail_string

    def get(self, item_id):
        cataloged_item = self._items[item_id]
        return cataloged_item
