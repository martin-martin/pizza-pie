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
* **OOP**: Create `Ingredients` class with `amount` and `name`
* Go to console and show some instances
* Add a dunder `__str__` method
* Create the `use` method
* In the console, show `use`, go overboard into `-` values
* Create a **conditional statement**
    - first use `print()`
    - then change to `assert()`
* Create a simple test (introduce TDD)
    - `assertRaises` for Exception created
    - `assertEqual` for `use()` amount reduction
* Run tests `python -m unittest` with and without `--verbose`