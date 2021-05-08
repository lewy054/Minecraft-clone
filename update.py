from ursina import *


class Update():
    def __init__(self, hand, slots):
        self.hand = hand
        self.slots = slots
        self._block_pick = 1

    def update_function(self):
        self.hand_position()
        self.select_block()

    def hand_position(self):
        if held_keys['left mouse'] or held_keys['right mouse']:
            self.hand.active()
        else:
            self.hand.passive()

    def select_block(self):
        if held_keys['1']:
            self.activate_slot()
            self._block_pick = 1
        elif held_keys['2']:
            self.activate_slot()
            self._block_pick = 2
        elif held_keys['3']:
            self.activate_slot()
            self._block_pick = 3
        elif held_keys['4']:
            self.activate_slot()
            self._block_pick = 4
        elif held_keys['5']:
            self.activate_slot()
            self._block_pick = 5

    def activate_slot(self):
        for slot in self.slots:
            self.slots[slot].passive()
        self.slots[self._block_pick - 1].active()

    @property
    def block_pick(self):
        return self._block_pick

    @block_pick.setter
    def block_pick(self, value):
        self._block_pick = value
