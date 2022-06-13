from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'pass_data_between_apps1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    language = models.StringField(label='What is your main language?')


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['language']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant

        # in settings.py need to add 'language' to PARTICIPANT_FIELDS.
        participant.language = player.language


page_sequence = [MyPage]
