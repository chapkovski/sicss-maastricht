from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Q(Page):
    form_model = 'player'
    form_fields = ['democrat']

    def before_next_page(self):
        self.participant.vars['democrat'] = self.player.democrat




page_sequence = [Q]
