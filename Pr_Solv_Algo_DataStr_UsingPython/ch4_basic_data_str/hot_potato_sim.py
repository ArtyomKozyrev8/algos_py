from typing import List, Any

from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.queue import Queue


def hot_potato(names: List[Any], num: int) -> Any:
    """
    Hot potato game simulation.
    :param names: list of players
    :param num: number of steps to exclude player from Queue
    :return: the last player
    """
    assert len(names) >= 1, "Should be at least one player"

    if len(names) == 1:
        return names[0]

    q = Queue()

    for i in names:
        q.enqueue(i)

    while q.size() > 1:
        for _ in range(num):
            item = q.dequeue()
            q.enqueue(item)
        q.dequeue()

    return q.dequeue()
