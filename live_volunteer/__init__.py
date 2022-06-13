from otree.api import *


doc = """
Live volunteer's dilemma (first player to click moves everyone forward).
"""


class Constants(BaseConstants):
    name_in_url = 'live_volunteer'
    players_per_group = 3
    num_rounds = 1
    reward = cu(1000)
    volunteer_cost = cu(500)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    has_volunteer = models.BooleanField(initial=False)


class Player(BasePlayer):
    is_volunteer = models.BooleanField()
    volunteer_id = models.IntegerField()


# PAGES
class MyPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return not group.has_volunteer

    @staticmethod
    def live_method(player: Player, data):
        group = player.group

        if group.has_volunteer:
            return
        if data.get('volunteer'):
            group.has_volunteer = True
            for p in player.get_others_in_group():
                p.payoff = Constants.reward
                p.is_volunteer = False
            player.is_volunteer = True
            player.payoff = Constants.reward - Constants.volunteer_cost
            return {0: dict(finished=True)}

    @staticmethod
    def error_message(player: Player, values):
        group = player.group
        if not group.has_volunteer:
            return "Can't move forward"


class Results(Page):
    pass


page_sequence = [MyPage, Results]
