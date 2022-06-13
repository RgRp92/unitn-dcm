from otree.api import *


doc = """
Question that lets you select multiple options
(multi-select, multiple choice / multiple answer)
"""


class Constants(BaseConstants):
    name_in_url = 'select_multiple'
    players_per_group = None
    num_rounds = 1
    languages = ['english', 'german', 'french', 'spanish', 'italian', 'chinese']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    english = models.BooleanField(blank=True)
    german = models.BooleanField(blank=True)
    french = models.BooleanField(blank=True)
    spanish = models.BooleanField(blank=True)
    italian = models.BooleanField(blank=True)
    chinese = models.BooleanField(blank=True)


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = Constants.languages


page_sequence = [MyPage]
