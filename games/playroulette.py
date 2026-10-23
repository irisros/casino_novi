
def print_choice_options():
    gamble_choice = int(input(f"""Kies één van de volgende opties (0 om te stoppen):
        1: rood
        2: zwart
        3: even
        4: oneven
        0: stop
                  """))
    return gamble_choice

def input_stake(gamble_choice, balance):
        stake = float(input("Hoeveel geld wil je inzetten?: "))
        if stake <= 0:
            print("Dit mag niet. Probeer opnieuw.")
            input_stake(gamble_choice, balance)
        if stake > balance:
            print("Te weinig saldo. Probeer opnieuw.")
            input_stake(gamble_choice, balance)
        return stake

def spin_action(spin):
    if spin == 0:
        kleur = "groen"
        odd_even = "geen"
    elif spin <= 18:
        if spin % 2 == 0:
            kleur = "zwart"
            odd_even = "even"
        else:
            kleur = "rood"
            odd_even = "oneven"
    elif spin > 18:
        if spin % 2 == 0:
            kleur = "rood"
            odd_even = "even"
        else:
            kleur = "zwart"
            odd_even = "oneven"
    return kleur, odd_even

def print_win_decision(choice, kleur, odd_even, balance, stake):
    win = False
    if choice == 1 and kleur == "rood":
        win = True
    elif choice == 2 and kleur == "zwart":
        win = True
    elif choice == 3 and odd_even == "even":
        win = True
    elif choice == 4 and odd_even == "oneven":
        win = True

    if win == True:
        balance += stake
        print(f'''Je hebt {stake} gewonnen. Je saldo is nu {balance}''')
    if win == False:
        balance -= stake
        print(f'''Je hebt {stake} verloren. Je saldo is nu {balance}''')
    return balance

def play_roulette(balance):
    round_number = 1
    while True:
        gamble_choice = print_choice_options()
        if gamble_choice == 0:
            break
        stake = input_stake(gamble_choice, balance)
        spin = (round_number * 7) % 37
        x, y = spin_action(spin)
        kleur = x
        odd_even = y
        balance = print_win_decision(gamble_choice, kleur, odd_even, balance, stake)
    return balance






