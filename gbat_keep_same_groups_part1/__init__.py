from otree.api import *


doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'gbat_keep_same_groups'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class GBATWait(WaitPage):
    group_by_arrival_time = True

    @staticmethod
    def after_all_players_arrive(group: Group):
        for p in group.get_players():
            participant = p.participant
            participant.past_group_id = group.id


class MyPage(Page):
    pass


page_sequence = [GBATWait, MyPage]
