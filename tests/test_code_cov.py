import pytest

class TestCodeCov():
    def test_code_coverage(self):
        actual = True
        expected = True
        assert actual == expected
    
    @pytest.mark.skip(reason = 'no reason, just skip')
    def test_to_skip(self):
        print('This test is skipped')
    
    @pytest.mark.xfail
    def test_to_xfail():
        pass
    