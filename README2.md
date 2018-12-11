# Python Fundamentals in 60 minutes

Project for CodingNomads' Python Webinar

## Intro (5 Minutes)

1) Talk about Python in general
    * show some cool projects
    * where is it used
    * fastest growing
    * our course
    
2) Open PyCharm, explain what an IDE is

3) Introduce the Pizza project

## The Pizza project

* Create project, mention `venv`s
* Make the file `food.py`
* **OOP**
    * In file: Create `Ingredients` class with `name`
        !!!! need to have **arguments** somewhat understood !!!!
        * Talk about strings, maybe mention that other languages have a char type but python doesn`t deal with this. Introduce that each letter can be accessed with it´s position in the string. Possibly introduce loops.
        * Console: make some ingredients (carrots, potatoes, peas, tomatoes)
        * Learned: datatypes: strings, variables
        * Learning: loops, OOP / classes
    * In file: Update `Ingredients` to have a `count`
        * Talk about integers
        * Console: instantiate some ingredients using name and count
        * Console: show basic python arithmetic and make some functions (add, subtract)
        * Learned: datatype integer, arithmetic operators
        * Learning: functions
    * In file: Create methods
        * the `use` method to add and subtract count
        * Console: show example of use method
        * Add a dunder `__str__` method using fstring
        * Console: show some fstring examples
        * Console: show some prettier ingredients (carrots, potatoes, peas, tomatoes)
        * Check off: methods, fstring, basic class functionality
        
    * In the console, show `use`, go overboard into `-` values
    * Create a **conditional statement**
        - first use `print()`
        - then change to `assert()`
    * Create a simple test (introduce TDD)
        - `assertRaises` for Exception created
        - `assertEqual` for `use()` amount reduction
    * Run tests `python -m unittest` with and without `--verbose`