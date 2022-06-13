from otree.api import *

doc = """
group_by_arrival_time: fall back to a smaller group if not enough people show up
"""


class Constants(BaseConstants):
    name_in_url = 'gbat_fallback_smaller_group_part1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


def waiting_seconds(player):
    import time

    participant = player.participant

    wait = int(time.time() - participant.wait_page_arrival)
    print('Player', player.id_in_subsession, 'waiting for', wait, 'seconds')
    return wait


def ranked_waiting_seconds(waiting_players):
    waits = [waiting_seconds(p) for p in waiting_players]
    waits.sort(reverse=True)
    return waits


def group_by_arrival_time_method(subsession, waiting_players):
    print("number of players waiting:", len(waiting_players))

    # ideal case
    if len(waiting_players) >= 4:
        print("Creating a full sized group!")
        return waiting_players[:4]

    waits = ranked_waiting_seconds(waiting_players)
    if len(waits) == 3 and waits[2] > 60:
        print(
            "3 players have been waiting for longer than a minute, "
            "so we settle for a group of 3"
        )
        return waiting_players
    if len(waits) >= 2 and waits[1] > 2 * 60:
        print(
            "2 players have been waiting for longer than 2 minutes, "
            "so we group whoever is available"
        )
        return waiting_players
    # etc...


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    favorite_color = models.StringField(label="What is your favorite color?")


class GBAT(WaitPage):
    group_by_arrival_time = True


class GroupTask(Page):
    form_model = 'player'
    form_fields = ['favorite_color']


class MyWait(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [GBAT, GroupTask, MyWait, Results]
