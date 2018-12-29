# FILE INPUT
with open('recipe.txt', 'r') as f:
    recipe = f.readlines()

# LISTS
ingredients = []
# FOR LOOP
for line in recipe:
    ingr = line.split()
    ingredients.append(ingr)

# DICTIONARIES
ing_dict = {}
for ingredient in ingredients:
    name = ingredient[1]
    # TYPE CONVERSION
    amount = int(ingredient[0])
    ing_dict[name] = amount

print(ing_dict)

ing_dict.pop('olive_oil')
ing_dict.pop('garlic_cloves')

def add_amount(ingredient_dict, ingredient, amount):
    """Adds to the amount of the specified ingredient."""
    ingredient_dict[ingredient] = ingredient_dict.get(ingredient, 0) + amount
    return ingredient_dict

for key, value in ing_dict.items():
    ing_dict = add_amount(ing_dict, key, value)

print(ing_dict)

# FILE OUTPUT
with open('new_recipe.txt', 'w') as f_out:
    recipe = "IMPROVED RECIPE\n\n"
    for name, amount in ing_dict.items():
        recipe += f'{amount} {name}\n'
    f_out.write(recipe)
