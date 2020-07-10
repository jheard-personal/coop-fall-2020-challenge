from enum import Enum

class Events(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4

class Event():
    def __init__(self, value, change, event):
        self.value = value
        self.change = change
        self.event = event

class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.current_event = -1
        self.events = []

    def add(self, num: int):
        self.current_event += 1
        self.events.append(Event(self.value, num, Events.ADD))
        self.value += num

    def subtract(self, num: int):
        self.current_event += 1
        self.events.append(Event(self.value, num, Events.SUBTRACT))
        self.value -= num

    def multiply(self, num: int):
        self.current_event += 1
        self.events.append(Event(self.value, num, Events.MULTIPLY))
        self.value *= num

    # Note: this performs integer division, and will floor the result
    def divide(self, num: int):
        self.current_event += 1
        self.events.append(Event(self.value, num, Events.DIVIDE))
        self.value //= num

    def undo(self):
        # Nothing to undo
        if self.current_event == -1:
            return
        self.value = self.events[self.current_event].value
        self.current_event -= 1

    def redo(self):
        # Nothing to redo
        if self.current_event == len(self.events)-1:
            return
        ev = self.events[self.current_event]
        self.__do_event(ev)
        self.current_event += 1

    def bulk_undo(self, steps: int):
        for _ in range(steps):
            self.undo()

    def bulk_redo(self, steps: int):
        for _ in range(steps):
            self.redo()

    def __do_event(self, ev: Event):
        if ev.event == Events.ADD:
            self.value += ev.change
        if ev.event == Events.SUBTRACT:
            self.value -= ev.change
        if ev.event == Events.MULTIPLY:
            self.value *= ev.change
        if ev.event == Events.DIVIDE:
            self.value //= ev.change
