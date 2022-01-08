import tkinter as tk

#   TITLES DICTIONARY
games = {
    'BATTLEFIELD V': '🌍World War II Program🌍',
    'CS: GO': '🏹🔱💥🔫 Arrows, Rifles, Spears, and Swords 🔫💥🔱🏹',
    'DOTA': '🧠💩🎲 002/375 🎲💩🧠',
    'GTAV': '👩‍💻| Digital Universe Program |👩‍💻',
    'SW': '👽🌌🛸🚀A Long Time Ago in a Galaxy Far, Far Away... (Part 2)🚀🛸🌌👽',
    'L4D': '🧟| Headshot Trainer Program |🧟',
    'MKII': '💀 Fight to Death No Rules Program ***WARNING*** GRAPHIC 💀',
    'MUSIC': '♩♪♫♬♭♯🎼🎵🎶| Transcribing My Favorite Songs |🎶🎵🎼♯♮♭♬♫♪♩',
    'RE': '🧟 Zombies, Paintings, and Blood 🧟',
    'POKER': '🙏🤹🃏🎲🙏',
    'SC2': '🚀 Galactic Warfare Program 👽',
    'SC': '🚀 Galactic Warfare Progra m 👽',
    'TEKKEN': '🥊Martial Arts Tournament Program🥊',
    'VALORANT': '🍄DOTA and CS Combined🍄',
    'WARZONE': '🏹🔱💥🔫Lethal Mechanics🔫💥🔱🏹',
    'TKEY_HOLODECK': 'live_624636030_NhD1DqANATansJEQXBXWnnKVq6ss9l',
    'TKEY_TOXIC': 'live_723874221_mKLlwiz5urFXcOhgjSdHjla3vz1sMS'
}


#   MAIN FUNCTION
def selected_item():
    for selected_index in option_list.curselection():
        key = options[selected_index]
        result_box.delete(0, 'end')
        result_box.insert(0, games[key])


#   ROOT
root = tk.Tk()
root.configure(background='teal')
root.geometry('750x400')
root.title('Stream Titles')

#   LABELS
game_label = tk.Label(root, text='Game', font=('Arial', 20), fg='yellow', bg='teal')
game_label.grid(row=0, column=0)

title_label = tk.Label(root, text='Title', font=('Arial', 20), fg='Red', bg='teal')
title_label.grid(row=0, column=2)

#   OPTIONS LISTBOX
options = []
for game in games:
    options.append(game)

option_list = tk.Listbox(root, cursor='cross', bg='grey', fg='yellow', selectbackground='green', selectmode='browse', font=('Arial', 13))
option_list.grid(row=1, column=0)
option_list.config(border=2, relief='sunken')
for option in options:
    option_list.insert(tk.END, option)

#   OPTIONS SCROLL
option_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=option_list.yview)
option_scrollbar.grid(row=1, column=1, sticky='nsw', rowspan=2)
option_list['yscrollcommand'] = option_scrollbar.set

#   BUTTONS
gen_button = tk.Button(root, text='GENERATE', command=selected_item, font=('Arial', 12))
gen_button.grid(row=2, column=0)

quit_button = tk.Button(root, text='QUIT', font=('Arial', 12), command=root.destroy)
quit_button.grid(row=3, column=3)

#   RESULT
result_box = tk.Entry(root, width=40, font=('Arial', 15))
result_box.grid(row=1, column=2, sticky='n')

root.mainloop()
