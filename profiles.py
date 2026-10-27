import library.calculations as calc
from main import sum_transaction

players = {}
current_player = None

def change_user():
    global current_player
    print("\n--- Wisselen van Account ---")
    email = input(f"Voer je e-mailadres in om in te loggen: "). lower()
                #Of typ 'admin' voor admin log in
    if email == 'admin':
        current_player = 'admin'
        print(f'Ingelogd als admin')
    elif email in players:
        current_player = email
        print(f'Welkom terug {players[email]['form_of_adress']}')
    else:
        print(f'E-mailadres niet gevonden.\n'
              f"Probeer het opnieuw of maak een nieuw account aan")


def new_user():
    print("\n--- Nieuw account Aanmaken ---")
    first_name, sum_transaction, surname, date_of_birth, email_address, form_of_adress = greeting()

    create_account(first_name, surname, date_of_birth, email_address, form_of_adress, sum_transaction , 0.0)

def create_account(first_name, surname, date_of_birth, email_address, form_of_adress, saldo):
    global current_player
    player_key = email_address.lower()
    players[player_key] = {
        "first_name": first_name,
        "surname": surname,
        "date_of_birth": date_of_birth,
        "email_address": email_address,
        "form_of_adress": form_of_adress,
        "saldo": saldo,
        "sum_transactions": sum_transaction}

    current_player = player_key

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

    first_name, sum_transaction = calc.transaction_input(f'Wat is uw Voornaam ? ', sum_transaction)

    surname, sum_transaction = calc.transaction_input(f'Wat is uw Achternaam ? ', sum_transaction)

    date_of_birth, sum_transaction = calc.transaction_input(f'Wat is u geboortedatum ? (dd-mm-yyyy) ', sum_transaction)

    email_address, sum_transaction = calc.transaction_input(f'Wat is u email adres? ', sum_transaction)

    gender, sum_transaction = calc.transaction_input('Wat is u geslacht ? (M/V/X) ', sum_transaction)
    gender = gender.upper()
    if gender == 'M':
        form_of_adress = f'meneer {surname}'
    elif gender == 'V':
        form_of_adress = f'mevrouw {surname}'
    else:
        form_of_adress = f'{first_name} {surname}'

    return first_name, sum_transaction, surname, date_of_birth, email_address, form_of_adress


# Admin commands
def all_users():
    print("\n[ADMIN] --- Alle Accounts ---")
    if not players:
        print("Er zijn momenteel geen accounts geregistreerd.")
    else:
        for email, data in players.items():
            print(f"Email: {email} | Naam: {data['form_of_adress']} | Saldo: € {data['saldo']:.2f}")

def delete_user():
    print("\n[ADMIN] --- Account Verwijderen ---")
    email = input("Voer het e-mailadres in van het account dat je wilt verwijderen\n").lower()

    if email in players:
        del players[email]
        print(f"Het account met e-mailadres: {email} is succesvol verwijderd.")
    else:
        print("E-mailadres niet gevonden. Er is niets verwijderd.")



