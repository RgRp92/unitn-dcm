from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'input_calculation'
    players_per_group = None
    num_rounds = 1
    APR = 0.07


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    amount = models.CurrencyField(min=0, max=100000)
    num_years = models.IntegerField(min=1, max=50)


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['amount', 'num_years']

    @staticmethod
    def js_vars(player: Player):
        return dict(APR=Constants.APR)


page_sequence = [MyPage]
