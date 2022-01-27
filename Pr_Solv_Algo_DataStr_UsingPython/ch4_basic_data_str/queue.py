from typing import Any


class Queue:
    def __init__(self) -> None:
        self._items = []

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._items})"

    def enqueue(self, item: Any) -> None:
        self._items.insert(0, item)

    def dequeue(self) -> Any:
        return self._items.pop()  # can raise Error

    def is_empty(self) -> bool:
        if not len(self._items):
            return True
        return False

    def size(self) -> int:
        return len(self._items)
