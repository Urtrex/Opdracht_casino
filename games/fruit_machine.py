import library.calculations as calc
import random


def determine_rolls(round_number):
    possible_outcomes = ["kers","citroen", "ster"]

    rol_1 = random.choice(possible_outcomes)
    rol_2 = random.choice(possible_outcomes)
    rol_3 = random.choice(possible_outcomes)

    return rol_1, rol_2, rol_3


def determine_profit(rol1, rol2, rol3, stake):
    if rol1 == rol2 == rol3:
        return stake * 3, True
    if rol1 == rol2 or rol1 == rol3 or rol2 == rol3:
        return stake, False
    return 0.0, False


def play_fruitmachine(saldo, sum_transaction):
    round_number = 1
    while True:
        print(f"\nCasino de Gouden lepel - fruitmachine")
        print("-" * 35)
        print(f"Huidig saldo: € {saldo:.2f}")


        stake = calc.stake(sum_transaction)
        saldo -= stake
        rol1, rol2, rol3 = determine_rolls(round_number)
        print(f"Rollen: {rol1} | {rol2} | {rol3}")

        profit, three_rolls = determine_profit(rol1, rol2, rol3, stake)

        if profit > 0:
            saldo += profit
            if three_rolls:
                print(f"Drie dezelfde! Je wint € {profit:.2f}")
            else:
                print(f"Twee dezelfde! Je wint € {profit:.2f}")
        else:
            print(f"Geen match. Je verliest € {stake:.2f}")

        print(f"Nieuw saldo: € {saldo:.2f}")
        round_number += 1

        action, sum_transaction = calc.transaction_input(f"Druk op enter om te spelen of typ stop om terug te gaan: ", sum_transaction)
        action = action.strip().lower()
        if action == "stop":
            return saldo, sum_transaction

