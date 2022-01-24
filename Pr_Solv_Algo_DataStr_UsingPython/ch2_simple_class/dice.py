from random import randint


class Dice:
    def __init__(self, side_number: int) -> None:
        assert side_number >= 3, "Number of sides should be >= 3"
        self.side_number = side_number
        self.cur_value = 1

    def throw(self) -> int:
        self.cur_value = randint(1, self.side_number)
        return self.cur_value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(cur_val={self.cur_value}, side_number={self.side_number})"

    def __str__(self) -> str:
        return str(self.cur_value)
