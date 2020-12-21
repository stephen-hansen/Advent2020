from utils import *
import re
import copy
from functools import *
from collections import *
import math

def main():
    # Load all lines
    lines = getlines_map_regex(r'(.*) \(contains (.*)\)')
    allergen_to_ingredient = {}
    allergen_ingredients = set()
    for m in lines:
        ingredients = m.group(1).split(' ')
        direct_allergens = m.group(2).split(', ')
        for allergen in direct_allergens:
            if allergen not in allergen_to_ingredient:
                allergen_to_ingredient[allergen] = set(ingredients)
            else:
                allergen_to_ingredient[allergen] = allergen_to_ingredient[allergen].intersection(set(ingredients))

    true_mapping = {}
    while True:
        removal = None
        for allergen, ingredients in allergen_to_ingredient.items():
            if len(ingredients) == 1 and allergen not in true_mapping:
                removal = list(ingredients)[0]
                true_mapping[allergen] = removal
                break
        if removal is None:
            break
        else:
            for allergen, ingredients in allergen_to_ingredient.items():
                if removal in ingredients:
                    ingredients.remove(removal)
    p(true_mapping)
    sorted_by_allergen = map(lambda y: y[1], sorted(list(true_mapping.items()), key=lambda x: x[0]))
    p(','.join(sorted_by_allergen))
    
if __name__ == '__main__':
    main()
