#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # Initialise max_batches using the first values in both dictionaries.
    recipe_values = list(recipe.values())
    ingredients_values = list(ingredients.values())
    max_batches = ingredients_values[0] // recipe_values[0]

    for k, v in recipe.items():
        # Check that the key from recipe is present in ingredients, if not set max_batches to zero.
        if k in ingredients.keys():
          # Use floor division to determine how many batches worth of each ingredient are present in ingredients. If the number is lower than the current max_batches, set the max_batches to the number.
            if ingredients[k] // v < max_batches:
                max_batches = ingredients[k] // v
        else:
            max_batches = 0
    return max_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
