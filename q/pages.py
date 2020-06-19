from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Q(Page):
    """ this app basically contains just one page, where we ask people to choose their political affiliation.
    That is of course for demo purposes only, because real-life implementation should be much more subtle.
    """
    form_model = 'player'
    form_fields = ['democrat']

    def before_next_page(self):
        """We need to pass this information to the next app, that's why we pass this app's field info to the
        participant.vars 'democrat' that we will use at the beginning of 'trust' game app.
        """
        self.participant.vars['democrat'] = self.player.democrat




page_sequence = [Q]
