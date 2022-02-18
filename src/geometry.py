from abc import ABC

class CoordinateSystem(ABC):
    """座標系"""
    pass

class WorldCoordinateSystem(CoordinateSystem):
    """ワールド座標系"""
    pass

class ThreeDimensionalRectangularCoordinateSystem(CoordinateSystem):
    """3次元直交座標系"""
    pass

class Coordinates(ABC):
    """座標"""
    pass

class ThreeDimensionalRectangularCoordinates(Coordinates):
    """3次元直交座標"""

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
        self._coordinate_system = ThreeDimensionalRectangularCoordinateSystem()

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

