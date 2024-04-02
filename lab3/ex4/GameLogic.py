import random

class GameLogic:
    def __init__(self, action_event, win_event):
        self.rocks = 0
        self.player_turn = True
        self.action_event = action_event
        self.win_event = win_event

    def start(self, amount):
        self.rocks = 5 if amount <= 0 else amount
        self.player_turn = True
        self.action_event(self.rocks)

    def action(self, amount):
        if amount < 1:
            amount = 1
        if amount > 3:
            amount = 3

        self.rocks -= amount
        if self.rocks <= 0:
            self.action_event(self.rocks)
            self.win_event(self.player_turn)
            return
        self.player_turn = not self.player_turn
        if not self.player_turn:
            self.ai_turn()
        self.action_event(self.rocks)

    def ai_turn(self):
        take = self.rocks % 4
        if take == 0:
            take = random.randint(1, 3)
        self.action(take)
