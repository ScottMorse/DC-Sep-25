
class App:

    lists = []

    @classmethod
    def view_lists(self):
        print(App.lists)

    @classmethod
    def remove_list(self,list_id):
        if not isinstance(list_id,int):
            raise ValueError("List id should be an integer.")   
        if len(App.lists) == 0:
            print("No lists in app.")
            return
        try:
            del App.lists[list_id - 1]
        except:
            print("List not found.")

        if len(App.lists) > 0:
            n = 1
            for _list in App.lists:
                _list._list_id = n
                n += 1

class ShoppingList:

    def __init__(self,title):
        if not isinstance(title,str):
            raise ValueError("Title should be a string.")
        self._title = title
        self._items = []
        self._list_id = len(App.lists) + 1
        App.lists.append(self)

    @property
    def title(self):
        return self._title
    
    @property
    def items(self):
        return self._items

    @property
    def description(self):
        return f"{self._list_id} {self.title}: {self.items}"

    def add_item(self,item):
        if not isinstance(item,ShoppingItem):
            raise ValueError("Not a ShoppingItem object.")
        self._items.append(item)

    def add_items(self,*items):
        for item in items:
            if not isinstance(item,ShoppingItem):
                raise ValueError("Not a ShoppingItem object.")
            self.add_item(item)
    
    def remove_item(self,item):
        if not isinstance(item,ShoppingItem):
            raise ValueError("Not a ShoppingItem object.")
        for i in range(len(self.items)):
            if item == self.items[i]:
                del self._items[i]
                break
        else:
            print("Item not found")
            return
        if len(self.items) == 0:
            self.complete()
    
    def complete(self):
        if self not in App.lists:
            print("List already completed.")
            return
        App.remove_list(self._list_id)

    def __repr__(self):
        return f"<{self._list_id} {self.title}>"

class ShoppingItem:

    def __init__(self,title):
        if not isinstance(title,str):
            raise ValueError("Title of item should be a string.")
        self._title = title.lower().capitalize()
    
    @property
    def title(self):
        return self._title

    def __repr__(self):
        return f"<{self.title}>"


if __name__ == "__main__":
    
    print("Testing...")
    fiesta = ShoppingList("Fiesta")
    milk = ShoppingItem("Milk")
    soda = ShoppingItem("Soda")
    fish = ShoppingItem("fish")
    fiesta.add_items(milk,soda,fish)

    walmart = ShoppingList("Walmart")
    walmart.add_items(ShoppingItem("paper"),ShoppingItem("napkins"),ShoppingItem("plate"),ShoppingItem("chips"))

    sams = ShoppingList("Sam's Club")
    [sams.add_item(ShoppingItem(item)) for item in ("chicken","beef","eggs","sugar","salt","pepper","honey")]
    
    App.lists

    fiesta.remove_item(milk)
    fiesta.remove_item(soda)
    fiesta.remove_item(fish)

    fiesta.complete()

    App.remove_list(2)

    walmart.complete()

    App.view_lists()

    print("Test complete with no errors.")

