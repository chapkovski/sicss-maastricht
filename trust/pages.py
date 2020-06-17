from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class FirstWP(WaitPage):
    group_by_arrival_time = True

    def is_displayed(self):
        return self.session.config.get('party_treatment', False)

    def get_players_for_group(self, waiting_players):
        democrats = [p for p in waiting_players if p.participant.vars['democrat']]
        republicans = [p for p in waiting_players if not p.participant.vars['democrat']]
        if len(democrats) > 1 and len(republicans) > 1:
            return [democrats[0], republicans[0]]
        undecided = [p for p in self.session.get_participants() if p.vars.get('democrat') is None]

        if len(undecided) == 0 and len(waiting_players) > 1:
            return waiting_players[:2]

    def after_all_players_arrive(self):
        print(self.group.get_players())


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
    FirstWP,
    SenderDecision,
    AfterSenderWP,
    ReceiverDecision,
    ResultsWaitPage,
    Results
]
