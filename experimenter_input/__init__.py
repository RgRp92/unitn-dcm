from otree.api import *


doc = """
Experimenter input during the experiment,
e.g. entering the result of a random draw.

If you want the experimenter to be able to make an input at any time,
you can use the REST API (especially the session_vars endpoint).
"""


class Constants(BaseConstants):
    name_in_url = 'experimenter_input'
    players_per_group = None
    num_rounds = 1
    password = 'mypass'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    exp_input = models.IntegerField()
    has_exp_input = models.BooleanField(initial=False)


class Player(BasePlayer):
    pass


# PAGES
class Intro(Page):
    pass


class ExpInput(Page):
    """
    It should be a live page so that you can notify all other players to advance
    also, prevents everyone from moving forward prematurely
    """

    @staticmethod
    def live_method(player: Player, data):
        group = player.group

        if ('exp_input' in data) and ('password' in data):
            if data['password'] != Constants.password:
                return {player.id_in_group: dict(error="Incorrect password")}
            group.exp_input = data['exp_input']
            group.has_exp_input = True
        return {0: dict(finished=group.has_exp_input)}

    @staticmethod
    def error_message(player: Player, values):
        group = player.group
        if not group.has_exp_input:
            return "Experimenter has not input data yet"


class MyPage(Page):
    pass


page_sequence = [Intro, ExpInput, MyPage]
