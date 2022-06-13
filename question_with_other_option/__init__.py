from otree.api import *

doc = """
Menu with an 'other' option that lets you type in a valueInput manually
"""


class Constants(BaseConstants):
    name_in_url = 'question_with_other_option'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    native_language = models.StringField(
        choices=['German', 'English', 'Chinese', 'Turkish', 'Other']
    )
    native_language_other = models.StringField(
        label="You selected 'other'. What is your native language?"
    )


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['native_language']


class MyPage2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.native_language == 'Other'

    form_model = 'player'
    form_fields = ['native_language_other']


page_sequence = [MyPage, MyPage2]
