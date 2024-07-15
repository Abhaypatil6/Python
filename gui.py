import tkinter as tk
from tkinter import messagebox

def show_custom_dialog():
    messagebox.showinfo("Custom Dialog", "This is a custom dialog box!")

def submit_form():
    username = username_entry.get()
    password = password_entry.get()
    gender = gender_var.get()
    hobbies = [hobby.get() for hobby in hobbies_vars if hobby.get()]
    
    print("Username:", username)
    print("Password:", password)
    print("Gender:", gender)
    print("Hobbies:", hobbies)

# Create main window
root = tk.Tk()
root.title("Python GUI")

# Create labels
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, sticky="e")

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, sticky="e")

gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=2, column=0, sticky="e")

hobbies_label = tk.Label(root, text="Hobbies:")
hobbies_label.grid(row=3, column=0, sticky="e")

# Create entry widgets
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

# Create radio buttons
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
male_radio.grid(row=2, column=1, sticky="w")

female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
female_radio.grid(row=2, column=1, sticky="e")

# Create checkboxes
hobbies_vars = [tk.BooleanVar() for _ in range(3)]
hobbies_checkboxes = []
hobbies_texts = ["Reading", "Gaming", "Traveling"]

for i, hobby_text in enumerate(hobbies_texts):
    checkbox = tk.Checkbutton(root, text=hobby_text, variable=hobbies_vars[i])
    checkbox.grid(row=3+i, column=1, sticky="w")
    hobbies_checkboxes.append(checkbox)

# Create buttons
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=4+len(hobbies_texts), column=0, columnspan=2)

custom_dialog_button = tk.Button(root, text="Show Custom Dialog", command=show_custom_dialog)
custom_dialog_button.grid(row=5+len(hobbies_texts), column=0, columnspan=2)

root.mainloop()