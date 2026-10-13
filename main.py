from datetime import datetime
import Library.fixed_values as const
import Library.Functions as calc

sum_transaction = 0
total_profit_or_loss = 0
roulette_selection = ""
first_game = True
stop_playing = False

print(f'Welkom bij Casino de Gouden Lepel')

first_name = input(f'Wat is uw Voornaam ? ')
sum_transaction = calc.calculate_transaction_cost(sum_transaction)

surname = input(f'Wat is uw Achternaam ? ')
sum_transaction = calc.calculate_transaction_cost(sum_transaction)

date_of_birth = input(f'Wat is u geboortedatum ? (dd-mm-yyyy) ')
sum_transaction = calc.calculate_transaction_cost(sum_transaction)

email_address = input(f'Wat is u email adres? ')
sum_transaction = calc.calculate_transaction_cost(sum_transaction)

gender = input(f'Wat is u geslacht ? (M/V/X) ').upper()
sum_transaction = calc.calculate_transaction_cost(sum_transaction)

if gender == 'M':
    form_of_adress = f'meneer {surname}'
elif gender == 'V':
    form_of_adress = f'mevrouw {surname}'
else:
    form_of_adress = f'{first_name} {surname}'

hour = datetime.now().hour
if hour < 11:
    greeting = 'Goedemorgen'
elif hour < 18:
    greeting = 'Goedemiddag'
else:
    greeting = 'Goedeavond'
birth_day, birth_month, birth_year = date_of_birth.split("-")
if const.CURRENT_YEAR - int(birth_year) < const.MIN_AGE:
    invoice = sum([const.COST_ENTRY, const.COST_AGE_CHECK, sum_transaction])
    print('Casino de Gouden Lepel')
    print('--------------------------------------------------------------------------------')
    print(f'Sorry {first_name} je bent te jong om te gokken, de minium leeftijd is {const.MIN_AGE} jaar oud '
          f'\nDe factuur van € {invoice} wordt verzonden naar het door u opgegeven e-mailadres {email_address} '
          f'\nIndien de factuur niet binnen 7 werkdagen na ontvangst is betaald, behouden wij ons het recht voor om '
          f'gerechtelijke stappen te ondernemen om het openstaande bedrag te innen. '
          f'\nNog een fijne dag gewenst')
    exit(1)


startbudget = float(input(f'{greeting} {form_of_adress}, \nHoeveel euro(€) heeft u vandaag te spenderen? '))
sum_transaction = calc.calculate_transaction_cost(sum_transaction)
saldo = calc.calculate_saldo(startbudget, sum_transaction)
invoice = startbudget - saldo


while saldo >= 0 and not stop_playing:
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

    roulette_selection = ""
    while roulette_selection not in ['1', '2', '3', '4', 'rood', 'zwart', 'even', 'oneven', '0', 'stop']:
        roulette_selection = input(f"Kies één van de volgende opties:"
                       f"\n1. Rood"
                       f"\n2. Zwart"
                       f"\n3. Even"
                       f"\n4. Oneven"
                       f"\n0. Stop \n").lower()
        sum_transaction = calc.calculate_transaction_cost(sum_transaction)
        if roulette_selection in ['1' , 'rood']:
            roulette_selection = '1'
            break
        elif roulette_selection in ['2' , 'zwart']:
            roulette_selection = '2'
            break
        elif roulette_selection in ['3' , 'even']:
            roulette_selection = '3'
            break
        elif roulette_selection in ['4' , 'oneven']:
            roulette_selection = '4'
            break
        elif roulette_selection in ['0' , 'stop']:
            roulette_selection = 0
            break
        else:
            continue
    if roulette_selection == 0:
        stop_playing = True
        continue
    stake = float(input(f'Hoeveel euro wil je inzetten? '))
    sum_transaction = calc.calculate_transaction_cost(sum_transaction)
    saldo -= const.TRANSACTION_COSTS
    if stake <= 0:
        print(f'Je inzet moet hoger dan € 0 zijn ')
        continue
    elif stake > saldo:
        print(f'Jouw {stake:.2f} is hoger dan je {saldo:.2f}')
        continue
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

saldo = calc.calculate_saldo(startbudget, sum_transaction) + total_profit_or_loss
total_cost = sum([const.COST_GAMBLING_TAX, const.COST_AGE_CHECK, const.COST_ENTRY, sum_transaction])
if total_profit_or_loss > total_cost:
    eind_saldo = startbudget + total_profit_or_loss - total_cost
    print('Casino de Gouden Lepel')
    print('--------------------------------------------------------------------------------')
    print(f"Beste, {form_of_adress}!")
    print(f"U heeft in totaal € {total_profit_or_loss:.2f} gewonnen aan de roulette tafel.")
    print(f"Na aftrek van de vaste kosten en transactie kosten (€ {total_cost:.2f}) ")
    print(f"Gaat u naar huis met een prachtig eindbedrag van: € {eind_saldo:.2f}!")
    print("\nEr wordt uiteraard GEEN factuur naar u verzonden.")
    print(f"We zullen u een mail sturen naar {email_address} zodat wij het gewonnen bedrag € {eind_saldo:.2f} kunnen door storten op u rekening ")
elif saldo <= 0:
    invoice = startbudget - total_profit_or_loss - total_cost
    print('Casino de Gouden Lepel')
    print('--------------------------------------------------------------------------------')
    print(
        f"Uw budget van € {startbudget:.2f} is opgebruikt. \nDe factuur van € {-invoice:.2f} wordt verzonden naar het door u opgegeven e-mailadres {email_address} "
        f"\nIndien de factuur niet binnen 7 werkdagen na ontvangst is betaald, behouden wij ons het recht voor om "
        f"gerechtelijke stappen te ondernemen om het openstaande bedrag te innen. "
        f"\nNog een fijne dag gewenst")
else:
    invoice = startbudget - total_profit_or_loss - total_cost
    print('Casino de Gouden Lepel')
    print('--------------------------------------------------------------------------------')
    print(
        f"De factuur van € {invoice:.2f} wordt verzonden naar het door u opgegeven e-mailadres {email_address} "
        f"\nIndien de factuur niet binnen 7 werkdagen na ontvangst is betaald, behouden wij ons het recht voor om "
        f"gerechtelijke stappen te ondernemen om het openstaande bedrag te innen. "
        f"\nNog een fijne dag gewenst")