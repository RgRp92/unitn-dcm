from otree.api import *


doc = """
"Widget to rank/reorder items". See http://sortablejs.github.io/Sortable/
for more examples.
"""


class Constants(BaseConstants):
    name_in_url = 'rank_widget'
    players_per_group = None
    num_rounds = 1
    choices = ['Martini', 'Margarita', 'White Russian', 'Pina Colada', 'Gin & Tonic']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ranking = models.StringField()


class MyPage(Page):
    form_model = 'player'
    form_fields = ['ranking']


class Results(Page):
    pass


page_sequence = [MyPage, Results]
