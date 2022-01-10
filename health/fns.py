import tkinter as tk


def step_two(choice, window, menu):
    if choice == 'Create?':
        #   Create the menu frame.
        choice_frame = tk.LabelFrame(window, text='Menu')
        choice_frame.grid(row=1, column=0)

        #   Create the meal box object, populate it, and grid the menu within the menu frame.
        meal_box = tk.Listbox(choice_frame, cursor='cross', bg='grey', fg='yellow', selectbackground='green',
                              selectmode='browse', font=('Arial', 13))
        meal_box.config(border=2, relief='sunken')
        for meal in menu:
            meal_box.insert(tk.END, meal)

        meal_box.grid(row=1, column=0)

        menu_scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=meal_box.yview)
        menu_scrollbar.grid(row=1, column=1, sticky='nsw', rowspan=2)
        meal_box['yscrollcommand'] = menu_scrollbar.set
        add = tk.Button(text='ADD')

        add.grid(row=2, column=1)
    elif choice == 'Update?':
        pass


#   Create new file.
def create():
    #   Check if one has already been created for that day.
    pass


#   Update a chosen file from a list.
def update():
    pass


#   Confirmation alert.
def new_win():
    pass
