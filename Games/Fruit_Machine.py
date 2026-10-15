import Library.Functions as calc


def determine_rolls(round_number):
    if round_number % 5 == 1:
        return "kers", "citroen", "ster"
    elif round_number % 5 == 2:
        return "kers", "kers", "kers"
    elif round_number % 5 == 3:
        return "ster", "ster", "citroen"
    elif round_number % 5 == 4:
        return "citroen", "kers", "ster"


    return "ster", "ster", "ster"


def determine_profit(rol1, rol2, rol3, stake):
    if rol1 == rol2 == rol3:
        return stake * 3
    if rol1 == rol2 or rol1 == rol3 or rol2 == rol3:
        return stake
    return 0.0


def play_fruitmachine(saldo):
    round_number = 1
    while True:
        print(f"\nCasino de Gouden lepel - fruitmachine")
        print("-" * 35)
        print(f"Huidig saldo: € {saldo:.2f}")
        stake = calc.stake()

        action = input("Druk op enter om te spelen of typ stop om terug te gaan: ").strip().lower()
        if action == "stop":
            return saldo

        stake = stake(saldo)
        saldo -= stake
        rol1, rol2, rol3 = determine_rolls(round_number)
        print(f"Rollen: {rol1} | {rol2} | {rol3}")

        profit = determine_profit(rol1, rol2, rol3, stake)

        if profit > 0:
            saldo += profit
            if rol1 == rol2 == rol3:
                print(f"Drie dezelfde! Je wint € {profit:.2f}")
            else:
                print(f"Twee dezelfde! Je wint € {profit:.2f}")
        else:
            print(f"Geen match. Je verliest € {stake:.2f}")

        print(f"Nieuw saldo: € {saldo:.2f}")
        round_number += 1