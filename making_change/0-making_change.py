#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)

    num = 0
    running = total

    for coin in sorted_coins:
        while running >= coin:
            running -= coin
            num += 1

    return num if running == 0 else -1
