This the basic implementation of the BlackJack Game environment and Agent find the optimal policy to play this game. 

Simple blackjack environment
    # youtube video for Rules 
    https://www.youtube.com/watch?v=eyoh-Ku9TCI

    This environment is taken from the book Reinforcement Learning: An Introduction
    by Richard S. Sutton and Andrew G. Barto 2014, 2015.
    
    Action space : [Hit, Stick] 
    Environment observations : [Usable ace, done] 
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

Report is there for more details.




