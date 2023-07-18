import random
import threading
from enum import Enum

Suits = Enum('Suits', ['DIAMOND', 'HEART', 'SPADE', 'CLUB'])
book = {Suits.DIAMOND : [-1,-1], Suits.HEART : [-1,-1], Suits.SPADE : [-1,-1], Suits.CLUB : [-1,-1]}


'''
suits_count = [common, short, full, full]
hand = (DIAMOND, HEART, SPADE, CLUB)
'''

def generate_hands(suits_count,players):
    deck = [suits_count[0] for i in range(12)] + [suits_count[1] for i in range(8)] + [suits_count[2] for i in range(10)] + [suits_count[3] for i in range(10)]
    random.shuffle(deck)
    hands = [{Suits.DIAMOND : 0, Suits.HEART : 0, Suits.SPADE : 0, Suits.CLUB : 0} for i in range(players)]
    
    for deal in range(len(deck)):
        hands[deal % players][deck[deal]] += 1
        
    return hands


def place_order(suit, price, bidding):
    book_suit = book[suit]
    if price <= 0:
        return
    if bidding:
        if price >= book_suit[1] and book_suit[1] != -1:
            trade(suit, true)
        elif price > book_suit[0]:
            book_suit[0] = price
    else:
        if price <= book_suit[0] and book_suit[0] != -1:
            trade(suit, true)
        elif price < book_suit[1]:
            book_suit[1] = price

def trade(suit, buying):
    print(
    clear_book()


def clear_book():
    book = {Suits.DIAMOND : [-1,-1], Suits.HEART : [-1,-1], Suits.SPADE : [-1,-1], Suits.CLUB : [-1,-1]}
    
    
def market():
    