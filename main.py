import library.fixed_values as const
import library.calculations as calc
import games.fruit_machine as fruit
import games.roulette as spin
import games.blackjack as jack
import profiles as prof

total_profit_or_loss = 0
roulette_selection = ""
first_game = True
stop_playing = False

print(f'Welkom bij Casino de Gouden Lepel')

prof.show_user_menu()
if prof.current_user is None or prof.current_user == "admin":
    print("Er is geen geldige speler ingelogd.\n"
          "Nog een fijne dag!!!")
    exit()

player_data = prof.players[prof.current_user]
first_name = player_data["first_name"]
date_of_birth = player_data["date_of_birth"]
email_address = player_data["email_address"]
form_of_address = player_data["form_of_adress"]
sum_transaction = player_data.get("sum_transaction", 0)
birth_year, greeting = calc.time_of_day(date_of_birth)

if calc.age_check(birth_year):
    invoice = sum([const.COST_ENTRY, const.COST_AGE_CHECK, sum_transaction])
    print('Casino de Gouden Lepel')
    print('--------------------------------------------------------------------------------')
    print(f'Sorry {first_name} je bent te jong om te gokken, de minium leeftijd is {const.MIN_AGE} jaar oud '
          f'\nDe factuur van € {invoice} wordt verzonden naar het door u opgegeven e-mailadres {email_address}'
          f'\nIndien de factuur niet binnen 7 werkdagen na ontvangst is betaald, behouden wij ons het recht voor om '
          f'gerechtelijke stappen te ondernemen om het openstaande bedrag te innen. '
          f'\nNog een fijne dag gewenst')
    exit(1)


startbudget, sum_transaction = calc.transaction_input(f'{greeting} {form_of_address}, \nHoeveel euro(€) heeft u vandaag te spenderen? ', sum_transaction)
startbudget = float(startbudget)
saldo = calc.calculate_saldo(startbudget, sum_transaction)

while saldo >= 0 and not stop_playing:
    first_game = calc.menu(startbudget, sum_transaction, saldo, first_game, form_of_address, total_profit_or_loss)
    which_game, sum_transaction = calc.which_game(sum_transaction)
    if which_game in ['1', 'roulette']:
        stop_playing, roulette_selection_choice, sum_transaction = spin.roulette_selection(sum_transaction, stop_playing)
        sum_transaction, saldo, total_profit_or_loss = spin.roulette_game(saldo, total_profit_or_loss, sum_transaction)
    elif which_game in ['2', 'fruit machine']:
        fruit.play_fruitmachine(saldo, sum_transaction)
    elif which_game in ['3', 'blackjack']:
        jack.play_blackjack(saldo, sum_transaction)
    elif which_game in ['4', 'stop']:
        stop_playing = True
prof.players[prof.current_user]["saldo"] = saldo
prof.players[prof.current_user]["sum_transaction"] = sum_transaction

saldo = calc.calculate_saldo(startbudget, sum_transaction) + total_profit_or_loss
total_cost = sum([const.COST_GAMBLING_TAX, const.COST_AGE_CHECK, const.COST_ENTRY, sum_transaction])
print('Casino de Gouden Lepel')
print('--------------------------------------------------------------------------------')
print(f"\nBeste, {form_of_address}!")
if total_profit_or_loss > total_cost:
    end_saldo = startbudget + total_profit_or_loss - total_cost
    print(f"U heeft in totaal € {total_profit_or_loss:.2f} gewonnen aan de roulette tafel.")
    print(f"Na aftrek van de vaste kosten en transactie kosten (€ {total_cost:.2f}) ")
    print(f"Gaat u naar huis met een prachtig eindbedrag van: € {end_saldo:.2f}!")
    print("\nEr wordt uiteraard GEEN factuur naar u verzonden.")
    print(f"We zullen u een mail sturen naar {email_address} zodat wij het gewonnen bedrag € {end_saldo:.2f} kunnen door storten op u rekening ")
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