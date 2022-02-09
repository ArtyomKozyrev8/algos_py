from typing import Union, Any


class Node:
    def __init__(self, val: Any):
        self.val = val
        self._next = None

    @property
    def next(self) -> Union["Node", None]:
        return self._next

    @next.setter
    def next(self, next_node: Union["Node", None]) -> None:
        self._next = next_node

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.val})"


class List:
    def __init__(self):
        self._head = None
        self._len = 0

    def __repr__(self):
        cur = self._head
        items = []
        while cur is not None:
            items.append(cur.val)
            cur = cur.next

        if items:
            items.append(None)

        return f"List({'->'.join(map(str, items))})"

    def reverse(self) -> "List":
        cur = self._head
        if cur is None:
            return self

        prev = None

        while True:
            _next = cur.next
            cur.next = prev
            prev = cur

            if _next is None:
                break

            cur = _next

        self._head = prev
        return self

    def repr_rec(self) -> str:
        def repr_rec_inner(node: Node) -> str:
            if node is None:
                return "None"

            return str(node.val) + "->" + repr_rec_inner(node.next)

        return repr_rec_inner(self._head)

    def add(self, item: Node) -> None:
        temp = self._head
        item.next = temp
        self._head = item
        self._len += 1

    def remove(self, item: Node) -> None:
        if self.is_empty():
            raise IndexError(f"Can't remove from empty list")

        cur = self._head
        prev = None
        while cur is not None:
            if cur.val == item.val:
                if prev is None:
                    self._head = cur.next
                else:
                    prev.next = cur.next
                self._len -= 1
                return
            prev = cur
            cur = cur.next

        raise ValueError(f"{item} is not in the List")

    def search(self, item: Node) -> bool:
        cur = self._head
        while cur is not None:
            if cur.val == item.val:
                return True
            cur = cur.next

        return False

    def is_empty(self) -> bool:
        if self._head is None:
            return True
        return False

    def size(self) -> int:
        return self._len

    def append(self, item: Node) -> None:
        cur = self._head
        while cur is not None:
            temp = cur.next
            if temp is None:
                break
            cur = cur.next
        cur.next = item
        self._len += 1

    def index(self, item: Node) -> int:
        cur = self._head
        index = 0
        while cur is not None:
            if cur.val == item.val:
                return index
            else:
                cur = cur.next
                index += 1
        raise ValueError(f"{item} is not in the list")

    def insert(self, pos: int, item: Node) -> None:
        cur = self._head
        prev = None
        cur_pos = 0
        while cur is not None:
            if cur_pos == pos:
                if prev is None:
                    self._head = item
                    self._head.next = cur
                    self._len += 1
                    return
                else:
                    prev.next = item
                    item.next = cur
                    self._len += 1
                    return
            cur_pos += 1
            prev = cur
            cur = cur.next

        if prev:
            prev.next = item
            item.next = cur
        else:
            self._head = item
        self._len += 1

    def pop(self, pos: int = None) -> Node:
        if self._len == 0:
            raise IndexError("Cant remove from empty List")

        cur = self._head
        prev = None

        if pos is None:
            while cur.next is not None:
                prev = cur
                cur = cur.next

            if prev is None:
                self._head = None
            else:
                prev.next = None

            self._len -= 1
        else:
            if self._len - 1 < pos:
                raise IndexError(f"Can't remove item in position {pos}. List length is {self._len}")

            index = 0
            while cur is not None:
                if index == pos:
                    if prev is None:
                        self._head = cur.next
                        break
                    else:
                        prev.next = cur.next

                prev = cur
                cur = cur.next
                index += 1
            self._len -= 1
