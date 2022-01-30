from typing import Any


class Dequeue:
    def __init__(self):
        self._items = []

    def __repr__(self):
        return f"{self.__class__.__name__}({self._items})"

    def add_rear(self, item: Any) -> None:
        self._items.insert(0, item)

    def add_front(self, item: Any) -> None:
        self._items.append(item)

    def remove_rear(self) -> Any:
        return self._items.pop(0)  # can cause error if empty

    def remove_front(self) -> Any:
        return self._items.pop()  # can cause error if empty

    def is_empty(self) -> Any:
        if not self._items:
            return True
        return False

    def size(self) -> int:
        return len(self._items)
