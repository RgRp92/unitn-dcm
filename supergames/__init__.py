from otree.api import *


doc = """
Supergames consisting of multiple rounds each
"""


def cumsum(lst):
    total = 0
    new = []
    for ele in lst:
        total += ele
        new.append(total)
    return new


class Constants(BaseConstants):
    name_in_url = 'supergames'
    players_per_group = None

    # first supergame lasts 2 rounds, second supergame lasts 3 rounds, etc...
    rounds_per_sg = [2, 3, 4, 5]
    sg_ends = cumsum(rounds_per_sg)
    num_rounds = sum(rounds_per_sg)


class Subsession(BaseSubsession):
    sg = models.IntegerField()
    period = models.IntegerField()
    is_last_period = models.BooleanField()


def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        sg = 1
        period = 1
        for ss in subsession.in_rounds(1, Constants.num_rounds):
            ss.sg = sg
            ss.period = period
            is_last_period = ss.round_number in Constants.sg_ends
            ss.is_last_period = is_last_period
            if is_last_period:
                sg += 1
                period = 1
            else:
                period += 1


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class NewSupergame(Page):
    @staticmethod
    def is_displayed(player: Player):
        subsession = player.subsession
        return subsession.period == 1


class Play(Page):
    pass


page_sequence = [NewSupergame, Play]
