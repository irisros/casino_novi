from games.playroulette import play_roulette
from games.playfruitmachine import play_fruitmachine
from games.blackjack import play_blackjack

MIN_AGE = 18
ENTRYTICKET = float(10)
MANDATORYDRINK = float(5)
GAMBLINGTAX = float(5)

def calculate_age(birthdate):
    birth_day, birth_month, birth_year = birthdate.split("-")
    age = 2026 - int(birth_year)
    return age

def check_age(birthdate):
    age = calculate_age(birthdate)
    if age < MIN_AGE:
        print("Je bent niet oud genoeg om toegang te krijgen tot een casino!")
        exit(1)
    return age

def determine_addressing(gender):
    if gender == 'vrouw':
        addressing = 'mevrouw'
    elif gender == 'man':
        addressing = 'meneer'
    else:
        addressing = ''
    return addressing

def determine_salutation(firstname, lastname, gender, addressing):
    salutation = f"""Welkom, {addressing} {firstname} {lastname}."""
    return salutation

def calculate_fixed_costs():
    fixed_costs = ENTRYTICKET + MANDATORYDRINK + GAMBLINGTAX
    return float(fixed_costs)

def input_startbudget():
    startbudget = input("Wat is je startbudget? ")
    return float(startbudget)

def calculate_balance(startbudget):
    balance = startbudget - calculate_fixed_costs()
    return float(balance)

def show_balance(balance):
    print(f"""Uw huidig saldo is {float(balance):.2f}""")
    return balance

def show_account(firstname, lastname, addressing, birthdate, age):
    print(f"""
    Casino de Gouden Driehoek - Account
    -------------------------------------------
    Naam:           {firstname + lastname}
    Aanspreekvorm:  {addressing}
    Geboortedatum:  {birthdate}
    Leeftijd:       {age}
    
    """)

def show_welcome_message(salutation, startbudget, fixed_costs, balance):
    welcome_message = f"""
    Casino de Gouden Driehoek
    ------------------------------------------- 
    {salutation}
    Startbudget:    €{startbudget:.2f}
    Vaste kosten:   €{fixed_costs:.2f}
    Saldo:          €{balance:.2f}
    """
    print(welcome_message)

def show_main_menu():
    main_menu_choice = input(f"""
    Casino de Gouden Driehoek - Hoofdmenu
    -------------------------------------------
    1. Spellen
    2. Saldo
    3. Account
    0. Stop
    
    Kies een optie: 
    """)
    return main_menu_choice

def show_games_menu():
    games_menu_choice = input(f"""
    Casino de Gouden Driehoek - Games Menu
    -------------------------------------------
    1. Fruitmachine
    2. Roulette
    3. Blackjack
    0. Terug
    
    Kies een optie: 
    """)
    return games_menu_choice

def main():
    firstname = input("Voornaam: ").title()
    lastname = input("Achternaam: ").title()

    birthdate = input("Wat is je geboortedatum? (DD-MM-YYYY):")
    age = calculate_age(birthdate)
    check_age(birthdate)

    gender = input("Geslacht: ").lower()
    addressing = determine_addressing(gender)

    salutation = determine_salutation(firstname, lastname, gender, addressing)
    startbudget = input_startbudget()
    fixed_costs = calculate_fixed_costs()
    balance = calculate_balance(startbudget)

    show_welcome_message(salutation, startbudget, fixed_costs, balance)
    while True:
        main_menu_choice = show_main_menu()
        if main_menu_choice == "1":
            while True:
                games_menu_choice = show_games_menu()
                if games_menu_choice == "1":
                    balance = play_fruitmachine(balance)
                elif games_menu_choice == "2":
                    balance = play_roulette(balance)
                elif games_menu_choice == "3":
                    balance = play_blackjack(balance)
                elif games_menu_choice == "0":
                    break
        elif main_menu_choice == "2":
            print(f""" Uw huidig saldo is {balance}""")
            continue
        elif main_menu_choice == "3":
            show_account(firstname, lastname, addressing, birthdate, age)
            continue
        elif main_menu_choice == "0":
            exit(1)
        else:
            print("Ongeldig. Probeer opnieuw.")
            continue

if __name__ == '__main__':
    main()




