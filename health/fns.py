import tkinter as tk
import sqlite3 as sql


def selected_item(box):
    for index in box.curselection():
        return index


#   Creates a new table within the main database using the current datetime.
def create(meal_list, table_name):
    #   Check if one has already been created for that day.
    pass
    #   Connect to main db. Create a new table using datetime as the table name.
    conn = sql.connect('main.db')
    c = conn.cursor()
    c.execute(f'create table {table_name} (calories int, protein int, carbs int, fiber int, fat int, cholesterol int, calcium int, iron int, magnesium int, sodium int, zinc int, vitamin a int, thiamine int, vitamin e int, riboflavin int, niacin int, vitamin b6 int, vitamin c int, vitamin b12 int, selenium int, sugar int, vitamin d int)')
    #   Populate the new table


def add_item(new_list, items_list, box, window, table_name):
    new_list.append(items_list[selected_item(box)])
    #   Create the menu frame.
    choice_frame = tk.LabelFrame(window, text='Add meals...')
    choice_frame.grid(row=1, column=1)

    #   create a new list box object and populate it using the appended list
    new_box = tk.Listbox(choice_frame, cursor='cross', bg='grey', fg='yellow', selectbackground='green',
                          selectmode='browse', font=('Arial', 13))
    new_box.config(border=2, relief='sunken')
    new_box.grid(row=1, column=1)
    for new_item in new_list:
        new_box.insert(tk.END, new_item)

    create_button = tk.Button(text='CREATE', command=lambda: create(new_list, table_name))
    create_button.grid(row=2, column=1)


def reset(new_items):
    new_items.clear()
    print('Items reset, cleared successfully')


def step_two(choice, window, menu, new_items, table_name):
    if choice == 'Create?':
        #   Create a new table.
        create(new_items, table_name)

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
        add_button = tk.Button(text='ADD', command=lambda: add_item(new_items, menu, meal_box, window))
        add_button.grid(row=3, column=0)
        reset_button = tk.Button(text='RESET', command=lambda: reset(new_items))
        reset_button.grid(row=4, column=0)

    elif choice == 'Update?':
        pass


#   Update a chosen file from a list.
def update():
    pass


