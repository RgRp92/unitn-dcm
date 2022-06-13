from otree.api import *


doc = """
Using CSS to style timer and chat box.
"""


class Constants(BaseConstants):
    name_in_url = 'css'
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
    timeout_seconds = 30 * 60


page_sequence = [MyPage]
