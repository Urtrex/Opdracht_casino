import random
import Library.fixed_values as const
#FUNCTIONS
def calculate_transaction_cost(sum_transaction):
    return sum_transaction + const.TRANSACTION_COSTS
def calculate_saldo(startbudget, sum_transaction):
    saldo = startbudget - sum([const.COST_GAMBLING_TAX, const.COST_ENTRY, sum_transaction, const.COST_AGE_CHECK])
    return saldo
def spin():
    spin_number = random.randint(0,36)
    if spin_number == 0:
        color = 'groen'
        parity = 'geen'
    else:
        if spin_number <= 18:
            if spin_number % 2 == 0:
                color = 'zwart'
                parity = 'even'
            else:
                color = 'rood'
                parity ='oneven'
        else:
            if spin_number % 2 == 0:
                color = 'rood'
                parity = 'even'
            else:
                color = 'zwart'
                parity = 'oneven'
    return spin_number, color, parity