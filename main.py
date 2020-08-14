import gym
import random
import numpy as np
from jaipur_game import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    h = Hand()
    h2 = Hand()
    pile = Deck()
    pile.deal_hand(h)
    pile.deal_hand(h2)
    h.read_cards()
    h2.read_cards()

    pile.read_cards()
    middle = MiddlePile()
    print("Cards left: " + middle.num_cards().__str__())
    middle.read_cards()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
