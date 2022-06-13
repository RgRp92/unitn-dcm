from otree.api import *


doc = """
Sequential / cascade game (symmetric)
"""


class Constants(BaseConstants):
    name_in_url = 'sequential_symmetric'
    players_per_group = 3
    num_rounds = 1
    main_template = __name__ + '/Decide.html'
    table_template = __name__ + '/table.html'
    form_fields = ['decision']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    decision = models.IntegerField(
        label="How many countries are there in Africa? (Make your best guess)"
    )


def vars_for_template1(player: Player):
    return dict(
        players=[
            p
            for p in player.get_others_in_group()
            if p.id_in_group < player.id_in_group
        ]
    )


# PAGES
class P1(Page):
    form_model = 'player'
    form_fields = Constants.form_fields
    template_name = Constants.main_template

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1

    vars_for_template = vars_for_template1


class WaitPage1(WaitPage):
    pass


class P2(Page):
    form_model = 'player'
    form_fields = Constants.form_fields
    template_name = Constants.main_template

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2

    vars_for_template = vars_for_template1


class WaitPage2(WaitPage):
    pass


class P3(Page):
    form_model = 'player'
    form_fields = Constants.form_fields
    template_name = Constants.main_template

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 3

    vars_for_template = vars_for_template1


class WaitPage3(WaitPage):
    pass


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        return dict(players=group.get_players())


page_sequence = [P1, WaitPage1, P2, WaitPage2, P3, WaitPage3, Results]
