from otree.api import *

doc = """Randomize multiple factors in a balanced way"""


class Constants(BaseConstants):
    name_in_url = 'randomize_cross_product'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    import itertools

    treatments = itertools.cycle(
        itertools.product([True, False], [True, False], [100, 200, 300])
    )
    for p in subsession.get_players():
        treatment = next(treatments)
        p.time_pressure = treatment[0]
        p.high_tax = treatment[1]
        p.endowment = treatment[2]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    time_pressure = models.BooleanField()
    high_tax = models.BooleanField()
    endowment = models.CurrencyField()


class MyPage(Page):
    pass


page_sequence = [MyPage]
