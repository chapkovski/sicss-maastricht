from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        if self.player.role() == 'sender':
            """We randomly select a possible sender's decision"""
            yield pages.SenderDecision,\
                  dict(sender_decision=random.randint(0,self.player.endowment))
        else:
            """We randomly select a possible receiver's decision"""
            yield pages.ReceiverDecision, dict(receiver_decision=random.randint(0,self.group.multiplied_sender))

        yield pages.Results
