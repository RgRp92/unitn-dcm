from otree.api import *


doc = """
Similar to the basic gbat_treatments app, except:
-   Treatments are balanced rather than independently randomized.
-   The game persists for multiple rounds
"""


class Constants(BaseConstants):
    name_in_url = 'gbat_treatments_complex'
    players_per_group = 2
    num_rounds = 3
    # boolean works when there are 2 treatments
    # if you have >2 treatments, change this to numbers or strings like
    # [1, 2, 3] or ['A', 'B', 'C'], etc.
    treatments = [True, False]


class Subsession(BaseSubsession):
    num_groups_created = models.IntegerField(initial=0)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class GBATWaitPage(WaitPage):
    group_by_arrival_time = True

    @staticmethod
    def is_displayed(player: Player):
        """only do GBAT in the first round. this way, players stay in the same group
        for all rounds."""
        return player.round_number == 1

    @staticmethod
    def after_all_players_arrive(group: Group):
        subsession = group.subsession

        # % is the modulus operator.
        # so when num_groups_created exceeds the max list index,
        # we go back to 0, thus creating a cycle.
        idx = subsession.num_groups_created % len(Constants.treatments)

        treatment = Constants.treatments[idx]
        for p in group.get_players():
            # since we want the treatment to persist for all rounds, we need to assign it
            # in a participant field (which persists across rounds)
            # rather than a group field, which is specific to the round.
            p.participant.time_pressure = treatment

        subsession.num_groups_created += 1


class MyPage(Page):
    pass


page_sequence = [GBATWaitPage, MyPage]
