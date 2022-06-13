
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
    tasks = ['1', '2', '3','4','5','6','7','8','9']
    num_CE = len(tasks)
    ###practice test####
    random_practice_choice_sit = random.randint(1, num_CE)
    num_rounds = num_CE*2
    quadratic_score_A = 5
    quadratic_score_B = 5
    prob_replace = 0.75
    prob_not_replace = 0.25
    max_num_try = 5 # Maximum number of tries practice test
    level1_cost =5
    level2_cost = 10
    level3_cost = 15
    level4_cost = 20
    # num_lottery=7

class Group(BaseGroup):

    sum_binding_sit_1 = models.IntegerField(initial=0)
    sum_binding_sit_2 = models.IntegerField(initial=0)
    sum_binding_sit_3 = models.IntegerField(initial=0)
    binding_sit = models.IntegerField(initial=0)
    #  bindinglottery = models.IntegerField(initial=0)
    #  bindinglotterygame = models.IntegerField(initial=0)

#def make_field_lottery(label):
    #   return models.StringField(
    #      label=label
#  )


def make_field_prediction(label):
    return models.IntegerField(
        label=label,
        min=0,
        default=0,
    )
class Player(BasePlayer):
    ##Practice choice situation
   # prob_replace =  models.FloatField(min=0,max=1)
  #  prob_not_replace =  models.FloatField(min=0,max=1)
 #   Test_choices_A_prob =  models.IntegerField(min=0,max=1)
 #   Test_choices_B_prob =  models.IntegerField(min=0,max=1)
 #   Test_choices_C_prob =  models.IntegerField(min=0,max=1)
  #  payoff_A_guess  = models.FloatField()
  #  payoff_B_guess = models.FloatField()
  #  payoff_C_guess = models.FloatField()


    ##Choices in each choice situation
    CE_choice_practice = make_field("Practice Choice situation")
    CE1_choice = make_field("Choice situation 1")
    CE2_choice = make_field("Choice situation 2")
    CE3_choice = make_field("Choice situation 3")
    CE4_choice = make_field("Choice situation 4")
    CE5_choice = make_field("Choice situation 5")
    CE6_choice = make_field("Choice situation 6")
    CE7_choice = make_field("Choice situation 7")
    CE8_choice = make_field("Choice situation 8")
    CE9_choice = make_field("Choice situation 9")

    ##Prediction of each Choice situtation
    # Practice CE
    CE_pract_pred_A = make_field_prediction("CE_prac_A")
    CE_pract_pred_B = make_field_prediction("CE_prac_A")
    CE_pract_pred_C = make_field_prediction("CE_prac_B")
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
    # CE3
    CE4_pred_A = make_field_prediction("CE4_A")
    CE4_pred_B = make_field_prediction("CE4_B")
    CE4_pred_C = make_field_prediction("CE4_C")
    # CE3
    CE5_pred_A = make_field_prediction("CE5_A")
    CE5_pred_B = make_field_prediction("CE5_B")
    CE5_pred_C = make_field_prediction("CE5_C")
    # CE3
    CE6_pred_A = make_field_prediction("CE6_A")
    CE6_pred_B = make_field_prediction("CE6_B")
    CE6_pred_C = make_field_prediction("CE6_C")
    # CE6
    CE7_pred_A = make_field_prediction("CE7_A")
    CE7_pred_B = make_field_prediction("CE7_B")
    CE7_pred_C = make_field_prediction("CE7_C")
    # CE8
    CE8_pred_A = make_field_prediction("CE8_A")
    CE8_pred_B = make_field_prediction("CE8_B")
    CE8_pred_C = make_field_prediction("CE8_C")
    # CE9
    CE9_pred_A = make_field_prediction("CE9_A")
    CE9_pred_B = make_field_prediction("CE9_B")
    CE9_pred_C = make_field_prediction("CE9_C")

    ##tari
    TARI =  models.FloatField(
        label="TAX",
        min=0,
        default=0,
    )

    ##LOTERY
    # Q1 = make_field_lottery("Q1")
    # Q2 = make_field_lottery("Q2")
    # Q3 = make_field_lottery("Q3")
    # Q4 = make_field_lottery("Q4")
    # Q5 = make_field_lottery("Q5")
    # Q6 = make_field_lottery("Q6")
    # Q7 = make_field_lottery("Q7")
    #  Q8 = make_field_lottery("Q8")
    #  Q9 = make_field_lottery("Q9")
    # played_lottery = models.StringField(initial="A")



#FUNCTION
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        subsession.session.other_part = subsession.session.num_participants-1
        subsession.session.random_prediction_A = random.randint(0, subsession.session.num_participants - 1)

        if subsession.session.random_prediction_A < (subsession.session.num_participants - 1):
            subsession.session.random_prediction_B = random.randint(0, subsession.session.num_participants - 1 - subsession.session.random_prediction_A)

        else:
            subsession.session.random_prediction_B = 0



        subsession.session.random_prediction_C = subsession.session.num_participants- 1 - subsession.session.random_prediction_A - subsession.session.random_prediction_B
        subsession.session.random_prediction_A_2 = random.randint(
            int(round((subsession.session.num_participants - 1) * 0.2, 0)),
            int(round((subsession.session.num_participants - 1) * 0.4, 0)))
        subsession.session.random_prediction_B_2 = random.randint(
            int(round((subsession.session.num_participants - 1) * 0.2, 0)),
            (int(round((subsession.session.num_participants - 1) * 0.4, 0))))
        subsession.session.random_prediction_C_2 = subsession.session.num_participants - 1 - subsession.session.random_prediction_A_2 - subsession.session.random_prediction_B_2
        subsession.session.random_ball_not_replaced = random.randint(0,Constants.prob_not_replace*100)
        subsession.session.random_ball_replaced = random.randint(Constants.prob_not_replace*100,100)
        if subsession.session.random_prediction_C_2 < 0:
            subsession.session.random_prediction_C_2 = 0

        list_choices_A_temp = " ".join(['A'] * (subsession.session.random_prediction_A_2 ))
        list_choices_B_temp = " ".join(['B'] * (subsession.session.random_prediction_B_2 ))
        list_choices_C_temp = " ".join(['C'] * (subsession.session.random_prediction_C_2 ))



        choices_str = list_choices_A_temp  + ' ' +      list_choices_B_temp + ' ' +  list_choices_C_temp
        list_choices = choices_str.split()

        subsession.session.chosen_letter_2 = random.choice(list_choices)
        listA_2 = []
        rnd = random.sample(list(range(1,subsession.session.num_participants)), subsession.session.random_prediction_A_2)
        example_prediction_average_A = []
        example_prediction_average_B = []
        example_prediction_average_C = []
        for i in range(0, subsession.session.random_prediction_A_2):
            n_t = int(rnd[i])
            if i == subsession.session.random_prediction_A_2 - 1:
                n = str(n_t) + "."
            else:
                n = str(n_t) + ","
            listA_2.append(n)

            example_prediction_average_A_temp = random.randint(
                int(round((subsession.session.num_participants - 1) * 0.2, 0)),
                int(round((subsession.session.num_participants - 1) * 0.7, 0)))

            example_prediction_average_B_temp = random.randint(
                int(round((subsession.session.num_participants - 1) * 0.2, 0)),
                (int(round((subsession.session.num_participants - 1) * 0.7, 0))))
            if example_prediction_average_B_temp + example_prediction_average_A_temp >= subsession.session.num_participants - 1:
                example_prediction_average_B_temp= subsession.session.num_participants - 1 - example_prediction_average_A_temp
                example_prediction_average_C_temp = 0
            else:
                example_prediction_average_C_temp =  subsession.session.num_participants - 1 - example_prediction_average_A_temp - example_prediction_average_B_temp

            example_prediction_average_A.append(example_prediction_average_A_temp)
            example_prediction_average_B.append(example_prediction_average_B_temp)
            example_prediction_average_C.append(example_prediction_average_C_temp)

        subsession.session.example_prediction_average_A= example_prediction_average_A
        subsession.session.example_prediction_average_B = example_prediction_average_B
        subsession.session.example_prediction_average_C = example_prediction_average_C
        subsession.session.listA_2 = listA_2

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
            p.participant.Test_choices_A = random.randint(0, subsession.session.other_part)
            p.participant.Test_choices_B = random.randint(0,subsession.session.other_part - p.participant.Test_choices_A)
            p.participant.Test_choices_C = subsession.session.other_part -p.participant.Test_choices_B - p.participant.Test_choices_A
            p.participant.Test_choices_A_pred = round(random.random()*subsession.session.other_part,2)
            p.participant.Test_choices_B_pred = round(random.random()*(subsession.session.other_part-p.participant.Test_choices_A_pred),2)
            p.participant.Test_choices_C_pred = subsession.session.other_part - p.participant.Test_choices_A_pred - p.participant.Test_choices_B_pred

            Pred_A = p.participant.Test_choices_A_pred/ subsession.session.other_part
            Pred_B =  p.participant.Test_choices_B_pred / subsession.session.other_part
            Pred_C =  p.participant.Test_choices_C_pred  / subsession.session.other_part
            factor1 = Pred_A * Pred_A + Pred_B * Pred_B + Pred_C * Pred_C
            p.participant.Test_payoff_a_pred = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_A - factor1),2)
            p.participant.Test_payoff_b_pred = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_B - factor1),2)
            p.participant.Test_payoff_c_pred = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_C - factor1),2)

            p.participant.num_prob_replace = 1
            p.participant.num_prob_not_replace = 1
            p.participant.num_Test_choices_A_prob = 1
            p.participant.num_Test_choices_B_prob = 1
            p.participant.num_Test_choices_C_prob= 1
            p.participant.num_payoff_A_guess= 1
            p.participant.num_payoff_B_guess= 1
            p.participant.num_payoff_C_guess= 1
            p.participant.num_Test_choices_A_pred = 1
            p.participant.num_Test_choices_B_pred = 1
            p.participant.num_Test_choices_C_pred = 1
            p.participant.num_Test_payoff_a_pred = 1
            p.participant.num_Test_payoff_b_pred = 1
            p.participant.num_Test_payoff_c_pred = 1

        for w in subsession.get_groups():
            w.binding_sit = random.randint(1,subsession.session.num_participants)


        ##Calculates sum of choices

def set_CE(group):
    for p in group.get_players():
            player1 = p.in_round(p.participant.task_rounds['1'])
            p.participant.CE1_ALL = player1.CE1_choice

            player1 = p.in_round(p.participant.task_rounds['2'])
            p.participant.CE2_ALL = player1.CE2_choice

            player1 = p.in_round(p.participant.task_rounds['3'])
            p.participant.CE3_ALL = player1.CE3_choice

            player1 = p.in_round(p.participant.task_rounds['4'])
            p.participant.CE4_ALL = player1.CE4_choice

            player1 = p.in_round(p.participant.task_rounds['5'])
            p.participant.CE5_ALL = player1.CE5_choice

            player1 = p.in_round(p.participant.task_rounds['6'])
            p.participant.CE6_ALL = player1.CE6_choice

            player1 = p.in_round(p.participant.task_rounds['7'])
            p.participant.CE7_ALL = player1.CE7_choice

            player1 = p.in_round(p.participant.task_rounds['8'])
            p.participant.CE8_ALL = player1.CE8_choice

            player1 = p.in_round(p.participant.task_rounds['9'])
            p.participant.CE9_ALL = player1.CE9_choice

            


def choice_binding(player,group):
    if group.binding_sit == 1:
        return player.participant.CE1_ALL
    if group.binding_sit ==2:
        return player.participant.CE2_ALL
    if group.binding_sit == 3:
        return player.participant.CE3_ALL
    if group.binding_sit == 4:
        return player.participant.CE4_ALL
    if group.binding_sit == 5:
        return player.participant.CE5_ALL

    if group.binding_sit == 6:
        return player.participant.CE6_ALL

    if group.binding_sit == 7:
        return player.participant.CE7_ALL

    if group.binding_sit == 8:
        return player.participant.CE8_ALL

    if group.binding_sit == 9:
        return player.participant.CE9_ALL


def group_pre_A_(player):
    if player.group.binding_sit == 1:
        player1 = player.in_round(player.participant.task_rounds['1']+ Constants.num_CE)
        return player1.CE1_pred_A
    if player.group.binding_sit == 2:
        player1 = player.in_round(player.participant.task_rounds['2']+ Constants.num_CE)
        return player1.CE2_pred_A
    if player.group.binding_sit == 3:
        player1 = player.in_round(player.participant.task_rounds['3']+ Constants.num_CE)
        return player1.CE3_pred_A
    if player.group.binding_sit == 4:
        player1 = player.in_round(player.participant.task_rounds['4']+ Constants.num_CE)
        return player1.CE4_pred_A
    if player.group.binding_sit == 5:
        player1 = player.in_round(player.participant.task_rounds['5']+ Constants.num_CE)
        return player1.CE5_pred_A
    if player.group.binding_sit == 5:
        player1 = player.in_round(player.participant.task_rounds['5']+ Constants.num_CE)
        return player1.CE5_pred_A
    if player.group.binding_sit == 6:
        player1 = player.in_round(player.participant.task_rounds['6']+ Constants.num_CE)
        return player1.CE6_pred_A
    if player.group.binding_sit == 7:
        player1 = player.in_round(player.participant.task_rounds['7']+ Constants.num_CE)
        return player1.CE7_pred_A
    if player.group.binding_sit == 8:
        player1 = player.in_round(player.participant.task_rounds['8']+ Constants.num_CE)
        return player1.CE8_pred_A
    if player.group.binding_sit == 9:
        player1 = player.in_round(player.participant.task_rounds['9']+ Constants.num_CE)
        return player1.CE9_pred_A

def group_pre_B_(player):
    if player.group.binding_sit == 1:
        player1 = player.in_round(player.participant.task_rounds['1']+ Constants.num_CE)
        return player1.CE1_pred_B
    if player.group.binding_sit ==2:
        player1 = player.in_round(player.participant.task_rounds['2']+ Constants.num_CE)
        return player1.CE2_pred_B
    if player.group.binding_sit ==3:
        player1 = player.in_round(player.participant.task_rounds['3']+ Constants.num_CE)
        return player1.CE3_pred_B
    if player.group.binding_sit ==4:
        player1 = player.in_round(player.participant.task_rounds['4']+ Constants.num_CE)
        return player1.CE4_pred_B
    if player.group.binding_sit ==5:
        player1 = player.in_round(player.participant.task_rounds['5']+ Constants.num_CE)
        return player1.CE5_pred_B
    if player.group.binding_sit ==6:
        player1 = player.in_round(player.participant.task_rounds['6']+ Constants.num_CE)
        return player1.CE6_pred_B
    if player.group.binding_sit ==7:
        player1 = player.in_round(player.participant.task_rounds['7']+ Constants.num_CE)
        return player1.CE7_pred_B
    if player.group.binding_sit ==8:
        player1 = player.in_round(player.participant.task_rounds['8']+ Constants.num_CE)
        return player1.CE8_pred_B
    if player.group.binding_sit ==9:
        player1 = player.in_round(player.participant.task_rounds['9']+ Constants.num_CE)
        return player1.CE9_pred_B
        

def group_pre_C_(player):
    if player.group.binding_sit == 1:
        player1 = player.in_round(player.participant.task_rounds['1']+ Constants.num_CE)
        return player1.CE1_pred_C
    if player.group.binding_sit ==2:
        player1 = player.in_round(player.participant.task_rounds['2']+ Constants.num_CE)
        return player1.CE2_pred_C
    if player.group.binding_sit ==3:
        player1 = player.in_round(player.participant.task_rounds['3']+ Constants.num_CE)
        return player1.CE3_pred_C
    if player.group.binding_sit ==4:
        player1 = player.in_round(player.participant.task_rounds['4']+ Constants.num_CE)
        return player1.CE4_pred_C
    if player.group.binding_sit ==5:
        player1 = player.in_round(player.participant.task_rounds['5']+ Constants.num_CE)
        return player1.CE5_pred_C
    if player.group.binding_sit ==6:
        player1 = player.in_round(player.participant.task_rounds['6']+ Constants.num_CE)
        return player1.CE6_pred_C
    if player.group.binding_sit ==7:
        player1 = player.in_round(player.participant.task_rounds['7']+ Constants.num_CE)
        return player1.CE7_pred_C
    if player.group.binding_sit ==8:
        player1 = player.in_round(player.participant.task_rounds['8']+ Constants.num_CE)
        return player1.CE8_pred_C
    if player.group.binding_sit ==9:
        player1 = player.in_round(player.participant.task_rounds['9']+ Constants.num_CE)
        return player1.CE9_pred_C
 

def final_cal(group):

    SUM_A = [0,0,0]
    SUM_B = [0,0,0]
    SUM_C = [0,0,0]
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
               SUM_A[0]= group_pre_A_(p) + SUM_A[0]
               SUM_B[0] = group_pre_B_(p) + SUM_B[0]
               SUM_C[0] = group_pre_C_(p) + SUM_C[0]
               cont_1 = cont_1 + 1

           else:
               if p.participant.group_elec == 2:
                   SUM_A[1] = group_pre_A_(p) + SUM_A[1]
                   SUM_B[1] = group_pre_B_(p) + SUM_B[1]
                   SUM_C[1] = group_pre_C_(p) + SUM_C[1]
                   cont_2 = cont_2 + 1

               else:
                   SUM_A[2] = group_pre_A_(p) + SUM_A[2]
                   SUM_B[2] = group_pre_B_(p) + SUM_B[2]
                   SUM_C[2] = group_pre_C_(p) + SUM_C[2]
                   cont_3 = cont_3 + 1


    for p in group.get_players():
          if p.participant.group_elec == 1:
              p.participant.group_pre_A_sum = SUM_A[0]
              p.participant.group_pre_B_sum =  SUM_B[0]
              p.participant.group_pre_C_sum =  SUM_C[0]
              p.participant.group_pre_cont = cont_1
              p.participant.list_choices_A = " ".join( ['A'] * (group.sum_binding_sit_1 - 1))
              p.participant.list_choices_B = " ".join(['B'] * (group.sum_binding_sit_2 ))
              p.participant.list_choices_C = " ".join(['C'] * (group.sum_binding_sit_3))

          else:
              if p.participant.group_elec == 2:
                  p.participant.group_pre_A_sum = SUM_A[1]
                  p.participant.group_pre_B_sum = SUM_B[1]
                  p.participant.group_pre_C_sum = SUM_C[1]
                  p.participant.group_pre_cont = cont_2
                  p.participant.list_choices_A = " ".join(['A'] * (group.sum_binding_sit_1))
                  p.participant.list_choices_B = " ".join(['B'] * (group.sum_binding_sit_2-1))
                  p.participant.list_choices_C = " ".join(['C'] * (group.sum_binding_sit_3))

              else:
                  p.participant.group_pre_A_sum = SUM_A[2]
                  p.participant.group_pre_B_sum = SUM_B[2]
                  p.participant.group_pre_C_sum = SUM_C[2]
                  p.participant.group_pre_cont = cont_3
                  p.participant.list_choices_A = " ".join(['A'] * (group.sum_binding_sit_1))
                  p.participant.list_choices_B = " ".join(['B'] * (group.sum_binding_sit_2))
                  p.participant.list_choices_C = " ".join(['C'] * (group.sum_binding_sit_3-1))

#def lottery_number(group):

    #   group.bindinglottery =   random.randint(0, Constants.num_lottery-1)
    #group.bindinglotterygame = random.randint(1, 10)

    #for p in group.get_players():
          #    temp =  [p.in_round(1).Q1,p.in_round(1).Q2,p.in_round(1).Q3,p.in_round(1).Q4,p.in_round(1).Q5,p.in_round(1).Q6,p.in_round(1).Q7]
         #p.in_round(1).played_lottery =temp[group.bindinglottery]




def payoffs(replace_pred, player):
    own_prediction_A= group_pre_A_(player)
    own_prediction_B = group_pre_B_(player)
    own_prediction_C = group_pre_C_(player)
    if replace_pred == 0:
           Pred_A =own_prediction_A/ (player.participant.num_players - 1)
           Pred_B = own_prediction_B/ (player.participant.num_players - 1)
           Pred_C =own_prediction_C/ (player.participant.num_players - 1)
           factor1 = Pred_A * Pred_A + Pred_B * Pred_B + Pred_C * Pred_C
           payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_A - factor1),2)
           payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_B - factor1),2)
           payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_C - factor1),2)


           payoffs = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c, pred_a = own_prediction_A,
                          pred_c = own_prediction_C, pred_b = own_prediction_B, error = False)
    else:
        if player.participant.group_pre_cont ==1 :
           payoffs = dict( error = True)
        else:
           Pred_A = ((player.participant.group_pre_A_sum -  own_prediction_A)/
                  (player.participant.group_pre_cont -1))/ (player.participant.num_players - 1)
           Pred_B = ((player.participant.group_pre_B_sum -  own_prediction_B)/
                  (player.participant.group_pre_cont -1))/ (player.participant.num_players - 1)
           Pred_C = ((player.participant.group_pre_C_sum -  own_prediction_C)/
                  (player.participant.group_pre_cont -1))/ (player.participant.num_players - 1)
           factor1 = Pred_A * Pred_A + Pred_B * Pred_B + Pred_C * Pred_C
           payoff_a =  round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_A - factor1),2)
           payoff_b =  round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_B - factor1),2)
           payoff_c =  round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_C - factor1),2)
           Pred_A = Pred_A * (player.participant.num_players - 1)
           Pred_B = Pred_B * (player.participant.num_players - 1)
           Pred_C = Pred_C * (player.participant.num_players - 1)

           payoffs = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c,pred_a = Pred_A,
                          pred_c = Pred_C, pred_b = Pred_B,  error = False)
    return  payoffs



# PAGES
# PAGES

#class Lottery_serie_1(Page):
#  form_model = 'player'
    #  form_fields = ['Q1','Q2','Q3','Q4','Q5','Q6','Q7']
    #  @staticmethod
    #  def is_displayed(player: Player):
#  participant = player.participant
        #  return player.round_number == 1


# class Wait_lottery(WaitPage):
    #   after_all_players_arrive = lottery_number
    # @staticmethod
    # def is_displayed(player: Player):
#   return player.round_number == 1


# class Results_lottery(Page):

    #   @staticmethod
    # def is_displayed(player: Player):
#   return player.round_number ==  1





class Practice_CE(Page):
    form_model = 'player'
    form_fields = ['CE_choice_practice']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Practice_Pred_CE(Page):
    form_model = 'player'
    form_fields = ['CE_pract_pred_A','CE_pract_pred_B','CE_pract_pred_C']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def live_method(player: Player, data):
        if data['clicked_button'] == 1:
            a= float(data['fieldA'])/(player.participant.num_players - 1)
            b = float(data['fieldB'])/(player.participant.num_players - 1)
            c = float(data['fieldC'])/(player.participant.num_players - 1)
            factor1 = a*a + b*b + c*c
            payoff_a =  round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*a - factor1),2)
            payoff_b =  round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*b - factor1),2)
            payoff_c =  round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*c - factor1),2)
            response = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c)
            player.participant.payoff_practice_A = payoff_a
            player.participant.payoff_practice_B = payoff_b
            player.participant.payoff_practice_C = payoff_c
            return{player.id_in_group: response }

#Passing data from Python to JavaScript (js_vars)
    @staticmethod
    def js_vars(player):
        return dict(number_players = player.participant.num_players,tempA=0,tempB=0,tempC=0)

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['CE_pract_pred_A'] + values['CE_pract_pred_B'] + values['CE_pract_pred_C'] != (player.participant.num_players- 1):
          return 'Sum of predictions has to be equal to  '  + str(player.participant.num_players- 1)

class Practice_payoff1(Page):

   # form_fields = ['Test_choices_A_prob','Test_choices_B_prob','Test_choices_C_prob',
   #                'prob_replace','prob_not_replace','payoff_A_guess','payoff_B_guess','payoff_C_guess',]
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def live_method(player: Player, data):
        if data['clicked_button'] == 1:
            if  float(data['prob_replace']) != Constants.prob_replace:
                error_prob_replace = True
                player.participant.num_prob_replace =  player.participant.num_prob_replace+1
            else:
                error_prob_replace = False
            if  float(data['prob_not_replace'])!= Constants.prob_not_replace:
                error_prob_not_replace = True
                player.participant.num_prob_not_replace = player.participant.num_prob_not_replace + 1
            else:
                error_prob_not_replace = False
            if player.participant.num_prob_replace == Constants.max_num_try or  player.participant.num_prob_not_replace ==  Constants.max_num_try  or (error_prob_replace== False and error_prob_not_replace == False):
                response = dict(error_prob_not_replace=error_prob_not_replace, error_prob_replace=error_prob_replace, stop= True)
            else:
                response = dict(error_prob_not_replace=error_prob_not_replace, error_prob_replace=error_prob_replace,
                                stop=False)
            return {player.id_in_group: response}
    @staticmethod
    def js_vars(player):
        return dict(prob_replace_correct = Constants.prob_replace,prob_not_replace_correct = Constants.prob_not_replace, prob_replace_guess = 99999, prob_not_replace_guess =99999)


class Practice_payoff2(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def live_method(player: Player, data):
        if data['clicked_button'] == 1:
            if float(data['Test_choices_A_prob']) != player.participant.Test_choices_A :
                error_Test_choices_A_prob = True
                player.participant.num_Test_choices_A_prob = player.participant.num_Test_choices_A_prob + 1
            else:
                error_Test_choices_A_prob = False
            if float(data['Test_choices_B_prob']) != player.participant.Test_choices_B :
                error_Test_choices_B_prob = True
                player.participant.num_Test_choices_B_prob = player.participant.num_Test_choices_B_prob + 1
            else:
                error_Test_choices_B_prob = False
            if float(data['Test_choices_C_prob']) != player.participant.Test_choices_C :
                error_Test_choices_C_prob = True
                player.participant.num_Test_choices_C_prob = player.participant.num_Test_choices_C_prob + 1
            else:
                error_Test_choices_C_prob = False
            if float(data['payoff_A_guess']) !=  player.participant.payoff_practice_A:
                error_payoff_A_guess = True
                player.participant.num_payoff_A_guess = player.participant.num_payoff_A_guess + 1
            else:
                error_payoff_A_guess = False
            if float(data['payoff_B_guess']) != player.participant.payoff_practice_B:
                error_payoff_B_guess = True
                player.participant.num_payoff_B_guess = player.participant.num_payoff_B_guess + 1
            else:
                error_payoff_B_guess = False
            if float(data['payoff_C_guess']) !=  player.participant.payoff_practice_C:
                error_payoff_C_guess = True
                player.participant.num_payoff_C_guess = player.participant.num_payoff_C_guess + 1
            else:
                error_payoff_C_guess = False



            if player.participant.num_Test_choices_A_prob == Constants.max_num_try or  \
                    player.participant.num_Test_choices_B_prob == Constants.max_num_try or  \
                    player.participant.num_Test_choices_C_prob == Constants.max_num_try or   \
                    player.participant.num_payoff_A_guess == Constants.max_num_try or \
                    player.participant.num_payoff_B_guess == Constants.max_num_try or \
                    player.participant.num_payoff_C_guess == Constants.max_num_try or \
                    (error_Test_choices_A_prob == False and error_Test_choices_B_prob == False and \
                     error_Test_choices_C_prob == False and error_payoff_A_guess == False and error_payoff_B_guess == False and \
                     error_payoff_C_guess == False ):
                response = dict(error_Test_choices_A_prob=error_Test_choices_A_prob, error_Test_choices_B_prob=error_Test_choices_B_prob,
                                error_Test_choices_C_prob=error_Test_choices_C_prob, error_payoff_A_guess = error_payoff_A_guess,
                                error_payoff_B_guess = error_payoff_B_guess, error_payoff_C_guess = error_payoff_C_guess,
                                stop=True)
            else:
                response = dict(error_Test_choices_A_prob=error_Test_choices_A_prob, error_Test_choices_B_prob=error_Test_choices_B_prob,
                                error_Test_choices_C_prob=error_Test_choices_C_prob, error_payoff_A_guess = error_payoff_A_guess,
                                error_payoff_B_guess = error_payoff_B_guess, error_payoff_C_guess = error_payoff_C_guess,
                                stop=False)
            return {player.id_in_group: response}

    @staticmethod
    def js_vars(player):
        return dict(Test_choices_A_prob_guess = 99999, Test_choices_B_prob_guess =99999, Test_choices_C_prob_guess =99999,
                    payoff_A_guess=99999,payoff_B_guess=99999, payoff_C_guess=99999  )



class Practice_payoff3(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def live_method(player: Player, data):
        if data['clicked_button'] == 1:
            if float(data['Test_choices_A_prob']) != player.participant.Test_choices_A :
                error_Test_choices_A_prob = True
                player.participant.num_Test_choices_A_pred = player.participant.num_Test_choices_A_pred + 1
            else:
                error_Test_choices_A_prob = False
            if float(data['Test_choices_B_prob']) != player.participant.Test_choices_B :
                error_Test_choices_B_prob = True
                player.participant.num_Test_choices_B_pred = player.participant.num_Test_choices_B_pred + 1
            else:
                error_Test_choices_B_prob = False
            if float(data['Test_choices_C_prob']) != player.participant.Test_choices_C :
                error_Test_choices_C_prob = True
                player.participant.num_Test_choices_C_pred = player.participant.num_Test_choices_C_pred + 1
            else:
                error_Test_choices_C_prob = False
            if float(data['payoff_A_guess']) !=  player.participant.Test_payoff_a_pred:
                error_payoff_A_guess = True
                player.participant.num_Test_payoff_a_pred = player.participant.num_Test_payoff_a_pred + 1
            else:
                error_payoff_A_guess = False
            if float(data['payoff_B_guess']) != player.participant.Test_payoff_b_pred:
                error_payoff_B_guess = True
                player.participant.num_Test_payoff_b_pred = player.participant.num_Test_payoff_b_pred + 1
            else:
                error_payoff_B_guess = False
            if float(data['payoff_C_guess']) !=  player.participant.Test_payoff_c_pred:
                error_payoff_C_guess = True
                player.participant.num_Test_payoff_c_pred = player.participant.num_Test_payoff_c_pred + 1
            else:
                error_payoff_C_guess = False



            if player.participant.num_Test_choices_A_pred == Constants.max_num_try or  \
                    player.participant.num_Test_choices_B_pred == Constants.max_num_try or  \
                    player.participant.num_Test_choices_C_pred== Constants.max_num_try or   \
                    player.participant.num_Test_payoff_a_pred == Constants.max_num_try or \
                    player.participant.num_Test_payoff_b_pred == Constants.max_num_try or \
                    player.participant.num_Test_payoff_c_pred == Constants.max_num_try or \
                    (error_Test_choices_A_prob == False and error_Test_choices_B_prob == False and \
                     error_Test_choices_C_prob == False and error_payoff_A_guess == False and error_payoff_B_guess == False and \
                     error_payoff_C_guess == False ):
                response = dict(error_Test_choices_A_prob=error_Test_choices_A_prob, error_Test_choices_B_prob=error_Test_choices_B_prob,
                                error_Test_choices_C_prob=error_Test_choices_C_prob, error_payoff_A_guess = error_payoff_A_guess,
                                error_payoff_B_guess = error_payoff_B_guess, error_payoff_C_guess = error_payoff_C_guess,
                                stop=True)
            else:
                response = dict(error_Test_choices_A_prob=error_Test_choices_A_prob, error_Test_choices_B_prob=error_Test_choices_B_prob,
                                error_Test_choices_C_prob=error_Test_choices_C_prob, error_payoff_A_guess = error_payoff_A_guess,
                                error_payoff_B_guess = error_payoff_B_guess, error_payoff_C_guess = error_payoff_C_guess,
                                stop=False)
            return {player.id_in_group: response}

    @staticmethod
    def js_vars(player):
        return dict(Test_choices_A_prob_guess = 99999, Test_choices_B_prob_guess =99999, Test_choices_C_prob_guess =99999,
                    payoff_A_guess=99999,payoff_B_guess=99999, payoff_C_guess=99999  )



class Introduction(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1




class Instruction_1(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    @staticmethod
    def vars_for_template(player):
        max_income = Constants.quadratic_score_A + Constants.quadratic_score_B
        min_income = Constants.quadratic_score_A - Constants.quadratic_score_B
        return dict(max_income=max_income, min_income=min_income)

class Instruction_2(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction_3(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Instruction_4(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction_5(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    @staticmethod
    def vars_for_template(player):
        max_income = Constants.quadratic_score_A + Constants.quadratic_score_B
        min_income = Constants.quadratic_score_A - Constants.quadratic_score_B
        return dict(max_income=max_income, min_income=min_income)

class Instruction_6(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction_7(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    @staticmethod
    def vars_for_template(player):
        max_income = Constants.quadratic_score_A + Constants.quadratic_score_B
        min_income = Constants.quadratic_score_A - Constants.quadratic_score_B
        return dict(max_income=max_income, min_income=min_income)


class Instruction_8(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction_9(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction_10(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction_11(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
class Instruction_12(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction_13(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction_14(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
class Instruction_15(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction_16(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction_17(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction_18(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction_19(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction_20(Page):
    form_model = 'player'
    form_fields = ['TARI']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction_21(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player):
        a= Constants.level1_cost*player.TARI/100
        b = Constants.level2_cost * player.TARI / 100
        c = Constants.level3_cost * player.TARI / 100
        d = Constants.level4_cost * player.TARI / 100
        return dict(a=a, b=b,c=c,d=d)


class Instruction_22(Page):

    @staticmethod
    def is_displayed(player: Player):
            return player.round_number == 1

class Instruction_23_practice_CE(Page):


    form_model = 'player'
    form_fields = ['CE_choice_practice']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Instruction_24(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    @staticmethod
    def vars_for_template(player):
        max_income = Constants.quadratic_score_A + Constants.quadratic_score_B
        min_income = Constants.quadratic_score_A - Constants.quadratic_score_B
        return dict(max_income=max_income, min_income=min_income)

class Instruction_25_1(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction_25_2(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    @staticmethod
    def vars_for_template(player):
        max_income = Constants.quadratic_score_A + Constants.quadratic_score_B
        min_income = Constants.quadratic_score_A - Constants.quadratic_score_B
        return dict(max_income=max_income, min_income=min_income, num_participants = player.participant.num_players-1)



class Instruction_26_practice_PRED(Page):
    form_model = 'player'
    form_fields = ['CE_pract_pred_A','CE_pract_pred_B','CE_pract_pred_C']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player):
        max_income = Constants.quadratic_score_A + Constants.quadratic_score_B
        min_income = Constants.quadratic_score_A - Constants.quadratic_score_B
        return dict(max_income=max_income, min_income=min_income, num_participants=player.participant.num_players - 1)

    @staticmethod
    def live_method(player: Player, data):
        if data['clicked_button'] == 1:
            a= float(data['fieldA'])/(player.participant.num_players - 1)
            b = float(data['fieldB'])/(player.participant.num_players - 1)
            c = float(data['fieldC'])/(player.participant.num_players - 1)
            factor1 = a*a + b*b + c*c
            payoff_a =  round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*a - factor1),2)
            payoff_b =  round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*b - factor1),2)
            payoff_c =  round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*c - factor1),2)
            response = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c)
            player.participant.payoff_practice_A = payoff_a
            player.participant.payoff_practice_B = payoff_b
            player.participant.payoff_practice_C = payoff_c
            return{player.id_in_group: response }

#Passing data from Python to JavaScript (js_vars)
    @staticmethod
    def js_vars(player):
        return dict(number_players = player.participant.num_players,tempA=0,tempB=0,tempC=0)

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['CE_pract_pred_A'] + values['CE_pract_pred_B'] + values['CE_pract_pred_C'] != (player.participant.num_players- 1):
          return 'Sum of predictions has to be equal to  '  + str(player.participant.num_players- 1)


class Instruction_27(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(Subsession):
        a = Subsession.session.random_prediction_A / (Subsession.session.num_participants - 1)
        b = Subsession.session.random_prediction_B / (Subsession.session.num_participants - 1)
        c = Subsession.session.random_prediction_C  / (Subsession.session.num_participants - 1)
        factor1 = a * a + b * b + c * c
        payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * a - factor1), 2)
        payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * b - factor1), 2)
        payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * c - factor1), 2)

        return dict(random_prediction_A= Subsession.session.random_prediction_A, random_prediction_B=Subsession.session.random_prediction_B,
                    random_prediction_C=Subsession.session.random_prediction_C,
                    random_payoff_A = payoff_a, random_payoff_B = payoff_b, random_payoff_C = payoff_c)



class Instruction_27_2(Page):
    form_model = 'player'
    form_fields = ['CE_pract_pred_A','CE_pract_pred_B','CE_pract_pred_C']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player):
        max_income = Constants.quadratic_score_A + Constants.quadratic_score_B
        min_income = Constants.quadratic_score_A - Constants.quadratic_score_B
        return dict(max_income=max_income, min_income=min_income, num_participants=player.participant.num_players - 1)

    @staticmethod
    def live_method(player: Player, data):
        if data['clicked_button'] == 1:
            a= float(data['fieldA'])/(player.participant.num_players - 1)
            b = float(data['fieldB'])/(player.participant.num_players - 1)
            c = float(data['fieldC'])/(player.participant.num_players - 1)
            factor1 = a*a + b*b + c*c
            payoff_a =  round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*a - factor1),2)
            payoff_b =  round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*b - factor1),2)
            payoff_c =  round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*c - factor1),2)
            response = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c)
            player.participant.payoff_practice_A = payoff_a
            player.participant.payoff_practice_B = payoff_b
            player.participant.payoff_practice_C = payoff_c
            return{player.id_in_group: response }

#Passing data from Python to JavaScript (js_vars)
    @staticmethod
    def js_vars(player):
        return dict(number_players = player.participant.num_players,tempA=0,tempB=0,tempC=0)

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['CE_pract_pred_A'] + values['CE_pract_pred_B'] + values['CE_pract_pred_C'] != (player.participant.num_players- 1):
          return 'Sum of predictions has to be equal to  '  + str(player.participant.num_players- 1)


class Instruction_28(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction_29(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Instruction_30(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction_31(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(Subsession):
        listA = list(range(1,Subsession.session.random_prediction_A_2+1))
        listB = list(range(1, Subsession.session.random_prediction_B_2 + 1))
        listC = list(range(1, Subsession.session.random_prediction_C_2 + 1))

        return dict(random_prediction_A=Subsession.session.random_prediction_A_2,
                    random_prediction_B=Subsession.session.random_prediction_B_2,
                    random_prediction_C=Subsession.session.random_prediction_C_2,
                    listA=listA,
                    listB=listB,
                    listC=listC)


class Instruction_32(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(Subsession):

        return dict(chosen_letter=Subsession.session.chosen_letter_2)

class Instruction_33(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1



class Instruction_34(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1



class Instruction_35(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(player):
        return dict(prob_replace=int(Constants.prob_replace*100), prob_not_replace=int(Constants.prob_not_replace*100),
                    prob_not_replace_1=int(Constants.prob_not_replace*100 + 1))

class Instruction_36(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(Subsession):
        return dict(random_ball_not_replaced=Subsession.session.random_ball_not_replaced)

class Instruction_37(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def vars_for_template(Subsession):
        return dict(random_ball_replaced=Subsession.session.random_ball_replaced)

class Instruction_37_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Instruction_38(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    @staticmethod
    def vars_for_template(Subsession):
        return dict(random_prediction_A=Subsession.session.random_prediction_A_2,
                    listA=Subsession.session.listA_2)


class Instruction_39(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    @staticmethod
    def vars_for_template(Subsession):
        cont=list(range(0,Subsession.session.random_prediction_A_2 ))
        example_prediction_average_A = {i: Subsession.session.example_prediction_average_A[i] for i in range(0, len(Subsession.session.example_prediction_average_A))}
        example_prediction_average_B = {i: Subsession.session.example_prediction_average_B[i] for i in
                                        range(0, len(Subsession.session.example_prediction_average_B))}
        example_prediction_average_C = {i: Subsession.session.example_prediction_average_C[i] for i in
                                        range(0, len(Subsession.session.example_prediction_average_C))}
        listA_2_temp1=Subsession.session.listA_2

        listA_2_temp2 = [s.replace(".", "") for s in listA_2_temp1]
        listA_2 = [s.replace(",", "") for s in listA_2_temp2]

        AverageA = round(sum(Subsession.session.example_prediction_average_A )/len(Subsession.session.example_prediction_average_A),1)
        AverageB = round(sum(Subsession.session.example_prediction_average_B )/len(Subsession.session.example_prediction_average_C),1)
        AverageC = round(sum(Subsession.session.example_prediction_average_C )/len(Subsession.session.example_prediction_average_C),1)

        return dict(example_prediction_average_A=example_prediction_average_A,
                    example_prediction_average_B=example_prediction_average_B,
                    example_prediction_average_C=example_prediction_average_C,
                    listA=listA_2 , cont = cont,
                    AverageA=AverageA,
                    AverageB=AverageB,
                    AverageC=AverageC,
                    )


class Instruction_40(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
    @staticmethod
    def vars_for_template(Subsession):
        cont=list(range(0,Subsession.session.random_prediction_A_2 ))
        example_prediction_average_A = {i: Subsession.session.example_prediction_average_A[i] for i in range(0, len(Subsession.session.example_prediction_average_A))}
        example_prediction_average_B = {i: Subsession.session.example_prediction_average_B[i] for i in
                                        range(0, len(Subsession.session.example_prediction_average_B))}
        example_prediction_average_C = {i: Subsession.session.example_prediction_average_C[i] for i in
                                        range(0, len(Subsession.session.example_prediction_average_C))}
        listA_2_temp1=Subsession.session.listA_2

        listA_2_temp2 = [s.replace(".", "") for s in listA_2_temp1]
        listA_2 = [s.replace(",", "") for s in listA_2_temp2]

        AverageA = round(sum(Subsession.session.example_prediction_average_A )/len(Subsession.session.example_prediction_average_A),1)
        AverageB = round(sum(Subsession.session.example_prediction_average_B )/len(Subsession.session.example_prediction_average_C),1)
        AverageC = round(sum(Subsession.session.example_prediction_average_C )/len(Subsession.session.example_prediction_average_C),1)

        return dict(example_prediction_average_A=example_prediction_average_A,
                    example_prediction_average_B=example_prediction_average_B,
                    example_prediction_average_C=example_prediction_average_C,
                    listA=listA_2 , cont = cont,
                    AverageA=AverageA,
                    AverageB=AverageB,
                    AverageC=AverageC,
                    )

class CE1(Page):
    form_model = 'player'
    form_fields = ['CE1_choice']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['1']


class CE2(Page):
    form_model = 'player'
    form_fields = ['CE2_choice']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['2']


class CE3(Page):
    form_model = 'player'
    form_fields = ['CE3_choice']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['3']

class CE4(Page):
    form_model = 'player'
    form_fields = ['CE4_choice']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['4']


class CE5(Page):
    form_model = 'player'
    form_fields = ['CE5_choice']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['5']


class CE6(Page):
    form_model = 'player'
    form_fields = ['CE6_choice']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['6']

class CE7(Page):
    form_model = 'player'
    form_fields = ['CE7_choice']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['7']


class CE8(Page):
    form_model = 'player'
    form_fields = ['CE8_choice']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['8']


class CE9(Page):
    form_model = 'player'
    form_fields = ['CE9_choice']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['9']



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
        return player.round_number == participant.task_rounds['1'] + Constants.num_CE

    @staticmethod
    def live_method(player: Player, data):
        if data['clicked_button'] == 1:
            a= float(data['fieldA'])/(player.participant.num_players - 1)
            b = float(data['fieldB'])/(player.participant.num_players - 1)
            c = float(data['fieldC'])/(player.participant.num_players - 1)
            factor1 = a*a + b*b + c*c
            payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*a - factor1),2)
            payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*b - factor1),2)
            payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*c - factor1),2)
            response = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c)
            return{player.id_in_group: response }

#Passing data from Python to JavaScript (js_vars)
    @staticmethod
    def js_vars(player):
        return dict(number_players = player.participant.num_players,tempA=0,tempB=0,tempC=0)

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['CE1_pred_A'] + values['CE1_pred_B'] + values['CE1_pred_C'] != (player.participant.num_players- 1):
          return 'Sum of predictions has to be equal to  '  + str(player.participant.num_players- 1)

class Pred_CE2(Page):
    form_model = 'player'
    form_fields = ['CE2_pred_A', 'CE2_pred_B', 'CE2_pred_C']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['2'] + Constants.num_CE

    @staticmethod
    def live_method(player: Player, data):
        if data['clicked_button'] == 1:
            a = float(data['fieldA']) / (player.participant.num_players - 1)
            b = float(data['fieldB']) /(player.participant.num_players - 1)
            c = float(data['fieldC']) / (player.participant.num_players - 1)
            factor1 = a * a + b * b + c * c
            payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * a - factor1),2)
            payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * b - factor1),2)
            payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * c - factor1),2)
            response = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c)
            return {player.id_in_group: response}

        # Passing data from Python to JavaScript (js_vars)
    @staticmethod
    def js_vars(player):
            return dict(number_players=player.participant.num_players, tempA=0, tempB=0, tempC=0)

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['CE2_pred_A'] + values['CE2_pred_B'] + values['CE2_pred_C'] !=  (player.participant.num_players- 1):
          return 'Sum of predictions has to be equal to  '  +  str(player.participant.num_players- 1)


class Pred_CE3(Page):
    form_model = 'player'
    form_fields = ['CE3_pred_A', 'CE3_pred_B', 'CE3_pred_C']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['3'] + Constants.num_CE


    @staticmethod
    def live_method(player: Player, data):
            if data['clicked_button'] == 1:
                a = float(data['fieldA']) / (player.participant.num_players - 1)
                b = float(data['fieldB']) / (player.participant.num_players - 1)
                c = float(data['fieldC']) / (player.participant.num_players - 1)
                factor1 = a * a + b * b + c * c
                payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * a - factor1),2)
                payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * b - factor1),2)
                payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * c - factor1),2)
                response = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c)
                return {player.id_in_group: response}

        # Passing data from Python to JavaScript (js_vars)
    @staticmethod
    def js_vars(player):
            return dict(number_players=player.participant.num_players, tempA=0, tempB=0, tempC=0)

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['CE3_pred_A'] + values['CE3_pred_B'] + values['CE3_pred_C'] !=  (player.participant.num_players- 1):
          return 'Sum of predictions has to be equal to  '  + str(player.participant.num_players- 1)

    @staticmethod
    def vars_for_template(player):
        return dict( a=0,  b=0,c=0,)

class Pred_CE4(Page):
    form_model = 'player'
    form_fields = ['CE4_pred_A','CE4_pred_B','CE4_pred_C']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['4'] + Constants.num_CE

    @staticmethod
    def live_method(player: Player, data):
        if data['clicked_button'] == 1:
            a= float(data['fieldA'])/(player.participant.num_players - 1)
            b = float(data['fieldB'])/(player.participant.num_players - 1)
            c = float(data['fieldC'])/(player.participant.num_players - 1)
            factor1 = a*a + b*b + c*c
            payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*a - factor1),2)
            payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*b - factor1),2)
            payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*c - factor1),2)
            response = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c)
            return{player.id_in_group: response }

#Passing data from Python to JavaScript (js_vars)
    @staticmethod
    def js_vars(player):
        return dict(number_players = player.participant.num_players,tempA=0,tempB=0,tempC=0)

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['CE4_pred_A'] + values['CE4_pred_B'] + values['CE4_pred_C'] != (player.participant.num_players- 1):
          return 'Sum of predictions has to be equal to  '  + str(player.participant.num_players- 1)

class Pred_CE5(Page):
    form_model = 'player'
    form_fields = ['CE5_pred_A', 'CE5_pred_B', 'CE5_pred_C']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['5'] + Constants.num_CE

    @staticmethod
    def live_method(player: Player, data):
        if data['clicked_button'] == 1:
            a = float(data['fieldA']) / (player.participant.num_players - 1)
            b = float(data['fieldB']) / (player.participant.num_players - 1)
            c = float(data['fieldC']) /(player.participant.num_players - 1)
            factor1 = a * a + b * b + c * c
            payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * a - factor1),2)
            payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * b - factor1),2)
            payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * c - factor1),2)
            response = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c)
            return {player.id_in_group: response}

        # Passing data from Python to JavaScript (js_vars)
    @staticmethod
    def js_vars(player):
            return dict(number_players=player.participant.num_players, tempA=0, tempB=0, tempC=0)

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['CE5_pred_A'] + values['CE5_pred_B'] + values['CE5_pred_C'] !=  (player.participant.num_players- 1):
          return 'Sum of predictions has to be equal to  '  +  str(player.participant.num_players - 1)


class Pred_CE6(Page):
    form_model = 'player'
    form_fields = ['CE6_pred_A', 'CE6_pred_B', 'CE6_pred_C']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['6'] + Constants.num_CE


    @staticmethod
    def live_method(player: Player, data):
            if data['clicked_button'] == 1:
                a = float(data['fieldA']) / (player.participant.num_players - 1)
                b = float(data['fieldB']) / (player.participant.num_players - 1)
                c = float(data['fieldC']) / (player.participant.num_players - 1)
                factor1 = a * a + b * b + c * c
                payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * a - factor1),2)
                payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * b - factor1),2)
                payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * c - factor1),2)
                response = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c)
                return {player.id_in_group: response}

        # Passing data from Python to JavaScript (js_vars)
    @staticmethod
    def js_vars(player):
            return dict(number_players=player.participant.num_players, tempA=0, tempB=0, tempC=0)

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['CE6_pred_A'] + values['CE6_pred_B'] + values['CE6_pred_C'] !=  (player.participant.num_players - 1):
          return 'Sum of predictions has to be equal to  '  + str(player.participant.num_players -1)

    @staticmethod
    def vars_for_template(player):
        return dict( a=0,  b=0,c=0,)

class Pred_CE7(Page):
    form_model = 'player'
    form_fields = ['CE7_pred_A','CE7_pred_B','CE7_pred_C']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == participant.task_rounds['7'] + Constants.num_CE

    @staticmethod
    def live_method(player: Player, data):
        if data['clicked_button'] == 1:
            a= float(data['fieldA'])/(player.participant.num_players - 1)
            b = float(data['fieldB'])/(player.participant.num_players - 1)
            c = float(data['fieldC'])/(player.participant.num_players - 1)
            factor1 = a*a + b*b + c*c
            payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*a - factor1),2)
            payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*b - factor1),2)
            payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*c - factor1),2)
            response = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c)
            return{player.id_in_group: response }

#Passing data from Python to JavaScript (js_vars)
    @staticmethod
    def js_vars(player):
        return dict(number_players = player.participant.num_players,tempA=0,tempB=0,tempC=0)

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['CE7_pred_A'] + values['CE7_pred_B'] + values['CE7_pred_C'] != (player.participant.num_players- 1):
          return 'Sum of predictions has to be equal to  '  + str(player.participant.num_players - 1)

class Pred_CE8(Page):
    form_model = 'player'
    form_fields = ['CE8_pred_A', 'CE8_pred_B', 'CE8_pred_C']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['8'] + Constants.num_CE

    @staticmethod
    def live_method(player: Player, data):
        if data['clicked_button'] == 1:
            a = float(data['fieldA']) /(player.participant.num_players - 1)
            b = float(data['fieldB']) / (player.participant.num_players - 1)
            c = float(data['fieldC']) / (player.participant.num_players - 1)
            factor1 = a * a + b * b + c * c
            payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * a - factor1),2)
            payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * b - factor1),2)
            payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * c - factor1),2)
            response = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c)
            return {player.id_in_group: response}

        # Passing data from Python to JavaScript (js_vars)
    @staticmethod
    def js_vars(player):
            return dict(number_players=player.participant.num_players, tempA=0, tempB=0, tempC=0)

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['CE8_pred_A'] + values['CE8_pred_B'] + values['CE8_pred_C'] !=  (player.participant.num_players- 1):
          return 'Sum of predictions has to be equal to  '  +  str(player.participant.num_players- 1)


class Pred_CE9(Page):
    form_model = 'player'
    form_fields = ['CE9_pred_A', 'CE9_pred_B', 'CE9_pred_C']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['9'] + Constants.num_CE


    @staticmethod
    def live_method(player: Player, data):
            if data['clicked_button'] == 1:
                a = float(data['fieldA']) / (player.participant.num_players - 1)
                b = float(data['fieldB']) / (player.participant.num_players - 1)
                c = float(data['fieldC']) / (player.participant.num_players - 1)
                factor1 = a * a + b * b + c * c
                payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * a - factor1),2)
                payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * b - factor1),2)
                payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * c - factor1),2)
                response = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c)
                return {player.id_in_group: response}

        # Passing data from Python to JavaScript (js_vars)
    @staticmethod
    def js_vars(player):
            return dict(number_players=player.participant.num_players, tempA=0, tempB=0, tempC=0)

    @staticmethod
    def error_message(player, values):
        print('values is', values)
        if values['CE9_pred_A'] + values['CE9_pred_B'] + values['CE9_pred_C'] !=  (player.participant.num_players- 1):
          return 'Sum of predictions has to be equal to  '  + str(player.participant.num_players - 1)

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
            choices_str = player.participant.list_choices_A + ' ' + player.participant.list_choices_B + ' ' + player.participant.list_choices_C
            list_choices = choices_str.split()

            player.participant.random_choice = random.choice(list_choices)
            random_choice = player.participant.random_choice
            if random_num <= Constants.prob_replace:
                replace_pred = 1
            else:
                replace_pred = 0
            payoff_set = payoffs(replace_pred, player)
            if  payoff_set['error'] == False :
                if random_choice == 'A':
                   player.payoff = payoff_set['payoff_a']
                else:
                   if random_choice == 'B':
                       player.payoff = payoff_set['payoff_b']
                   else:
                       player.payoff = payoff_set['payoff_c']
                response = dict(replace_pred=replace_pred, payoff_a=payoff_set['payoff_a'],
                            payoff_b=payoff_set['payoff_b'], payoff_c=payoff_set['payoff_c'], finalpayoff=player.payoff,
                            pred_a=payoff_set['pred_a'],  pred_b=payoff_set['pred_b'], pred_c=payoff_set['pred_c'],
                            round=1, choices = ' '.join(list_choices))
            else:
                player.payoff = 99999
                response = dict(replace_pred=replace_pred, payoff_a="Error",
                            payoff_b="Error", payoff_c="Error", finalpayoff=player.payoff,
                            pred_a="Error",  pred_b="Error", pred_c="Error",
                            round=1,choices = ' '.join(list_choices))


            return {player.id_in_group: response}
        else:
            if data['clicked_button'] == 2:
                if player.participant.payoff == 99999:
                    response = dict(random_choice=player.participant.random_choice, finalpayoff="Error",
                                round=2)
                else:
                    response = dict(random_choice=player.participant.random_choice,
                                    finalpayoff=player.participant.payoff,
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


page_sequence = [#Introduction,
     #Instruction_1,
    #  Instruction_2,
    #      Instruction_3,
    #     Instruction_4,
    #     Instruction_5,
    #     Instruction_6,
    #     Instruction_7,
    #    Instruction_8,
                 Instruction_9,
                 Instruction_10,
      Instruction_11,
      Instruction_12,
Instruction_13,
Instruction_14,
    Instruction_15,
     Instruction_16,
      Instruction_17,
 Instruction_18,
Instruction_19,
Instruction_20,
Instruction_21,
Instruction_22,
Instruction_23_practice_CE,
Instruction_24,
Instruction_25_1,
Instruction_25_2,
Instruction_26_practice_PRED,
Instruction_27,
Instruction_27_2,
Instruction_28,
Instruction_29,
                 Instruction_30,
Instruction_31,
Instruction_32,
Instruction_33,
Instruction_34,
Instruction_35,
Instruction_36,
Instruction_37,
Instruction_37_2,
Instruction_38,
Instruction_39,
Instruction_40,
    #Practice_CE, Practice_Pred_CE,
     Practice_payoff1,Practice_payoff2, Practice_payoff3,CE1, CE2, CE3,CE4, CE5, CE6,CE7, CE8, CE9, Wait_CE, Pred_CE1,  Pred_CE2, Pred_CE3,
                 Pred_CE4,  Pred_CE5, Pred_CE6,Pred_CE7,  Pred_CE8, Pred_CE9,Wait_CE2,Show_bindingsit,Results]
