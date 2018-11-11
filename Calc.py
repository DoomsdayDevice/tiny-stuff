from tkinter import *


class Calculator (Frame):
    """creates a frame inside the window"""
    def __init__(self, window):
        Frame.__init__(self, window)
        window.geometry("305x450")
        window.title("SkyNet v1.1")
        window.resizable(False, False)

        self.grid()
        self.x = 0
        self.y = 0
        self.create_variables()
        self.create_widgets()
        self.create_buttons()
        self.update_text()
        # self.updateText()

    def create_variables(self):
        # the current number
        self.crnt_numb = DoubleVar()
        self.crnt_numb = 0
        # the number that was put into memory, the one before the operation button was pressed
        self.first_number = None
        self.point_is_pressed = False
        # current operation field, set as a variable, label updates automatically
        self.crnt_op_field = StringVar()
        self.crnt_op_field.set("0")

    def create_widgets(self):
        # the number field at the top
        self.number_field = Text(self, width=35, height=1)
        self.number_field.grid(row=self.y, column=self.x, columnspan=4, sticky=E, padx=10, pady=10)
        self.y += 1

        Label(self, textvariable=self.crnt_op_field).grid(row=1, column=self.x, columnspan=4, padx=5, pady=5, sticky=E)
        self.y += 1

    def create_buttons(self):
        # number buttons

        # clearing the field
        self.clear_fields_bt = CalcButton(text="CLEAR", fg="red",
                                          parent=self, width=17, columnspan=2, command="self.clear_fields")
        self.y += 1
        # digit buttons
        self.digit_buttons = []
        counter = 1
        for i in range(0, 3):
            for j in range(0, 3):
                self.create_digit(counter)
                counter += 1
                self.x += 1
            self.x = 0
            self.y += 1

        self.x = 0
        self.y = 6
        self.create_digit(0)
        # point button
        self.x += 1
        self.point_button = CalcButton(text=".", parent=self, command="self.point")
        # sign button
        self.x += 1
        self.sign_button = CalcButton(text="-/+", parent=self, command="self.sign")

        # division
        self.y = 2
        self.division_button = CalcButton(text=":", parent=self, command="self.divide")
        # multiplication
        self.x += 1
        self.multi_button = CalcButton(text="X", parent=self, command="self.multi")
        # subtraction
        self.y += 1
        self.subtraction_button = CalcButton(text="-", parent=self, command="self.subtract")
        # addition
        self.y += 1
        self.add_button = CalcButton(text="+", parent=self, height=8, rowspan=2, command="self.add")
        # inference
        self.y += 2
        self.infer_button = CalcButton(text="=", parent=self, command="self.infer")

    def create_digit(self, i):
        self.digit_buttons.append(DigitButton(text=i, digit=i, parent=self, command="self.digit_button"))

    def update_text(self):
        # updates text in the number field
        self.number_field.delete(0.0, END)
        self.number_field.insert(0.0, str(self.crnt_numb))
        # for some reason the numbers appear on line 1, but column 0
        if self.number_field.get(1.0, 1.5) == "1488":
            self.photo = PhotoImage(file="swastika.gif")
            new_window = Toplevel()
            new_window.title("heil")
            label = Label(new_window, bg="red", image=self.photo)
            label.grid()
        if self.number_field.get(1.0, 1.4) == "228":
            self.photo = PhotoImage(file="manager.gif")
            new_window = Toplevel()
            new_window.title("smoek weed evry day")
            label = Label(master=new_window, image=self.photo)
            label.pack()


class CalcButton(Button):
    def __init__(self, text, parent, command="self.press", columnspan=1, rowspan=1, width=6, height=3, fg="black"):
        # using "eval" to convert the string passed down into an object reference
        Button.__init__(self, master=parent, width=width, height=height, text=text, command=eval(command), fg=fg)
        self.grid(column=parent.x, row=parent.y, pady=6, padx=2, columnspan=columnspan, rowspan=rowspan)
        self.parent = parent

    def clear_fields(self):
        self.parent.number_field.delete(0.0, END)
        self.parent.number_field.insert(0.0, '0')
        self.parent.crnt_op_field.set("0")
        self.parent.crnt_numb = 0
        self.parent.first_number = None
        self.unpoint()

    """point button funcs"""
    def point(self):
        self.parent.point_is_pressed = True
        self.parent.point_button.config(bg="grey")

    def unpoint(self):
        self.parent.point_is_pressed = False
        self.parent.point_button.config(bg="SystemButtonFace")

    def press(self): pass

    def sign(self):
        #
        if self.parent.crnt_numb < 0:
            self.parent.crnt_numb = abs(self.parent.crnt_numb)
        else:
            self.parent.crnt_numb = 0 - self.parent.crnt_numb
        self.parent.update_text()

    def divide(self):
        if self.parent.first_number is None:
            self.parent.first_number = self.parent.crnt_numb
            self.parent.crnt_op_field.set(str(self.parent.crnt_numb) + " : ")
            self.parent.crnt_sign = ":"
            self.parent.crnt_numb = 0
            self.unpoint()
        else:
            self.infer()

    def multi(self):
        if self.parent.first_number is None:
            self.parent.first_number = self.parent.crnt_numb
            self.parent.crnt_op_field.set(str(self.parent.crnt_numb) + " X ")
            self.parent.crnt_sign = "x"
            self.parent.crnt_numb = 0
            self.unpoint()
        else:
            self.infer()

    def subtract(self):
        if self.parent.first_number is None:
            self.parent.first_number = self.parent.crnt_numb
            self.parent.crnt_op_field.set(str(self.parent.crnt_numb) + " - ")
            self.parent.crnt_sign = "-"
            self.parent.crnt_numb = 0
            self.unpoint()
        else:
            self.infer()

    def add(self):
        if self.parent.first_number is None:
            self.parent.first_number = self.parent.crnt_numb
            self.parent.crnt_op_field.set(str(self.parent.crnt_numb) + " + ")
            self.parent.crnt_sign = "+"
            self.parent.crnt_numb = 0
            self.unpoint()
        else:
            self.infer()

    def infer(self):
        if self.parent.crnt_sign == ":":
            self.parent.first_number = self.parent.first_number / self.parent.crnt_numb
        elif self.parent.crnt_sign == "x":
            self.parent.first_number = self.parent.first_number * self.parent.crnt_numb
        elif self.parent.crnt_sign == "+":
            self.parent.first_number = self.parent.first_number + self.parent.crnt_numb
        elif self.parent.crnt_sign == "-":
            self.parent.first_number = self.parent.first_number - self.parent.crnt_numb
        self.parent.crnt_op_field.set(self.parent.crnt_op_field.get() +
                                      str(self.parent.crnt_numb) + " = " + str(self.parent.first_number))
        self.parent.first_number = None
        self.parent.crnt_numb = 0
        self.unpoint()


class DigitButton(CalcButton):
    # digits
    def __init__(self, digit, **kwargs):
        CalcButton.__init__(self, **kwargs)
        self.digit = digit

    def digit_button(self):
        if self.parent.point_is_pressed and float(self.parent.crnt_numb).is_integer():
            self.parent.crnt_numb = float(str(self.parent.crnt_numb) + ".%s" % self.digit)
        elif self.parent.point_is_pressed:
            self.parent.crnt_numb = float(str(self.parent.crnt_numb) + "%s" % self.digit)
        else:
            self.parent.crnt_numb = int(str(self.parent.crnt_numb) + str(self.digit))
        self.parent.update_text()


my_window = Tk()
my_calc = Calculator(my_window)
my_window.mainloop()
