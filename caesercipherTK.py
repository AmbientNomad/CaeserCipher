from tkinter import *
from tkinter import ttk

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def decoder():
    user_message = textbox.get('1.0', 'end')
    cypher = int(shift_entry.get())
    solved_list = []  # Will store our converted letters before saving as a new message

    for character in message:

        if character.isalpha():  # Need to confirm character is a letter, 'else' it returns that character

            # Variable and if statement for determining which letter of the alphabet will be swapped
            change_index = alphabet.index(character.lower()) + cypher
            if change_index < 0:
                change_index = len(alphabet) - abs(change_index)
            elif change_index > len(alphabet) - 1:
                change_index = change_index - len(alphabet)

            if character.isupper():  # Simple check to determine upper case or lower case replacement
                solved_list.append(alphabet[change_index].upper())
            else:
                solved_list.append(alphabet[change_index])

        else:
            solved_list.append(character)
    new_message = "".join(solved_list)
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', new_message)


root = Tk()
root.title("Caeser Cypher")
root.resizable(width=False, height=False)

mainwindow = ttk.Frame(root, padding="5 5 5 5")
mainwindow.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

textbox = Text(mainwindow, width=50, height=10)
textbox.grid(column=0, row=0, columnspan=3)
message = textbox.get('1.0', 'end')

ttk.Label(mainwindow, text="Shift number, 1-25, positive or negative:").grid(column=0, row=1)

shift_entry = ttk.Entry(mainwindow, width=10)
shift_entry.grid(column=1, row=1)

ttk.Button(mainwindow, text="Encrypt", command=decoder).grid(column=2, row=1)

textbox.focus()
root.mainloop()
