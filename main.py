import random
from card import card
from time import sleep

random.seed()


def set_deck_file():
    file = open("description.txt", "r")
    deck = list()
    for i in range(22):
        txt = file.readline().split("#")
        deck.append(card(txt[0], txt[1], txt[2], txt[3]))
    # print(len(deck))
    return deck


def print_info():
    print()
    print("List of commands:")
    print("s - single card")
    print("d - daily")
    print("w - weekly")
    print("m - monthly")
    print("sh - shuffle")
    print("info - this list")
    print("again - restart")
    print("stop - end of session")
    print()


def draw_hand(deck, num):
    if len(deck) > num:
        indexes, hand = [i for i in range(len(deck))], list()
        for i in range(num):
            index = random.randint(0, len(indexes) - 1)
            hand.append(deck[index])
            del indexes[index]
            del deck[index]
        print()
        return hand
    else:
        deck = refill(deck)

        indexes, hand = [i for i in range(len(deck))], list()
        for i in range(num):
            index = random.randrange(0, len(indexes))
            hand.append(deck[index])
            del indexes[index]
            del deck[index]
        print()
        return hand


def refill(deck):
    deck.clear()
    sleep(0.5)
    print("Deck is empty!")
    print("Refiling.......")
    sleep(1.5)
    print("READY")
    deck.clear()
    deck = set_deck_file()
    shuffle(deck, 1)
    return deck


def see_cards(hand):
    while len(hand) > 0:
        ur_card = hand[0]
        del hand[0]
        if ur_card.id_card == 3:
            print(ur_card.id_card, '. ', ur_card.name)
            print(ur_card.description_up)
            print(ur_card.description_down)
        else:
            print(str(ur_card.id_card) + ". " + str(ur_card.name) + " -> " + str(ur_card.poss))
            nex_cmd = input("Show description (y/n): ")
            if nex_cmd == "y":
                if ur_card.poss == "up":
                    print(ur_card.description_up)
                else:
                    print(ur_card.description_down)
                print()
            else:
                continue


def main():
    print_info()
    deck: list = set_deck_file()
    hand: list
    # cmd = None
    shuffle(deck, 1)
    while True:
        cmd = input("Command: ")
        if cmd == 'sh':  # shuffle deck n-times
            times = input("Enter times to shuffle: ")
            shuffle(deck, times)
        elif cmd == 's':  # single check
            hand = draw_hand(deck, 1)
            see_cards(hand)
        elif cmd == 'd':  # daily check
            hand = draw_hand(deck, 2)
            see_cards(hand)
        elif cmd == 'w':  # weekly check
            hand = draw_hand(deck, 4)
            see_cards(hand)
        elif cmd == 'm':  # monthly check
            hand = draw_hand(deck, 18)
            see_cards(hand)
        elif cmd == 'again':
            deck: list = set_deck_file()
        elif cmd == 'info':  # single check
            print_info()
        elif cmd == 'stop':  # single check
            break
        else:
            print('Invalid command')


def shuffle(deck, times):
    for i in range(int(times)):
        random.shuffle(deck)
        for card_t in deck:
            poss = random.randint(0, 1)
            if poss == 1:
                card_t.poss = 'up'
            else:
                card_t.poss = 'down'


if __name__ == '__main__':
    main()
