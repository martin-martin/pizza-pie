import time
# maybe Soup


class Pizza:

    # CLASS VARIABLES
    perfect_temperature = 210  # celsius
    oven_ready = False

    # CLASS METHODS
    # this counts for every instance of the class (=every pizza we made)
    # because once the oven is ready, we can keep making pizza!
    # so once the oven is ready for one pizza, it's ready for all of them!
    # HOWEVER: if calling heat_oven() on a child class it only affects the child class
    #          if calling it on the parent class, it affects all child classes
    @classmethod
    def heat_oven(cls):
        """Takes about 14sec to heat up the oven to perfect pizza temperature."""
        temperature = 25  # celsius; kinda room temp
        while temperature < cls.perfect_temperature:
            time.sleep(0.2)
            temperature += 2
        # set a class variable from within the @classmethod
        cls.oven_ready = True
        print(f"Oven is ready at {cls.perfect_temperature}°C")


class Margarita(Pizza):
    # mozzarella, tomatoes, basil
    pass


class Marinara(Pizza):
    # garlic, anchovies, oregano
    pass


