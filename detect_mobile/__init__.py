from otree.api import *

doc = """Detect and block mobile browsers"""


class Constants(BaseConstants):
    name_in_url = 'detect_mobile'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    is_mobile = models.BooleanField()


# PAGES
class MobileCheck(Page):
    form_model = 'player'
    form_fields = ['is_mobile']

    def error_message(player: Player, values):
        if values['is_mobile']:
            return "Sorry, this experiment does not allow mobile browsers."


class Task(Page):
    pass


page_sequence = [MobileCheck, Task]
