from abc import ABCMeta, abstractmethod


class ExpatriateOptions(metaclass=ABCMeta):
    """
    下拉选项抽象类
    """

    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def options(self):
        pass
