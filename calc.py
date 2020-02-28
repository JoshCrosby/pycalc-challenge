'''
Calculate the tip amount from a restaurant bill
'''


class TipError(Exception):
    '''generic exception for the class'''
    # pass


class Bill:
    '''class for restaurant bill'''
    def __init__(self, bill_amount, tip_percent):
        '''init'''
        self.bill_amount = bill_amount
        self.tip_percent = tip_percent

    def __repr__(self):
        '''repr the class'''
        return (f'{self.__class__.__name__}'
                f'({self.bill_amount}, {self.tip_percent})')

    def __str__(self):
        '''return a pretty version :) '''
        return (f'Bill amount: $ {self.bill_amount} '
                f'Tip percentage: {self.tip_percent} % '
                f'Total bill: $ {self.calc_tip()}')

    def calc_tip(self):
        '''
        Calculate the tip based on input.

        Input:
        Bill amount - should be a positive float
        Tip percentage - should be an integer, i.e. 15 == 15%

        Output:
        Total bill - assumption tax is calculated, tip + bill amount
        '''
        try:
            if isinstance(self.bill_amount,
                          (int, float)) and isinstance(self.tip_percent, int):
                return self.bill_amount * (1.0 * self.tip_percent / 100)
        except ValueError as e:
            raise TipError(e.__cause__)
