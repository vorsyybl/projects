import food
import sqlite3 as sql
import fns
import tkinter as tk

#   Root tk window.
root_main = tk.Tk()
root_main.geometry('420x800')
root_main.title('Food Tracker')

#   Data/storage.
options = ('Create?', 'Update?', 'View?')
nutrients = [nutrient for nutrient in food.all_nuts]
menu = [meal for meal in food.foods]
new_items = []

#   Skeleton configuration.
# root_main.rowconfigure(0)

#   Step One.
options_frame = tk.LabelFrame(root_main, text='What would you like to do?')
options_frame.grid(row=0, column=0)
choice = tk.StringVar()
choice.set('Create?')

create_button = tk.Radiobutton(options_frame, text=options[0], value=options[0], variable=choice)
create_button.grid(row=0, column=0)
update_button = tk.Radiobutton(options_frame, text=options[1], value=options[1], variable=choice)
update_button.grid(row=1, column=0)
view_button = tk.Radiobutton(options_frame, text=options[2], value=options[2], variable=choice)
view_button.grid(row=2, column=0)

#   Step Two.
choice_set_button = tk.Button(root_main, text='Continue...', command=lambda: fns.step_two(choice.get(), root_main, menu, new_items))
choice_set_button.grid(row=0, column=1)

#   Connect to db, grab a cursor.
conn = sql.connect('main.db')
c = conn.cursor()

# c.execute(f'insert into days_doses values ({calories}, {protein}, {carbs}, {fiber}, {fat}, {cholesterol}, {calcium}, {iron}, {magnesium}, {potassium}, {sodium}, {zinc}, {vitamin_a}, {thiamine}, {vitamin_e}, {riboflavin}, {niacin}, {vitamin_b6}, {folate}, {vitamin_c}, {vitamin_b12}, {selenium}, {sugar}, {vitamin_d})')
# conn.commit()
#
# c.execute(f'update days_doses set calories = {calories+calories_new}, protein = {protein+protein_new}, carbs = {carbs+carbs_new}, fiber = {fiber+fiber_new}, fat = {fat+fat_new}, cholesterol = {cholesterol+cholesterol_new}, calcium = {calcium+calcium_new}, iron = {iron+iron_new}, magnesium = {magnesium+magnesium_new}, potassium = {potassium+potassium_new}, sodium = {sodium+sodium}, zinc = {zinc+zinc_new}, vitamin_a = {vitamin_a+vitamin_a_new}, thiamine = {thiamine+thiamine_new}, vitamin_e = {vitamin_e+vitamin_e_new}, riboflavin = {riboflavin+riboflavin_new}, niacin = {niacin+niacin_new}, vitamin_b6 = {vitamin_b6+vitamin_b6_new}, folate = {folate+folate_new}, vitamin_c = {vitamin_c+vitamin_c_new}, vitamin_b12 = {vitamin_b12+vitamin_b12_new}, selenium = {selenium+selenium_new}, sugar = {sugar+sugar_new}, vitamin_d = {vitamin_d+vitamin_d_new}')
# conn.commit()

root_main.mainloop()
