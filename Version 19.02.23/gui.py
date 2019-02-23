import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.box = Gtk.Box(spacing=2)
        self.box.set_border_width(2)## set border width, not the container width

        self.button1 = Gtk.Button(label="Hello")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Goodbye")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

        self.grid.add(self.box)

        # self.upButton = Gtk.Button(label="up")
        # self.upButton.connect("clicked", self.on_upButton_clicked)
        # self.grid.attach(self.upButton, 1, 0, 1, 1)## object, col, row, width, height
        #
        # self.downButton = Gtk.Button(label="down")
        # self.downButton.connect("clicked", self.on_downButton_clicked)
        # self.grid.attach(self.downButton, 1, 1, 1, 1)## object, col, row, width, height

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.set_border_width(2)## set border width, not the container width
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        button = Gtk.Button()
        button.add(Gtk.Arrow(Gtk.ArrowType.UP, Gtk.ShadowType.NONE))
        button.connect("clicked", self.on_upButton_clicked)
        box.add(button)

        button = Gtk.Button()
        button.add(Gtk.Arrow(Gtk.ArrowType.DOWN, Gtk.ShadowType.NONE))
        button.connect("clicked", self.on_downButton_clicked)
        box.add(button)

        self.grid.add(box)

        self.set_decorated(False)




    def on_button1_clicked(self, widget):
        print("Hello")

    def on_button2_clicked(self, widget):
        print("Goodbye")

    def on_upButton_clicked(self, widget):
        print("up")

    def on_downButton_clicked(self, widget):
        print("down")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()