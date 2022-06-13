
from otree.api import *

import random
import itertools
import json

doc = """
Your app description
"""

#Function
def make_field(label):
    return models.IntegerField(
        choices=[[1,"A"],[2,"B"], [3, "Statusquo"]],
       # choices=[1, 2, 3],
        label=label,
        widget=widgets.RadioSelect,
       # widget=widgets.RadioSelectHorizontal,
    )

#Function




class Subsession(BaseSubsession):
    pass

class Constants(BaseConstants):

    players_per_group = None
    name_in_url = 'DCM_CM'
    tasks = ['A', 'B', 'C']
    num_CE = len(tasks)
    num_rounds = num_CE*2
    quadratic_score_A = 5
    quadratic_score_B = 5
    prob_replace = 0.7


class Group(BaseGroup):

    sum_binding_sit_1 = models.IntegerField(initial=0)
    sum_binding_sit_2 = models.IntegerField(initial=0)
    sum_binding_sit_3 = models.IntegerField(initial=0)
    binding_sit = models.IntegerField(initial =0)

def make_field_prediction(label):
     return models.IntegerField(
        label=label,
        min = 0,
        default=0,
     )



class Player(BasePlayer):

    ##Choices in each choice situation

    CE1_choice = make_field("Choice situation 1")
    CE2_choice = make_field("Choice situation 2")
    CE3_choice = make_field("Choice situation 3")

    ##Prediction of each Choice situtation
    #CE1
    CE1_pred_A = make_field_prediction("CE1_A")
    CE1_pred_B = make_field_prediction("CE1_B")
    CE1_pred_C = make_field_prediction("CE1_C")
    #CE2
    CE2_pred_A = make_field_prediction("CE2_A")
    CE2_pred_B = make_field_prediction("CE2_B")
    CE2_pred_C = make_field_prediction("CE2_C")
    #CE3
    CE3_pred_A = make_field_prediction("CE3_A")
    CE3_pred_B = make_field_prediction("CE3_B")
    CE3_pred_C = make_field_prediction("CE3_C")




#FUNCTION
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:

        for p in subsession.get_players():
            round_numbers = list(range(1, Constants.num_CE + 1 ))
            random.shuffle(round_numbers)
            p.participant.task_rounds = dict(zip(Constants.tasks, round_numbers))
            p.participant.num_players = subsession.session.num_participants
            p.participant.group_pre_A = 0
            p.participant.group_pre_B = 0
            p.participant.group_pre_C = 0
            p.participant.group_elec =0
            p.participant.random_choice = 0


        for w in subsession.get_groups():
            w.binding_sit = random.randint(1,subsession.session.num_participants)

        ##Calculates sum of choices
def set_CE(group):
    for p in group.get_players():
            player1 = p.in_round(p.participant.task_rounds['A'])
            p.participant.CE1_ALL = player1.CE1_choice

            player1 = p.in_round(p.participant.task_rounds['B'])
            p.participant.CE2_ALL = player1.CE2_choice

            player1 = p.in_round(p.participant.task_rounds['C'])
            p.participant.CE3_ALL = player1.CE3_choice


def choice_binding(player,group):
    if group.binding_sit == 1:
        return player.participant.CE1_ALL
    else:
        if group.binding_sit ==2:
            return player.participant.CE2_ALL
        else:
            return player.participant.CE3_ALL

def group_pre_A_(player):
    if player.group.binding_sit == 1:
        player1 = player.in_round(player.participant.task_rounds['A']+ Constants.num_CE)
        return player1.CE1_pred_A

    else:
        if player.group.binding_sit ==2:
            player1 = player.in_round(player.participant.task_rounds['B']+ Constants.num_CE)
            return player1.CE2_pred_A
        else:
            player1 = player.in_round(player.participant.task_rounds['C']+ Constants.num_CE)
            return player1.CE3_pred_A

def group_pre_B_(player):
    if player.group.binding_sit == 1:
        player1 = player.in_round(player.participant.task_rounds['A']+ Constants.num_CE)
        return player1.CE1_pred_B

    else:
        if player.group.binding_sit ==2:
            player1 = player.in_round(player.participant.task_rounds['B']+ Constants.num_CE)
            return player1.CE2_pred_B
        else:
            player1 = player.in_round(player.participant.task_rounds['C']+ Constants.num_CE)
            return player1.CE3_pred_B

def group_pre_C_(player):
    if player.group.binding_sit == 1:
        player1 = player.in_round(player.participant.task_rounds['A']+ Constants.num_CE)
        return player1.CE1_pred_C

    else:
        if player.group.binding_sit ==2:
            player1 = player.in_round(player.participant.task_rounds['B']+ Constants.num_CE)
            return player1.CE2_pred_C
        else:
            player1 = player.in_round(player.participant.task_rounds['C'] + Constants.num_CE)
            return player1.CE3_pred_C

def final_cal(group):

    average_A = [0,0,0]
    average_B = [0,0,0]
    average_C = [0,0,0]
    cont_1=0
    cont_2=0
    cont_3=0
    group1 = group.in_round(1)
    group.binding_sit = group1.binding_sit

    for p in group.get_players():


           p.participant.group_elec = choice_binding(p, group)

           group.sum_binding_sit_1 = p.participant.group_elec* (p.participant.group_elec == 1) + group.sum_binding_sit_1
           group.sum_binding_sit_2 = int(p.participant.group_elec * (p.participant.group_elec == 2) / 2 )+ group.sum_binding_sit_2
           group.sum_binding_sit_3 = int( p.participant.group_elec * (p.participant.group_elec == 3) / 3) + group.sum_binding_sit_3

           if p.participant.group_elec == 1:
               average_A[0]= group_pre_A_(p) + average_A[0]
               average_B[0] = group_pre_B_(p) + average_B[0]
               average_C[0] = group_pre_C_(p) + average_C[0]
               cont_1 = cont_1 + 1
           else:
               if p.participant.group_elec == 2:
                   average_A[1] = group_pre_A_(p) + average_A[1]
                   average_B[1] = group_pre_B_(p) + average_B[1]
                   average_C[1] = group_pre_C_(p) + average_C[1]
                   cont_2 = cont_2 + 1
               else:
                   average_A[2] = group_pre_A_(p) + average_A[2]
                   average_B[2] = group_pre_B_(p) + average_B[2]
                   average_C[2] = group_pre_C_(p) + average_C[2]
                   cont_3 = cont_3 + 1

    for p in group.get_players():
          if p.participant.group_elec == 1:
              p.participant.group_pre_A = average_A[0]/cont_1
              p.participant.group_pre_B =  average_B[0]/cont_1
              p.participant.group_pre_C =  average_C[0]/cont_1
          else:
              if p.participant.group_elec == 2:
                  p.participant.group_pre_A = average_A[1] / cont_2
                  p.participant.group_pre_B = average_B[1] / cont_2
                  p.participant.group_pre_C = average_C[1] / cont_2
              else:
                  p.participant.group_pre_A = average_A[2] / cont_3
                  p.participant.group_pre_B = average_B[2] / cont_3
                  p.participant.group_pre_C = average_C[2] / cont_3



def payoffs(replace_pred, player):
    if replace_pred == 0:
           Pred_A = group_pre_A_(player)/ player.participant.num_players
           Pred_B = group_pre_B_(player)/ player.participant.num_players
           Pred_C = group_pre_C_(player)/ player.participant.num_players
           factor1 = Pred_A * Pred_A + Pred_B * Pred_B + Pred_C * Pred_C
           payoff_a = Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_A - factor1)
           payoff_b = Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_B - factor1)
           payoff_c = Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_C - factor1)

           Pred_A = Pred_A* player.participant.num_players
           Pred_B = Pred_B* player.participant.num_players
           Pred_C = Pred_C* player.participant.num_players

           payoffs = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c, pred_a = Pred_A,
                          pred_c = Pred_C, pred_b = Pred_B)
    else:
        Pred_A = player.participant.group_pre_A/ player.participant.num_players
        Pred_B = player.participant.group_pre_B/ player.participant.num_players
        Pred_C = player.participant.group_pre_C/ player.participant.num_players
        factor1 = Pred_A * Pred_A + Pred_B * Pred_B + Pred_C * Pred_C
        payoff_a = Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_A - factor1)
        payoff_b = Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_B - factor1)
        payoff_c = Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_C - factor1)
        Pred_A = Pred_A * player.participant.num_players
        Pred_B = Pred_B * player.participant.num_players
        Pred_C = Pred_C * player.participant.num_players

        payoffs = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c,pred_a = Pred_A,
                          pred_c = Pred_C, pred_b = Pred_B)
    return  payoffs



# PAGES
class CE1(Page):
    form_model = 'player'
    form_fields = ['CE1_choice']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['A']


class CE2(Page):
    form_model = 'player'
    form_fields = ['CE2_choice']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['B']


class CE3(Page):
    form_model = 'player'
    form_fields = ['CE3_choice']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['C']


class Wait_CE(WaitPage):
    after_all_players_arrive = set_CE
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number ==  Constants.num_CE


class Pred_CE1(Page):
    form_model = 'player'
    form_fields = ['CE1_pred_A','CE1_pred_B','CE1_pred_C']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['A'] + Constants.num_CE

    @staticmethod
    def live_method(player: Player, data):
        if data['clicked_button'] == 1:
            a= float(data['fieldA'])/player.participant.num_players
            b = float(data['fieldB'])/player.participant.num_players
            c = float(data['fieldC'])/player.participant.num_players
            factor1 = a*a + b*b + c*c
            payoff_a = Constants.quadratic_score_A + Constants.quadratic_score_B*(2*a - factor1)
            payoff_b = Constants.quadratic_score_A + Constants.quadratic_score_B*(2*b - factor1)
            payoff_c = Constants.quadratic_score_A + Constants.quadratic_score_B*(2*c - factor1)
            response = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c)
            return{player.id_in_group: response }

#Passing data from Python to JavaScript (js_vars)
    @staticmethod
    def js_vars(player):
        return dict(number_players = player.participant.num_players,tempA=0,tempB=0,tempC=0)

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['CE1_pred_A'] + values['CE1_pred_B'] + values['CE1_pred_C'] != player.participant.num_players:
          return 'Sum of predictions has to be equal to  '  + str(player.participant.num_players)

class Pred_CE2(Page):
    form_model = 'player'
    form_fields = ['CE2_pred_A', 'CE2_pred_B', 'CE2_pred_C']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['B'] + Constants.num_CE

    @staticmethod
    def live_method(player: Player, data):
        if data['clicked_button'] == 1:
            a = float(data['fieldA']) / player.participant.num_players
            b = float(data['fieldB']) / player.participant.num_players
            c = float(data['fieldC']) / player.participant.num_players
            factor1 = a * a + b * b + c * c
            payoff_a = Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * a - factor1)
            payoff_b = Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * b - factor1)
            payoff_c = Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * c - factor1)
            response = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c)
            return {player.id_in_group: response}

        # Passing data from Python to JavaScript (js_vars)
    @staticmethod
    def js_vars(player):
            return dict(number_players=player.participant.num_players, tempA=0, tempB=0, tempC=0)

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['CE2_pred_A'] + values['CE2_pred_B'] + values['CE2_pred_C'] !=  player.participant.num_players:
          return 'Sum of predictions has to be equal to  '  +  str(player.participant.num_players)


class Pred_CE3(Page):
    form_model = 'player'
    form_fields = ['CE3_pred_A', 'CE3_pred_B', 'CE3_pred_C']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['C'] + Constants.num_CE


    @staticmethod
    def live_method(player: Player, data):
            if data['clicked_button'] == 1:
                a = float(data['fieldA']) / player.participant.num_players
                b = float(data['fieldB']) / player.participant.num_players
                c = float(data['fieldC']) / player.participant.num_players
                factor1 = a * a + b * b + c * c
                payoff_a = Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * a - factor1)
                payoff_b = Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * b - factor1)
                payoff_c = Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * c - factor1)
                response = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c)
                return {player.id_in_group: response}

        # Passing data from Python to JavaScript (js_vars)
    @staticmethod
    def js_vars(player):
            return dict(number_players=player.participant.num_players, tempA=0, tempB=0, tempC=0)

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['CE3_pred_A'] + values['CE3_pred_B'] + values['CE3_pred_C'] !=  player.participant.num_players:
          return 'Sum of predictions has to be equal to  '  + str(player.participant.num_players)\

    @staticmethod
    def vars_for_template(player):
        return dict( a=0,  b=0,c=0,)

class Wait_CE2(WaitPage):
    after_all_players_arrive = final_cal
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number ==  Constants.num_CE*2

class Show_bindingsit(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number ==  Constants.num_CE*2

    @staticmethod
    def vars_for_template(player):
        return dict(a=player.group.binding_sit )

class Results(Page):
    @staticmethod
    def live_method(player: Player, data):
        if data['clicked_button'] == 1:
            random_num = random.random()
            list_choices = [1] * player.group.sum_binding_sit_1 + [2] * player.group.sum_binding_sit_2 + [
                3] * player.group.sum_binding_sit_3
            player.participant.random_choice = random.choice(list_choices)
            random_choice = player.participant.random_choice
            if random_num <= Constants.prob_replace:
                replace_pred = 1

            else:
                replace_pred = 0

            payoff_set = payoffs(replace_pred, player)
            if random_choice == 1:
                player.payoff = payoff_set['payoff_a']
            else:
                if random_choice == 2:
                    player.payoff = payoff_set['payoff_b']

                else:
                    player.payoff = payoff_set['payoff_c']

            response = dict(replace_pred=replace_pred, payoff_a=payoff_set['payoff_a'],
                            payoff_b=payoff_set['payoff_b'], payoff_c=payoff_set['payoff_c'], finalpayoff=player.payoff,
                            pred_a=payoff_set['pred_a'], pred_c=payoff_set['pred_c'], pred_b=payoff_set['pred_b'],
                            round=1)

            return {player.id_in_group: response}
        else:
            if data['clicked_button'] == 2:
                response = dict(random_choice=player.participant.random_choice, finalpayoff=player.participant.payoff,
                                round=2)
                return {player.id_in_group: response}


    @staticmethod
    def is_displayed(player: Player):
        return player.round_number ==  Constants.num_CE*2


#def custom_export(players: Player):
#    # header row
#    yield ['session', 'participant_code','participant_CE1', 'round_number', 'id_in_group', 'payoff']
#    for p in players:
#        participant = p.participant
#        session = p.session
#        yield [session.code, participant.code, participant.CE1_ALL, p.round_number, p.id_in_group, p.payoff]


page_sequence = [CE1, CE2, CE3, Wait_CE, Pred_CE1,  Pred_CE2, Pred_CE3,Wait_CE2,Show_bindingsit,Results]
