from mycroft import MycroftSkill, intent_file_handler


class FoodOrder(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('order.food.intent')
    def handle_order_food(self, message):
        self.speak_dialog('order.food')


def create_skill():
    return FoodOrder()

