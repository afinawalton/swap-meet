class Item:

    def __init__(self, category="", condition=0.0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition <= 2.0:
            return "Better luck next time"
        elif self.condition == 3.0:
            return "This one's just about average"
        else:
            return "You're in luck -- it's perfect!"