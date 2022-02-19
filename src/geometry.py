from abc import ABC
import math

class CoordinateSystem(ABC):
    """座標系"""
    pass

class WorldCoordinateSystem(CoordinateSystem):
    """ワールド座標系"""
    pass

class TwoDimensionalRectangularCoordinateSystem(CoordinateSystem):
    """2次元直交座標系"""
    pass

class ThreeDimensionalRectangularCoordinateSystem(CoordinateSystem):
    """3次元直交座標系"""
    pass

class Coordinates(ABC):
    """座標"""
    pass

class TwoDimensionalRectangularCoordinates(Coordinates):
    """2次元直交座標"""

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._coordinate_system = TwoDimensionalRectangularCoordinateSystem()

    def __str__(self):
        return "({},{})".format(self._x, self._y)

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

    def translate(self, x, y):
        """平行移動する"""
        return TwoDimensionalRectangularCoordinates(self._x + x, self._y + y)

    def rotate(self, theta):
        """原点まわりに回転する.

        x軸からy軸に向かう方向が正の向き.

        Args:
            theta (float): 回転角度[Radian]

        Returns:
            TwoDimensionalRectangularCoordinates: 回転後の座標
        """
        return TwoDimensionalRectangularCoordinates(
            self._x * math.cos(theta) - self._y * math.sin(theta),
            self._x * math.sin(theta) + self._y * math.cos(theta)
        )

def calc_inner_point(point_a, point_b, m, n):
    """内分点を求める.

    異なる2点A, Bを結ぶ線分を、Aの方からm:n(m>0, n>0)に内分する点を求める.
    A           P     B
    *-----------*-----*
          m        n

    Args:
        point_a (TwoDimensionalRectangularCoordinates): 点A
        point_b (TwoDimensionalRectangularCoordinates): 点B
        m (float): 点A側の比
        n (float): 点B側の比

    Returns:
        TwoDimensionalRectangularCoordinates: 内分点
    """
    return TwoDimensionalRectangularCoordinates(
        (m * point_b.x + n * point_a.x) / (m + n),
        (m * point_b.y + n * point_a.y) / (m + n)
    )

def calc_outer_point(point_a, point_b, m, n):
    """外分点を求める.

    異なる2点A, Bを結ぶ線分を、Aの方からm:n(m>0, n>0, m!=n)に外分する点を求める.
    A           B     P
    *-----------*-----*
                <- n ->
    <------- m ------->

    Args:
        point_a (TwoDimensionalRectangularCoordinates): 点A
        point_b (TwoDimensionalRectangularCoordinates): 点B
        m (float): 点A側の比(m != n)
        n (float): 点B側の比(m != n)

    Returns:
        TwoDimensionalRectangularCoordinates: 外分点
    """
    return TwoDimensionalRectangularCoordinates(
        (m * point_b.x - n * point_a.x) / (m - n),
        (m * point_b.y - n * point_a.y) / (m - n)
    )

class Circle:
    """円"""

    def __init__(self, center, radius):
        """円コンストラクタ.

        Args:
            center (TwoDimensionalRectangularCoordinates): 中心
            radius (float): 半径
        """
        self._center = center
        self._radius = radius

    def __str__(self):
        return "{},{}".format(str(self._center), self._radius)

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
