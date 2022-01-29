from random import randint
from typing import Union, List

from Pr_Solv_Algo_DataStr_UsingPython.ch4_basic_data_str.queue import Queue


class PrintingTask:
    def __init__(self, creation_time: int) -> None:
        assert creation_time >= 0
        self.pages: int = randint(1, 20)  # how many pages we need to print
        self.creation_time: int = creation_time  # when task was created
        self.wait_time: int = 0  # how much time left before printer started and finished the task
        self.completed = False  # shows if printer finished the task

    def __repr__(self) -> str:
        return f"PrintingTask(pages={self.pages}, creation_time={self.creation_time})"

    def __str__(self) -> str:
        if self.completed:
            return f"PrintingTask(pages={self.pages}, creation_time={self.creation_time}," \
                   f" was_finished={self.creation_time + self.wait_time})"
        else:
            return repr(self)

    def calculate_wait_time(self, current_time: int) -> None:
        """Calculates how much time left from moment when task was created till the moment task was finished"""
        assert current_time >= self.creation_time
        self.wait_time = current_time - self.creation_time  # how much time left from task creation
        self.completed = True  # mark as finished


class Printer:
    def __init__(self, ppm: int) -> None:
        self._ppm = ppm  # pages per minute
        self.task_queue: Queue = Queue()  # contains all tasks to do
        self._current_task = None  # let's start from no active tasks
        self._time_to_complete_task = 0  # time left to complete current task
        self._current_time = 0  # system time

    def work(self):
        """Simulates work of printer"""
        self._current_time += 1
        if self._current_task:
            self._time_to_complete_task -= 1
            if self._time_to_complete_task == 0:  # task was finished
                self._current_task.calculate_wait_time(self._current_time)
                self._current_task = None
        else:
            self._get_new_task()

    def _get_new_task(self):
        """Takes new task """
        if not self.task_queue.is_empty():
            task = self.task_queue.dequeue()
            self._current_task = task
            self._time_to_complete_task = self._current_task.pages * 60 / self._ppm
            self._time_to_complete_task -= 1


def create_task(cur_time: int) -> Union[None, PrintingTask]:
    """Support function which creates Printing Task or do nothing"""
    if randint(0, 181) == 180:
        return PrintingTask(cur_time)
    return None


def get_results(tasks: List[PrintingTask]) -> None:
    """Displays results of experiment"""
    completed_tasks = [i for i in tasks if i.completed]
    avg_wait = sum([i.wait_time for i in tasks]) / len(completed_tasks)
    print(
        (
            f"Total Tasks: {len(tasks)}. Completed Tasks: {len(completed_tasks)}."
            f" Avg Wait: {avg_wait:.3f} NOT Finished Tasks: {len(tasks) - len(completed_tasks)} "
        )
    )

    not_completed_tasks = [i for i in tasks if not i.completed]

    if not_completed_tasks:
        print(f"Not Completed: {', '.join(map(str, not_completed_tasks))}")
        print(f"Prev finished task: {', '.join(map(str, completed_tasks[-2:]))}")


if __name__ == '__main__':
    # simulate experiment 20 time
    for _ in range(20):
        _tasks = []
        printer = Printer(ppm=20)
        for t in range(3600):  # t is current_time
            if new_task := create_task(cur_time=t):
                _tasks.append(new_task)
                printer.task_queue.enqueue(new_task)
            printer.work()

        get_results(_tasks)

