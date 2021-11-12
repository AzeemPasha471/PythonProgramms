'''
@Author: Md Azeem pasha
@Date: 2021-11-09
@Title :Flip Coin and print percentage of Heads and Tails '''

import random

def flipCoin():
    no_of_flip = int(input(" Enter number of time coin to be fliped: "))
    tail = 0
    head = 0

    for toss in range(no_of_flip):
        toss = random.random()
        if toss <0.5:
            tail=tail + 1
        else:
            head=head + 1
        percentHead= (head / no_of_flip) * 100
        percentTail=100 - percentHead
    print("Percentage Of Head:",percentHead)
    print("Percentage Of Tail:",percentTail)

flipCoin()


