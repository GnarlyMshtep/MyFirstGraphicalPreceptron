
class Point:
    def __init__(self, xy: list):
        self.coords = xy
        self.label = 1 if xy[0] > xy[1] else -1

    def getCoords(self) -> list:
        return self.coords

    def getLabel(self) -> int:
        return self.label

    """
    So.. this is how you violate encapsulation in Python. I didn't wanna get messy with it as it wasn't the focus
    @property
    def coords(self):
        return self._coords

    @property
    def label(self):
        return self._label

    @a.setter
    def a(self, var):
        if var > 0 and var % 2 == 0:
            self.__a = var
        else:
            self.__a = 2
    """
