from datetime import datetime
import random
#(Vaste waarden / Constanten)
huidig_jaar = 2026
kost_toegang = 5
kost_gok_belasting = 15
kost_leeftijd_check = 1
kost_vast = kost_toegang + kost_gok_belasting + kost_leeftijd_check
kost_transactie = 0.01
min_leeftijd = 18

#FUNCTIES
def berekening_transactie(som_transactie):
    return som_transactie + kost_transactie
def berekening_Saldo(startbudget,som_transactie):
    saldo = startbudget - sum([kost_gok_belasting,kost_toegang,som_transactie,kost_leeftijd_check])
    return saldo
def spin():
    spin_getal = random.randint(0,36)
    if spin_getal == 0:
        kleur = 'groen'
        type_getal = 'geen'
    else:
        if spin_getal <= 18:
            if spin_getal % 2 == 0:
                kleur = 'zwart'
                type_getal = 'even'
            else:
                kleur = 'rood'
                type_getal ='oneven'
        else:
            if spin_getal % 2 == 0:
                kleur = 'rood'
                type_getal = 'even'
            else:
                kleur = 'zwart'
                type_getal = 'oneven'
    return spin_getal, kleur, type_getal

som_transactie = 0
totale_winst_of_verlies = 0
optie_spel = ""
eerste_keer_spel = True

print(f'Welkom bij Casino de Gouden Lepel')

voornaam = input(f'Wat is uw Voornaam ? ')
som_transactie = berekening_transactie(som_transactie)

achternaam = input(f'Wat is uw Achternaam ? ')
som_transactie = berekening_transactie(som_transactie)

geboortedatum = input(f'Wat is u geboortedatum ? (dd-mm-yyyy) ')
som_transactie = berekening_transactie(som_transactie)

email_adres = input(f'Wat is u email adres? ')
som_transactie = berekening_transactie(som_transactie)

geslacht = input(f'Wat is u geslacht ? (man of vrouw) ')
som_transactie = berekening_transactie(som_transactie)

if geslacht == 'man':
    aanspreekvorm = f'meneer {achternaam}'
elif geslacht == 'vrouw':
    aanspreekvorm = f'mevrouw {achternaam}'
else:
    aanspreekvorm = f'{voornaam} {achternaam}'

uur = datetime.now().hour
if uur < 11:
    begroeting = 'Goedemorgen'
elif uur < 18:
    begroeting = 'Goedemiddag'
else:
    begroeting = 'Goedeavond'
birth_day, birth_month, birth_year = geboortedatum.split("-")
if huidig_jaar - int(birth_year) < min_leeftijd:
    factuur = sum([kost_toegang,kost_leeftijd_check,som_transactie])
    print('Casino de Gouden Lepel')
    print('--------------------------------------------------------------------------------')
    print(f'Sorry {voornaam} je bent te jong om te gokken, de minium leeftijd is {min_leeftijd} jaar oud '
          f'\nDe factuur van € {factuur} wordt verzonden naar het door u opgegeven e-mailadres {email_adres} '
          f'\nIndien de factuur niet binnen 7 werkdagen na ontvangst is betaald, behouden wij ons het recht voor om '
          f'gerechtelijke stappen te ondernemen om het openstaande bedrag te innen. '
          f'\nNog een fijne dag gewenst')
    exit(1)


startbudget = float(input(f'{begroeting} {aanspreekvorm}, \nHoeveel euro(€) heeft u vandaag te spenderen? '))
som_transactie = berekening_transactie(som_transactie)
saldo = berekening_Saldo(startbudget,som_transactie)
factuur = startbudget - saldo


while saldo >= 0:
    print('Casino de Gouden Lepel')
    print('--------------------------------------------------------------------------------')
    if eerste_keer_spel:
        print(f'Welkom, {aanspreekvorm}')
        eerste_keer_spel = False
    else:
        if totale_winst_of_verlies <= 0:
            print(f"Verlies:        € {-totale_winst_of_verlies:.2f} ")
        else:
            print(f"Winst:          € {totale_winst_of_verlies:.2f} ")

    print(f"Startbudget:        € {startbudget:.2f} ")
    print(f"Vaste kosten:       € {kost_vast:.2f} ")
    print(f"Transactie kosten:  € {som_transactie:.2f} ")
    print(f"Saldo:              € {saldo:.2f}")
    print(f'\nJe hebt nog genoeg budget voor toegang tot het casino.')

    optie_spel = ""
    while optie_spel not in ['1', '2', '3', '4', 'rood', 'zwart', 'even', 'oneven', '0', 'stop']:
        optie_spel = input(f"Kies één van de volgende opties:"
                       f"\n1. Rood"
                       f"\n2. Zwart"
                       f"\n3. Even"
                       f"\n4. Oneven"
                       f"\n0. Stop \n").lower()
        som_transactie = berekening_transactie(som_transactie)
        if optie_spel in ['1' , 'rood']:
            optie_spel = '1'
            break
        elif optie_spel in ['2' , 'zwart']:
            optie_spel = '2'
            break
        elif optie_spel in ['3' , 'even']:
            optie_spel = '3'
            break
        elif optie_spel in ['4' , 'oneven']:
            optie_spel = '4'
            break
        elif optie_spel in ['0' , 'stop']:
            optie_spel = 0
            break
        else:
            continue
    if optie_spel == 0:
        saldo = 0
        continue
    inzet = float(input(f'Hoeveel euro wil je inzetten? '))
    som_transactie = berekening_transactie(som_transactie)
    saldo -= kost_transactie
    if inzet <= 0:
        print(f'Je inzet moet hoger dan € 0 zijn ')
        continue
    elif inzet > saldo:
        print(f'Jouw {inzet:.2f} is hoger dan je {saldo:.2f}')
        continue
    else:
        saldo -= inzet
        spin_getal, kleur, type_getal = spin()
        print(f'[SPIN] \nHet balletje landt op: {spin_getal} ({kleur.upper()}, {type_getal})')
        win = False
        if optie_spel == '1' and kleur == 'rood':
            win = True
        elif optie_spel == '2' and kleur == 'zwart':
            win = True
        elif optie_spel == '3' and type_getal == 'even':
            win = True
        elif optie_spel == '4' and type_getal == 'oneven':
            win = True
        if win:
            winst = inzet * 2
            saldo += winst
            totale_winst_of_verlies += winst
            print(f'Proficiat! je hebt € {winst:.2f} gewonnen!')

        else:
            print(f'Je bent je inzet van € {inzet:.2f} kwijt.')
            totale_winst_of_verlies -= inzet

totale_kosten = sum([kost_gok_belasting,kost_leeftijd_check,kost_toegang,som_transactie])
if totale_winst_of_verlies > totale_kosten:
    eind_saldo = startbudget + totale_winst_of_verlies - totale_kosten
    print('Casino de Gouden Lepel')
    print('--------------------------------------------------------------------------------')
    print(f"Beste, {aanspreekvorm}!")
    print(f"U heeft in totaal € {totale_winst_of_verlies:.2f} gewonnen aan de roulette tafel.")
    print(f"Na aftrek van de vaste kosten en transactie kosten (€ {totale_kosten:.2f}) ")
    print(f"Gaat u naar huis met een prachtig eindbedrag van: € {eind_saldo:.2f}!")
    print("\nEr wordt uiteraard GEEN factuur naar u verzonden.")
    print(f"We zullen u een mail sturen naar {email_adres} zodat wij het gewonnen bedrag € {eind_saldo:.2f} kunnen door storten op u rekening ")
else:
    factuur = totale_kosten - totale_winst_of_verlies
    print('Casino de Gouden Lepel')
    print('--------------------------------------------------------------------------------')
    print(f"Uw budget van € {startbudget:.2f} is opgebruikt. \nDe factuur van € {factuur:.2f} wordt verzonden naar het door u opgegeven e-mailadres {email_adres} "
          f"\nIndien de factuur niet binnen 7 werkdagen na ontvangst is betaald, behouden wij ons het recht voor om "
          f"gerechtelijke stappen te ondernemen om het openstaande bedrag te innen. "
          f"\nNog een fijne dag gewenst")