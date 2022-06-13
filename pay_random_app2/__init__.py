from otree.api import *


doc = """
"""


class Constants(BaseConstants):
    name_in_url = 'pay_random_app2'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    potential_payoff = models.CurrencyField()


# PAGES
class MyPage(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        """in a single-player game you typically set payoff in before_next_page,
        so that's what we demonstrate here.
        """
        participant = player.participant
        import random

        potential_payoff = random.randint(100, 200)
        player.potential_payoff = potential_payoff
        # this is designed for apps that have a single round.
        # if your app has multiple rounds, see the pay_random_round app.
        participant.app_payoffs[__name__] = potential_payoff


class Results(Page):
    pass


page_sequence = [MyPage, Results]
