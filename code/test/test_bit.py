from unittest import TestCase
from hypothesis import given
import hypothesis.strategies as st

from app.bit import encode, decode


class Bit(TestCase):
    def test_encode_5(self):
        assert encode(5) == '0b101'

    def test_decode_5(self):
        assert decode('0b101') == 5

    @given(st.integers(min_value=0))
    def test_encode_decode_es_igual_a_lo_inicial(self, num):
        assert decode(encode(num)) == num
