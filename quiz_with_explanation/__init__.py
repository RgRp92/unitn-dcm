from otree.api import *


doc = """
Quiz with explanation. Re-display the previous page's form as read-only, with answers/explanation.
"""


class Constants(BaseConstants):
    name_in_url = 'quiz_with_explanation'
    players_per_group = None
    num_rounds = 1
    form_template = __name__ + '/form.html'


def get_quiz_data():
    return [
        dict(
            name='a',
            solution=True,
            explanation="2 is prime. It has no factorization other than 1 and itself.",
        ),
        dict(
            name='b',
            solution=False,
            explanation="39 is not prime because it can be factored to 3 * 13.",
        ),
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    a = models.BooleanField(label="Is 2 a prime number?")
    b = models.BooleanField(label="Is 39 a prime number?")


class MyPage(Page):
    form_model = 'player'
    form_fields = ['a', 'b']

    @staticmethod
    def vars_for_template(player: Player):
        fields = get_quiz_data()
        return dict(fields=fields, show_solutions=False)


class Results(Page):
    form_model = 'player'
    form_fields = ['a', 'b']

    @staticmethod
    def vars_for_template(player: Player):
        fields = get_quiz_data()
        # we add an extra key 'is_correct' to each field
        for d in fields:
            d['is_correct'] = getattr(player, d['name']) == d['solution']
        return dict(fields=fields, show_solutions=True)

    @staticmethod
    def error_message(player: Player, values):
        for field in values:
            if getattr(player, field) != values[field]:
                return "A field was somehow changed but this page is read-only."


page_sequence = [MyPage, Results]
