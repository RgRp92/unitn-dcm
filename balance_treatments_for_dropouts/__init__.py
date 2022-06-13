from otree.api import *


doc = """
Your app description
"""

TREATMENTS = ['red', 'blue', 'green']


class Constants(BaseConstants):
    name_in_url = 'balance_treatments_for_dropouts'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    session = subsession.session
    session.completions_by_treatment = {color: 0 for color in TREATMENTS}


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    color = models.StringField()


# PAGES
class Intro(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        session = player.session

        player.color = min(
            TREATMENTS, key=lambda color: session.completions_by_treatment[color],
        )


class Task(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        session = player.session
        session.completions_by_treatment[player.color] += 1


page_sequence = [Intro, Task]
