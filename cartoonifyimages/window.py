from tkinter import *

root = Tk()  # creating a small GUI window.

# customizing root window title
root.title("Welcome to Python Lobby")
# customizing root window dimension
root.geometry('350x200')  # root.geometry('weidthxheight')
# placing label to our GUI app
# label = Label(root, text="We are Python Lobby-ian")
label = Label(root, text="name", font=("Helvetica", 12), fg='white', bg='black')
# fg = foreground color, it is used to change the text color/label color.
# bg = background color, it is used to change the background color of label.
# font = this argument is used to give custom font-family and size to our text.
label.pack()
root.mainloop()  # finally execute our loop
