
cook_book = {}
with open("recipes.txt", 'r', encoding="utf - 8") as f:
    while True:
        dish_name = f.readline().strip()
        if not dish_name:
            break

        num_ingredients = int(f.readline().strip())
        ingredients_list = []

        for _ in range(num_ingredients):
            ingredient_name, quantity, measure = f.readline().strip().split(' | ')
            ingredients_list.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure,
                })

        f.readline()
        cook_book[dish_name] = ingredients_list

print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list:
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity']*person_count}
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']*person_count
    return shop_list


shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(shop_list)








