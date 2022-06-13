from otree.api import *


doc = """
Of course oTree has a readymade chat widget described here: 
https://otree.readthedocs.io/en/latest/multiplayer/chat.html

But you can use this if you want a chat box that is more easily customizable,
or if you want programmatic access to the chat messages. 

This app can also help you learn about live pages in general.
"""


class Constants(BaseConstants):
    name_in_url = 'chat_from_scratch'
    players_per_group = None
    num_rounds = 1
    chat_template = __name__ + '/chat.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


class Message(ExtraModel):
    group = models.Link(Group)
    sender = models.Link(Player)
    text = models.StringField()


def to_dict(msg: Message):
    return dict(sender=msg.sender.id_in_group, text=msg.text)


# PAGES
class MyPage(Page):
    @staticmethod
    def js_vars(player: Player):
        return dict(my_id=player.id_in_group)

    @staticmethod
    def live_method(player: Player, data):
        my_id = player.id_in_group
        group = player.group

        if 'text' in data:
            text = data['text']
            msg = Message.create(group=group, sender=player, text=text)
            return {0: [to_dict(msg)]}
        return {my_id: [to_dict(msg) for msg in Message.filter(group=group)]}


page_sequence = [MyPage]
