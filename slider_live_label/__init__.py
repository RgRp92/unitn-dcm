from otree.api import *


doc = """
Slider with live updating label
"""


class Constants(BaseConstants):
    name_in_url = 'slider_live_label'
    players_per_group = None
    num_rounds = 1
    endowment = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    give = models.IntegerField(
        min=0, max=Constants.endowment, label="How much do you want to give?"
    )


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['give']

    @staticmethod
    def js_vars(player: Player):
        return dict(endowment=Constants.endowment)


page_sequence = [MyPage]
