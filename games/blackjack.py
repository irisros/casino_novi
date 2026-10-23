import random

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def make_deck_list():
    decklist = []
    for suits in SUITS:
        for ranks in RANKS:
            decklist.append(suits + ranks)
    return decklist

def get_two_random(decklist):
    random.shuffle(decklist)
    return [decklist.pop(), decklist.pop()]

def get_one_random(decklist):
    random.shuffle(decklist)
    return [decklist.pop()]

def ask_for_bet2(balance):
    while True:
        bet = float(input("Hoeveel wil je inzetten?: "))
        if bet <= 0:
            print("De inzet moet groter zijn dan 0!")
            continue
        if bet > balance:
            print("Te weinig saldo. Probeer opnieuw.")
            continue
        return float(bet)

def total_count(custom_list):
    total_count = 0
    aces = 0
    for items in custom_list:
        if items[1:] == "A":
            total_count += 11
            aces += 1
        elif items[1:] == "J" or items[1:] == "K" or items[1:] == "Q":
            total_count += 10
        else:
            total_count += int(items[1:])
    while total_count > 21 and aces >= 1:
        total_count -= 10
        aces -= 1
    return total_count

def play_blackjack(balance):

    player_hand = []
    dealer_hand = []
    while True:
        decklist = make_deck_list()
        player_hand.clear()
        dealer_hand.clear()

        start_game = input(
        f"""Welkom bij Blackjack! Je huidige saldo is {balance}. Kies één van de volgende opties:
        1: Beginnen
        2: Stoppen
        Kies je antwoord:
        """
        )
        if start_game == "2":
            return balance
        elif start_game == "1":
            bet = ask_for_bet2(balance)
            balance -= bet
            print(f"""
            Huidig saldo: {balance}
            Je inzet: {bet}""")

        player_hand.extend(get_two_random(decklist))
        dealer_hand.extend(get_two_random(decklist))

        print(f"""
        Jouw hand: {player_hand[0]} |  {player_hand[1]}
        Dealer toont: {dealer_hand[0]} | ?? """)
        while True:
            random.shuffle(decklist)
            hit_or_stand = input(f"""Wat wil je doen?
                    1: Hit
                    2: Stand
                    """)
            if hit_or_stand == "1":
                player_hand.extend(get_one_random(decklist))
                print(f"""
                Je trekt: {player_hand[-1]}
                Jouw hand: {player_hand}""")
            elif hit_or_stand == "2":
                print(f"""
                Dealer hand: {dealer_hand}""")

                while True:
                    sum_dealer = total_count(dealer_hand)
                    if sum_dealer >= 17:
                        break
                    elif sum_dealer < 17:
                        dealer_hand.extend(get_one_random(decklist))
                        print(f"""De hand van de dealer is nu: {dealer_hand}""")
                        continue

                sum_player = total_count(player_hand)
                if sum_dealer > 21:
                    print(f"""Je hebt gewonnen omdat de totale som van de lijst van de dealer boven de 21 komt. Je krijgt 2x je inzet""")

                    break
                elif sum_player > 21:
                    print("Je hebt verloren omdat je boven de 21 hebt. Je krijgt niks.")
                elif sum_player > sum_dealer:
                    print(f""""Jij hebt hoger, dus, gewonnen!""")
                    balance += 2 * bet
                    break
                elif sum_player == sum_dealer:
                    print(f"""Gelijkspel. Je krijgt je inzet terug""")
                    balance += bet
                    break
                elif sum_player < sum_dealer:
                    print(f"""Je hebt verloren. Je krijgt niks.""")
                    break

                return balance


















