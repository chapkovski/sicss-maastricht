from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class FirstWP(WaitPage):
    """This is the first page in a sequence.
    Here we get the participants from the previous app (Q), and
    try to create groups of two, based on their political affiliation that they stated
    in the first app
    """
    group_by_arrival_time = True

    def is_displayed(self):
        """We need to do this sorting only in a treatment that takes this political
        affiliation into account. That's why we skip this page if in a specific experimental session
        this treatment variable is not set.
        """
        return self.session.config.get('party_treatment', False)

    def get_players_for_group(self, waiting_players):
        """This is a special method to create groups dynamically based on some properties they have,
        and on their arrival time (if needed). The logic is simple:
        we get all players who currently wait. We take all democrats and republicans from there, and
        from 1 democrat, and 1 republican we form the group which proceeds further in a Trust game.

        The only problematic thing here is to solve the balancing issue: what if number of republicans
        not equals the number of democrats. There are many ways to resolve this. The current one is the most naive:
        as soon as everyone in an experimental session makes his/her decision re political affiliation,
        and there are no more available R-D pairs left, we just match the rest pairwise regardless their affiliation.

        """
        democrats = [p for p in waiting_players if p.participant.vars['democrat']]
        republicans = [p for p in waiting_players if not p.participant.vars['democrat']]
        if len(democrats) > 1 and len(republicans) > 1:
            return [democrats[0], republicans[0]]
        undecided = [p for p in self.session.get_participants() if p.vars.get('democrat') is None]

        if len(undecided) == 0 and len(waiting_players) > 1:
            return waiting_players[:2]


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
