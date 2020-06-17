from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class SenderDecision(Page):
    form_model = 'group'
    form_fields = ['sender_decision']

    def is_displayed(self):
        return self.player.role() == 'sender'


class AfterSenderWP(WaitPage):
    after_all_players_arrive = 'set_multiplied_amount'


class ReceiverDecision(Page):
    form_model = 'group'
    form_fields = ['receiver_decision']

    def is_displayed(self):
        return self.player.role() == 'receiver'


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass


page_sequence = [
    SenderDecision,
    AfterSenderWP,
    ReceiverDecision,
    ResultsWaitPage,
    Results
]
