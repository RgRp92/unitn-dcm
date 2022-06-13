from otree.api import *


doc = """
Select a random round for payment
"""


class Constants(BaseConstants):
    name_in_url = 'pay_random_round'
    players_per_group = None
    num_rounds = 4
    endowment = cu(100)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    give_amount = models.CurrencyField(
        min=0, max=100, label="How much do you want to give?"
    )


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['give_amount']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import random

        participant = player.participant

        if player.round_number == Constants.num_rounds:
            random_round = random.randint(1, Constants.num_rounds)
            participant.selected_round = random_round
            player_in_selected_round = player.in_round(random_round)
            player.payoff = Constants.endowment - player_in_selected_round.give_amount


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds


page_sequence = [MyPage, Results]
