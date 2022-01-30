from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.deque import Dequeue


def check_palindrome(x: str) -> bool:
    if len(x) <= 1:
        return True

    q = Dequeue()

    for i in x:
        q.add_front(i)

    while q.size() > 1:
        if q.remove_rear() != q.remove_front():
            return False

    return True
