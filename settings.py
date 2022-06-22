from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.000, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    dict(
        name='DCM_1to9',
        display_name="Mattina_DCM-control-CS_1to9",
        num_demo_participants=3,
        app_sequence=['DCM_italian_final'],
    ),
    dict(
        name='DCM_9to1',
        display_name="Pomerggio_DCM-control-CS_9to1",
        num_demo_participants=3,
        app_sequence=['DCM_italian_final2'],
    ),
dict(
        name='Mattina_CM_Treatment_1to9',
        display_name="CM_Treatment_1to9",
        num_demo_participants=4,
        app_sequence=['DCM_treatment_final_tat_18'],
    ),
dict(
        name='Pomeriggio_CM_Treatment_9to1',
        display_name="CM_Treatment_9to1",
        num_demo_participants=4,
        app_sequence=['DCM_treatment_final_tat_18_2'],
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'
INSTALLED_APPS = ['otree']

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

ROOMS = [
    dict(
        name='pilot_1',
        display_name = 'Studio Pilota 1',
        participant_label_file='rooms/pilot1label.txt',
        use_secure_urls=True
    ),
    dict(
        name='pilot_2',
        display_name='Studio Pilota 2',
        participant_label_file='rooms/pilot2label.txt',
        use_secure_urls=True
    ),
    dict(
        name='21_Giugno_Mattina',
        display_name='21 Giugno Mattina',
        participant_label_file='rooms/21_giugno_matt.txt',
        use_secure_urls=True
    ),
    dict(
        name='21_Giugno_Pomeriggio',
        display_name='21 Giugno Pomeriggio',
        participant_label_file='rooms/21_giugno_pom.txt',
        use_secure_urls=True
    ),
    dict(
        name='22_Giugno_Mattina',
        display_name='22 Giugno Mattina',
        participant_label_file='rooms/22_giugno_matt.txt',
        use_secure_urls=True
    ),
    dict(
        name='22_Giugno_Pomeriggio',
        display_name='22 Giugno Pomeriggio',
        participant_label_file='rooms/22_giugno_pom.txt',
        use_secure_urls=True
    ),
    dict(
        name='24_Giugno_Mattina',
        display_name='24 Giugno Mattina',
        participant_label_file='rooms/24_giugno_matt.txt',
        use_secure_urls=True
    ),
    dict(
        name='24_Giugno_Pomeriggio',
        display_name='24 Giugno Pomeriggio',
        participant_label_file='rooms/24_giugno_pom.txt',
        use_secure_urls=True
    ),
    dict(
        name='27_Giugno_Mattina',
        display_name='27 Giugno Mattina',
        participant_label_file='rooms/27_giugno_matt.txt',
        use_secure_urls=True
    ),
    dict(
        name='27_Giugno_Pomeriggio',
        display_name='27 Giugno Pomeriggio',
        participant_label_file='rooms/27_giugno_pom.txt',
        use_secure_urls=True
    ),
    dict(
        name='28_Giugno_Mattina',
        display_name='28 Giugno Mattina',
        participant_label_file='rooms/28_giugno_matt.txt',
        use_secure_urls=True
    ),
    dict(
        name='28_Giugno_Pomeriggio',
        display_name='28 Giugno Pomeriggio',
        participant_label_file='rooms/28_giugno_pom.txt',
        use_secure_urls=True
    ),
    dict(
        name='29_Giugno_Mattina',
        display_name='29 Giugno Mattina',
        participant_label_file='rooms/29_giugno_matt.txt',
        use_secure_urls=True
    ),
    dict(
        name='29_Giugno_Pomeriggio',
        display_name='29 Giugno Pomeriggio',
        participant_label_file='rooms/29_giugno_pom.txt',
        use_secure_urls=True
    ),
    dict(
        name='30_Giugno_Mattina',
        display_name='30 Giugno Mattina',
        participant_label_file='rooms/30_giugno_matt.txt',
        use_secure_urls=True
    ),    dict(
        name='30_Giugno_Pomeriggio',
        display_name='30 Giugno Pomeriggio',
        participant_label_file='rooms/30_giugno_pom.txt',
        use_secure_urls=True
    ),    dict(
        name='1_Luglio_Mattina',
        display_name='1 Luglio Mattina',
        participant_label_file='rooms/1_luglio_matt.txt',
        use_secure_urls=True
    ),
    dict(
        name='1_Luglio_Pomeriggio',
        display_name='1 Luglio Pomeriggio',
        participant_label_file='rooms/1_luglio_pom.txt',
        use_secure_urls=True
    ),
    dict(
        name='4_Luglio_Mattina',
        display_name='4 Luglio Mattina',
        participant_label_file='rooms/4_luglio_matt.txt',
        use_secure_urls=True
    ),
    dict(
        name='4_Luglio_Pomeriggio',
        display_name='4 Luglio Pomeriggio',
        participant_label_file='rooms/4_luglio_pom.txt',
        use_secure_urls=True
    ),
    dict(
        name='5_Luglio_Mattina',
        display_name='5 Luglio Mattina',
        participant_label_file='rooms/5_luglio_matt.txt',
        use_secure_urls=True
    ),
    dict(
        name='5_Luglio_Pomeriggio',
        display_name='5 Luglio Pomeriggio',
        participant_label_file='rooms/5_luglio_pom.txt',
        use_secure_urls=True
    ),
    dict(
        name='6_Luglio_Mattina',
        display_name='6 Luglio Mattina',
        participant_label_file='rooms/6_luglio_matt.txt',
        use_secure_urls=True
    ),
    dict(
        name='6_Luglio_Pomeriggio',
        display_name='6 Luglio Pomeriggio',
        participant_label_file='rooms/6_luglio_pom.txt',
        use_secure_urls=True
    ),
    dict(
        name='7_Luglio_Mattina',
        display_name='7 Luglio Mattina',
        participant_label_file='rooms/7_luglio_matt.txt',
        use_secure_urls=True
    ),
    dict(
        name='7_Luglio_Pomeriggio',
        display_name='7 Luglio Pomeriggio',
        participant_label_file='rooms/7_luglio_pom.txt',
        use_secure_urls=True
    ),
    dict(
        name='8_Luglio_Mattina',
        display_name='8 Luglio Mattina',
        participant_label_file='rooms/8_luglio_matt.txt',
        use_secure_urls=True
    ),
    dict(
        name='8_Luglio_Pomeriggio',
        display_name='8 Luglio Pomeriggio',
        participant_label_file='rooms/8_luglio_pom.txt',
        use_secure_urls=True
    ),
    dict(
        name='Extra_day_1',
        display_name='Extra day 1',
        participant_label_file='rooms/extra_day_1.txt',
        use_secure_urls=True
    ),
    dict(
        name='Extra_day_2',
        display_name='Extra day 2',
        participant_label_file='rooms/extra_day_2.txt',
        use_secure_urls=True
    ),

]

ADMIN_USERNAME = 'admin'
# for security, best to set admin passwordInput in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


DEMO_PAGE_TITLE = """
Recipes for common tasks in oTree
"""

DEMO_PAGE_INTRO_HTML = """
Recipes for common tasks in oTree
"""


# don't share this with anybody.
SECRET_KEY = 'fnv*lfr%ghepfge1rg1a56t0sj+9d*p&1+&g%q@j!ju@zu^v@6'

SESSION_FIELDS = [
    'player_temp_AB_',
    'completions_by_treatment',
    'past_groups',
    'matrices',
    'wait_for_ids',
    'arrived_ids',
    'other_part',
    'random_prediction_A',
    'random_prediction_B',
    'random_prediction_C',
    'random_prediction_A_2',
    'random_prediction_B_2',
    'random_prediction_C_2',
    'chosen_letter_2',
    'random_ball_not_replaced',
    'random_ball_replaced',
    'listA_2',
    'example_prediction_average_A',
    'example_prediction_average_B',
    'example_prediction_average_C',
    'example_prediction_A',
    'example_prediction_B',
    'example_prediction_C',
    'example_prediction_payoff_C',
    'example_prediction_payoff_A',
    'example_prediction_payoff_B',
]

PARTICIPANT_FIELDS = [
    'accept',
    'player_temp_AB',
    'TARI',
    'contador',
    'expiry',
    'finished_rounds',
    'language',
    'num_rounds',
    'partner_history',
    'past_group_id',
    'progress',
    'selected_round',
    'task_rounds',
    'wait_page_arrival',
    'time_pressure',
    'app_payoffs',
    'CE1_ALL',
     'CE2_ALL',
     'CE3_ALL',
    'CE4_ALL',
     'CE5_ALL',
     'CE6_ALL',
     'CE7_ALL',
     'CE8_ALL',
     'CE9_ALL',
    'CE1_ALL_as_shown',
     'CE2_ALL_as_shown',
     'CE3_ALL_as_shown',
    'CE4_ALL_as_shown',
     'CE5_ALL_as_shown',
     'CE6_ALL_as_shown',
     'CE7_ALL_as_shown',
     'CE8_ALL_as_shown',
     'CE9_ALL_as_shown',
    'predA',
    'predB',
    'predC',
    'num_players',
    'replace_predictions_practice',
    'replace_predictions',
    'group_pre_A_sum_practice',
    'group_pre_B_sum_practice',
    'group_pre_C_sum_practice',
    'group_pre_cont_practice',
    'list_choices_A_practice',
    'list_choices_B_practice',
    'list_choices_C_practice',
    'group_pre_A_sum',
    'group_pre_B_sum',
    'group_pre_C_sum',
    'group_pre_cont',
    'group_list_pred_A_practice',
    'group_list_pred_B_practice',
    'group_list_pred_C_practice',
    'group_list_pred_A',
    'group_list_pred_B',
    'group_list_pred_C',
    'group_elec',
    'random_choice',
    'random_choice_practice',
    'group_pre_A_sum_practice',
    'group_pre_B_sum_practice',
    'group_pre_C_sum_practice',
    'group_pre_cont_practice',
    'list_choices_A_practice',
    'list_choices_B_practice',
    'list_choices_C_practice',
   'group_list_pred_A_practice',
   'participant.group_list_pred_B_practice',
   'group_list_pred_C_practice',
   'id_resto',
    'random_number',
    'list_choices_A',
    'list_choices_B',
    'list_choices_C',
    'Test_choices_A',
    'Test_choices_B',
    'Test_choices_C',
    'Test_choices_A_pred',
    'Test_choices_B_pred',
    'Test_choices_C_pred',
    'Test_payoff_a_pred',
    'Test_payoff_b_pred',
    'Test_payoff_c_pred',
    'payoff_practice_A',
    'payoff_practice_B',
    'payoff_practice_C',
    'num_prob_replace', #Number of times
    'num_prob_not_replace',
    'num_Test_choices_A_prob',
    'num_Test_choices_B_prob',
    'num_Test_choices_C_prob',
    'num_payoff_A_guess',
    'num_payoff_B_guess',
    'num_payoff_C_guess',
    'num_Test_choices_A_pred',
    'num_Test_choices_B_pred',
    'num_Test_choices_C_pred',
    'num_Test_payoff_a_pred',
    'num_Test_payoff_b_pred',
    'num_Test_payoff_c_pred',
    'TARI',
    'choice_binding_sit'
    'anno_di_nascita',
    'household_n'
]

