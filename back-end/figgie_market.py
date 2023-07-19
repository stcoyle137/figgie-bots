import random
import threading
import random
from enum import Enum

Suits = Enum('Suits', ['DIAMOND', 'HEART', 'SPADE', 'CLUB'])

book = {Suits.DIAMOND : [-1,-1], Suits.HEART : [-1,-1], Suits.SPADE : [-1,-1], Suits.CLUB : [-1,-1]}
active_traders = {Suits.DIAMOND : [-1,-1], Suits.HEART : [-1,-1], Suits.SPADE : [-1,-1], Suits.CLUB : [-1,-1]}


'''
suits_count = [common, short, full, full]
hand = (DIAMOND, HEART, SPADE, CLUB)
'''

def generate_hands(suits_count,players):
    deck = [suits_count[0] for i in range(12)] + [suits_count[1] for i in range(8)] + [suits_count[2] for i in range(10)] + [suits_count[3] for i in range(10)]
    random.shuffle(deck)
    
    hands = [{Suits.DIAMOND : 0, Suits.HEART : 0, Suits.SPADE : 0, Suits.CLUB : 0} for i in range(players)]
    json_hands = [{Suits.DIAMOND.name : 0, Suits.HEART.name : 0, Suits.SPADE.name : 0, Suits.CLUB.name : 0} for i in range(players)]
    
    for deal in range(len(deck)):
        hands[deal % players][deck[deal]] += 1
        string_hands[deal % players][deck[deal].name] += 1
        
    return hands, json_hands


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
    clear_book()


def clear_book():
    book = {Suits.DIAMOND : [-1,-1], Suits.HEART : [-1,-1], Suits.SPADE : [-1,-1], Suits.CLUB : [-1,-1]}
    
    
class Player():
    def __init__(self, trader_id, api_id, bank, hand):
        self.api_id = random.randint(2**16,2**20)
        self.trader_id = trader_id
        self.bank = bank
        self.hand = hand
    
    def trade(self, payment, suit, bidding):
        if self.valid_trade(payment, suit, bidding):
            return false
        self.bank += self.payment * (-1 if isBidding else 1)
        self.hand[suit] += (1 if isBidding else -1)
        return self.hand, self.bank
    
    
    def valided_trade(self, payment, suit, bidding):
        if bidding and payment > self.bank:
            return false
        elif not bidding and self.hand[suit] <= 0:
            return false
        else:
            return true
    
    
    
        
    
class Market():
    
    def __init__(self):
        
    