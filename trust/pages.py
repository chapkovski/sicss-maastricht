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
        """If there are enough participants to make D-R group we do it. """
        if len(democrats) > 1 and len(republicans) > 1:
            return [republicans[0], democrats[0], ]
        """If no one undecided left, we match participants into pairs regardless their affiliation"""
        undecided = [p for p in self.session.get_participants() if p.vars.get('democrat') is None]
        if len(undecided) == 0 and len(waiting_players) > 1:
            return waiting_players[:2]




class SenderDecision(Page):
    form_model = 'group'
    form_fields = ['sender_decision']

    def is_displayed(self):
        """This page is shown only to a sender"""
        return self.player.role() == 'sender'


class AfterSenderWP(WaitPage):
    """At this page a receiver  will wait for a Sender's decision.
    As soon as all group members are here we calculate the multiplied amount so the receiver would know the
    maximum amount he can send back.
    """
    after_all_players_arrive = 'set_multiplied_amount'


class ReceiverDecision(Page):
    """This is a bit naive because actually if Sender did not send anything at all, there is no
    sense to show this page to a receiver (if he gets nothing from Sender, he can't send anything back.
    But for the sake of simplicity let's keep it like that.
    """
    form_model = 'group'
    form_fields = ['receiver_decision']

    def is_displayed(self):
        """This page is shown only to a sender"""
        return self.player.role() == 'receiver'


class ResultsWaitPage(WaitPage):
    """At this page a sender  will wait for a receiver's decision.
    As soon as all members are here we calculate the payoffs of both members"""
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    """We show results here"""
    pass


page_sequence = [
    FirstWP,
    SenderDecision,
    AfterSenderWP,
    ReceiverDecision,
    ResultsWaitPage,
    Results
]
