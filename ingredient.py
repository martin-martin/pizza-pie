carrots = 10


# CLASSES AND OBJECT-ORIENTED PROGRAMMING
class Ingredient:

    # PYTHON 'CONSTRUCTOR' - not exactly the same because you can have a (blank) class without __init__
    #                       gets called on creation of every new instance
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    # PYTHON METHODS
    def use(self, amount):
        # CONDITIONAL STATEMENTS
        # RELATIONAL OPERATORS < <= >= > == !=
        if self.amount - amount < 0:
            # (maybe) EXCEPTION HANDLING
            raise Exception(f"Not enough of {self.name} left! There are only {self.amount}, you wanted {amount}.")
        else:
            self.amount -= amount
            return self.amount

    # CUSTOM DUNDER STR
    def __str__(self):
        # STRING FORMATTING
        return f'You have {self.amount} left of {self.name}.'
