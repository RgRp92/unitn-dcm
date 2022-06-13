from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'pay_random_app1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        p.participant.app_payoffs = {}


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    potential_payoff = models.CurrencyField()


# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        """
        In multiplayer games, payoffs are typically set in after_all_players_arrive,
        so that's what we demonstrate here.
        """
        import random

        for p in group.get_players():
            participant = p.participant
            potential_payoff = random.randint(100, 200)
            p.potential_payoff = potential_payoff
            # __name__ is the name of the current app
            participant.app_payoffs[__name__] = potential_payoff


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
