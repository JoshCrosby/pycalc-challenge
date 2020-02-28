import pytest

from calc import Bill


class TestBill:
    def test_20p_of_100_is_20_dollars(self):
        '''100 * 20% = 20'''
        bill = Bill(100.00, 20)
        assert bill.calc_tip() == 20

    def test_twenty_of_100_is_not_numeric(self):
        '''twenty * 100 is not numeric'''
        with pytest.raises(Exception) as e:
            bill = Bill(100.00, "twenty")
            assert bill.calc_tip()

    def test_tip_is_positive(self):
        '''make sure our tip is > 0'''
        with pytest.raises(Exception) as e:
            bill = Bill(100.00, -10)
            assert bill.calc_tip()
