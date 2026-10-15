import Library.fixed_values as const
import Library.Functions as calc
import Games.Fruit_Machine as fruit
import Games.Roulette as spin

total_profit_or_loss = 0
roulette_selection = ""
first_game = True
stop_playing = False

print(f'Welkom bij Casino de Gouden Lepel')
first_name, sum_transaction, surname, date_of_birth, email_address, form_of_adress = calc.greeting()
birth_year, greeting = calc.time_of_day(date_of_birth)

if calc.age_check(birth_year):
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

while saldo >= 0 and not stop_playing:
    first_game = calc.menu(startbudget,sum_transaction,saldo,first_game, form_of_adress,total_profit_or_loss)
    which_game, sum_transaction = calc.which_game(sum_transaction)
    if which_game in ['1', 'roulette']:
        stop_playing, roulette_selection_choice, sum_transaction = spin.roulette_selection(sum_transaction, stop_playing)
        sum_transaction, saldo, total_profit_or_loss = spin.roulette_game(saldo, total_profit_or_loss, sum_transaction)
    elif which_game in ['2', 'fruit machine']:
        fruit.play_fruitmachine(saldo)


saldo = calc.calculate_saldo(startbudget, sum_transaction) + total_profit_or_loss
total_cost = sum([const.COST_GAMBLING_TAX, const.COST_AGE_CHECK, const.COST_ENTRY, sum_transaction])
print('Casino de Gouden Lepel')
print('--------------------------------------------------------------------------------')
print(f"\nBeste, {form_of_adress}!")
if total_profit_or_loss > total_cost:
    eind_saldo = startbudget + total_profit_or_loss - total_cost
    print(f"U heeft in totaal € {total_profit_or_loss:.2f} gewonnen aan de roulette tafel.")
    print(f"Na aftrek van de vaste kosten en transactie kosten (€ {total_cost:.2f}) ")
    print(f"Gaat u naar huis met een prachtig eindbedrag van: € {eind_saldo:.2f}!")
    print("\nEr wordt uiteraard GEEN factuur naar u verzonden.")
    print(f"We zullen u een mail sturen naar {email_address} zodat wij het gewonnen bedrag € {eind_saldo:.2f} kunnen door storten op u rekening ")
elif saldo <= 0:
    invoice = startbudget - total_profit_or_loss - total_cost
    print(
        f"Uw budget van € {startbudget:.2f} is opgebruikt. \nDe factuur van € {-invoice:.2f} wordt verzonden naar het door u opgegeven e-mailadres {email_address} "
        f"\nIndien de factuur niet binnen 7 werkdagen na ontvangst is betaald, behouden wij ons het recht voor om "
        f"gerechtelijke stappen te ondernemen om het openstaande bedrag te innen. "
        f"\nNog een fijne dag gewenst")
else:
    invoice = startbudget - total_profit_or_loss - total_cost
    print(
        f"De factuur van € {invoice:.2f} wordt verzonden naar het door u opgegeven e-mailadres {email_address} "
        f"\nIndien de factuur niet binnen 7 werkdagen na ontvangst is betaald, behouden wij ons het recht voor om "
        f"gerechtelijke stappen te ondernemen om het openstaande bedrag te innen. "
        f"\nNog een fijne dag gewenst")