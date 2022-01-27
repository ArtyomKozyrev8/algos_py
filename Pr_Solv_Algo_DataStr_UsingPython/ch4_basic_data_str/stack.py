from typing import Any


class Stack:
    def __init__(self) -> None:
        self._items = []

    def __repr__(self) -> str:
        return f"Stack({self._items})"

    def peek(self) -> Any:
        return self._items[-1]

    def is_empty(self) -> bool:
        if len(self._items) > 0:
            return False
        return True

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self) -> Any:
        return self._items.pop()  # can raise error if empty

    def size(self) -> int:
        return len(self._items)
