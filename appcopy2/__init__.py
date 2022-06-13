from appcopy1 import *


class Constants(Constants):
    name_in_url = 'appcopy2'


# need to copy/paste Subsession/Group/Player classes from appcopy1
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    aaa = models.IntegerField()


class Player(BasePlayer):
    bbb = models.IntegerField()
