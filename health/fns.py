import tkinter as tk
import sqlite3 as sql
import pandas as pd
import food


#   Returns index of selected item.
def selected_item(box):
    for index in box.curselection():
        return index


#   Inserts nutritional data from foods dict for every key into main db.
def insert_data(new_items, data, db):
    #   Connect.
    conn = sql.connect(db)
    c = conn.cursor()

    #   Access the number of times each item occurs in new_list.
    value_counts = pd.value_counts(new_items)

    #   Get access to the numbers per key, and multiply each by their respective count.
    

#   Creates a new table within the main database using the current datetime.
def create_table(new_items, data, db):
    #   Check if one has already been created for that day.
    pass

    #   Connect to main db. Create a new table using datetime as the table name.
    conn = sql.connect(db)
    c = conn.cursor()
    c.execute('drop table if exists test1')
    c.execute(f'create table test1 (calories int, protein int, carbs int, fiber int, fat int, cholesterol int, calcium int, iron int, magnesium int, sodium int, zinc int, vitamin_a int, thiamine int, vitamin_e int, riboflavin int, niacin int, vitamin_b6 int, vitamin_c int, vitamin_b12 int, selenium int, sugar int, vitamin_d int)')

    #   Populate the new table
    insert_data(new_items, data, db)


def add_item(new_items, menu, box, window, db):
    #   Add selected item to items to add list
    new_items.append(menu[selected_item(box)])

    #   Create the menu frame.
    choice_frame = tk.LabelFrame(window, text='Add meals...')
    choice_frame.grid(row=1, column=1)

    #   create a new list box object and populate it using the appended list
    new_box = tk.Listbox(choice_frame, cursor='cross', bg='grey', fg='yellow', selectbackground='green',
                          selectmode='browse', font=('Arial', 13))
    new_box.config(border=2, relief='sunken')
    new_box.grid(row=1, column=1)
    for new_item in new_items:
        new_box.insert(tk.END, new_item)

    print(new_items)

    #   After adding all items, create the table in db along with data.
    create_button = tk.Button(text='CREATE', command=lambda: create_table(new_items, food.foods, db))
    create_button.grid(row=2, column=1)


def reset(new_items):
    new_items.clear()
    print('Items reset, cleared successfully')


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
