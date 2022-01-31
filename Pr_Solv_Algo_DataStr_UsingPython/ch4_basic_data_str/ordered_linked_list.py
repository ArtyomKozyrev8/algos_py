from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.linked_list import Node
from typing import Any


class OrderedList:
    def __init__(self):
        self._head = None
        self._len = 0

    def __repr__(self):
        cur = self._head
        items = []
        while cur is not None:
            items.append(cur.val)
            cur = cur.next

        return f"OrderedList({', '.join(map(str, items))})"

    def add(self, item: Node) -> None:
        if self.is_empty():
            self._head = item
            self._len += 1
            return

        cur = self._head
        prev = None

        while cur is not None:
            if item.val >= cur.val:
                prev = cur
                cur = cur.next
            else:
                if prev:
                    prev.next = item
                    item.next = cur
                else:
                    self._head = item
                    item.next = cur
                self._len += 1
                return

        prev.next = item
        self._len += 1

    def remove(self, item: Node) -> None:
        if self.is_empty():
            raise IndexError("Can't remove item from empty List")

        cur = self._head
        prev = None
        while cur is not None:
            if cur.val > item.val:
                raise ValueError(f"{item} does not exist in the List")

            if cur.val == item.val:
                if prev:
                    prev.next = cur.next
                else:
                    self._head = cur.next
                self._len -= 1
                return

            prev = cur
            cur = cur.next

        raise ValueError(f"{item} does not exist in the List")

    def search(self, item: Node) -> bool:
        if self.is_empty():
            return False

        cur = self._head

        while cur is not None:
            if cur.val > item.val:
                return False
            elif cur.val == item.val:
                return True
            else:
                cur = cur.next

        return False

    def is_empty(self) -> bool:
        if self._len == 0:
            return True
        return False

    def size(self) -> int:
        return self._len

    def index(self, item: Node) -> int:
        if self.is_empty():
            raise IndexError("List is empty")

        cur = self._head
        index = 0
        while cur is not None:
            if cur.val > item.val:
                raise ValueError(f"{item} does not exist in List")
            elif cur.val == item.val:
                return index
            else:
                cur = cur.next
                index += 1

        raise ValueError(f"{item} does not exist in List")

    def pop(self, pos: int = None) -> Any:
        """The method is the same as it is for not ordered Linked List. I just decided to code it again"""
        if self.is_empty():
            raise IndexError("List is empty")

        if pos is None:
            pos = self.size() - 1

        cur = self._head
        prev = None
        cur_pos = 0

        while cur is not None:
            if cur_pos == pos:
                if prev:
                    prev.next = cur.next
                else:
                    self._head = cur.next

                self._len -= 1
                return cur.val
            else:
                cur_pos += 1
                prev = cur
                cur = cur.next

        raise IndexError(f"There is no index {pos} in the List")
