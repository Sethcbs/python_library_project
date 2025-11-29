from .catalog import Catalog 
from .items import Item

class Member:
    def __init__(self, name: str) -> None:
        self._name = name
        self._borrowed_ids = [] 

    def borrow(self, Id: id) -> None:
        print(f"Currently borrowing: {len(self._borrowed_ids)} items.")
        print(f"Allowed number of borrows is '{Item.borrows_allowed(self)}'")
        if len(self._borrowed_ids) == Item.borrows_allowed(self):
            raise ValueError(f"You are at the max number of borrows for this Member. Borrows = {Item.borrows_allowed}.")
        if Id not in self._borrowed_ids:
            self._borrowed_ids.append(Id)
        else:
            raise ValueError(f"You are already borrowing an item with the ID '{Id}'.")

    def name(self) -> str:
        return self._name

    def borrowed_ids(self) -> set():
        return self._borrowed_ids
    
    def list_details(self, catalog: Catalog):
        details = []
        for borrowed_id in self._borrowed_ids:
            details.append(catalog.get_item_details(borrowed_id))
        return details
    
    def return_item(self, item_id):
        if item_id not in self._borrowed_ids:
            raise ValueError(f"You don't have any items with the ID '{item_id}'.")
        else:
            self._borrowed_ids.remove(item_id)
