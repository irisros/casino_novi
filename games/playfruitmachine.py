def ask_for_bet(balance):
    while True:
        bet = float(input("Hoeveel wil je inzetten?: "))
        if bet <= 0:
            print("De inzet moet groter zijn dan 0!")
            continue
        if bet > balance:
            print("Te weinig saldo. Probeer opnieuw.")
            continue
        return float(bet)

def determine_rolls(round_number):
    roll = int(round_number) % 5
    if roll == 0:
        return "kers", "citroen", "ster"
    elif roll == 1:
        return "kers", "kers", "kers"
    elif roll == 2:
        return "ster", "ster", "citroen"
    elif roll == 3:
        return "citroen", "kers","ster"
    elif roll == 4:
        return "ster", "ster", "ster"

def determine_payout(roll1, roll2, roll3, bet, balance):
    if roll1 == "kers" and roll2 == "citroen" and roll3 == "ster":
        print("helaas niets gewonnen")
    elif roll1 == "kers" and roll2 == "kers" and roll3 == "kers":
        print("Drie keer kers, je krijgt 3 keer je inzet terug!")
        balance += bet * 3
    elif roll1 == "ster" and roll2 == "ster" and roll3 == "citroen":
        print("Twee keer ster, je krijgt 1 keer je inzet terug!")
        balance += bet
    elif roll1 == "citroen" and roll2 == "kers" and roll3 == "ster":
        print("Helaas niets gewonnen")
    elif roll1 == "ster" and roll2 == "ster" and roll3 == "ster":
        print("Drie keer ster, je krijgt 3 keer je inzet terug!")
        balance += bet * 3
    return balance

def play_fruitmachine(balance):
    round_number = 1
    while True:
        print(
            f"""Welkom bij de fruitmachine! Je huidige saldo is {balance}. Wil je dit spel beginnen, of stoppen?
            1: beginnen
            2: stoppen
             """)
        speelkeuze = input("Kies hier: ")
        if speelkeuze == "2":
            return balance
        elif speelkeuze == "1":
            bet = ask_for_bet(balance)
        balance -= bet
        roll1, roll2, roll3 = determine_rolls(round_number)
        balance = determine_payout(roll1, roll2, roll3, bet, balance)
        round_number += 1