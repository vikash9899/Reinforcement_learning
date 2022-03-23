import numpy as np
import math


""" Simple blackjack environment
    # youtube video for Rules 
    https://www.youtube.com/watch?v=eyoh-Ku9TCI

    This environment is taken from the book Reinforcement Learning: An Introduction
    by Richard S. Sutton and Andrew G. Barto 2014, 2015.
    
    1. Blackjack is a card game where the goal is to obtain cards that sum to as
    near as possible to 21 without going over. They're playing against a fixed
    dealer.

    2. Face cards (Jack, Queen, King) have point value 10. 
    
    3. Aces can either count as 11 or 1, and it's called 'usable' at 11.
    
    4. This game is placed with an infinite deck (or with replacement).
    
    5. The game starts with each (player and dealer) having one face up and one
    face down card.
    
    6. The player can request additional cards (hit=1) until they decide to stop
    (stick=0) or exceed 21 (bust).
    
    7. After the player sticks, the dealer reveals their facedown card, and draws
    until their sum is 17 or greater.  If the dealer goes bust the player wins.
    
    8. If neither player nor dealer busts, the outcome (win, lose, draw) is
    decided by whose sum is closer to 21.  The reward for winning is +1,
    drawing is 0, and losing is -1.
    
    9. The observation of a 3-tuple of: the players current sum,
    the dealer's one showing card (1-10 where 1 is ace),
    and whether or not the player holds a usable ace (0 or 1).
"""


class BlackJack:

    def __init__(self) -> None:
        self.cards = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
                      'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        # 1 for Ace and 10, 10, 10 for the face cards
        self.cards_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.nCards = math.inf
        self.nA = 2
        self.Actions = ["Hit", "Stick"]
        self.States = []
        for i in range(1, 31):
            self.States.append(i)
        self.nS = len(self.States)
        self.winner = ''
        self.start()

    def start(self):
        k = self.__delta_card()

        self.dealers_hand = [self.cards_value[k]]
        self.dealers_cards = [self.cards[k]]
        k = self.__delta_card()

        self.players_hand = [self.cards_value[k]]
        self.players_cards = [self.cards[k]]
        k = self.__delta_card()
        self.players_hand.append(self.cards_value[k])
        self.players_cards.append(self.cards[k])

        reward = 0
        done = False

        return {'pCards': self.players_cards, 'nState': self.__score(self.players_cards, self.players_hand),
                'dealers_cards': self.dealers_cards, 'dealers_score': self.__score(self.dealers_cards, self.dealers_hand),
                # 'action': action,
                'reward': reward, 'done': done}

    def play(self, action):
        done = False
        if action == 'Hit':
            k = self.__delta_card()
            self.players_hand.append(self.cards_value[k])
            self.players_cards.append(self.cards[k])
            bust = self.__bust(self.players_cards, self.players_hand)
            if bust:
                done = True
                reward = -1
            else:
                done = False
                reward = 0

        elif action == 'Stick':
            done = True
            while self.__score(self.dealers_cards, self.dealers_hand) < 17:
                k = self.__delta_card()
                self.dealers_hand.append(self.cards_value[k])
                self.dealers_cards.append(self.cards[k])

            bust = self.__bust(self.dealers_cards, self.dealers_hand)

            if bust:
                reward = 1
            else:
                dealer = self.__score(self.dealers_cards, self.dealers_hand)
                player = self.__score(self.players_cards, self.players_hand)
                if dealer < player:
                    reward = 1
                else:
                    reward = -1

        return {'pCards': self.players_cards, 'nState': self.__score(self.players_cards, self.players_hand),
                'dealers_cards': self.dealers_cards, 'dealers_score': self.__score(self.dealers_cards, self.dealers_hand),
                'action': action,
                'reward': reward, 'done': done}

    def __bust(self, cards, hands):
        if self.__score(cards, hands) > 21:
            return True
        else:
            return False

    def __score(self, cards, hands):
        if self.__usable_ace(cards, hands):
            return sum(hands) + 10
        else:
            return sum(hands)

    def __usable_ace(self, cards, hands):
        if 'Ace' in cards and sum(hands)+10 < 21:
            return True
        else:
            return False

    def __delta_card(self):
        return np.random.randint(0, 13)
