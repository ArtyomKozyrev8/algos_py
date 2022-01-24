class LogicGate:
    def __init__(self, label: str) -> None:
        self.label = label

    def do_logic(self):
        raise NotImplemented

    def get_output(self):
        return self.do_logic()


class UnaryGate(LogicGate):
    def __init__(self, label: str, _input: bool) -> None:
        super().__init__(label)
        self.input = _input

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.label}, {self.input})"


class BinaryGate(LogicGate):
    def __init__(self, label: str, a: bool, b: bool) -> None:
        super().__init__(label)
        self.a = a
        self.b = b

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.label}, {self.a}, {self.b})"


class AndGate(BinaryGate):
    def do_logic(self) -> bool:
        return self.a and self.b


class OrGate(BinaryGate):
    def do_logic(self) -> bool:
        return self.a or self.b


class NotGate(UnaryGate):
    def do_logic(self) -> bool:
        return not self.input
