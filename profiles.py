import Library.calculations as calc


players = {}
current_player = None



def all_users():
    print("\n[ADMIN] --- Alle Accounts ---")
    pass

def delete_user():
    print("\n[ADMIN] --- Account Verwijderen ---")
    pass

def create_account(first_name, surname, date_of_birth, email_address, form_of_adress, saldo):
    global current_player
    player_key = email_address.lower()
    players[player_key] = {
        "first_name": first_name,
        "surname": surname,
        "date_of_birth": date_of_birth,
        "email_address": email_address,
        "form_of_adress": form_of_adress,
        "saldo": saldo,}

    current_player = player_key


def change_user():
    print("\n--- Wisselen van Account ---")
    pass

def show_user_menu(current_user,):
    while True:
        print("\n===== ACCOUNT MENU =====")
        print("1. Nieuw account")
        print("2. Wissel account")

        if current_user == "admin":
            print("3. [ADMIN] Toon alle accounts")
            print("4. [ADMIN] Verwijder account")

        print("0. Terug naar menu")
        print("========================")

        choice = input("Maak een choice: ")
        match choice:
            case "1":
                new_user()
            case "2":
                change_user()
            case "3" if current_user == "admin":
                all_users()
            case "4" if current_user == "admin":
                delete_user()
            case "0":
                print("Terugkeren naar het menu...")
                break
            case _:
                print("Ongeldige choice of je hebt hier geen rechten voor.")

def greeting():
    sum_transaction = 0

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

    return first_name, sum_transaction, surname, date_of_birth, email_address, form_of_adress