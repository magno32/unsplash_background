#!/usr/bin/python
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from g_random_background import update_background

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onRandomPressed(self, button):
        width = str(int(widthSpinner.get_value()))
        height = str(int(heightSpinner.get_value()))
        update_background(width, height)


builder = Gtk.Builder()
builder.add_from_file("main.glade")
builder.connect_signals(Handler())

widthSpinner = builder.get_object("widthSpinner")
widthSpinner.set_range(0,9999)
widthSpinner.set_value(1920)

heightSpinner = builder.get_object("heightSpinner")
heightSpinner.set_range(0,9999)
heightSpinner.set_value(1080)

window = builder.get_object("mainWindow")
window.show_all()

Gtk.main()
