import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

text = []

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_default_size(350, 500)
        self.set_resizable(False)
        self.set_title("Calculator")

        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.text_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.text_box.set_vexpand(False)
        self.text_box.set_valign(Gtk.Align.START)
        self.text_box.set_size_request(-1, 100)

        self.keyboard_grid = Gtk.Grid()
        self.keyboard_grid.set_vexpand(True)
        self.keyboard_grid.set_row_homogeneous(True)
        self.keyboard_grid.set_column_homogeneous(True)

        self.main_box.append(self.text_box)
        self.main_box.append(self.keyboard_grid)

        self.num_button_0 = Gtk.Button(label="0")
        self.num_button_1 = Gtk.Button(label="1")
        self.num_button_2 = Gtk.Button(label="2")
        self.num_button_3 = Gtk.Button(label="3")
        self.num_button_4 = Gtk.Button(label="4")
        self.num_button_5 = Gtk.Button(label="5")
        self.num_button_6 = Gtk.Button(label="6")
        self.num_button_7 = Gtk.Button(label="7")
        self.num_button_8 = Gtk.Button(label="8")
        self.num_button_9 = Gtk.Button(label="9")

        self.func_button_dividing = Gtk.Button(label="/")
        self.func_button_multiply = Gtk.Button(label="*")
        self.func_button_minus = Gtk.Button(label="-")
        self.func_button_plus = Gtk.Button(label="+")
        self.func_button_equals = Gtk.Button(label="=")
        self.func_button_dot = Gtk.Button(label=".")
        self.func_button_del = Gtk.Button(label="<")

        self.num_button_0.connect('clicked', self.buttons_clicked, 0)
        self.num_button_1.connect('clicked', self.buttons_clicked, 1)
        self.num_button_2.connect('clicked', self.buttons_clicked, 2)
        self.num_button_3.connect('clicked', self.buttons_clicked, 3)
        self.num_button_4.connect('clicked', self.buttons_clicked, 4)
        self.num_button_5.connect('clicked', self.buttons_clicked, 5)
        self.num_button_6.connect('clicked', self.buttons_clicked, 6)
        self.num_button_7.connect('clicked', self.buttons_clicked, 7)
        self.num_button_8.connect('clicked', self.buttons_clicked, 8)
        self.num_button_9.connect('clicked', self.buttons_clicked, 9)

        self.func_button_dividing.connect('clicked', self.buttons_clicked, "/")
        self.func_button_multiply.connect('clicked', self.buttons_clicked, "*")
        self.func_button_minus.connect('clicked', self.buttons_clicked, "-")
        self.func_button_plus.connect('clicked', self.buttons_clicked, "+")
        self.func_button_equals.connect('clicked', self.buttons_clicked, "=")
        self.func_button_dot.connect('clicked', self.buttons_clicked, ".")
        self.func_button_del.connect('clicked', self.buttons_clicked, "<")

        self.enter_box = Gtk.Label(label="          ")
        
        self.keyboard_grid.attach(self.num_button_7, 0, 0, 1, 1)
        self.keyboard_grid.attach(self.num_button_8, 1, 0, 1, 1)
        self.keyboard_grid.attach(self.num_button_9, 2, 0, 1, 1)
        self.keyboard_grid.attach(self.func_button_dividing, 3, 0, 1, 1)

        self.keyboard_grid.attach(self.num_button_4, 0, 1, 1, 1)
        self.keyboard_grid.attach(self.num_button_5, 1, 1, 1, 1)
        self.keyboard_grid.attach(self.num_button_6, 2, 1, 1, 1)
        self.keyboard_grid.attach(self.func_button_multiply, 3, 1, 1, 1)

        self.keyboard_grid.attach(self.num_button_1, 0, 2, 1, 1)
        self.keyboard_grid.attach(self.num_button_2, 1, 2, 1, 1)
        self.keyboard_grid.attach(self.num_button_3, 2, 2, 1, 1)
        self.keyboard_grid.attach(self.func_button_minus, 3, 2, 1, 1)

        self.keyboard_grid.attach(self.num_button_0, 0, 3, 1, 1)
        self.keyboard_grid.attach(self.func_button_dot, 1, 3, 1, 1)
        self.keyboard_grid.attach(self.func_button_equals, 2, 3, 1, 1)
        self.keyboard_grid.attach(self.func_button_plus, 3, 3, 1, 1)

        self.text_box.append(self.enter_box)
        self.text_box.append(self.func_button_del)

        self.set_child(self.main_box)


    def buttons_clicked(self, button, label):
        global text
        if label in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "/", "*", "+", "-", "."]:
            text.append(str(label))  # Додаємо значення як рядок
        elif label == "<":
            text.pop()
        elif label == "=":
            if text[-1] in ["/", "*", "+", "-", "."]:
                print("Error")
                text = []
            else:
                has_consecutive_signs = False
                for i in range(len(text) - 1):
                    if text[i] in ["/", "*", "+", "-", "."] and text[i + 1] in ["/", "*", "+", "-", "."]:
                        has_consecutive_signs = True
                        break
                
                if has_consecutive_signs:
                    print("Error: два знаки підряд.")
                    text = []
                else:
                    expression = "".join(text)
                    result = eval(expression)
                    print(result)
                    text = []

        str_enter = ""
        for i in text:
            i = str(i)
            str_enter += i

        print(str_enter)


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.window = MainWindow(application=app)
        self.window.present()


app = MyApp(application_id="com.fand1l.gtk_calculator")
app.run(sys.argv)
