import pytest


class Weight(object):
    def __init__(self, kilometers=0, pounds=0):
        self.kilometers = kilometers
        self.pounds = pounds

        if self.kilometers is not None:
            self.unit = "kilometers"
        if self.pounds is not None:
            self.unit = "pounds"

    @classmethod
    def _to_kilos(cls):
        if cls.unit == 'kilograms':
            return cls
        return Weight(cls.weight / 2.2, 'kilograms')

    @classmethod
    def _to_pounds(cls):
        if cls.unit == 'pounds':
            return cls
        return Weight(cls.weight * 2.2, 'pounds')

    def __add__(self, other):
        other_converted = other

        if self.unit != other.unit:
            method_name = 'kilograms' if self.unit == 'kilograms' else 'pounds'

            fn_to_use = getattr(Weight, '_to_{}').format(method_name)

            other_converted = fn_to_use(other)

        return Weight(self.weight + other_converted.weight, self.unit)

    def __sub__(self, other):
        return Weight(self.weight - other.weight, 'kilograms')


#########################################################################
w1 = Weight(kilograms=80)
w2 = Weight(pounds=46)
w3 = w1 + w2

print(w3.kilograms)  # 100.90
print(w3.pounds)  # 222.0


def test_add_only_pounds():
    w1 = Weight(pounds=37)
    w2 = Weight(pounds=22)
    w3 = w1 + w2

    assert w3.pounds == 59


def test_add_kilograms_to_pounds():
    w1 = Weight(kilograms=80)
    w2 = Weight(pounds=46)
    w3 = w1 + w2

    assert w3.kilograms == pytest.approx(100.90, rel=0.01)
    assert w3.pounds == pytest.approx(222.0, rel=0.01)


def test_add_only_kilograms():
    w1 = Weight(kilograms=80)
    w2 = Weight(kilograms=25)
    w3 = w1 + w2

    assert w3.kilograms == 105
