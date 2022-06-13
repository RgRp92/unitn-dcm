from otree.api import *


doc = """
Ranking your top N choices from a list of options.
"""


class Constants(BaseConstants):
    name_in_url = 'rank_topN'
    players_per_group = None
    num_rounds = 1
    choices = ['Martini', 'Margarita', 'White Russian', 'Pina Colada', 'Gin & Tonic']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def make_rank_field(label):
    return models.StringField(choices=Constants.choices, label=label)


class Player(BasePlayer):
    rank1 = make_rank_field("Top choice")
    rank2 = make_rank_field("Second choice")
    rank3 = make_rank_field("Third choice")


class MyPage(Page):
    form_model = 'player'
    form_fields = ['rank1', 'rank2', 'rank3']

    @staticmethod
    def error_message(player: Player, values):
        choices = [values['rank1'], values['rank2'], values['rank3']]
        if len(set(choices)) != len(choices):
            return "You cannot choose the same item twice"


class Results(Page):
    pass


page_sequence = [MyPage, Results]
