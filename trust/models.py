from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Philip Chapkovski'

doc = """
Trust game goes here
"""


class Constants(BaseConstants):
    name_in_url = 'trust'
    players_per_group = 2
    num_rounds = 1
    coef = 3
    endowment = 10


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.endowment = Constants.endowment

    def party_treatment(self):
        """We use this just to show the other member party affilation conditionally on the treatment"""
        return self.session.config.get('party_treatment')


class Group(BaseGroup):
    """Why we store these values on the group level? Because these two are the same for both players."""
    sender_decision = models.CurrencyField(min=0)
    receiver_decision = models.CurrencyField(min=0)
    multiplied_sender = models.CurrencyField()

    def sender_decision_max(self):
        """This method lets us set the max value of sender decision dynamically.
        In this specific scenario we don't need it and could set max right in the field declaration.
        But it makes sense to still do it here, just in case later on the endowment will be variable (and for
        demo purposes of this workshop, obviously :) )
        """
        return self.get_player_by_role('sender').endowment

    def receiver_decision_max(self):
        """The amount receiver can get back is  dynamic in a sense that it depends on how much Sender decided to send
        """

        return self.multiplied_sender

    def set_multiplied_amount(self):
        """This method is called when sender is done with his decision.
        This is actually can be skipped but it's nice to have a multiplied data immediately stored in a
        resulting dataset"""
        self.multiplied_sender = self.sender_decision * Constants.coef

    def set_payoffs(self):
        """This method is executed when receiver is done with his decision - to calculate final payoffs"""
        sender = self.get_player_by_role('sender')
        receiver = self.get_player_by_role('receiver')
        sender.payoff = sender.endowment - self.sender_decision + self.receiver_decision
        receiver.payoff = receiver.endowment + self.multiplied_sender - self.receiver_decision


class Player(BasePlayer):
    endowment = models.CurrencyField()

    def other_party(self):
        """We get the other player's affiliation here. It is not the most elegant way for many reasons,
        but the simplest one. (see more on that in Django docs on get_FIELD_display"""
        other = self.get_others_in_group()[0]
        if other.participant.vars['democrat']:
            return 'democrat'
        else:
            return 'republican'

    def role(self):
        """Since they get assign into groups dynamically we guarantee here that the roles will be assigned
        randomly and not based on their political affilation or anything like that. We may change this if
        we want to, balancing R-D groups with D-R groups or by introducing any other (more complicated) logic."""
        if self.id_in_group == 1:
            return 'sender'
        else:
            return 'receiver'
