from otree.api import *


doc = """
group by arrival time, but in each round assign to a new partner.
"""


class Constants(BaseConstants):
    name_in_url = 'gbat_new_partners'
    players_per_group = None
    num_rounds = 3


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    session = subsession.session
    session.past_groups = []


def group_by_arrival_time_method(subsession: Subsession, waiting_players):
    session = subsession.session

    import itertools

    for possible_group in itertools.combinations(waiting_players, 2):
        # use a set, so that we can easily compare even if order is different
        # e.g. {1, 2} == {2, 1}
        pair_ids = set(p.id_in_subsession for p in possible_group)
        if pair_ids not in session.past_groups:
            # mark this group as used, so we don't repeat it in the next round.
            session.past_groups.append(pair_ids)
            return possible_group


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class ResultsWaitPage(WaitPage):
    group_by_arrival_time = True
    body_text = "Waiting to pair you with someone you haven't already played with"


class MyPage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(partner=player.get_others_in_group()[0])


page_sequence = [ResultsWaitPage, MyPage]
