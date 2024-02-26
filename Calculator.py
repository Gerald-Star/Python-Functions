from tkinter import *
win = Tk()
win.title('Calculator')
win.geometry('515x365')
win.resizable(0, 0)


def btn_click(item):
    global expression
    # ! this expressions takes any number clicked
    expression = expression + str(item)
    # ! the input of this set expression gets into the StringVar
    input_text.set(expression)


expression = ""
input_text = StringVar()  # StringVar function is use to hold data in python


# input fiend frame
input_frame = Frame(win, width=312, height=50)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=(
    'arial', 18, 'bold'), width=45, justify=RIGHT, textvariable=input_text)
input_field.grid(row=0, column=0)

# increase the input height of input field
input_field.pack(ipady=10)

# Button frame
btns_frame = Frame(win, width=310, height=270)
btns_frame.pack()

# After adding the command functionalities, # ! create a function to clear the input field


def bt_clear():
    global expression
    # passing an empty string clears any input with the clear button
    input_text.set("")

# Create a function for the Equal button # ! pass this function to the equal button


def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


# states the button on the center of the app # ! command=lambda: btn_click()
# ! pass the clear button function on clear
clear = Button(btns_frame, text='C', width=38, height=3, command=lambda: bt_clear()).grid(
    row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(btns_frame, text='/', width=10,
                height=3, command=lambda: btn_click('/')).grid(row=0, column=3, padx=1, pady=1)

# Button Second Row # ! use the command=lambda: btn_click(7) to apply the functionalities of buttons
# ! lambda is an anonymous function, it can take any number of arguments

seven = Button(btns_frame, text='7', width=10, height=3, command=lambda: btn_click(7)).grid(
    row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text='8', width=10, height=3, command=lambda: btn_click(8)).grid(
    row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text='9', width=10, height=3, command=lambda: btn_click(9)).grid(
    row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text='*', width=10, height=3, command=lambda: btn_click('*')).grid(
    row=1, column=3, padx=1, pady=1)

#  button third row # ! add the command=lambda: btn_click()

four = Button(btns_frame, text='4', width=10, height=3, command=lambda: btn_click(4)).grid(
    row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text='5', width=10, height=3, command=lambda: btn_click(5)).grid(
    row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text='6', width=10, height=3, command=lambda: btn_click(6)).grid(
    row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame, text='-', width=10, height=3, command=lambda: btn_click('-')).grid(
    row=2, column=3, padx=1, pady=1)

# Button fourth row # ! add the command=lambda: btn_click()

one = Button(btns_frame, text='1', width=10, height=3, command=lambda: btn_click(1)).grid(
    row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text='2', width=10, height=3, command=lambda: btn_click(2)).grid(
    row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text='3', width=10, height=3, command=lambda: btn_click(3)).grid(
    row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text='+', width=10, height=3, command=lambda: btn_click('+')).grid(
    row=3, column=3, padx=1, pady=1)

#  Button Fifth row # ! command=lambda: btn_click()

zero = Button(btns_frame, text='0', width=24, height=3, command=lambda: btn_click('0')).grid(
    row=4, column=0, columnspan=2, padx=1, pady=1)
point = Button(btns_frame, text='.', width=10, height=3, command=lambda: btn_click('.')).grid(
    row=4, column=2, padx=1, pady=1)
equal = Button(btns_frame, text='=', width=10, height=3, command=lambda: bt_equal()).grid(
    row=4, column=3, padx=1, pady=1)


win.mainloop()
