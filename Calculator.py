import os
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

import CalculatorFunctions as cf
from functools import partial

print(tkinter.TkVersion)
print(tkinter.TclVersion)

#tkinter._test()

CALC = cf.Calculator()

def get_entry_value():
    value = result.get()
    print("Setting Input Value:", value)
    CALC.input_value = float(value)

def entry_update(**kwargs):
    try:
        def result_condition() -> str:
            if result.get() == "0.0":
                return ''
            else:
                return result.get()

        value = (result_condition() + kwargs.get("value"))
        result.delete(0, tkinter.END) #deletes the current value
        result.insert(0, value) #inserts new value assigned by 2nd parameter


    except ValueError:
        pass

"""
TODO: Figure out logic here to take the input value, move to memory, place the operation to be done
in memory as well and updating the current value accordingly. Should trigger the prior operation in 
memory so additional press after new input performs the operation.
"""
def equal_entries():
    get_entry_value()
    if not CALC.lock:
        print("Current Value before set:", CALC.current_value)
        print("Input Value before set:", CALC.input_value)
        CALC.current_value = CALC.input_value
        print("Current Value after set:", CALC.current_value)
    if CALC.procedure == "add":
        CALC.add()
    elif CALC.procedure == "subtract":
        CALC.subtract()
    elif CALC.procedure == "multiply":
        CALC.multiply()
    elif CALC.procedure == "divide":    
        CALC.divide()
    result.delete(0, tkinter.END) #deletes the current value
    entry_update(value = str(CALC.current_value))
    CALC.set_final_value()
    CALC.lock = True
    print("Current Value after equal_entries:", CALC.current_value)


def perform_operation(method:str):
    if CALC.init_state:
        get_entry_value()
        if not CALC.lock:
            CALC.current_value = float(CALC.input_value)
        CALC.procedure = method
        CALC.init_state = False
        CALC.refresh_screen = True
        CALC.lock = True
        result.delete(0, tkinter.END) #deletes the current value
    else:
        if not CALC.lock:
            CALC.current_value = float(CALC.input_value)
        CALC.procedure = method
        equal_entries()
        CALC.lock = True
        CALC.refresh_screen = False
        result.delete(0, tkinter.END) #deletes the current value



# def perform_operation(method:str):
#     get_entry_value()
#     if CALC.init_state:
#         CALC.current_value = float(CALC.input_value)
#         entry_update(value = str(CALC.input_value))
#     CALC.procedure = method
#     CALC.init_state = False
#     equal_entries()
#     CALC.lock = True        


def equals():
    equal_entries()
    CALC.lock = False
    CALC.init_state = True
    CALC.refresh_screen = True
    CALC.current_value = 0.0



# Create a window!
main_window = tkinter.Tk()
main_window.title("Calculator")
main_window.geometry("200x200-8-200")


main_window.columnconfigure(0, weight=1)
main_window.rowconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)
main_window.rowconfigure(2, weight=0)
main_window.columnconfigure(3, weight=1)
main_window.rowconfigure(3, weight=1)
main_window.columnconfigure(4, weight=1)
main_window.rowconfigure(4, weight=1)
main_window.rowconfigure(5, weight=1)
main_window.rowconfigure(6, weight=1)
main_window.rowconfigure(7, weight=1)

# Result window
result_frame = tkinter.Frame(main_window, padx=5)
result_frame.grid(row=0, column=0, sticky='new')
result = tkinter.Entry(result_frame)
result.insert(0, '0.0')
result.bind('<Left-Click>')
result.grid(row=0, column=0, sticky='new')

# Button Frame
button_frame = tkinter.Frame(main_window, padx=5)
button_frame.grid(row=1, column=0, sticky='new')

# Row 1 Buttons
c_button = tkinter.Button(button_frame, text='C')
ce_button = tkinter.Button(button_frame, text='CE')
percent_button = tkinter.Button(button_frame, text='%')
divide_button = tkinter.Button(button_frame, text='/', command=lambda: perform_operation("divide"))
c_button.grid(row=1, column=0, sticky='nsew')
ce_button.grid(row=1, column=1, sticky='nsew')
percent_button.grid(row=1, column=2, sticky='nsew')
divide_button.grid(row=1, column=3, sticky='nsew')

# Row 2 Buttons
seven_button = tkinter.Button(button_frame, text='7', command=lambda: entry_update(value='7'))
eight_button = tkinter.Button(button_frame, text='8', command=lambda: entry_update(value='8'))
nine_button = tkinter.Button(button_frame, text='9', command=lambda: entry_update(value='9'))
plus_button = tkinter.Button(button_frame, text='+', command=lambda: perform_operation("add"))
seven_button.grid(row=2, column=0, sticky='nsew')
eight_button.grid(row=2, column=1, sticky='nsew')
nine_button.grid(row=2, column=2, sticky='nsew')
plus_button.grid(row=2, column=3, sticky='nsew')

# Row 3 Buttons
four_button = tkinter.Button(button_frame, text='4', command=lambda: entry_update(value='4'))
five_button = tkinter.Button(button_frame, text='5', command=lambda: entry_update(value='5'))
six_button = tkinter.Button(button_frame, text='6', command=lambda: entry_update(value='6'))
minus_button = tkinter.Button(button_frame, text='-', command=lambda: perform_operation("subtract"))
four_button.grid(row=3, column=0, sticky='nsew')
five_button.grid(row=3, column=1, sticky='nsew')
six_button.grid(row=3, column=2, sticky='nsew')
minus_button.grid(row=3, column=3, sticky='nsew')

# Row 4 Buttons
one_button = tkinter.Button(button_frame, text='1', command=lambda: entry_update(value='1'))
two_button = tkinter.Button(button_frame, text='2', command=lambda: entry_update(value='2'))
three_button = tkinter.Button(button_frame, text='3', command=lambda: entry_update(value='3'))
star_button = tkinter.Button(button_frame, text='*', command=lambda: perform_operation("multiply"))
one_button.grid(row=4, column=0, sticky='nsew')
two_button.grid(row=4, column=1, sticky='nsew')
three_button.grid(row=4, column=2, sticky='nsew')
star_button.grid(row=4, column=3, sticky='nsew')

# Row 5 Buttons
zero_button = tkinter.Button(button_frame, text='0')
period_button = tkinter.Button(button_frame, text='.')
equal_button = tkinter.Button(button_frame, text='=', command=lambda: equals())

zero_button.grid(row=5, column=0, sticky='nsew')
period_button.grid(row=5, column=1, sticky='nsew')
equal_button.grid(row=5, column=2, sticky='nsew', columnspan=2)


main_window.update()
main_window.minsize(button_frame.winfo_width() + 5, result_frame.winfo_height() + button_frame.winfo_height() + 5)
main_window.mainloop()

print(CALC.input_value)