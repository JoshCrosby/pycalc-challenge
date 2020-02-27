'''
Calculate the tip amount from a restaurant bill
'''


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
        return (f'Bill amount: $ {self.bill_amount}'
                f'Tip percentage: {self.tip_percentage} %'
                f'Total bill: $ {self.calc_tip}')

    def calc_tip(self):
        '''
        Calculate the tip based on input.

        Input:
        Bill amount - should be a positive float
        Tip percentage - should be an integer, i.e. 15 == 15%

        Output:
        Total bill - assumption tax is calculated, tip + bill amount
        '''
        return (self.bill_amount * (1.0 * self.tip_percent / 100))

    def valid_tip(self):
        '''return a valid tip above 0. No $, strings, or negative'''
        pass
