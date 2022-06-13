from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'appcopy1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    bbb = models.IntegerField(widget=widgets.RadioSelectHorizontal)


def bbb_choices(player: Player):
    return [1, 2, 3]


class MyPage(Page):
    # every page needs an explicit template_name
    template_name = 'appcopy1/MyPage.html'

    form_model = 'player'
    form_fields = ['bbb']


page_sequence = [MyPage]
