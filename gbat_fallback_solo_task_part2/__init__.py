from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'gbat_fallback_solo_task_part2'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class SoloTask(Page):
    pass


page_sequence = [SoloTask]
