import pytest
import sys
import os

from src.helpers import multiply_two 

print('TESTING test_code_cov.py')

class TestHelpers():
    def test_multiply_two(self):
        actual = multiply_two(3)
        expected = 6
        assert actual == expected
    
    @pytest.mark.skip(reason = 'no reason, just skip')
    def test_to_skip(self):
        print('This test is skipped')
    
    @pytest.mark.xfail
    def test_to_xfail(self):
        pass
    