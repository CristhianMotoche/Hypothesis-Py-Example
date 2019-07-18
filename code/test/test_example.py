from unittest import TestCase
from hypothesis import given
import hypothesis.strategies as st

from app.suma import suma


class ExampleTest(TestCase):
    def test_suma_2_2_igual_4(self):
        assert suma(2, 2) == 4

    @given(st.integers(), st.integers())
    def test_sum(self, x, y):
        assert suma(x, y) == y + x
