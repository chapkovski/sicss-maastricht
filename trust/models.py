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
    players_per_group = None
    num_rounds = 1
    coef = 3
    endowment = 10


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.endowment = Constants.endowment


class Group(BaseGroup):
    sender_decision = models.CurrencyField(min=0)
    receiver_decision = models.CurrencyField(min=0)
    multiplied_sender = models.CurrencyField()

    def sender_decision_max(self):
        return self.get_player_by_role('sender').endowment

    def receiver_decision_max(self):
        return self.multiplied_sender

    def set_multiplied_amount(self):
        self.multiplied_sender = self.sender_decision * Constants.coef

    def set_payoffs(self):
        sender = self.get_player_by_role('sender')
        receiver = self.get_player_by_role('receiver')
        sender.payoff = sender.endowment - self.sender_decision + self.receiver_decision
        receiver.payoff = receiver.endowment + self.multiplied_sender - self.receiver_decision


class Player(BasePlayer):
    endowment = models.CurrencyField()

    def role(self):
        if self.id_in_group == 1:
            return 'sender'
        else:
            return 'receiver'