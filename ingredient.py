carrots = 10










# CLASSES AND OBJECT-ORIENTED PROGRAMMING
class Ingredient:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def use(self, amount):
        # CONDITIONAL STATEMENTS
        if self.amount - amount < 0:
            # (maybe) EXCEPTION HANDLING
            raise Exception(f"Not enough of {self.name} left! There are only {self.amount}, you wanted {amount}.")
        else:
            self.amount -= amount
            return self.amount

    def __str__(self):
        # STRING FORMATTING
        return f'You have {self.amount} left of {self.name}.'
