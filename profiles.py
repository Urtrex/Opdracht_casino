import library.calculations as calc

players = {}
current_user = None

def change_user(sum_transaction):
    global current_user
    print("\n--- Wisselen van Account ---")
                                                        # Of typ 'admin' voor admin log in
    email, sum_transaction = calc.transaction_input(f"Voer je e-mailadres in om in te loggen: ", sum_transaction)
    email = email.lower()
    if email == 'admin':
        current_user = 'admin'
        print(f'Ingelogd als admin')
    elif email in players:
        current_user = email
        print(f"Welkom terug {players[email]['form_of_adress']}")
    else:
        print(f'E-mailadres niet gevonden.\n'
              f"Probeer het opnieuw of maak een nieuw account aan")
    return sum_transaction


def new_user():
    print("\n--- Nieuw account Aanmaken ---")
    first_name, sum_transaction, surname, date_of_birth, email_address, form_of_adress = greeting()

    create_account(first_name, surname, date_of_birth, email_address, form_of_adress, sum_transaction , 0.0)

def create_account(first_name, surname, date_of_birth, email_address, form_of_adress, sum_transaction ,saldo):
    global current_user
    player_key = email_address.lower()
    players[player_key] = {
        "first_name": first_name,
        "surname": surname,
        "date_of_birth": date_of_birth,
        "email_address": email_address,
        "form_of_adress": form_of_adress,
        "saldo": saldo,
        "sum_transaction": sum_transaction}

    current_user = player_key

def show_user_menu():
    global current_user
    sum_transaction = 0
    while True:
        print("\n===== ACCOUNT MENU =====")
        print("1. Nieuw account")
        print("2. Wissel account")

        if current_user == "admin":
            print("4. [ADMIN] Toon alle accounts")
            print("5. [ADMIN] Verwijder account")
        else:
            print("3. Saldo opwaarderen")

        print("0. spelen")
        print("========================")

        if current_user == 'admin':
            print("Huidige gebruiker: ADMIN")
        elif current_user in players:
            print(f"Huidige gebruiker: {players[current_user]['first_name']}")
        else:
            print("Huidige gebruiker: Geen (Log in of maak een account")

        choice, sum_transaction = calc.transaction_input("Maak een keuze: ", sum_transaction)
        match choice:
            case "1":
                new_user()
            case "2":
                sum_transaction = change_user(sum_transaction)
            case "3" if current_user is not None and current_user != "admin":
                sum_transaction = add_saldo(sum_transaction)
            case "4" if current_user == "admin":
                all_users()

            case "5" if current_user == "admin":
                delete_user()
            case "0":
                print("Terugkeren naar het menu...")
                break
            case _:
                print("Ongeldige choice of je hebt hier geen rechten voor.")

def add_saldo(sum_transaction):
    global current_user

    if current_user is None or current_user == 'admin':
        print(f"Fout: Er is op dit moment geen account ingelogd.")
        return

    extra_budget, sum_transaction = calc.transaction_input(f"Hoeveel euro wil je toevoegen aan je saldo? ", sum_transaction)
    extra_budget = float(extra_budget)
    players[current_user]["saldo"] += extra_budget

    new_saldo = players[current_user]["saldo"]
    print(f"Succes met spelen! Je saldo is nu: € {new_saldo:.2f}")

    return sum_transaction

def greeting():
    sum_transaction = 0

    first_name, sum_transaction = calc.transaction_input(f'Wat is uw Voornaam ? ', sum_transaction)

    surname, sum_transaction = calc.transaction_input(f'Wat is uw Achternaam ? ', sum_transaction)

    date_of_birth, sum_transaction = calc.transaction_input(f'Wat is u geboortedatum ? (dd-mm-yyyy) ', sum_transaction)

    email_address, sum_transaction = calc.transaction_input(f'Wat is u email adres? ', sum_transaction)

    gender, sum_transaction = calc.transaction_input('Wat is u geslacht ? (M/V/X) ', sum_transaction)
    gender = gender.upper()
    if gender == 'M':
        form_of_address = f'meneer {surname}'
    elif gender == 'V':
        form_of_address = f'mevrouw {surname}'
    else:
        form_of_address = f'{first_name} {surname}'

    return first_name, sum_transaction, surname, date_of_birth, email_address, form_of_address


# Admin commands
def all_users():
    print("\n[ADMIN] --- Alle Accounts ---")
    if not players:
        print("Er zijn momenteel geen accounts geregistreerd.")
    else:
        for email, data in players.items():
            print(f"Email: {email} | Naam: {data['form_of_adress']} | Saldo: € {data['saldo']:.2f}")

def delete_user():
    global current_user
    print("\n[ADMIN] --- Account Verwijderen ---")
    email = input("Voer het e-mailadres in van het account dat je wilt verwijderen\n").lower()
    if email in players:
        del players[email]
        print(f"Het account met e-mailadres: {email} is succesvol verwijderd. ")
        if current_user == email:
            current_user = None
    else:
        print("E-mailadres niet gevonden. Er is niets verwijderd.")
