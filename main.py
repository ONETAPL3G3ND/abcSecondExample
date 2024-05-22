from abc import ABCMeta, abstractmethod

class Animals(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        ...

    @abstractmethod
    def punch(self):
        ...


class Dog(Animals):
    def run(self):
        return "run"


if __name__ == '__main__':
    d = Dog() #TypeError: Can't instantiate abstract class Dog without an implementation for abstract method 'punch'
