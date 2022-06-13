from otree.api import *


doc = """
Timer: replacing the default timer with your own
"""


class Constants(BaseConstants):
    name_in_url = 'timer_custom'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class MyPage(Page):
    timeout_seconds = 60


page_sequence = [MyPage]
