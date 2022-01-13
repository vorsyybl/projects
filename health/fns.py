import tkinter as tk
import sqlite3 as sql
import pandas as pd
import food


def selected_item(box):
    for index in box.curselection():
        return index


def insert_data(db, data):
    conn = sql.connect(db)
    c = conn.cursor()

    counts = pd.value_counts(data)
    unique_keys = set(data)
    print(unique_keys)

    for key in unique_keys:
        count = counts[key]
        calories = food.foods[key]['calories'] * count
        protein = food.foods[key]['protein']
        carbs = food.foods[key]['carbs'] * count
        fiber = food.foods[key]['fiber'] * count
        fat = food.foods[key]['fat'] * count
        cholesterol = food.foods[key]['cholesterol'] * count
        calcium = food.foods[key]['calcium'] * count
        iron = food.foods[key]['iron'] * count
        magnesium = food.foods[key]['magnesium'] * count
        sodium = food.foods[key]['sodium'] * count
        zinc = food.foods[key]['zinc'] * count
        vitamin_a = food.foods[key]['vitamin a'] * count
        thiamine = food.foods[key]['thiamine'] * count
        vitamin_e = food.foods[key]['vitamin e'] * count
        riboflavin = food.foods[key]['riboflavin'] * count
        niacin = food.foods[key]['niacin'] * count
        vitamin_b6 = food.foods[key]['vitamin b6'] * count
        vitamin_c = food.foods[key]['vitamin c'] * count
        vitamin_b12 = food.foods[key]['vitamin b12'] * count
        selenium = food.foods[key]['selenium'] * count
        sugar = food.foods[key]['sugar'] * count
        vitamin_d = food.foods[key]['vitamin d'] * count

        c.execute(f'insert into test1 values ({calories}, {protein}, {carbs}, {fiber}, {fat}, {cholesterol}, {calcium}, {iron}, {magnesium}, {sodium}, {zinc}, {vitamin_a}, {thiamine}, {vitamin_e}, {riboflavin}, {niacin}, {vitamin_b6}, {vitamin_c}, {vitamin_b12}, {selenium}, {sugar}, {vitamin_d})')
        print('Data inserted..')
        print(data)

#   Creates a new table within the main database using the current datetime.
def create_table(db, data):
    #   Check if one has already been created for that day.
    pass

    #   Connect to main db.
    conn = sql.connect(db)
    c = conn.cursor()

    #   Create a new table using datetime as the table name.
    c.execute('drop table if exists test1')
    c.execute(f'create table test1 (calories int, protein int, carbs int, fiber int, fat int, cholesterol int, '
              f'calcium int, iron int, magnesium int, sodium int, zinc int, vitamin_a int, thiamine int, '
              f'vitamin_e int, riboflavin int, niacin int, vitamin_b6 int, vitamin_c int, vitamin_b12 int, '
              f'selenium int, sugar int, vitamin_d int)')

    #   Populate the new table.
    insert_data(db, data)


def add_item(new_items, items, box, window, db):
    #   Add selected item to items to add list
    new_items.append(items[selected_item(box)])

    #   Create the menu frame.
    choice_frame = tk.LabelFrame(window, text='New Items')
    choice_frame.grid(row=1, column=1)

    #   create a new list box object and populate it using the appended list
    new_box = tk.Listbox(choice_frame, cursor='cross', bg='grey', fg='yellow', selectbackground='green',
                          selectmode='browse', font=('Arial', 13))
    new_box.config(border=2, relief='sunken')
    new_box.grid(row=1, column=1)
    for new_item in new_items:
        new_box.insert(tk.END, new_item)

    #   After adding all items, create the table in db along with data.
    create_button = tk.Button(text='CREATE', command=lambda: create_table(db, new_items))
    create_button.grid(row=2, column=1)


def reset(new_items):
    new_items.clear()


def step_two(choice, window, menu, new_items, db):
    if choice == 'Create?':
        #   Create the menu frame.
        choice_frame = tk.LabelFrame(window, text='Add meals...')
        choice_frame.grid(row=1, column=0)

        #   Create the meal box object, populate it, and grid the menu within the menu frame.
        meal_box = tk.Listbox(choice_frame, cursor='cross', bg='grey', fg='yellow', selectbackground='green',
                              selectmode='browse', font=('Arial', 13))
        meal_box.config(border=2, relief='sunken')
        for meal in menu:
            meal_box.insert(tk.END, meal)
        meal_box.grid(row=1, column=0)

        #   Make and add a scrollbar to the meal box object.
        menu_scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=meal_box.yview)
        menu_scrollbar.grid(row=1, column=1, sticky='nsw', rowspan=2)
        meal_box['yscrollcommand'] = menu_scrollbar.set

        #   Buttons.
        add_button = tk.Button(text='ADD', command=lambda: add_item(new_items, menu, meal_box, window, db))
        add_button.grid(row=3, column=0)
        reset_button = tk.Button(text='RESET', command=lambda: reset(new_items))
        reset_button.grid(row=4, column=0)

    elif choice == 'Update?':
        pass


#   Update a chosen file from a list.
def update():
    pass
