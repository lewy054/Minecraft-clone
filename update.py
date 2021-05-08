from ursina import *
block_pick = 1


def update_function(hand):
    hand_position(hand)
    select_block()


def hand_position(hand):
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()


def select_block():
    global block_pick
    if held_keys['1']:
        block_pick = 1
    elif held_keys['2']:
        block_pick = 2
    elif held_keys['3']:
        block_pick = 3
    elif held_keys['4']:
        block_pick = 4
