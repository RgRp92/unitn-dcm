from otree.api import *

doc = """
Timeout spanning multiple pages
"""


class Constants(BaseConstants):
    name_in_url = 'multi_page_timeout'
    players_per_group = None
    num_rounds = 1
    timer_text = "Time to complete this section:"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


def get_timeout_seconds1(player: Player):
    participant = player.participant
    import time

    return participant.expiry - time.time()


def is_displayed1(player: Player):
    return get_timeout_seconds1(player) > 0


class Intro(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        import time

        participant.expiry = time.time() + 60


class Page1(Page):
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = Constants.timer_text


class Page2(Page):
    is_displayed = is_displayed1
    get_timeout_seconds = get_timeout_seconds1
    timer_text = Constants.timer_text


class Page3(Page):
    is_displayed = is_displayed1
    timer_text = Constants.timer_text
    get_timeout_seconds = get_timeout_seconds1


page_sequence = [Intro, Page1, Page2, Page3]
