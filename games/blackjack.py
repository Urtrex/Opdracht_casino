import random
import library.fixed_values as const
import library.calculations as calc

def create_deck():
    deck = [f"{rank}{suit}" for suit in const.SUITS for rank in const.RANKS]

    return deck

def draw_card(deck, hand):
    drew_card = deck.pop()
    hand.append(drew_card)

    return drew_card

def show_hand(label, hand, hide_card = False):
    if hide_card and len(hand) >= 2:
        visible_cards = [hand[0], "??"]
        visible_cards += hand[2:]
    else:
        visible_cards = hand

    print(f"{label}: {' | '.join(visible_cards)}")

def calculate_card_value(card):
    rank = card[:-1]
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 11
    else:
        return int(rank)


def calculate_hand_value(hand):
    total = 0
    for card in hand:
        total += calculate_card_value(card)
    number_of_aces = 0
    for card in hand:
        if card[:-1] == 'A':
            number_of_aces += 1
    while total > 21 and number_of_aces > 0:
        total -= 10
        number_of_aces -= 1
    return total


def play_blackjack(saldo,sum_transaction):
    first_game = True
    while True:
        print(f"\nCasino de Gouden lepel - Black Jack")
        print("-" * 35)
        print(f"Huidig saldo: € {saldo:.2f}")

        if not first_game:
            action, sum_transaction = calc.transaction_input(f"Druk op enter om te spelen of typ stop om terug te gaan: ", sum_transaction)
            action = action.strip().lower()
            if action == "stop":
                return saldo , sum_transaction
        else:
            first_game = False

        hand_player = []
        hand_dealer = []
        stake = calc.stake(sum_transaction)
        saldo -= stake
        deck = create_deck()
        random.shuffle(deck)

        draw_card(deck, hand_player)
        draw_card(deck, hand_player)
        # Player draws 2 cards
        draw_card(deck, hand_dealer)
        draw_card(deck, hand_dealer)
        # Dealer draws 2 cards

        show_hand("speler",hand_player)
        show_hand("Dealer", hand_dealer, hide_card = True)
        value_hand_player = calculate_hand_value(hand_player)
        value_hand_dealer = calculate_hand_value(hand_dealer)

        print(f"Jouw totale waarde: {value_hand_player}")

        while value_hand_player < 21:
            hit_stand, sum_transaction = calc.transaction_input(f'HIT of STAND ', sum_transaction)
            hit_stand = hit_stand.lower().strip()

            if hit_stand == 'hit':
                card = draw_card(deck, hand_player)
                print(f'Je trekt: {card}')
                show_hand("speler", hand_player)
                value_hand_player = calculate_hand_value(hand_player)
                print(f'Jouw totale waarde: {value_hand_player}')

                if value_hand_player > 21:
                    print(f'YOUR BUSTED!')
                    break

            elif hit_stand == 'stand':
                break

            else:
                continue

        show_hand('Dealer', hand_dealer)

        if value_hand_player <= 21:
            while value_hand_dealer < 17:
                card = draw_card(deck,hand_dealer)
                print(f'Dealer trekt{card}')
                show_hand('Dealer', hand_dealer)
                value_hand_dealer = calculate_hand_value(hand_dealer)

        print(f"\nEinduitslag:")
        print(f"Jouw score: {value_hand_player} | Dealer score: {value_hand_dealer}")

        if value_hand_player > 21:
            print(f"Je verliest € {stake:.2f}")
        elif value_hand_dealer > 21:
            saldo += stake * 2
            print(f'WINNER! Dealer is bust. Je wint € {stake * 2:.2f}')
        elif value_hand_player == value_hand_dealer:
            saldo += stake
            print("Push! Gelijkspel, je krijgt je inzet terug.")
        elif value_hand_player > value_hand_dealer:
            saldo += stake * 2
            print(f'WINNER! Je wint € {stake * 2:.2f}')
        else:
            print(f"Je verliest € {stake:.2f}")