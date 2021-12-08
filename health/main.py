import food as fd
import sqlite3 as sql
import fns

conn = sql.connect('main.db')
c = conn.cursor()

all_nuts = (
        'calories', 'protein', 'carbs', 'fiber', 'fat', 'cholesterol', 'calcium', 'iron', 'magnesium', 'potassium',
        'sodium', 'zinc', 'vitamin a', 'thiamine', 'vitamin e', 'riboflavin', 'niacin', 'vitamin b6', 'folate',
        'vitamin c', 'vitamin b12', 'selenium', 'sugar', 'vitamin d')

nutrients = {}

table = fns.create_or_update()

if table == "create":
    c.execute('drop table if exists days_doses')
    c.execute(f'create table days_doses (calories int, protein int, carbs int, fiber int, fat int, cholesterol int, calcium int, iron int, magnesium int, potassium int, sodium int, zinc int, vitamin_a int, thiamine int, vitamin_e int, riboflavin int, niacin int, vitamin_b6 int, folate int, vitamin_c int, vitamin_b12 int, selenium int, sugar int, vitamin_d int)')

    while input("Do you want to keep entering foods? y/n ").lower() == 'y':
        choice = input("What food? ")
        number = int(input("How many? "))

        for food in fd.foods:
            if choice == food:
                for base_nutrient in fd.foods[choice]:
                    for nutrient in all_nuts:
                        if base_nutrient == nutrient:
                            if base_nutrient in nutrients:
                                nutrients[base_nutrient] += fd.foods[food][base_nutrient] * number
                            else:
                                nutrients[base_nutrient] = fd.foods[food][base_nutrient] * number

    calories = nutrients['calories']
    protein = nutrients['protein']
    carbs = nutrients['carbs']
    fiber = nutrients['fiber']
    fat = nutrients['fat']
    cholesterol = nutrients['cholesterol']
    calcium = nutrients['calcium']
    iron = nutrients['iron']
    magnesium = nutrients['magnesium']
    potassium = nutrients['potassium']
    sodium = nutrients['sodium']
    zinc = nutrients['zinc']
    vitamin_a = nutrients['vitamin a']
    thiamine = nutrients['thiamine']
    vitamin_e = nutrients['vitamin e']
    riboflavin = nutrients['riboflavin']
    niacin = nutrients['niacin']
    vitamin_b6 = nutrients['vitamin b6']
    folate = nutrients['folate']
    vitamin_c = nutrients['vitamin c']
    vitamin_b12 = nutrients['vitamin b12']
    selenium = nutrients['selenium']
    sugar = nutrients['sugar']
    vitamin_d = nutrients['vitamin d']

    c.execute(f'insert into days_doses values ({calories}, {protein}, {carbs}, {fiber}, {fat}, {cholesterol}, {calcium}, {iron}, {magnesium}, {potassium}, {sodium}, {zinc}, {vitamin_a}, {thiamine}, {vitamin_e}, {riboflavin}, {niacin}, {vitamin_b6}, {folate}, {vitamin_c}, {vitamin_b12}, {selenium}, {sugar}, {vitamin_d})')

    conn.commit()
else:
    c.execute('select*from days_doses;')
    data = c.fetchall()
    old_nuts = data[0]

    calories, protein, carbs, fiber, fat, cholesterol, calcium, iron, magnesium, potassium, sodium, zinc, vitamin_a,thiamine, vitamin_e, riboflavin, niacin, vitamin_b6, folate, vitamin_c, vitamin_b12, selenium, sugar, vitamin_d = old_nuts

    while input("Do you want to keep entering foods? y/n ").lower() == 'y':
        choice = input("What food? ")
        number = int(input("How many? "))

        for food in fd.foods:
            if choice == food:
                for base_nutrient in fd.foods[choice]:
                    for nutrient in all_nuts:
                        if base_nutrient == nutrient:
                            if base_nutrient in nutrients:
                                nutrients[base_nutrient] += fd.foods[food][base_nutrient] * number
                            else:
                                nutrients[base_nutrient] = fd.foods[food][base_nutrient] * number

        calories_new = nutrients['calories']
        protein_new = nutrients['protein']
        carbs_new = nutrients['carbs']
        fiber_new = nutrients['fiber']
        fat_new = nutrients['fat']
        cholesterol_new = nutrients['cholesterol']
        calcium_new = nutrients['calcium']
        iron_new = nutrients['iron']
        magnesium_new = nutrients['magnesium']
        potassium_new = nutrients['potassium']
        sodium_new = nutrients['sodium']
        zinc_new = nutrients['zinc']
        vitamin_a_new = nutrients['vitamin a']
        thiamine_new = nutrients['thiamine']
        vitamin_e_new = nutrients['vitamin e']
        riboflavin_new = nutrients['riboflavin']
        niacin_new = nutrients['niacin']
        vitamin_b6_new = nutrients['vitamin b6']
        folate_new = nutrients['folate']
        vitamin_c_new = nutrients['vitamin c']
        vitamin_b12_new = nutrients['vitamin b12']
        selenium_new = nutrients['selenium']
        sugar_new = nutrients['sugar']
        vitamin_d_new = nutrients['vitamin d']

        c.execute(f'update days_doses set calories = {calories+calories_new}, protein = {protein+protein_new}, carbs = {carbs+carbs_new}, fiber = {fiber+fiber_new}, fat = {fat+fat_new}, cholesterol = {cholesterol+cholesterol_new}, calcium = {calcium+calcium_new}, iron = {iron+iron_new}, magnesium = {magnesium+magnesium_new}, potassium = {potassium+potassium_new}, sodium = {sodium+sodium}, zinc = {zinc+zinc_new}, vitamin_a = {vitamin_a+vitamin_a_new}, thiamine = {thiamine+thiamine_new}, vitamin_e = {vitamin_e+vitamin_e_new}, riboflavin = {riboflavin+riboflavin_new}, niacin = {niacin+niacin_new}, vitamin_b6 = {vitamin_b6+vitamin_b6_new}, folate = {folate+folate_new}, vitamin_c = {vitamin_c+vitamin_c_new}, vitamin_b12 = {vitamin_b12+vitamin_b12_new}, selenium = {selenium+selenium_new}, sugar = {sugar+sugar_new}, vitamin_d = {vitamin_d+vitamin_d_new}')
        conn.commit()
print(nutrients)
