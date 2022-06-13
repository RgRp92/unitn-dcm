from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'random_num_rounds'
    players_per_group = None
    num_rounds = 20


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    import random

    for p in subsession.get_players():
        p.participant.num_rounds = random.randint(1, 20)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    num_rounds = models.IntegerField()


# PAGES
class MyPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number < participant.num_rounds


class End(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds


page_sequence = [MyPage, End]
