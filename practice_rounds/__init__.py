from otree.api import *


doc = """Practice rounds"""


class Constants(BaseConstants):
    name_in_url = 'practice_rounds'
    players_per_group = None
    num_practice_rounds = 2
    num_real_rounds = 10
    num_rounds = num_practice_rounds + num_real_rounds


class Subsession(BaseSubsession):
    is_practice_round = models.BooleanField()
    real_round_number = models.IntegerField()


def creating_session(subsession: Subsession):
    subsession.is_practice_round = (
        subsession.round_number <= Constants.num_practice_rounds
    )
    if not subsession.is_practice_round:
        subsession.real_round_number = (
            subsession.round_number - Constants.num_practice_rounds
        )


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    response = models.IntegerField()
    solution = models.IntegerField()
    is_correct = models.BooleanField()


class Play(Page):
    form_model = 'player'
    form_fields = ['response']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        # the **2 is just an example used in this game (squaring a number)
        player.solution = player.round_number ** 2

        player.is_correct = player.response == player.solution


class PracticeFeedback(Page):
    @staticmethod
    def is_displayed(player: Player):
        subsession = player.subsession
        return subsession.is_practice_round


class Results(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == Constants.num_rounds

    @staticmethod
    def vars_for_template(player: Player):
        score = 0
        for p in player.in_rounds(
            Constants.num_practice_rounds + 1, Constants.num_rounds
        ):
            score += p.is_correct
        return dict(score=score)


page_sequence = [Play, PracticeFeedback, Results]
