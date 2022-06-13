
from otree.api import *

import random
import itertools
import json

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'DCM_CM'
    players_per_group = None
    tasks = ['A', 'B', 'C']
    num_rounds = len(tasks)



class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

#FUNCTION
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, Constants.num_rounds + 1 ))
            random.shuffle(round_numbers)
            p.participant.task_rounds = dict(zip(Constants.tasks, round_numbers))


# PAGES
class CE1(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['A']


class CE2(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['B']


class CE3(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['C']



class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number ==  Constants.num_rounds






page_sequence = [CE1, CE2, CE3, Results]

