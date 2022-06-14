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
        name='DCM_treatment',
        display_name="DCM_treatment",
        num_demo_participants=3,
        app_sequence=['DCM_CM_v2'],
    ),
    dict(
        name='DCM_treatment_final',
        display_name="DCM_treatment_final",
        num_demo_participants=3,
        app_sequence=['DCM_treatment_final'],
    ),
    dict(
        name='DCM_pilot',
        display_name="DCM_pilot",
        num_demo_participants=10,
        app_sequence=['DCM_pilot_italian'],
    ),
    dict(
        name='DCM_1to9',
        display_name="DCM-control-CS_1to9",
        num_demo_participants=3,
        app_sequence=['DCM_italian_final'],
    ),
    dict(
        name='DCM_9to1',
        display_name="DCM-control-CS_9to1",
        num_demo_participants=3,
        app_sequence=['DCM_italian_final2'],
    ),
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'
INSTALLED_APPS = ['otree']

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

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
    )
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
]
