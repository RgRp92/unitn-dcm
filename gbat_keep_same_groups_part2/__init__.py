from otree.api import *


doc = """
Preserve same groups as a previous app that used group_by_arrival time.
"""


class Constants(BaseConstants):
    name_in_url = 'gbat_keep_same_groups_part2'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


def group_by_arrival_time_method(subsession: Subsession, waiting_players):
    d = {}
    for p in waiting_players:
        group_id = p.participant.past_group_id
        if group_id not in d:
            d[group_id] = []
        players_in_my_group = d[group_id]
        players_in_my_group.append(p)
        if len(players_in_my_group) == 2:
            return players_in_my_group


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class GBATWait(WaitPage):
    group_by_arrival_time = True


class MyPage(Page):
    pass


page_sequence = [GBATWait, MyPage]
