from abc import ABC

class CoordinateSystem(ABC):
    """座標系"""
    pass

class WorldCoordinateSystem(CoordinateSystem):
    """ワールド座標系"""
    pass

class Point:
    """座標点"""

    def __init__(self, x=0.0, y=0.0, z=0.0, coordinate_system=WorldCoordinateSystem()):
        self._x = x
        self._y = y
        self._z = z
        self._coordinate_system = coordinate_system

    def __str__(self):
        return "({},{},{})".format(self._x, self._y, self._z)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

