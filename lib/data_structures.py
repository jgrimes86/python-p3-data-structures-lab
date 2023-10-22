spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = [food["name"] for food in spicy_foods]
    return food_names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: ' + ('🌶' * food["heat_level"]))


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    food_by_cuisine = dict()
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            food_by_cuisine.update({"name": food["name"], "cuisine": food["cuisine"], "heat_level": food["heat_level"]})
    return food_by_cuisine

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    heat_list = [food["heat_level"] for food in spicy_foods]
    number_of_foods = len(spicy_foods)
    sum_of_heats = 0
    for heat_amount in heat_list:
        sum_of_heats = sum_of_heats + heat_amount
    average_heat_level = sum_of_heats / number_of_foods
    return average_heat_level

get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
