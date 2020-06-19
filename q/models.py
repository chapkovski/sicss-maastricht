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

author = 'Philipp Chapkovski'

doc = """
This is a one-question app where we collect players' political affiliation so we can match them into
Republican-Democrat pairs later.
"""


class Constants(BaseConstants):
    name_in_url = 'q'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    """in the database just True/False value is stored (0/1). But we would like to show them as Democrat/Republican
    choice, that's why we put the choices into parentheses (False, 'Republican') etc."""
    democrat = models.BooleanField(
        choices=[(False, 'Republican'), (True, 'Democrat')],
        widget=widgets.RadioSelectHorizontal
    )
