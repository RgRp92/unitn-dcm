
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
    name_in_url = 'Control_1to9'
    tasks = ['1', '2', '3','4','5','6','7','8','9']
    num_CE = len(tasks)
    ###practice test####
    random_practice_choice_sit = random.randint(1, num_CE)
    random_practice_alternative = random.choice(['A','B','C'])
    num_rounds = 1
    quadratic_score_A = 5
    quadratic_score_B = 5
    prob_replace = 0.75
    prob_not_replace = 0.25
    max_num_try = 5 # Maximum number of tries practice test


    CS1_location_A = 0
    CS2_location_A = 1
    CS3_location_A = -1
    CS4_location_A = -1
    CS5_location_A = -1
    CS6_location_A = 0
    CS7_location_A = 1
    CS8_location_A = 0
    CS9_location_A = 1

    CS1_rainab_A =-1
    CS2_rainab_A = 1
    CS3_rainab_A =1
    CS4_rainab_A =0
    CS5_rainab_A =0
    CS6_rainab_A =1
    CS7_rainab_A =-1
    CS8_rainab_A =0
    CS9_rainab_A =-1

    CS1_maintan_A =0
    CS2_maintan_A =0
    CS3_maintan_A =-1
    CS4_maintan_A =1
    CS5_maintan_A =0
    CS6_maintan_A =1
    CS7_maintan_A =1
    CS8_maintan_A =-1
    CS9_maintan_A =-1

    CS1_cost_A =-1
    CS2_cost_A =1
    CS3_cost_A =-1
    CS4_cost_A =1
    CS5_cost_A =0
    CS6_cost_A =2
    CS7_cost_A =-1
    CS8_cost_A =1
    CS9_cost_A =-1

    CS1_location_B =1
    CS2_location_B = 0
    CS3_location_B = 0
    CS4_location_B =-1
    CS5_location_B =1
    CS6_location_B =1
    CS7_location_B =-1
    CS8_location_B =-1
    CS9_location_B =0

    CS1_rainab_B = 0
    CS2_rainab_B = 0
    CS3_rainab_B = -1
    CS4_rainab_B = -1
    CS5_rainab_B = 1
    CS6_rainab_B = 0
    CS7_rainab_B = 1
    CS8_rainab_B = -1
    CS9_rainab_B = 1

    CS1_maintan_B =1
    CS2_maintan_B =-1
    CS3_maintan_B =0
    CS4_maintan_B =-1
    CS5_maintan_B =-1
    CS6_maintan_B =0
    CS7_maintan_B =0
    CS8_maintan_B =1
    CS9_maintan_B =1

    CS1_cost_B = 1
    CS2_cost_B = -1
    CS3_cost_B = 1
    CS4_cost_B = -1
    CS5_cost_B = 1
    CS6_cost_B = -1
    CS7_cost_B = 2
    CS8_cost_B = 0
    CS9_cost_B = 1

    Location_level_1="Priorità  nel Centro città"
    Location_level_2 = "Priorità nelle Periferie"
    Location_level_3 = "Equamente  distribuito tra centro citta’ e periferia"

    Maintenance_level_1 = "2"
    Maintenance_level_2 = "4"
    Maintenance_level_3 = "6"

    runoff_level_1 = "25%"
    runoff_level_2 = "50%"
    runoff_level_3 = "75%"


    level1_cost = 10
    level2_cost = 15
    level3_cost = 20
    level4_cost = 25






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

def make_likert_scale_5(label):
    return  models.IntegerField(
        choices=[[1,"1"], [2,"2"], [3,"3"], [4,"4"], [5,"5"]],
        widget=widgets.RadioSelectHorizontal,
        label=label,
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


    accept = models.IntegerField(
        choices=[[1,"Si"], [0,"No"]],
        widget=widgets.RadioSelect
    )

    futuro_studies =  models.IntegerField(
        choices=[[1,"Si"], [0,"No"]],
        widget=widgets.RadioSelect  )



    ##Choices in each choice situation
    CE_choice_practice =  models.IntegerField(
        choices=[[1, "A"], [2, "B"], [3, "Statusquo"]],
        # choices=[1, 2, 3],
        label="Practice Choice situation",
        widget=widgets.RadioSelect,
        blank=True,
    )
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

    ## INFORMATIVA PER IL TRATTAMENTO NELL’AMBITO DEL RECLUTAMENTO DEI PARTECIPANTI ALLA RICERCA

    nome = models.StringField(    blank=True)
    cognome = models.StringField(        blank=True)
    email = models.StringField(        blank=True)
    numero_di_cellulare = models.StringField(blank=True)
    nato_a = models.StringField(        blank=True)
    mesi_di_nascita = models.IntegerField(
        choices=[[1, "Gennaio"], [2, "Febbraio"], [3, "Marzo"], [4, "Aprile"], [5, "Maggio"],
        [6, "Giugno"], [7, "Luglio"], [8, "Agosto"], [9, "Settembre"], [10, "Ottobre"], [11, "Novembre"],
        [12, "Dicembre"]],blank = True)
    giorno_di_nascita_30 = models.IntegerField(
    choices = list(range(1, 30)),blank = True)

    anni_di_nascita = models.IntegerField(choices = list(range(1920, 2005)),blank = True   )



    player_temp_AB =  models.IntegerField(default=0)
    ##Questionnario
    #Behavioural question
    Member_env_group = models.IntegerField(
        choices=[[0,"Si"],[1,"No"]],
        widget=widgets.RadioSelect,
    )

    green_areas_frequency = models.IntegerField(
        choices=[[0, "Quasi mai"], [1, "Raramente"], [2, "A volte "], [3, "Spesso"], [4, "Molto spesso"]],
       widget = widgets.RadioSelect,
    )



    recreational_outdoor = models.IntegerField(
        choices=[[0, "Quasi mai"], [1, "Raramente"], [2, "A volte "], [3, "Spesso"], [4, "Molto spesso"]],
       widget = widgets.RadioSelect,
    )

    Own_house = models.IntegerField(
        choices=[[0, "Si"], [1, "No"]],
                 widget = widgets.RadioSelect,

    )

    vivi_affito = models.IntegerField(
        choices=[[0, "Si"], [1, "No"]],
        widget=widgets.RadioSelect,

    )

    Own_house_green_roof = models.IntegerField(
        choices=[[0, "Si"], [1, "No"] ],
        widget=widgets.RadioSelect,
        blank=True
    )


    Consider_install_green_roof = models.IntegerField(
        choices=[[0, "Si"], [1, "No"], [2,"Non saprei"]],
                 widget = widgets.RadioSelect,
        blank=True
    )

    Consider_rent_green_roof = models.IntegerField(
        choices=[[0, "Si"], [1, "No"], [2,"Non saprei"]],
                 widget = widgets.RadioSelect,
        blank=True
    )

    #Attitudes

    # Risk meassuements
    Risk_willigness_scale = make_likert_scale_5("risk_general")
    R1 = make_likert_scale_5("R1")
    R2 = make_likert_scale_5("R2")
    R3 = make_likert_scale_5("R3")
    R4 = make_likert_scale_5("R4")
    R5 = make_likert_scale_5("R5")

    # Nature relatedness
    NR1 = make_likert_scale_5("NR6")
    NR2 = make_likert_scale_5("NR6")
    NR3 = make_likert_scale_5("NR6")
    NR4 = make_likert_scale_5("NR6")
    NR5 = make_likert_scale_5("NR6")
    NR6 = make_likert_scale_5("NR6")

    # Sense of Place
    SP1 = make_likert_scale_5("SP1")
    SP2 = make_likert_scale_5("SP2")
    SP3 = make_likert_scale_5("SP3")
    SP4 = make_likert_scale_5("SP4")
    SP5 = make_likert_scale_5("SP5")

    # Climate change experience and expectation

    affected_flooding = models.IntegerField(
        choices=[[0, "Si"], [1, "No"]],
        widget=widgets.RadioSelect,
    )

    lik_severe_flood = make_likert_scale_5("severe_flood")
    lik_mild_flood = make_likert_scale_5("mild_flood")
    serious_problem = make_likert_scale_5("serious_prob")

    # Green roofs aesthetics
    AE1 = make_likert_scale_5("AE1")
    AE2 = make_likert_scale_5("AE2")
    AE3 = make_likert_scale_5("AE3")
    AE4 = make_likert_scale_5("AE4")

    # Green roofs services
    SGR1  = make_likert_scale_5("SGR1")
    SGR2 = make_likert_scale_5("SGR2")
    SGR3 = make_likert_scale_5("SGR3")

    # Socioeconomics
    anni_natto =models.IntegerField(
        label="Anno di nascita",
        min=1900,
        max=2004)
    gender  = models.IntegerField(
        choices=[[0, "Femminile"], [1, "Maschile"], [2, "Altro"]],
        widget = widgets.RadioSelect )

    person_14_less = models.IntegerField(
        label="Ragazzi di età inferiore ai 14 anni",
        min=0,
        max=30)
    person_15_19 = models.IntegerField(
        label="Adolescenti tra i 15 e i 19 anni",
        min=0,
        max=30)
    person_20_40 = models.IntegerField(
        label="Adulti tra i 20 e i 40 anni",
        min=0,
        max=30)
    person_41_65 = models.IntegerField(
        label="Adulti tra i 41 e i 65 anni",
        min=0,
        max=30)
    person_65 = models.IntegerField(
        label="Adulti di età superiore ai 66 anni",
        min=0,
        max=30)

    Education = models.IntegerField(
        choices=[[0, "Nessuno studio formale"], [1, "Scuola elementare"], [2, "Scuola secondaria"],  [3, "Scuola superiore"],
                 [4, "Laurea Triennale"], [5, "Laurea Magistrale"],[6, "Dottorato di ricerca"]],
        widget=widgets.RadioSelect)




    residente_trento = models.IntegerField(
        choices=[[0, "Si"], [1, "No"]],
        widget=widgets.RadioSelect,
    )


    Circoscrizioni_residente = models.IntegerField(
        choices=[[0, "A - Centro Storico "], [1, "B - S. Giuseppe, S. Chiara "], [2, "C - Piedicastello (Sud) "],
                 [3, "D - Piedicastello (Nord)   "], [4, "E - Mattarello  "], [5, "F - Gardolo  "], [6, "G - Oltrefersina  (Nord) "],
                 [7, "H - Oltrefersina  (Sud) "],
                 [8, "I - Meano  "], [9, "J - Ravina,Romagnano  "], [10, "K - Povo "], [11, "L - Sardagna  "], [12, "M - Villazzano  "],
                 [13, "N - Argentario  "], [14, "O - Bondone  "],
                 [15, "Altro , dove?"]], blank=True,
        widget=widgets.RadioSelect)

    Circoscrizioni_residente_altro = models.StringField(
        blank=True  )

    domiciliato_trento = models.IntegerField(
        choices=[[0, "Si"], [1, "No"]],
        widget=widgets.RadioSelect,
    )

    Circoscrizioni_domiciliato = models.IntegerField(
        choices=[[0, "A - Centro Storico "], [1, "B- S. Giuseppe – S. Chiara "], [2, "C - Piedicastello (Sud) "],
                 [3, "D- Piedicastello (Nord)   "], [4, "E- Mattarello  "], [5, "F- Gardolo  "], [6, "G-Oltrefersina  (Nord) "],
                 [7, "H- Oltrefersina  (Sud) "],
                 [8, "I- Meano  "], [9, "J- Ravina-Romagnano  "], [10, "K- Povo "], [11, "L- Sardagna  "], [12, "M- Villazzano  "],
                 [13, "N- Argentario  "], [14, "O- Bondone  "],
                 [15, "Altro , dove?"]],   blank=True,
        widget=widgets.RadioSelect)


    Circoscrizioni_domiciliato_altro = models.StringField(
        blank=True  )

    lavori_trento = models.IntegerField(
        choices=[[0, "Si"], [1, "No"]],
        widget=widgets.RadioSelect,
    )

    Circoscrizioni_lavori = models.IntegerField(
        choices=[[0, "A - Centro Storico "], [1, "B- S. Giuseppe – S. Chiara "], [2, "C - Piedicastello (Sud) "],
                 [3, "D- Piedicastello (Nord)   "], [4, "E- Mattarello  "], [5, "F- Gardolo  "], [6, "G-Oltrefersina  (Nord) "],
                 [7, "H- Oltrefersina  (Sud) "],
                 [8, "I- Meano  "], [9, "J- Ravina-Romagnano  "], [10, "K- Povo "], [11, "L- Sardagna  "], [12, "M- Villazzano  "],
                 [13, "N- Argentario  "], [14, "O- Bondone  "],
                 [15, "Altro , dove?"]], blank=True,
        widget=widgets.RadioSelect)

    Circoscrizioni_lavori_altro = models.StringField(
        blank=True
    )

    nato_trento = models.IntegerField(
        choices=[[0, "Si"], [1, "No"]],
        widget=widgets.RadioSelect,
    )

    anni_trento = models.IntegerField(
        label="anni",
        min=0,
        max=100, blank=True)

    Natto_italy = models.IntegerField(
        choices=[[0, "Si"], [1, "No"]],
        widget=widgets.RadioSelect,
        blank=True,
    )

    Regione_nato = models.IntegerField(
        choices =[[0,  "Trentino - Alto Adige"],  [1,"Friuli - Venezia Giulia"],
    [2,"Veneto"], [3,"Lombardia"], [4,"Piemonte"],[5,"Valle d  'Aosta"],
    [6,"Liguria"],[7,"Emilia - Romagna"],[8,"Toscana"],[9,"Marche"], [ 10,"Umbria"], [11,"Lazio"],
    [12,"Abruzzo"],[13,"Campania"], [14,"Sicilia"], [15,"Puglia"],[16,"Calabria"],
    [17,"Sardegna"], [18,"Basilicata"], [19,"Molise"]] ,
        widget=widgets.RadioSelect, blank=True,
    )

    country_natto = models.StringField(
        Label ="Paese di nascita", blank=True,
    )


    occupazione  = models.IntegerField( choices =[[0,  "Occupato"],
    [1,  "Disoccupato"],
    [2,  "Studente"],
    [3,  "Pensionato"],
    [4,  "Altro"]],   widget = widgets.RadioSelect, )

    occupazione_altro = models.StringField( blank=True  )

    Campo_lavoro = models.IntegerField( choices = [[0,"Scienze ambientali"],
    [1,"Scienze forestali o agrarie"],
    [2,"Ingegneria"],
    [3,"Architettura"],
    [4,"Altro  si prega  di  specificare"]], widget = widgets.RadioSelect )

    Campo_lavoro_altro = models.StringField( blank=True  )

    reddito  = models.IntegerField(
        choices=[[0, "Nessuno, non percepisco reddito "], [1, "Meno di € 19,999"], [2, "Tra i € 20.000 e i € 39.999"],
                 [3, "Tra i € 40.000 e i € 69.999"],
                 [4, "Tra i € 70.000 e i € 99.999"], [5, "Tra € 100.000 e i € 199.999"],
                 [6, "Superiore ai € 120.000"]],
        widget=widgets.RadioSelect)

    TARI = models.FloatField(
        label="TAX",
    )


#FUNCTION
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:

        for p in subsession.get_players():
            p.participant.accept = 0
            round_numbers = list(range(1, Constants.num_CE + 1 ))
            #random.shuffle(round_numbers)
            p.participant.contador=1
            p.participant.player_temp_AB = 1

            p.participant.task_rounds = dict(zip(Constants.tasks, round_numbers))
            p.participant.num_players = subsession.session.num_participants
            p.participant.group_pre_A = 0
            p.participant.group_pre_B = 0
            p.participant.group_pre_C = 0
            p.participant.group_elec =0
            p.participant.random_choice = 0
            #p.participant.Test_choices_A = random.randint(0, subsession.session.other_part)
            #p.participant.Test_choices_B = random.randint(0,subsession.session.other_part - p.participant.Test_choices_A)
            #p.participant.Test_choices_C = subsession.session.other_part -p.participant.Test_choices_B - p.participant.Test_choices_A
            #p.participant.Test_choices_A_pred = round(random.random()*subsession.session.other_part,1)
            #p.participant.Test_choices_B_pred = round(random.random()*(subsession.session.other_part-p.participant.Test_choices_A_pred),1)
            #p.participant.Test_choices_C_pred = subsession.session.other_part - p.participant.Test_choices_A_pred - p.participant.Test_choices_B_pred

            #Pred_A = p.participant.Test_choices_A_pred/ subsession.session.other_part
            #Pred_B =  p.participant.Test_choices_B_pred / subsession.session.other_part
            #Pred_C =  p.participant.Test_choices_C_pred  / subsession.session.other_part
            #factor1 = Pred_A * Pred_A + Pred_B * Pred_B + Pred_C * Pred_C
            #p.participant.Test_payoff_a_pred = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_A - factor1),1)
            #p.participant.Test_payoff_b_pred = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_B - factor1),1)
            #p.participant.Test_payoff_c_pred = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_C - factor1),1)

            #p.participant.num_prob_replace = 1
            #p.participant.num_prob_not_replace = 1
            #p.participant.num_Test_choices_A_prob = 1
            #p.participant.num_Test_choices_B_prob = 1
            #p.participant.num_Test_choices_C_prob= 1
            #p.participant.num_payoff_A_guess= 1
            #p.participant.num_payoff_B_guess= 1
            #p.participant.num_payoff_C_guess= 1
            #p.participant.num_Test_choices_A_pred = 1
            #p.participant.num_Test_choices_B_pred = 1
            #p.participant.num_Test_choices_C_pred = 1
            #p.participant.num_Test_payoff_a_pred = 1
            #p.participant.num_Test_payoff_b_pred = 1
            #p.participant.num_Test_payoff_c_pred = 1

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
           payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_A - factor1),1)
           payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_B - factor1),1)
           payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_C - factor1),1)


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
           payoff_a =  round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_A - factor1),1)
           payoff_b =  round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_B - factor1),1)
           payoff_c =  round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * Pred_C - factor1),1)
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



class questionario_base (Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1  and player.participant.accept ==1



###BEHAVIORAL_Questions
class Questionario_1 (Page):
    form_model = 'player'
    form_fields = ['Member_env_group',
                   'green_areas_frequency',
                   'recreational_outdoor',
                   'Own_house',
                   'vivi_affito',
                   'Own_house_green_roof',
                   'Consider_install_green_roof',
                   'Consider_rent_green_roof' ]
    # Behavioural question
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1  and player.participant.accept ==1

###Riks meassurements

class Questionario_2(Page):
        form_model = 'player'
        form_fields = ['Risk_willigness_scale',
                       'R1',
                       'R2',
                       'R3',
                       'R4',
                       'R5']
        @staticmethod
        def is_displayed(player: Player):
            return player.round_number ==  1  and player.participant.accept ==1
# Nature relatedness
class Questionario_3(Page):
            form_model = 'player'
            form_fields = ['NR1',
                           'NR2',
                           'NR3',
                           'NR4',
                           'NR5',
                           'NR6']

            @staticmethod
            def is_displayed(player: Player):
                return player.round_number ==  1  and player.participant.accept ==1

#sense of place
class Questionario_4(Page):
    form_model = 'player'
    form_fields = ['SP1',
                   'SP2',
                   'SP3',
                   'SP4',
                   'SP5']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number ==1  and player.participant.accept ==1

# Green roofs aesthetics  # Green roofs services
class Questionario_5(Page):
        form_model = 'player'
        form_fields = ['AE1',
                       'AE2',
                       'AE3',
                       'AE4',
                       'SGR1',
                        'SGR2',
                       'SGR3']

        @staticmethod
        def is_displayed(player: Player):
            return player.round_number ==1  and player.participant.accept ==1

class Questionario_6(Page):
    form_model = 'player'
    form_fields = ['affected_flooding',
                   'lik_severe_flood',
                   'lik_mild_flood',
                   'serious_problem']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number ==  1  and player.participant.accept ==1

class Questionario_7(Page):
    form_model = 'player'
    form_fields = ['anni_natto',
                   'gender',
                   'person_14_less',
                   'person_15_19',
                   'person_20_40',
                   'person_41_65',
                   'person_65',
                   'Education']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1  and player.participant.accept ==1


class Questionario_8(Page):
    form_model = 'player'
    form_fields = ['residente_trento',
                   'Circoscrizioni_residente',
                   'Circoscrizioni_residente_altro',
                  ]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number ==  1  and player.participant.accept ==1


class Questionario_9(Page):
    form_model = 'player'
    form_fields = [ 'domiciliato_trento',
                     'Circoscrizioni_domiciliato',
                     'Circoscrizioni_domiciliato_altro' ]

    @staticmethod
    def is_displayed(player: Player):
        residente_trento = player.field_maybe_none("residente_trento")
        return   player.round_number ==1 and residente_trento == 1    and player.participant.accept ==1


class Questionario_10(Page):
    form_model = 'player'
    form_fields = [  'lavori_trento',
                     'Circoscrizioni_lavori',
                     'Circoscrizioni_lavori_altro' ]

    @staticmethod
    def is_displayed(player: Player):
        residente_trento = player.field_maybe_none("residente_trento")
        domiciliato_trento = player.field_maybe_none("domiciliato_trento")
        return player.round_number ==  1 \
               and residente_trento == 1 and domiciliato_trento == 1 and player.participant.accept ==1


class Questionario_11(Page):
    form_model = 'player'
    form_fields = [  'nato_trento',
                     'anni_trento',
                     'Regione_nato' ]

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number ==  1  and player.participant.accept ==1


class Questionario_12(Page):
    form_model = 'player'
    form_fields = [  'occupazione',
                     'occupazione_altro',
                     'Campo_lavoro',
                     'Campo_lavoro_altro',
                     'reddito',
                     'TARI']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number ==  1  and player.participant.accept ==1

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
            payoff_a =  round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*a - factor1),1)
            payoff_b =  round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*b - factor1),1)
            payoff_c =  round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*c - factor1),1)
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

class Consent_1(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Consent_2(Page):
    form_model = 'player'
    form_fields = ['accept']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.accept = player.accept

class Consent_3(Page):
    form_model = 'player'
    form_fields = ['futuro_studies']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1  and player.participant.accept ==1

class Consent_4(Page):
    form_model = 'player'
    form_fields = ['nome', 'cognome','email',
                   'numero_di_cellulare','nato_a',
                   'mesi_di_nascita','giorno_di_nascita_30', 'anni_di_nascita']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1  and player.participant.accept ==1 and player.futuro_studies == 1

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
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_4(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_5(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1
    @staticmethod
    def vars_for_template(player):
        max_income = Constants.quadratic_score_A + Constants.quadratic_score_B
        min_income = Constants.quadratic_score_A - Constants.quadratic_score_B
        return dict(max_income=max_income, min_income=min_income)

class Instruction_6(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_7(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1
    @staticmethod
    def vars_for_template(player):
        max_income = Constants.quadratic_score_A + Constants.quadratic_score_B
        min_income = Constants.quadratic_score_A - Constants.quadratic_score_B
        return dict(max_income=max_income, min_income=min_income)

class Instruction_8(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_9(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_10(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_11(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_12_1(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_12_2(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_13(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_14(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_15(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_16(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_17(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_18(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_19(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_20(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_20_2(Page):
    form_model = 'player'
    form_fields = ['TARI']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_21(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

    @staticmethod
    def vars_for_template(player):
        a =  Constants.level1_cost*player.TARI/100
        b = Constants.level2_cost * player.TARI / 100
        c = Constants.level3_cost * player.TARI / 100
        d = Constants.level4_cost * player.TARI / 100
        return dict(a=a, b=b,c=c,d=d)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.TARI= player.TARI

class Instruction_22(Page):

    @staticmethod
    def is_displayed(player: Player):
            return player.round_number == 1 and player.participant.accept ==1

class Instruction_23_practice_CE(Page):


    form_model = 'player'
    form_fields = ['CE_choice_practice']

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

   # @staticmethod
   # def vars_for_template(player):
   #         cost_2 = str(Constants.level1_cost * player.participant.TARI / 100)

    #        cost_1 = str(Constants.level2_cost * player.participant.TARI / 100)

     #       return dict(   costs1=cost_1,
      #              costs2=cost_2)


class Instruction_23_2(Page):


    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_24(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1
    @staticmethod
    def vars_for_template(player):
        max_income = Constants.quadratic_score_A + Constants.quadratic_score_B
        min_income = Constants.quadratic_score_A - Constants.quadratic_score_B
        return dict(max_income=max_income, min_income=min_income)

class Instruction_25_1(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_25_2(Page):

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1
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
        return player.round_number == 1 and player.participant.accept ==1

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
        return player.round_number == 1 and player.participant.accept ==1

    @staticmethod
    def vars_for_template(player):
        return dict(num_participants =player.participant.num_players - 1)

    @staticmethod
    def live_method(player: Player, data):
        if data['clicked_button'] == 1:
            a = player.CE_pract_pred_A / (player.participant.num_players - 1)
            b = player.CE_pract_pred_B / (player.participant.num_players - 1)
            c = player.CE_pract_pred_C / (player.participant.num_players - 1)
            factor1 = a * a + b * b + c * c
            payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * a - factor1), 1)
            payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * b - factor1), 1)
            payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * c - factor1), 1)
            response = dict(payoff_a=payoff_a, payoff_b=payoff_b, payoff_c=payoff_c)
            player.participant.payoff_practice_A = payoff_a
            player.participant.payoff_practice_B = payoff_b
            player.participant.payoff_practice_C = payoff_c
            return {player.id_in_group: response}

    # Passing data from Python to JavaScript (js_vars)
    @staticmethod
    def js_vars(player):
        return dict(number_players=player.participant.num_players, temp=0)

class Instruction_27_2(Page):
    form_model = 'player'
    form_fields = ['CE_pract_pred_A','CE_pract_pred_B','CE_pract_pred_C']
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

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
            payoff_a =  round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*a - factor1),1)
            payoff_b =  round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*b - factor1),1)
            payoff_c =  round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*c - factor1),1)
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
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_29(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1


class Instruction_30(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_31(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

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
        return player.round_number == 1 and player.participant.accept ==1

    @staticmethod
    def vars_for_template(Subsession):

        return dict(chosen_letter=Subsession.session.chosen_letter_2)

class Instruction_32_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_33(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1
    @staticmethod
    def vars_for_template(Subsession):
        return dict(prob_replace=int(Constants.prob_replace*100),
                    prob_NOT_replace=int(Constants.prob_not_replace*100),
                    chosen_letter=Subsession.session.chosen_letter_2)

class Instruction_33_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1
    @staticmethod
    def vars_for_template(Subsession):
        return dict(prob_replace=int(Constants.prob_replace*100),
                    prob_NOT_replace=int(Constants.prob_not_replace*100),
                    chosen_letter=Subsession.session.chosen_letter_2)

class Instruction_34(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_35(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

    @staticmethod
    def vars_for_template(player):
        return dict(prob_replace=int(Constants.prob_replace*100), prob_not_replace=int(Constants.prob_not_replace*100),
                    prob_not_replace_1=int(Constants.prob_not_replace*100 + 1))

class Instruction_36(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

    @staticmethod
    def vars_for_template(Subsession):

        return dict(random_ball_not_replaced=Subsession.session.random_ball_not_replaced,
                    chosen_letter=Subsession.session.chosen_letter_2)

class Instruction_37(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

    @staticmethod
    def vars_for_template(Subsession):
        return dict(random_ball_replaced=Subsession.session.random_ball_replaced)

class Instruction_37_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

class Instruction_38(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1
    @staticmethod
    def vars_for_template(Subsession):

        return dict(chosen_letter=Subsession.session.chosen_letter_2)

class Instruction_39(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1
    @staticmethod
    def vars_for_template(Subsession):
        if Constants.random_practice_alternative == 'A':
            cont=list(range(0,Subsession.session.random_prediction_A_2 ))
            leng=Subsession.session.random_prediction_A_2
            random_prediction_A = Subsession.session.random_prediction_A_2
        else:
            if Constants.random_practice_alternative == 'B':
                cont = list(range(0, Subsession.session.random_prediction_B_2))
                leng = Subsession.session.random_prediction_B_2
                random_prediction_A = Subsession.session.random_prediction_B_2
            else:
                cont = list(range(0, Subsession.session.random_prediction_C_2))
                leng = Subsession.session.random_prediction_C_2
                random_prediction_A = Subsession.session.random_prediction_C_2


        example_prediction_average_A = {i: Subsession.session.example_prediction_average_A[i] for i in range(0, leng)}
        example_prediction_average_B = {i: Subsession.session.example_prediction_average_B[i] for i in
                                        range(0, leng)}
        example_prediction_average_C = {i: Subsession.session.example_prediction_average_C[i] for i in
                                        range(0, leng)}
        listA_2_temp1=Subsession.session.listA_2[0:leng]

        listA_2_temp2 = [s.replace(".", "") for s in listA_2_temp1]
        listA_2 = [s.replace(",", "") for s in listA_2_temp2]

        AverageA = round(sum(Subsession.session.example_prediction_average_A[0:leng] )/leng,1)
        AverageB = round(sum(Subsession.session.example_prediction_average_B[0:leng])/leng,1)
        AverageC = round(sum(Subsession.session.example_prediction_average_C[0:leng] )/leng,1)

        return dict(example_prediction_average_A=example_prediction_average_A,
                    example_prediction_average_B=example_prediction_average_B,
                    example_prediction_average_C=example_prediction_average_C,
                    listA=listA_2 , cont = cont,
                    AverageA=AverageA,
                    AverageB=AverageB,
                    AverageC=AverageC,listA_=Subsession.session.listA_2[0:leng],
                    random_prediction_A=random_prediction_A
                    )

class Instruction_39_2(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1

    @staticmethod
    def vars_for_template(Subsession):
        if Constants.random_practice_alternative == 'A':
            cont = list(range(0, Subsession.session.random_prediction_A_2))
            leng = Subsession.session.random_prediction_A_2
            random_prediction_A = Subsession.session.random_prediction_A_2
        else:
            if Constants.random_practice_alternative == 'B':
                cont = list(range(0, Subsession.session.random_prediction_B_2))
                leng = Subsession.session.random_prediction_B_2
                random_prediction_A = Subsession.session.random_prediction_B_2
            else:
                cont = list(range(0, Subsession.session.random_prediction_C_2))
                leng = Subsession.session.random_prediction_C_2
                random_prediction_A = Subsession.session.random_prediction_C_2

        example_prediction_average_A = {i: Subsession.session.example_prediction_average_A[i] for i in range(0, leng)}
        example_prediction_average_B = {i: Subsession.session.example_prediction_average_B[i] for i in
                                        range(0, leng)}
        example_prediction_average_C = {i: Subsession.session.example_prediction_average_C[i] for i in
                                        range(0, leng)}
        listA_2_temp1 = Subsession.session.listA_2[0:leng]

        listA_2_temp2 = [s.replace(".", "") for s in listA_2_temp1]
        listA_2 = [s.replace(",", "") for s in listA_2_temp2]

        AverageA = round(sum(Subsession.session.example_prediction_average_A[0:leng]) / leng, 1)
        AverageB = round(sum(Subsession.session.example_prediction_average_B[0:leng]) / leng, 1)
        AverageC = round(sum(Subsession.session.example_prediction_average_C[0:leng]) / leng, 1)

        a = AverageA / (Subsession.session.num_participants - 1)
        b = AverageB / (Subsession.session.num_participants - 1)
        c = AverageC / (Subsession.session.num_participants - 1)
        factor1 = a * a + b * b + c * c
        payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * a - factor1), 1)
        payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * b - factor1), 1)
        payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * c - factor1), 1)

        return dict(example_prediction_average_A=example_prediction_average_A,
                    example_prediction_average_B=example_prediction_average_B,
                    example_prediction_average_C=example_prediction_average_C,
                    listA=listA_2, cont=cont,
                    AverageA=AverageA,
                    AverageB=AverageB,
                    AverageC=AverageC,
                    payoff_a=payoff_a,
                    payoff_b=payoff_b,
                    payoff_c=payoff_c,
                    listA_=Subsession.session.listA_2[0:leng],
                    random_prediction_A=random_prediction_A,
                    chosen_letter=Subsession.session.chosen_letter_2)

class Instruction_40(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1 and player.participant.accept ==1
    @staticmethod
    def vars_for_template(Subsession):
        if Constants.random_practice_alternative == 'A':
            cont = list(range(0, Subsession.session.random_prediction_A_2))
            leng = Subsession.session.random_prediction_A_2
            random_prediction_A = Subsession.session.random_prediction_A_2
        else:
            if Constants.random_practice_alternative == 'B':
                cont = list(range(0, Subsession.session.random_prediction_B_2))
                leng = Subsession.session.random_prediction_B_2
                random_prediction_A = Subsession.session.random_prediction_B_2
            else:
                cont = list(range(0, Subsession.session.random_prediction_C_2))
                leng = Subsession.session.random_prediction_C_2
                random_prediction_A = Subsession.session.random_prediction_C_2

        example_prediction_average_A = {i: Subsession.session.example_prediction_average_A[i] for i in range(0, leng)}
        example_prediction_average_B = {i: Subsession.session.example_prediction_average_B[i] for i in
                                        range(0, leng)}
        example_prediction_average_C = {i: Subsession.session.example_prediction_average_C[i] for i in
                                        range(0, leng)}
        listA_2_temp1 = Subsession.session.listA_2[0:leng]

        listA_2_temp2 = [s.replace(".", "") for s in listA_2_temp1]
        listA_2 = [s.replace(",", "") for s in listA_2_temp2]

        AverageA = round(sum(Subsession.session.example_prediction_average_A[0:leng]) / leng, 1)
        AverageB = round(sum(Subsession.session.example_prediction_average_B[0:leng]) / leng, 1)
        AverageC = round(sum(Subsession.session.example_prediction_average_C[0:leng]) / leng, 1)

        a = AverageA / (Subsession.session.num_participants - 1)
        b = AverageB / (Subsession.session.num_participants - 1)
        c = AverageC / (Subsession.session.num_participants - 1)
        factor1 = a * a + b * b + c * c
        payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * a - factor1), 1)
        payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * b - factor1), 1)
        payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * c - factor1), 1)

        return dict(example_prediction_average_A=example_prediction_average_A,
                    example_prediction_average_B=example_prediction_average_B,
                    example_prediction_average_C=example_prediction_average_C,
                    listA=listA_2 , cont = cont,
                    AverageA=AverageA,
                    AverageB=AverageB,
                    AverageC=AverageC,
                    payoff_a=payoff_a,
                    payoff_b=payoff_b,
                    payoff_c=payoff_c,
                    listA_=Subsession.session.listA_2[0:leng],
                    random_prediction_A=random_prediction_A,
                    chosen_letter=Subsession.session.chosen_letter_2)

class CE1(Page):
    form_model = 'player'
    form_fields = ['CE1_choice']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 1 and player.participant.accept ==1

    @staticmethod
    def vars_for_template(player):

        if player.participant.player_temp_AB ==1:
            location_1 = (Constants.CS1_location_A==-1)*Constants.Location_level_1 + \
                         (Constants.CS1_location_A==0)*Constants.Location_level_2 + \
                         (Constants.CS1_location_A==1)*Constants.Location_level_3

            location_2 = (Constants.CS1_location_B == -1) * Constants.Location_level_1 + \
                         (Constants.CS1_location_B == 0) * Constants.Location_level_2 + \
                         (Constants.CS1_location_B == 1) * Constants.Location_level_3

            rainab_1 = (Constants.CS1_rainab_A == -1) * Constants.runoff_level_1 + \
                         (Constants.CS1_rainab_A == 0) * Constants.runoff_level_2 + \
                         (Constants.CS1_rainab_A == 1) * Constants.runoff_level_3

            rainab_2 = (Constants.CS1_rainab_B == -1) * Constants.runoff_level_1 + \
                       (Constants.CS1_rainab_B == 0) * Constants.runoff_level_2 + \
                       (Constants.CS1_rainab_B == 1) * Constants.runoff_level_3

            maintan_1 = (Constants.CS1_maintan_A == -1) * Constants.Maintenance_level_1 + \
                       (Constants.CS1_maintan_A == 0) * Constants.Maintenance_level_2 + \
                       (Constants.CS1_maintan_A == 1) * Constants.Maintenance_level_3

            maintan_2 = (Constants.CS1_maintan_B == -1) * Constants.Maintenance_level_1 + \
                    (Constants.CS1_maintan_B == 0) * Constants.Maintenance_level_2 + \
                    (Constants.CS1_maintan_B == 1) * Constants.Maintenance_level_3


            cost_1 = (Constants.CS1_cost_A == -1) * str(Constants.level1_cost) + \
                        (Constants.CS1_cost_A == 0) * str(Constants.level2_cost) + \
                        (Constants.CS1_cost_A == 1) * str(Constants.level3_cost)

            cost_2 = (Constants.CS1_cost_B == -1) * str(Constants.level1_cost) + \
                 (Constants.CS1_cost_B == 0) * str(Constants.level2_cost ) + \
                 (Constants.CS1_cost_B == 1) * str(Constants.level3_cost )

        else:

            location_1 = (Constants.CS1_location_A == -1) * Constants.Location_level_1 + \
                         (Constants.CS1_location_A == 0) * Constants.Location_level_2 + \
                         (Constants.CS1_location_A == 1) * Constants.Location_level_3

            location_2 = (Constants.CS1_location_B == -1) * Constants.Location_level_1 + \
                         (Constants.CS1_location_B == 0) * Constants.Location_level_2 + \
                         (Constants.CS1_location_B == 1) * Constants.Location_level_3

            rainab_1 = (Constants.CS1_rainab_A == -1) * Constants.runoff_level_1 + \
                       (Constants.CS1_rainab_A == 0) * Constants.runoff_level_2 + \
                       (Constants.CS1_rainab_A == 1) * Constants.runoff_level_3

            rainab_2 = (Constants.CS1_rainab_B == -1) * Constants.runoff_level_1 + \
                       (Constants.CS1_rainab_B == 0) * Constants.runoff_level_2 + \
                       (Constants.CS1_rainab_B == 1) * Constants.runoff_level_3

            maintan_1 = (Constants.CS1_maintan_A == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS1_maintan_A == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS1_maintan_A == 1) * Constants.Maintenance_level_3

            maintan_2 = (Constants.CS1_maintan_B == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS1_maintan_B == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS1_maintan_B == 1) * Constants.Maintenance_level_3

            cost_1 = (Constants.CS1_cost_A == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS1_cost_A == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS1_cost_A == 1) * str(Constants.level3_cost )

            cost_2 = (Constants.CS1_cost_B == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS1_cost_B == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS1_cost_B == 1) * str(Constants.level3_cost )


        return dict(location_1 =location_1,
        location_2 =location_2,
        rainab_1 =rainab_1,
        rainab_2 = rainab_2 ,
        maintan_1 = maintan_1 ,
        maintan_2 = maintan_2 ,
        cost_1 = cost_1 ,
        cost_2= cost_2 ,
        random_display_A_B=player.player_temp_AB)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.contador = player.participant.contador + 1
        player.player_temp_AB = player.participant.player_temp_AB
        if player.player_temp_AB==2:
            if player.CE1_choice==1:
                player.CE1_choice=2
            else:
                if player.CE1_choice==2:
                    player.CE1_choice=1

        #player.participant.player_temp_AB = 1
        # player1 = player.in_round(player.participant.task_rounds['1'])
        # player.participant.CE1_ALL = player1.CE1_choice

class CE2(Page):
    form_model = 'player'
    form_fields = ['CE2_choice']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == 1 and player.participant.accept ==1

    @staticmethod
    def vars_for_template(player):

        if player.participant.player_temp_AB == 1:
            location_1 = (Constants.CS2_location_A == -1) * Constants.Location_level_1 + \
                         (Constants.CS2_location_A == 0) * Constants.Location_level_2 + \
                         (Constants.CS2_location_A == 1) * Constants.Location_level_3

            location_2 = (Constants.CS2_location_B == -1) * Constants.Location_level_1 + \
                         (Constants.CS2_location_B == 0) * Constants.Location_level_2 + \
                         (Constants.CS2_location_B == 1) * Constants.Location_level_3

            rainab_1 = (Constants.CS2_rainab_A == -1) * Constants.runoff_level_1 + \
                       (Constants.CS2_rainab_A == 0) * Constants.runoff_level_2 + \
                       (Constants.CS2_rainab_A == 1) * Constants.runoff_level_3

            rainab_2 = (Constants.CS2_rainab_B == -1) * Constants.runoff_level_1 + \
                       (Constants.CS2_rainab_B == 0) * Constants.runoff_level_2 + \
                       (Constants.CS2_rainab_B == 1) * Constants.runoff_level_3

            maintan_1 = (Constants.CS2_maintan_A == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS2_maintan_A == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS2_maintan_A == 1) * Constants.Maintenance_level_3

            maintan_2 = (Constants.CS2_maintan_B == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS2_maintan_B == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS2_maintan_B == 1) * Constants.Maintenance_level_3

            cost_1 = (Constants.CS2_cost_A == -1) * str(Constants.level1_cost) +\
                     (Constants.CS2_cost_A == 0) * str(Constants.level2_cost )+ \
                     (Constants.CS2_cost_A == 1) * str(Constants.level3_cost  )

            cost_2 = (Constants.CS2_cost_B == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS2_cost_B == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS2_cost_B == 1) * str(Constants.level3_cost )

        else:

            location_1 = (Constants.CS2_location_A == -1) * Constants.Location_level_1 + \
                         (Constants.CS2_location_A == 0) * Constants.Location_level_2 + \
                         (Constants.CS2_location_A == 1) * Constants.Location_level_3

            location_2 = (Constants.CS2_location_B == -1) * Constants.Location_level_1 + \
                         (Constants.CS2_location_B == 0) * Constants.Location_level_2 + \
                         (Constants.CS2_location_B == 1) * Constants.Location_level_3

            rainab_1 = (Constants.CS2_rainab_A == -1) * Constants.runoff_level_1 + \
                       (Constants.CS2_rainab_A == 0) * Constants.runoff_level_2 + \
                       (Constants.CS2_rainab_A == 1) * Constants.runoff_level_3

            rainab_2 = (Constants.CS2_rainab_B == -1) * Constants.runoff_level_1 + \
                       (Constants.CS2_rainab_B == 0) * Constants.runoff_level_2 + \
                       (Constants.CS2_rainab_B == 1) * Constants.runoff_level_3

            maintan_1 = (Constants.CS2_maintan_A == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS2_maintan_A == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS2_maintan_A == 1) * Constants.Maintenance_level_3

            maintan_2 = (Constants.CS2_maintan_B == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS2_maintan_B == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS2_maintan_B == 1) * Constants.Maintenance_level_3

            cost_1 = (Constants.CS2_cost_A == -1) * str(Constants.level1_cost) + \
                     (Constants.CS2_cost_A == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS2_cost_A == 1) * str(Constants.level3_cost )

            cost_2 = (Constants.CS2_cost_B == -1) * str(Constants.level1_cost) + \
                     (Constants.CS2_cost_B == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS2_cost_B == 1) * str(Constants.level3_cost)

        return dict(location_1=location_1,
                    location_2=location_2,
                    rainab_1=rainab_1,
                    rainab_2=rainab_2,
                    maintan_1=maintan_1,
                    maintan_2=maintan_2,
                    cost_1=cost_1,
                    cost_2=cost_2, random_display_A_B=player.player_temp_AB)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.contador = player.participant.contador + 1
        player.player_temp_AB = player.participant.player_temp_AB
        if player.player_temp_AB == 2:
            if player.CE2_choice == 1:
                player.CE2_choice = 2
            else:
                if player.CE2_choice == 2:
                    player.CE2_choice = 1

        # player.participant.player_temp_AB = 1
       # player2 = player.in_round(player.participant.task_rounds['2'])
    # player.participant.CE2_ALL = player2.CE2_choice

class CE3(Page):
    form_model = 'player'
    form_fields = ['CE3_choice']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == 1 and player.participant.accept ==1

    @staticmethod
    def vars_for_template(player):

        if player.participant.player_temp_AB == 1:
            location_1 = (Constants.CS3_location_A == -1) * Constants.Location_level_1 + \
                         (Constants.CS3_location_A == 0) * Constants.Location_level_2 + \
                         (Constants.CS3_location_A == 1) * Constants.Location_level_3

            location_2 = (Constants.CS3_location_B == -1) * Constants.Location_level_1 + \
                         (Constants.CS3_location_B == 0) * Constants.Location_level_2 + \
                         (Constants.CS3_location_B == 1) * Constants.Location_level_3

            rainab_1 = (Constants.CS3_rainab_A == -1) * Constants.runoff_level_1 + \
                       (Constants.CS3_rainab_A == 0) * Constants.runoff_level_2 + \
                       (Constants.CS3_rainab_A == 1) * Constants.runoff_level_3

            rainab_2 = (Constants.CS3_rainab_B == -1) * Constants.runoff_level_1 + \
                       (Constants.CS3_rainab_B == 0) * Constants.runoff_level_2 + \
                       (Constants.CS3_rainab_B == 1) * Constants.runoff_level_3

            maintan_1 = (Constants.CS3_maintan_A == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS3_maintan_A == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS3_maintan_A == 1) * Constants.Maintenance_level_3

            maintan_2 = (Constants.CS3_maintan_B == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS3_maintan_B == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS3_maintan_B == 1) * Constants.Maintenance_level_3

            cost_1 = (Constants.CS3_cost_A == -1) * str(Constants.level1_cost)   + \
                     (Constants.CS3_cost_A == 0) * str(Constants.level2_cost)  + \
                     (Constants.CS3_cost_A == 1) * str(Constants.level3_cost)

            cost_2 = (Constants.CS3_cost_B == -1) * str(Constants.level1_cost) + \
                     (Constants.CS3_cost_B == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS3_cost_B == 1) * str(Constants.level3_cost )

        else:

            location_1 = (Constants.CS3_location_A == -1) * Constants.Location_level_1 + \
                         (Constants.CS3_location_A == 0) * Constants.Location_level_2 + \
                         (Constants.CS3_location_A == 1) * Constants.Location_level_3

            location_2 = (Constants.CS3_location_B == -1) * Constants.Location_level_1 + \
                         (Constants.CS3_location_B == 0) * Constants.Location_level_2 + \
                         (Constants.CS3_location_B == 1) * Constants.Location_level_3

            rainab_1 = (Constants.CS3_rainab_A == -1) * Constants.runoff_level_1 + \
                       (Constants.CS3_rainab_A == 0) * Constants.runoff_level_2 + \
                       (Constants.CS3_rainab_A == 1) * Constants.runoff_level_3

            rainab_2 = (Constants.CS3_rainab_B == -1) * Constants.runoff_level_1 + \
                       (Constants.CS3_rainab_B == 0) * Constants.runoff_level_2 + \
                       (Constants.CS3_rainab_B == 1) * Constants.runoff_level_3

            maintan_1 = (Constants.CS3_maintan_A == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS3_maintan_A == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS3_maintan_A == 1) * Constants.Maintenance_level_3

            maintan_2 = (Constants.CS3_maintan_B == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS3_maintan_B == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS3_maintan_B == 1) * Constants.Maintenance_level_3

            cost_1 = (Constants.CS3_cost_A == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS3_cost_A == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS3_cost_A == 1) * str(Constants.level3_cost)

            cost_2 = (Constants.CS3_cost_B == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS3_cost_B == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS3_cost_B == 1) * str(Constants.level3_cost )

        return dict(location_1=location_1,
                    location_2=location_2,
                    rainab_1=rainab_1,
                    rainab_2=rainab_2,
                    maintan_1=maintan_1,
                    maintan_2=maintan_2,
                    cost_1=cost_1,
                    cost_2=cost_2, random_display_A_B=player.player_temp_AB)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.contador = player.participant.contador + 1
        player.player_temp_AB = player.participant.player_temp_AB
        if player.player_temp_AB == 2:
            if player.CE3_choice == 1:
                player.CE3_choice = 2
            else:
                if player.CE3_choice == 2:
                    player.CE3_choice = 1

        # player.participant.player_temp_AB = 1
        # player3 = player.in_round(player.participant.task_rounds['3'])
        # player.participant.CE3_ALL = player3.CE3_choice

class CE4(Page):
    form_model = 'player'
    form_fields = ['CE4_choice']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 1 and player.participant.accept ==1

    @staticmethod
    def vars_for_template(player):

        if player.participant.player_temp_AB == 1:
            location_1 = (Constants.CS4_location_A == -1) * Constants.Location_level_1 + \
                         (Constants.CS4_location_A == 0) * Constants.Location_level_2 + \
                         (Constants.CS4_location_A == 1) * Constants.Location_level_3

            location_2 = (Constants.CS4_location_B == -1) * Constants.Location_level_1 + \
                         (Constants.CS4_location_B == 0) * Constants.Location_level_2 + \
                         (Constants.CS4_location_B == 1) * Constants.Location_level_3

            rainab_1 = (Constants.CS4_rainab_A == -1) * Constants.runoff_level_1 + \
                       (Constants.CS4_rainab_A == 0) * Constants.runoff_level_2 + \
                       (Constants.CS4_rainab_A == 1) * Constants.runoff_level_3

            rainab_2 = (Constants.CS4_rainab_B == -1) * Constants.runoff_level_1 + \
                       (Constants.CS4_rainab_B == 0) * Constants.runoff_level_2 + \
                       (Constants.CS4_rainab_B == 1) * Constants.runoff_level_3

            maintan_1 = (Constants.CS4_maintan_A == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS4_maintan_A == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS4_maintan_A == 1) * Constants.Maintenance_level_3

            maintan_2 = (Constants.CS4_maintan_B == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS4_maintan_B == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS4_maintan_B == 1) * Constants.Maintenance_level_3

            cost_1 = (Constants.CS4_cost_A == -1) * str(Constants.level1_cost) + \
                     (Constants.CS4_cost_A == 0) * str(Constants.level2_cost )+ \
                     (Constants.CS4_cost_A == 1) * str(Constants.level3_cost )

            cost_2 = (Constants.CS4_cost_B == -1) * str(Constants.level1_cost) + \
                     (Constants.CS4_cost_B == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS4_cost_B == 1) * str(Constants.level3_cost )

        else:

            location_1 = (Constants.CS4_location_A == -1) * Constants.Location_level_1 + \
                         (Constants.CS4_location_A == 0) * Constants.Location_level_2 + \
                         (Constants.CS4_location_A == 1) * Constants.Location_level_3

            location_2 = (Constants.CS4_location_B == -1) * Constants.Location_level_1 + \
                         (Constants.CS4_location_B == 0) * Constants.Location_level_2 + \
                         (Constants.CS4_location_B == 1) * Constants.Location_level_3

            rainab_1 = (Constants.CS4_rainab_A == -1) * Constants.runoff_level_1 + \
                       (Constants.CS4_rainab_A == 0) * Constants.runoff_level_2 + \
                       (Constants.CS4_rainab_A == 1) * Constants.runoff_level_3

            rainab_2 = (Constants.CS4_rainab_B == -1) * Constants.runoff_level_1 + \
                       (Constants.CS4_rainab_B == 0) * Constants.runoff_level_2 + \
                       (Constants.CS4_rainab_B == 1) * Constants.runoff_level_3

            maintan_1 = (Constants.CS4_maintan_A == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS4_maintan_A == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS4_maintan_A == 1) * Constants.Maintenance_level_3

            maintan_2 = (Constants.CS4_maintan_B == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS4_maintan_B == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS4_maintan_B == 1) * Constants.Maintenance_level_3

            cost_1 = (Constants.CS4_cost_A == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS4_cost_A == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS4_cost_A == 1) * str(Constants.level3_cost )

            cost_2 = (Constants.CS4_cost_B == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS4_cost_B == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS4_cost_B == 1) * str(Constants.level3_cost )

        return dict(location_1=location_1,
                    location_2=location_2,
                    rainab_1=rainab_1,
                    rainab_2=rainab_2,
                    maintan_1=maintan_1,
                    maintan_2=maintan_2,
                    cost_1=cost_1,
                    cost_2=cost_2, random_display_A_B=player.player_temp_AB)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.contador = player.participant.contador + 1
        player.player_temp_AB = player.participant.player_temp_AB
        if player.player_temp_AB == 2:
            if player.CE4_choice == 1:
                player.CE4_choice = 2
            else:
                if player.CE4_choice == 2:
                    player.CE4_choice = 1

        #  player.participant.player_temp_AB = 1
        # player4 = player.in_round(player.participant.task_rounds['4'])
        # player.participant.CE4_ALL = player4.CE4_choice

class CE5(Page):
    form_model = 'player'
    form_fields = ['CE5_choice']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == 1 and player.participant.accept ==1

    @staticmethod
    def vars_for_template(player):

        if player.participant.player_temp_AB == 1:
            location_1 = (Constants.CS5_location_A == -1) * Constants.Location_level_1 + \
                         (Constants.CS5_location_A == 0) * Constants.Location_level_2 + \
                         (Constants.CS5_location_A == 1) * Constants.Location_level_3

            location_2 = (Constants.CS5_location_B == -1) * Constants.Location_level_1 + \
                         (Constants.CS5_location_B == 0) * Constants.Location_level_2 + \
                         (Constants.CS5_location_B == 1) * Constants.Location_level_3

            rainab_1 = (Constants.CS5_rainab_A == -1) * Constants.runoff_level_1 + \
                       (Constants.CS5_rainab_A == 0) * Constants.runoff_level_2 + \
                       (Constants.CS5_rainab_A == 1) * Constants.runoff_level_3

            rainab_2 = (Constants.CS5_rainab_B == -1) * Constants.runoff_level_1 + \
                       (Constants.CS5_rainab_B == 0) * Constants.runoff_level_2 + \
                       (Constants.CS5_rainab_B == 1) * Constants.runoff_level_3

            maintan_1 = (Constants.CS5_maintan_A == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS5_maintan_A == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS5_maintan_A == 1) * Constants.Maintenance_level_3

            maintan_2 = (Constants.CS5_maintan_B == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS5_maintan_B == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS5_maintan_B == 1) * Constants.Maintenance_level_3

            cost_1 = (Constants.CS5_cost_A == -1) * str(Constants.level1_cost)   + \
                     (Constants.CS5_cost_A == 0) * str(Constants.level2_cost)  + \
                     (Constants.CS5_cost_A == 1) * str(Constants.level3_cost )

            cost_2 = (Constants.CS5_cost_B == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS5_cost_B == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS5_cost_B == 1) * str(Constants.level3_cost )

        else:

            location_1 = (Constants.CS5_location_A == -1) * Constants.Location_level_1 + \
                         (Constants.CS5_location_A == 0) * Constants.Location_level_2 + \
                         (Constants.CS5_location_A == 1) * Constants.Location_level_3

            location_2 = (Constants.CS5_location_B == -1) * Constants.Location_level_1 + \
                         (Constants.CS5_location_B == 0) * Constants.Location_level_2 + \
                         (Constants.CS5_location_B == 1) * Constants.Location_level_3

            rainab_1 = (Constants.CS5_rainab_A == -1) * Constants.runoff_level_1 + \
                       (Constants.CS5_rainab_A == 0) * Constants.runoff_level_2 + \
                       (Constants.CS5_rainab_A == 1) * Constants.runoff_level_3

            rainab_2 = (Constants.CS5_rainab_B == -1) * Constants.runoff_level_1 + \
                       (Constants.CS5_rainab_B == 0) * Constants.runoff_level_2 + \
                       (Constants.CS5_rainab_B == 1) * Constants.runoff_level_3

            maintan_1 = (Constants.CS5_maintan_A == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS5_maintan_A == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS5_maintan_A == 1) * Constants.Maintenance_level_3

            maintan_2 = (Constants.CS5_maintan_B == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS5_maintan_B == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS5_maintan_B == 1) * Constants.Maintenance_level_3

            cost_1 = (Constants.CS5_cost_A == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS5_cost_A == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS5_cost_A == 1) * str(Constants.level3_cost )

            cost_2 = (Constants.CS5_cost_B == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS5_cost_B == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS5_cost_B == 1) * str(Constants.level3_cost )

        return dict(location_1=location_1,
                    location_2=location_2,
                    rainab_1=rainab_1,
                    rainab_2=rainab_2,
                    maintan_1=maintan_1,
                    maintan_2=maintan_2,
                    cost_1=cost_1,
                    cost_2=cost_2, random_display_A_B=player.player_temp_AB)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.contador = player.participant.contador + 1
        player.player_temp_AB = player.participant.player_temp_AB
        if player.player_temp_AB == 2:
            if player.CE5_choice == 1:
                player.CE5_choice = 2
            else:
                if player.CE5_choice == 2:
                    player.CE5_choice = 1

        #   player.participant.player_temp_AB = 1
        #   player5 = player.in_round(player.participant.task_rounds['5'])
        #  player.participant.CE5_ALL = player5.CE5_choice

class CE6(Page):
    form_model = 'player'
    form_fields = ['CE6_choice']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == 1 and player.participant.accept ==1

    @staticmethod
    def vars_for_template(player):

        if player.participant.player_temp_AB == 1:
            location_1 = (Constants.CS6_location_A == -1) * Constants.Location_level_1 + \
                         (Constants.CS6_location_A == 0) * Constants.Location_level_2 + \
                         (Constants.CS6_location_A == 1) * Constants.Location_level_3

            location_2 = (Constants.CS6_location_B == -1) * Constants.Location_level_1 + \
                         (Constants.CS6_location_B == 0) * Constants.Location_level_2 + \
                         (Constants.CS6_location_B == 1) * Constants.Location_level_3

            rainab_1 = (Constants.CS6_rainab_A == -1) * Constants.runoff_level_1 + \
                       (Constants.CS6_rainab_A == 0) * Constants.runoff_level_2 + \
                       (Constants.CS6_rainab_A == 1) * Constants.runoff_level_3

            rainab_2 = (Constants.CS6_rainab_B == -1) * Constants.runoff_level_1 + \
                       (Constants.CS6_rainab_B == 0) * Constants.runoff_level_2 + \
                       (Constants.CS6_rainab_B == 1) * Constants.runoff_level_3

            maintan_1 = (Constants.CS6_maintan_A == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS6_maintan_A == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS6_maintan_A == 1) * Constants.Maintenance_level_3

            maintan_2 = (Constants.CS6_maintan_B == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS6_maintan_B == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS6_maintan_B == 1) * Constants.Maintenance_level_3

            cost_1 = (Constants.CS6_cost_A == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS6_cost_A == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS6_cost_A == 1) * str(Constants.level3_cost )+ \
                     (Constants.CS6_cost_A == 2) * str(Constants.level4_cost)

            cost_2 = (Constants.CS6_cost_B == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS6_cost_B == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS6_cost_B == 1) * str(Constants.level3_cost ) +\
                     (Constants.CS6_cost_B == 2) * str(Constants.level4_cost)

        else:

            location_1 = (Constants.CS6_location_A == -1) * Constants.Location_level_1 + \
                         (Constants.CS6_location_A == 0) * Constants.Location_level_2 + \
                         (Constants.CS6_location_A == 1) * Constants.Location_level_3

            location_2 = (Constants.CS6_location_B == -1) * Constants.Location_level_1 + \
                         (Constants.CS6_location_B == 0) * Constants.Location_level_2 + \
                         (Constants.CS6_location_B == 1) * Constants.Location_level_3

            rainab_1 = (Constants.CS6_rainab_A == -1) * Constants.runoff_level_1 + \
                       (Constants.CS6_rainab_A == 0) * Constants.runoff_level_2 + \
                       (Constants.CS6_rainab_A == 1) * Constants.runoff_level_3

            rainab_2 = (Constants.CS6_rainab_B == -1) * Constants.runoff_level_1 + \
                       (Constants.CS6_rainab_B == 0) * Constants.runoff_level_2 + \
                       (Constants.CS6_rainab_B == 1) * Constants.runoff_level_3

            maintan_1 = (Constants.CS6_maintan_A == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS6_maintan_A == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS6_maintan_A == 1) * Constants.Maintenance_level_3

            maintan_2 = (Constants.CS6_maintan_B == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS6_maintan_B == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS6_maintan_B == 1) * Constants.Maintenance_level_3

            cost_1 = (Constants.CS6_cost_A == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS6_cost_A == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS6_cost_A == 1) * str(Constants.level3_cost ) + \
                     (Constants.CS6_cost_A == 2) * str(Constants.level4_cost)

            cost_2 = (Constants.CS6_cost_B == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS6_cost_B == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS6_cost_B == 1) * str(Constants.level3_cost )+\
                    (Constants.CS6_cost_B == 2) * str(Constants.level4_cost)


        return dict(location_1=location_1,
                    location_2=location_2,
                    rainab_1=rainab_1,
                    rainab_2=rainab_2,
                    maintan_1=maintan_1,
                    maintan_2=maintan_2,
                    cost_1=cost_1,
                    cost_2=cost_2, random_display_A_B=player.player_temp_AB)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.contador = player.participant.contador + 1
        player.player_temp_AB = player.participant.player_temp_AB
        if player.player_temp_AB == 2:
            if player.CE6_choice == 1:
                player.CE6_choice = 2
            else:
                if player.CE6_choice == 2:
                    player.CE6_choice = 1

        #  player.participant.player_temp_AB = 1
        #  player6 = player.in_round(player.participant.task_rounds['6'])
        # player.participant.CE6_ALL = player6.CE6_choice

class CE7(Page):
    form_model = 'player'
    form_fields = ['CE7_choice']

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant
        return player.round_number == 1 and player.participant.accept ==1

    @staticmethod
    def vars_for_template(player):

        if player.participant.player_temp_AB == 1:
            location_1 = (Constants.CS7_location_A == -1) * Constants.Location_level_1 + \
                         (Constants.CS7_location_A == 0) * Constants.Location_level_2 + \
                         (Constants.CS7_location_A == 1) * Constants.Location_level_3

            location_2 = (Constants.CS7_location_B == -1) * Constants.Location_level_1 + \
                         (Constants.CS7_location_B == 0) * Constants.Location_level_2 + \
                         (Constants.CS7_location_B == 1) * Constants.Location_level_3

            rainab_1 = (Constants.CS7_rainab_A == -1) * Constants.runoff_level_1 + \
                       (Constants.CS7_rainab_A == 0) * Constants.runoff_level_2 + \
                       (Constants.CS7_rainab_A == 1) * Constants.runoff_level_3

            rainab_2 = (Constants.CS7_rainab_B == -1) * Constants.runoff_level_1 + \
                       (Constants.CS7_rainab_B == 0) * Constants.runoff_level_2 + \
                       (Constants.CS7_rainab_B == 1) * Constants.runoff_level_3

            maintan_1 = (Constants.CS7_maintan_A == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS7_maintan_A == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS7_maintan_A == 1) * Constants.Maintenance_level_3

            maintan_2 = (Constants.CS7_maintan_B == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS7_maintan_B == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS7_maintan_B == 1) * Constants.Maintenance_level_3

            cost_1 = (Constants.CS7_cost_A == -1) * str(Constants.level1_cost) + \
                     (Constants.CS7_cost_A == 0) * str(Constants.level2_cost)+ \
                     (Constants.CS7_cost_A == 1) * str(Constants.level3_cost )+ \
                     (Constants.CS7_cost_A == 2) * str(Constants.level4_cost)

            cost_2 = (Constants.CS7_cost_B == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS7_cost_B == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS7_cost_B == 1) * str(Constants.level3_cost)+ \
                     (Constants.CS7_cost_B == 2) * str(Constants.level4_cost)


        else:

            location_1 = (Constants.CS7_location_A == -1) * Constants.Location_level_1 + \
                         (Constants.CS7_location_A == 0) * Constants.Location_level_2 + \
                         (Constants.CS7_location_A == 1) * Constants.Location_level_3

            location_2 = (Constants.CS7_location_B == -1) * Constants.Location_level_1 + \
                         (Constants.CS7_location_B == 0) * Constants.Location_level_2 + \
                         (Constants.CS7_location_B == 1) * Constants.Location_level_3

            rainab_1 = (Constants.CS7_rainab_A == -1) * Constants.runoff_level_1 + \
                       (Constants.CS7_rainab_A == 0) * Constants.runoff_level_2 + \
                       (Constants.CS7_rainab_A == 1) * Constants.runoff_level_3

            rainab_2 = (Constants.CS7_rainab_B == -1) * Constants.runoff_level_1 + \
                       (Constants.CS7_rainab_B == 0) * Constants.runoff_level_2 + \
                       (Constants.CS7_rainab_B == 1) * Constants.runoff_level_3

            maintan_1 = (Constants.CS7_maintan_A == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS7_maintan_A == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS7_maintan_A == 1) * Constants.Maintenance_level_3

            maintan_2 = (Constants.CS7_maintan_B == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS7_maintan_B == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS7_maintan_B == 1) * Constants.Maintenance_level_3

            cost_1 = (Constants.CS7_cost_A == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS7_cost_A == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS7_cost_A == 1) * str(Constants.level3_cost )+ \
                     (Constants.CS7_cost_A == 2) * str(Constants.level4_cost)

            cost_2 = (Constants.CS7_cost_B == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS7_cost_B == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS7_cost_B == 1) * str(Constants.level3_cost ) + \
                     (Constants.CS7_cost_B == 2) * str(Constants.level4_cost)

        return dict(location_1=location_1,
                    location_2=location_2,
                    rainab_1=rainab_1,
                    rainab_2=rainab_2,
                    maintan_1=maintan_1,
                    maintan_2=maintan_2,
                    cost_1=cost_1,
                    cost_2=cost_2, random_display_A_B=player.player_temp_AB)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.contador = player.participant.contador + 1
        player.player_temp_AB = player.participant.player_temp_AB
        if player.player_temp_AB == 2:
            if player.CE7_choice == 1:
                player.CE7_choice = 2
            else:
                if player.CE7_choice == 2:
                    player.CE7_choice = 1

        #  player.participant.player_temp_AB = 1
        # player7 = player.in_round(player.participant.task_rounds['7'])
        #  player.participant.CE7_ALL = player7.CE7_choice

class CE8(Page):
    form_model = 'player'
    form_fields = ['CE8_choice']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number ==1 and player.participant.accept ==1

    @staticmethod
    def vars_for_template(player):

        if player.participant.player_temp_AB == 1:
            location_1 = (Constants.CS8_location_A == -1) * Constants.Location_level_1 + \
                         (Constants.CS8_location_A == 0) * Constants.Location_level_2 + \
                         (Constants.CS8_location_A == 1) * Constants.Location_level_3

            location_2 = (Constants.CS8_location_B == -1) * Constants.Location_level_1 + \
                         (Constants.CS8_location_B == 0) * Constants.Location_level_2 + \
                         (Constants.CS8_location_B == 1) * Constants.Location_level_3

            rainab_1 = (Constants.CS8_rainab_A == -1) * Constants.runoff_level_1 + \
                       (Constants.CS8_rainab_A == 0) * Constants.runoff_level_2 + \
                       (Constants.CS8_rainab_A == 1) * Constants.runoff_level_3

            rainab_2 = (Constants.CS8_rainab_B == -1) * Constants.runoff_level_1 + \
                       (Constants.CS8_rainab_B == 0) * Constants.runoff_level_2 + \
                       (Constants.CS8_rainab_B == 1) * Constants.runoff_level_3

            maintan_1 = (Constants.CS8_maintan_A == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS8_maintan_A == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS8_maintan_A == 1) * Constants.Maintenance_level_3

            maintan_2 = (Constants.CS8_maintan_B == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS8_maintan_B == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS8_maintan_B == 1) * Constants.Maintenance_level_3

            cost_1 = (Constants.CS8_cost_A == -1) *  str(Constants.level1_cost)  + \
                     (Constants.CS8_cost_A == 0) *  str(Constants.level2_cost)  + \
                     (Constants.CS8_cost_A == 1) *  str(Constants.level3_cost)

            cost_2 = (Constants.CS8_cost_B == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS8_cost_B == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS8_cost_B == 1) * str(Constants.level3_cost )

        else:

            location_1 = (Constants.CS8_location_A == -1) * Constants.Location_level_1 + \
                         (Constants.CS8_location_A == 0) * Constants.Location_level_2 + \
                         (Constants.CS8_location_A == 1) * Constants.Location_level_3

            location_2 = (Constants.CS8_location_B == -1) * Constants.Location_level_1 + \
                         (Constants.CS8_location_B == 0) * Constants.Location_level_2 + \
                         (Constants.CS8_location_B == 1) * Constants.Location_level_3

            rainab_1 = (Constants.CS8_rainab_A == -1) * Constants.runoff_level_1 + \
                       (Constants.CS8_rainab_A == 0) * Constants.runoff_level_2 + \
                       (Constants.CS8_rainab_A == 1) * Constants.runoff_level_3

            rainab_2 = (Constants.CS8_rainab_B == -1) * Constants.runoff_level_1 + \
                       (Constants.CS8_rainab_B == 0) * Constants.runoff_level_2 + \
                       (Constants.CS8_rainab_B == 1) * Constants.runoff_level_3

            maintan_1 = (Constants.CS8_maintan_A == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS8_maintan_A == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS8_maintan_A == 1) * Constants.Maintenance_level_3

            maintan_2 = (Constants.CS8_maintan_B == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS8_maintan_B == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS8_maintan_B == 1) * Constants.Maintenance_level_3

            cost_1 = (Constants.CS8_cost_A == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS8_cost_A == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS8_cost_A == 1) * str(Constants.level3_cost )

            cost_2 = (Constants.CS8_cost_B == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS8_cost_B == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS8_cost_B == 1) * str(Constants.level3_cost )

        return dict(location_1=location_1,
                    location_2=location_2,
                    rainab_1=rainab_1,
                    rainab_2=rainab_2,
                    maintan_1=maintan_1,
                    maintan_2=maintan_2,
                    cost_1=cost_1,
                    cost_2=cost_2, random_display_A_B=player.player_temp_AB)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.contador = player.participant.contador + 1
        player.player_temp_AB = player.participant.player_temp_AB
        if player.player_temp_AB == 2:
            if player.CE8_choice == 1:
                player.CE8_choice = 2
            else:
                if player.CE8_choice == 2:
                    player.CE8_choice = 1

        #  player.participant.player_temp_AB = 1

        # player8 = player.in_round(player.participant.task_rounds['8'])
        #  player.participant.CE8_ALL = player8.CE8_choice

class CE9(Page):
    form_model = 'player'
    form_fields = ['CE9_choice']
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == 1 and player.participant.accept ==1

    @staticmethod
    def vars_for_template(player):

        if player.participant.player_temp_AB == 1:
            location_1 = (Constants.CS9_location_A == -1) * Constants.Location_level_1 + \
                         (Constants.CS9_location_A == 0) * Constants.Location_level_2 + \
                         (Constants.CS9_location_A == 1) * Constants.Location_level_3

            location_2 = (Constants.CS9_location_B == -1) * Constants.Location_level_1 + \
                         (Constants.CS9_location_B == 0) * Constants.Location_level_2 + \
                         (Constants.CS9_location_B == 1) * Constants.Location_level_3

            rainab_1 = (Constants.CS9_rainab_A == -1) * Constants.runoff_level_1 + \
                       (Constants.CS9_rainab_A == 0) * Constants.runoff_level_2 + \
                       (Constants.CS9_rainab_A == 1) * Constants.runoff_level_3

            rainab_2 = (Constants.CS9_rainab_B == -1) * Constants.runoff_level_1 + \
                       (Constants.CS9_rainab_B == 0) * Constants.runoff_level_2 + \
                       (Constants.CS9_rainab_B == 1) * Constants.runoff_level_3

            maintan_1 = (Constants.CS9_maintan_A == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS9_maintan_A == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS9_maintan_A == 1) * Constants.Maintenance_level_3

            maintan_2 = (Constants.CS9_maintan_B == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS9_maintan_B == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS9_maintan_B == 1) * Constants.Maintenance_level_3

            cost_1 = (Constants.CS9_cost_A == -1) * str( Constants.level1_cost )+ \
                     (Constants.CS9_cost_A == 0) * str(Constants.level2_cost) + \
                     (Constants.CS9_cost_A == 1) * str(Constants.level3_cost )

            cost_2 = (Constants.CS9_cost_B == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS9_cost_B == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS9_cost_B == 1) * str(Constants.level3_cost )

        else:

            location_1 = (Constants.CS9_location_A == -1) * Constants.Location_level_1 + \
                         (Constants.CS9_location_A == 0) * Constants.Location_level_2 + \
                         (Constants.CS9_location_A == 1) * Constants.Location_level_3

            location_2 = (Constants.CS9_location_B == -1) * Constants.Location_level_1 + \
                         (Constants.CS9_location_B == 0) * Constants.Location_level_2 + \
                         (Constants.CS9_location_B == 1) * Constants.Location_level_3

            rainab_1 = (Constants.CS9_rainab_A == -1) * Constants.runoff_level_1 + \
                       (Constants.CS9_rainab_A == 0) * Constants.runoff_level_2 + \
                       (Constants.CS9_rainab_A == 1) * Constants.runoff_level_3

            rainab_2 = (Constants.CS9_rainab_B == -1) * Constants.runoff_level_1 + \
                       (Constants.CS9_rainab_B == 0) * Constants.runoff_level_2 + \
                       (Constants.CS9_rainab_B == 1) * Constants.runoff_level_3

            maintan_1 = (Constants.CS9_maintan_A == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS9_maintan_A == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS9_maintan_A == 1) * Constants.Maintenance_level_3

            maintan_2 = (Constants.CS9_maintan_B == -1) * Constants.Maintenance_level_1 + \
                        (Constants.CS9_maintan_B == 0) * Constants.Maintenance_level_2 + \
                        (Constants.CS9_maintan_B == 1) * Constants.Maintenance_level_3

            cost_1 = (Constants.CS9_cost_A == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS9_cost_A == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS9_cost_A == 1) * str(Constants.level3_cost )

            cost_2 = (Constants.CS9_cost_B == -1) * str(Constants.level1_cost ) + \
                     (Constants.CS9_cost_B == 0) * str(Constants.level2_cost ) + \
                     (Constants.CS9_cost_B == 1) * str(Constants.level3_cost)

        return dict(location_1=location_1,
                    location_2=location_2,
                    rainab_1=rainab_1,
                    rainab_2=rainab_2,
                    maintan_1=maintan_1,
                    maintan_2=maintan_2,
                    cost_1=cost_1,
                    cost_2=cost_2, random_display_A_B=player.player_temp_AB)

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.contador = player.participant.contador + 1
        player.player_temp_AB = player.participant.player_temp_AB
        if player.player_temp_AB == 2:
            if player.CE9_choice == 1:
                player.CE9_choice = 2
            else:
                if player.CE9_choice == 2:
                    player.CE9_choice = 1

        #  player.participant.player_temp_AB = 1

        #  player9 = player.in_round(player.participant.task_rounds['9'])
        #  player.participant.CE9_ALL = player9.CE9_choice

class remarks(Page):

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number ==1

class grazie(Page):

    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number ==1

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
            payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*a - factor1),1)
            payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*b - factor1),1)
            payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*c - factor1),1)
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
            payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * a - factor1),1)
            payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * b - factor1),1)
            payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * c - factor1),1)
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
                payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * a - factor1),1)
                payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * b - factor1),1)
                payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * c - factor1),1)
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
            payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*a - factor1),1)
            payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*b - factor1),1)
            payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*c - factor1),1)
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
            payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * a - factor1),1)
            payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * b - factor1),1)
            payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * c - factor1),1)
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
                payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * a - factor1),1)
                payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * b - factor1),1)
                payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * c - factor1),1)
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
            payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*a - factor1),1)
            payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*b - factor1),1)
            payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B*(2*c - factor1),1)
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
            payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * a - factor1),1)
            payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * b - factor1),1)
            payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * c - factor1),1)
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
                payoff_a = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * a - factor1),1)
                payoff_b = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * b - factor1),1)
                payoff_c = round(Constants.quadratic_score_A + Constants.quadratic_score_B * (2 * c - factor1),1)
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


page_sequence = [
    Introduction,
    Instruction_1,
    Instruction_2,
    Consent_1,
    Consent_2,
    Consent_3,
    Consent_4,
    Instruction_3,
    Instruction_4,
    Instruction_5,
    Instruction_8,
    Instruction_9,
    Instruction_10,
    Instruction_11,
    Instruction_12_1,
    #Instruction_12_2,
    Instruction_13,
    Instruction_14,
    Instruction_15,
    Instruction_16,
    Instruction_17,
    Instruction_19,
    Instruction_20,
    Instruction_22,
    Instruction_23_practice_CE,
    Instruction_23_2,
    CE1,
    CE2,
    CE3,
    CE4,
    CE5,
    CE6,
    CE7,
    CE8,
    CE9,
    questionario_base,
    Questionario_1,
    Questionario_2,
    Questionario_3,
    Questionario_4,
    Questionario_5,
    Questionario_6,
    Questionario_7,
    Questionario_8,
    Questionario_9,
    Questionario_10,
    Questionario_11,
    Questionario_12,
    remarks,
    grazie,
        ]
