from otree.api import *


doc = """
Question that lets you select multiple options
(multi-select, multiple choice / multiple answer)
"""


class Constants(BaseConstants):
    name_in_url = 'multi_select_complex'
    players_per_group = None
    num_rounds = 1
    languages = [
        dict(name='english', label="I speak English"),
        dict(name='french', label="Je parle français"),
        dict(name='spanish', label="Hablo español"),
        dict(name='finnish', label="Puhun suomea"),
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    english = models.BooleanField(blank=True)
    french = models.BooleanField(blank=True)
    spanish = models.BooleanField(blank=True)
    finnish = models.BooleanField(blank=True)


# PAGES
class MyPage(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        return [lang['name'] for lang in Constants.languages]

    @staticmethod
    def error_message(player: Player, values):
        num_selected = 0
        for lang in Constants.languages:
            if values[lang['name']]:
                num_selected += 1
        if num_selected < 1:
            return "You must select at least 1 language."


page_sequence = [MyPage]
