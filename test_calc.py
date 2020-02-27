import pytest

from calc import Bill


class TestBill:
    def test_20p_of_100_is_20_dollars(self):
        '''100 * 20% = 20'''
        bill = Bill(100.00, 20)
        assert bill.calc_tip() == 20

    def test_neg20p_of_100_reprompts(self):
        '''can't have a negative tip'''
        bill = Bill(100.00, -20)
        assert bill.valid_tip == False
