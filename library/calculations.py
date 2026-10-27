from datetime import datetime
import random
import library.fixed_values as const


#FUNCTIONS
def transaction_input(prompt, sum_transaction):
    result = input(prompt)
    sum_transaction = calculate_transaction_cost(sum_transaction)

    return result, sum_transaction

def calculate_transaction_cost(sum_transaction):
    return sum_transaction + const.TRANSACTION_COSTS

def time_of_day(date_of_birth):
    hour = datetime.now().hour
    if hour < 11:
        greeting = 'Goedemorgen'
    elif hour < 18:
        greeting = 'Goedemiddag'
    else:
        greeting = 'Goedeavond'
    birth_day, birth_month, birth_year = date_of_birth.split("-")
    
    return birth_year, greeting

def age_check (birth_year):
    if const.CURRENT_YEAR - int(birth_year) < const.MIN_AGE:
       age_check = True
    else:
        age_check = False
    return age_check

def menu(startbudget,sum_transaction,saldo,first_game, form_of_adress, total_profit_or_loss):
    print('Casino de Gouden Lepel')
    print('--------------------------------------------------------------------------------')
    if first_game:
        print(f'Welkom, {form_of_adress}')
        first_game = False
    else:
        if total_profit_or_loss <= 0:
            print(f"Verlies:        € {-total_profit_or_loss:.2f} ")
        else:
            print(f"Winst:          € {total_profit_or_loss:.2f} ")

    print(f"Startbudget:        € {startbudget:.2f} ")
    print(f"Vaste kosten:       € {const.COST_FIXED:.2f} ")
    print(f"Transactie kosten:  € {sum_transaction:.2f} ")
    print(f"Saldo:              € {saldo:.2f}")
    print(f'\nJe hebt nog genoeg budget voor toegang tot het casino.')

    return first_game

def which_game(sum_transaction):
    while True:
        which_game, sum_transaction = transaction_input("Welke game wil je spelen?\n"
            "(1) Roulette\n"
            "(2) Fruit machine\n"
            "(3) Blackjack\n"
            "(4) Stop met spelen\n", sum_transaction)
        which_game = which_game.lower()

        if which_game in ['1', '2', '3', '4', 'roulette', 'fruit machine', 'blackjack','stop']:
            return which_game, sum_transaction

        print("Ongeldige keuze, probeer opnieuw.")



def stake(sum_transaction):
    stake, sum_transaction = transaction_input(f'Hoeveel euro wil je inzetten? ', sum_transaction)

    return stake, sum_transaction


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