from otree.api import *


doc = """
App where we choose the app to be paid
"""


class Constants(BaseConstants):
    name_in_url = 'pay_random_app3'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    app_to_pay = models.StringField()


class PayRandomApp(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import random

        participant = player.participant
        apps = [
            'pay_random_app1',
            'pay_random_app2',
        ]
        app_to_pay = random.choice(apps)
        participant.payoff = participant.app_payoffs[app_to_pay]
        player.app_to_pay = app_to_pay


class Results(Page):
    pass


page_sequence = [PayRandomApp, Results]
