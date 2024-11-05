'''import tkinter as tk
from tkinter import messagebox
import os
def submit():
    user_input = text_widget.get('1.0', 'end')
    print(user_input,end='')
    filepath = os.path.join("C:/Projects/Face_Recognition/faces",user_input,".JPG")
    print(filepath)



root = tk.Tk()
root.title('User Input')

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

text_widget = tk.Text(frame, width=40, height=10)
text_widget.pack(padx=5, pady=5)

submit_button = tk.Button(frame, text='Submit', command=submit)
submit_button.pack(padx=5, pady=5)

root.mainloop()'''

import os

usn = input("Enter your USN : ")
filepath = os.path.join("C:/Projects/Face_Recognition/faces",usn,".JPG")
print(filepath)