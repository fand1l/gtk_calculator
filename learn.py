import sys
import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_default_size(600, 250)
        self.set_title("Random application")

        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.box1)

        self.button = Gtk.Button(label="Test")
        self.box1.append(self.box2)
        self.box1.append(self.box3)

        self.box2.append(self.button)

        self.button.connect('clicked', self.hello)

        self.check = Gtk.CheckButton(label="Test check")
        self.box2.append(self.check)

    def hello(self, button):
        print("Hello")
        if self.check.get_active():
            print("Checked")

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.window = MainWindow(application=app)
        self.window.present()

app = MyApp(application_id="com.fand1l.gtk_calculator")
app.run(sys.argv)
