from otree.api import *

doc = """Timeout on a WaitPage (exit the experiment)"""

class Constants(BaseConstants):
    name_in_url = 'wait_page_timeout'
    players_per_group = None
    num_rounds = 1
    timeout = 15


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    import random

    for p in subsession.get_players():
        p.completion_code = random.randint(10 ** 6, 10 ** 7)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    timeout = models.FloatField()
    completion_code = models.IntegerField()


# PAGES
class MyPage(Page):
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        import time

        # 15 seconds on wait page max
        player.timeout = time.time() + Constants.timeout


class ResultsWaitPage(WaitPage):
    template_name = 'wait_page_timeout/ResultsWaitPage.html'

    @staticmethod
    def js_vars(player: Player):
        return dict(timeout=Constants.timeout)

    @staticmethod
    def vars_for_template(player: Player):
        import time

        timeout_happened = time.time() > player.timeout
        return dict(timeout_happened=timeout_happened)


class Task(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Task]
