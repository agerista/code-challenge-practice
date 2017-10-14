import pytest
import math


class Distance(object):
    def __init__(self, meters=None, feet=None):
        # Please don't change this method
        if not any((meters, feet)):
            raise ValueError("Provide at least one measure of distance")

        self.meters = meters
        self.feet = feet

    def distance_in_meters(self):
        if self.meters is not None:
            return self.meters
        return self.feet / 3.2808

    def distance_in_feet(self):
        if self.feet is not None:
            return self.feet
        return self.meters * 3.28

    def distance_in_kilometers(self):
        if self.feet is not None:
            return self.feet * 0.0003048
        return self.meters * 0.001

    def distance_in_miles(self):
        if self.feet is not None:
            return self.feet * 0.000189394
        return self.meters * 0.000621371


##########################################################################
d = Distance(meters=8000)
print d.distance_in_meters()
print d.distance_in_miles()

def test_meters_to_miles():
    d = Distance(meters=8000)

    assert d.distance_in_meters() == 8000
    assert d.distance_in_miles() == pytest.approx(4.96, rel=1e-2)

def test_meters_to_feet():
    d = Distance(meters=8000)

    assert d.distance_in_meters() == 8000
    assert d.distance_in_feet() == 26240



def test_feet_to_kilometers():
    d = Distance(feet=25000)

    assert d.distance_in_feet() == 25000
    assert d.distance_in_kilometers() == pytest.approx(7.62, rel=1e-2)


def test_feet_to_meter():
    d = Distance(feet=25000)

    assert d.distance_in_feet() == 25000
    assert d.distance_in_meters() == pytest.approx(7621.95, rel=1e-2)


def test_meters_to_kilometers():
    d = Distance(meters=8000)

    assert d.distance_in_meters() == 8000
    assert d.distance_in_kilometers() == 8


def test_feet_to_miles():
    d = Distance(feet=25000)

    assert d.distance_in_feet() == 25000
    assert d.distance_in_miles() == pytest.approx(4.76, rel=1e-2)
