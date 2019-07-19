from unittest import TestCase
from hypothesis import given
import hypothesis.strategies as st

from app.suma import suma


class SumaTest(TestCase):
    def test_suma_2_2_igual_4(self):
        assert suma(2, 2) == 4

    def test_suma_4_1_igual_5(self):
        assert suma(4, 1) == 5

    @given(st.integers(), st.integers())
    def test_suma_comutativa(self, x, y):
        assert suma(x, y) == suma(y, x)

    @given(st.integers())
    def test_suma_x_mas_uno_mas_uno_es_igual_a_x_mas_dos(self, x):
        assert suma(suma(x, 1), 1) == suma(x, 2)

    @given(st.integers())
    def test_suma_elemento_neutro(self, x):
        assert suma(x, 0) == x
