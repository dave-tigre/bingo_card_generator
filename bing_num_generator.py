import numpy as np
import pandas as pd
import random

gridSize = 5
minNum = 1
maxNum = 50

def draw_card():
    letters = ['B','I','N','G','O']
    nums = range(minNum, maxNum)
    return str(random.choice(letters))+str(random.choice(nums))


def main():
    gen_bool = True
    visited = []
    card = draw_card()
    while True:
        gen_bool = input("Generate new number?")
        if gen_bool == 'y':           
            while card not in visited:
                visited.append(card)
                print(draw_card())
            card = draw_card()
main()