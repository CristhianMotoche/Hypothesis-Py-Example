from unittest import TestCase
from hypothesis import given
import hypothesis.strategies as st

from app.suma import suma


class ExampleTest(TestCase):
    def test_suma_2_2_igual_4(self):
        assert suma(2, 2) == 4

    @given(st.integers(), st.integers())
    def test_sum_tran(self, x, y):
        assert suma(x, y) == suma(y, x)

    @given(st.integers())
    def test_sum_many_equal(self, x):
        assert suma(suma(x, 1), 1) == suma(x, 2)

    @given(st.integers())
    def test_sum_neutral_element(self, x):
        assert suma(x, 0) == x
