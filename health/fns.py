import tkinter as tk

def step_two(choice, window, menu):
    if choice == 'Create?':
        #   Create the menu frame.
        choice_frame = tk.LabelFrame(window, text='Frame works create')
        choice_frame.grid(row=1, column=0)

        #   Grid the menu within the menu frame.
        meal_box = tk.Listbox(choice_frame, cursor='cross', bg='grey', fg='yellow', selectbackground='green',
                              selectmode='browse', font=('Arial', 13))
        meal_box.config(border=2, relief='sunken')
        for meal in menu:
            meal_box.insert(tk.END, meal)

        meal_box.grid(row=1, column=0)
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


