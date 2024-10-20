import tkinter as tk
from tkinter import messagebox
import random
import string
                                                                             
def generate_password(password_length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    if password_length < 6:
        messagebox.showerror("Error", "Password length should be at least 6 characters.")
        return None
    
    # Generate the password
    password = ''.join(random.choice(all_characters) for i in range(password_length))
    return password

def copy_password_to_clipboard():                                                                           
    root.clipboard_clear()
    
    password = password_entry.get()

    root.clipboard_append(password)
    
    root.update()

root = tk.Tk()
root.title("Password Generator")

password_length_label = tk.Label(root, text="Enter password length:")
password_length_label.pack()

password_length_entry = tk.Entry(root)
password_length_entry.pack()

generate_password_button = tk.Button(root, text="Generate Password", 
                                 command=lambda: password_entry.delete(0, tk.END) or password_entry.insert(0, generate_password(int(password_length_entry.get()))))
generate_password_button.pack()

password_entry = tk.Entry(root)
password_entry.pack()

copy_password_button = tk.Button(root, text="Copy to Clipboard", command=copy_password_to_clipboard)
copy_password_button.pack()

root.mainloop()