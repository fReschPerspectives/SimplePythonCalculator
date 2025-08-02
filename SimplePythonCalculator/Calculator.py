import platform
import tkinter

from SimplePythonCalculator import CalculatorFunctions as cf

CALC = cf.Calculator()

def get_entry_value():
    value = result.get()
    CALC.input_value = float(value)

def entry_update(value):
    try:
        current = "" if result.get() == "0.0" else result.get()
        new_value = current + str(value)
        result.delete(0, tkinter.END)
        result.insert(0, new_value)
    except ValueError:
        pass

def clear():
    result.delete(0, tkinter.END)
    result.insert(0, "0.0")

def clear_all():
    clear()
    CALC.init_state = True
    CALC.lock = False
    CALC.refresh_screen = False
    CALC.procedure = ""
    CALC.initial_value = 0.0
    CALC.input_value = 0.0
    CALC.current_value = 0.0
    CALC.final_value = 0.0

def percent_function():
    get_entry_value()
    CALC.current_value = CALC.input_value / 100.0
    result.delete(0, tkinter.END)
    result.insert(0, str(CALC.current_value))

def equal_entries():
    get_entry_value()
    if not CALC.lock:
        CALC.current_value = CALC.input_value
    if CALC.procedure == "add":
        CALC.add()
    elif CALC.procedure == "subtract":
        CALC.subtract()
    elif CALC.procedure == "multiply":
        CALC.multiply()
    elif CALC.procedure == "divide":
        CALC.divide()
    result.delete(0, tkinter.END)
    result.insert(0, str(CALC.current_value))
    CALC.set_final_value()
    CALC.lock = True

def perform_operation(method):
    if CALC.init_state:
        get_entry_value()
        if not CALC.lock:
            CALC.current_value = float(CALC.input_value)
        CALC.procedure = method
        CALC.init_state = False
        CALC.refresh_screen = True
        CALC.lock = True
        result.delete(0, tkinter.END)
    else:
        if not CALC.lock:
            CALC.current_value = float(CALC.input_value)
        equal_entries()
        CALC.procedure = method
        CALC.lock = True
        CALC.refresh_screen = False
        result.delete(0, tkinter.END)

def equals():
    equal_entries()
    CALC.lock = False
    CALC.init_state = True
    CALC.refresh_screen = True
    CALC.current_value = 0.0

def create_button(frame, text, command, row, col, colspan=1, width=2):
    btn = tkinter.Button(frame, text=text, command=command, width=width)
    btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew")
    return btn

main_window = tkinter.Tk()
main_window.title("Calculator")
if platform.system() == "Windows":
    main_window.geometry("100x100")
    result_frame = tkinter.Frame(main_window, padx=9)
    result_frame.grid(row=0, column=0, sticky="new")
    result = tkinter.Entry(result_frame, width=17)
    result.insert(0, "0.0")
    result.grid(row=0, column=0, sticky="new")

    button_frame = tkinter.Frame(main_window, padx=5)
    button_frame.grid(row=1, column=0, sticky="new")
elif platform.system() == "Linux":
    main_window.geometry("225x180")
    result_frame = tkinter.Frame(main_window, padx=9)
    result_frame.grid(row=0, column=0, sticky="new")
    result = tkinter.Entry(result_frame, width=22)
    result.insert(0, "0.0")
    result.grid(row=0, column=0, sticky="new")

    button_frame = tkinter.Frame(main_window, padx=5)
    button_frame.grid(row=1, column=0, sticky="new")
else:
    main_window.geometry("225x175")
    result_frame = tkinter.Frame(main_window, padx=9)
    result_frame.grid(row=0, column=0, sticky="new")
    result = tkinter.Entry(result_frame, width=22)
    result.insert(0, "0.0")
    result.grid(row=0, column=0, sticky="new")

    button_frame = tkinter.Frame(main_window, padx=5)
    button_frame.grid(row=1, column=0, sticky="new")

# Button layout: (text, command, row, col, colspan)
buttons = [
    ("C", clear, 1, 0), ("CE", clear_all, 1, 2), ("%", percent_function, 1, 4), ("/", lambda: perform_operation("divide"), 1, 6),
    ("7", lambda: entry_update("7"), 2, 0), ("8", lambda: entry_update("8"), 2, 2), ("9", lambda: entry_update("9"), 2, 4), ("+", lambda: perform_operation("add"), 2, 6),
    ("4", lambda: entry_update("4"), 3, 0), ("5", lambda: entry_update("5"), 3, 2), ("6", lambda: entry_update("6"), 3, 4), ("-", lambda: perform_operation("subtract"), 3, 6),
    ("1", lambda: entry_update("1"), 4, 0), ("2", lambda: entry_update("2"), 4, 2), ("3", lambda: entry_update("3"), 4, 4), ("*", lambda: perform_operation("multiply"), 4, 6),
    ("0", lambda: entry_update("0"), 5, 0), (".", lambda: entry_update("."), 5, 2), ("=", equals, 5, 4, 3, 8)
]

for b in buttons:
    text, cmd, row, col = b[:4]
    colspan = b[4] if len(b) > 4 else 1
    width = b[5] if len(b) > 5 else 2
    create_button(button_frame, text, cmd, row, col, colspan, width)

main_window.update()
main_window.minsize(
    result_frame.winfo_width(),
    result_frame.winfo_height() + button_frame.winfo_height() + 5,
)
main_window.mainloop()