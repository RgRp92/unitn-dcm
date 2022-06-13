from otree.api import *

doc = """
Simple version of comprehension test
"""


class Constants(BaseConstants):
    name_in_url = 'comprehension_test_simple'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    quiz1 = models.IntegerField(label='What is 2 + 2?')
    quiz2 = models.IntegerField(label="What year did COVID-19 start?")
    quiz3 = models.BooleanField(label="Is 9 a prime number?")


class MyPage(Page):
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2', 'quiz3']

    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(quiz1=4, quiz2=2019, quiz3=False)

        if values != solutions:
            return "One or more answers were incorrect."


class Results(Page):
    pass


page_sequence = [MyPage, Results]
