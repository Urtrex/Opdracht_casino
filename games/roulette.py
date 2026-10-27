import library.fixed_values as const
import library.calculations as calc


def roulette_selection(sum_transaction, stop_playing):

    roulette_selection_choice = ""
    while roulette_selection_choice not in ['1', '2', '3', '4', 'rood', 'zwart', 'even', 'oneven', '0', 'stop'] and not stop_playing:

            roulette_selection_choice, sum_transaction = calc.transaction_input(f"Kies één van de volgende opties:"
                           f"\n1. Rood"
                           f"\n2. Zwart"
                           f"\n3. Even"
                           f"\n4. Oneven"
                           f"\n0. Stop \n", sum_transaction)
            roulette_selection_choice = roulette_selection_choice.lower()

            if roulette_selection_choice in ['1' , 'rood']:
                roulette_selection_choice = '1'
                break
            elif roulette_selection_choice in ['2' , 'zwart']:
                roulette_selection_choice = '2'
                break
            elif roulette_selection_choice in ['3' , 'even']:
                roulette_selection_choice = '3'
                break
            elif roulette_selection_choice in ['4' , 'oneven']:
                roulette_selection_choice = '4'
                break
            elif roulette_selection_choice in ['0' , 'stop']:
                stop_playing = True
                return stop_playing, roulette_selection_choice, sum_transaction
            else:
              continue

    return stop_playing, roulette_selection_choice, sum_transaction



def roulette_game(saldo, total_profit_or_loss, sum_transaction):
    stake = calc.stake(sum_transaction)
    sum_transaction = calc.calculate_transaction_cost(sum_transaction)
    saldo -= const.TRANSACTION_COSTS
    if stake <= 0:
        print(f'Je inzet moet hoger dan € 0 zijn ')

    elif stake > saldo:
        print(f'Jouw {stake:.2f} is hoger dan je {saldo:.2f}')

    else:
        saldo -= stake
        spin_number, color, parity = calc.spin()
        print(f'[SPIN] \nHet balletje landt op: {spin_number} ({color.upper()}, {parity})')
        win = False
        if roulette_selection == '1' and color == 'rood':
            win = True
        elif roulette_selection == '2' and color == 'zwart':
            win = True
        elif roulette_selection == '3' and parity == 'even':
            win = True
        elif roulette_selection == '4' and parity == 'oneven':
            win = True
        if win:
            profit = stake * 2
            saldo += profit
            total_profit_or_loss += profit
            print(f'Proficiat! je hebt € {profit:.2f} gewonnen!')

        else:
            print(f'Je bent je inzet van € {stake:.2f} kwijt.')
            total_profit_or_loss -= stake

    return sum_transaction, saldo, total_profit_or_loss