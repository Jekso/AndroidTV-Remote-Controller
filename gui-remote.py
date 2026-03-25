#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from android_tv_rc import AndroidTVController


# Replace with your device's IP
# To get your Android TV ip address follow this link: https://www.and>
# When running this code for first time and your TV is not paired, ch>
# Then run the code again
ip = '192.168.12.57'
controller = AndroidTVController(ip)
controller.connect()
controller.is_connected()

class Controller:
    def press_home(self):
        controller.press_home()

    def press_tv(self):
        controller.press_tv()

    def press_enter(self):
        controller.press_enter()

    def press_back(self):
        controller.press_back()

    def press_dpad_up(self):
        controller.press_dpad_up()

    def press_dpad_down(self):
        controller.press_dpad_down()

    def press_dpad_left(self):
        controller.press_dpad_left()

    def press_dpad_right(self):
        controller.press_dpad_right()

    def press_volume_up(self):
        controller.press_volume_up()

    def press_volume_down(self):
        controller.press_volume_down()

    def press_volume_mute(self):
        controller.press_mute()

    def press_power(self):
        controller.press_power()

    def press_sleep(self):
        controller.press_sleep()

    def press_soft_sleep(self):
        controller.press_soft_sleep()

    def press_wakeup(self):
        controller.press_wakeup()

class RemoteControllerGUI(Gtk.Window):
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        
        self.set_title("Remote Controller GUI")
        
        self.controller = Controller()  # Initialize your controller here
        
        # Create a vertical box
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        
        # Create a horizontal box for home and tv buttons
        hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        button_home = Gtk.Button(label="Home")
        button_tv = Gtk.Button(label="TV")
        button_home.connect("clicked", lambda *args: self.controller.press_home())
        button_tv.connect("clicked", lambda *args: self.controller.press_tv())
        hbox1.add(button_home)
        hbox1.add(button_tv)
        
        # Create a horizontal box for enter and back buttons
        hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        button_enter = Gtk.Button(label="Enter")
        button_back = Gtk.Button(label="Back")
        button_enter.connect("clicked", lambda *args: self.controller.press_enter())
        button_back.connect("clicked", lambda *args: self.controller.press_back())
        hbox2.add(button_enter)
        hbox2.add(button_back)
        
        # Create a horizontal box for dpad up, down, left and right buttons
        hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        button_up = Gtk.Button(label="Up")
        button_down = Gtk.Button(label="Down")
        button_left = Gtk.Button(label="Left")
        button_right = Gtk.Button(label="Right")
        button_up.connect("clicked", lambda *args: self.controller.press_dpad_up())
        button_down.connect("clicked", lambda *args: self.controller.press_dpad_down())
        button_left.connect("clicked", lambda *args: self.controller.press_dpad_left())
        button_right.connect("clicked", lambda *args: self.controller.press_dpad_right())
        hbox3.add(button_up)
        hbox3.add(button_down)
        hbox3.add(button_left)
        hbox3.add(button_right)
        
        # Create a horizontal box for volume up, down and mute buttons
        hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        button_volume_up = Gtk.Button(label="Vol Up")
        button_volume_down = Gtk.Button(label="Vol Down")
        button_volume_mute = Gtk.Button(label="Mute")
        button_volume_up.connect("clicked", lambda *args: self.controller.press_volume_up())
        button_volume_down.connect("clicked", lambda *args: self.controller.press_volume_down())
        button_volume_mute.connect("clicked", lambda *args: self.controller.press_volume_mute())
        hbox4.add(button_volume_up)
        hbox4.add(button_volume_down)
        hbox4.add(button_volume_mute)
        
        # Create a horizontal box for power, sleep and wake up buttons
        hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        button_power = Gtk.Button(label="Power")
        button_sleep = Gtk.Button(label="Sleep")
        button_wakeup = Gtk.Button(label="Wake Up")
        button_power.connect("clicked", lambda *args: self.controller.press_power())
        button_sleep.connect("clicked", lambda *args: self.controller.press_sleep())
        button_wakeup.connect("clicked", lambda *args: self.controller.press_wakeup())
        hbox5.add(button_power)
        hbox5.add(button_sleep)
        hbox5.add(button_wakeup)
        
        vbox.pack_start(hbox1, False, False, 0)
        vbox.pack_start(hbox2, False, False, 0)
        vbox.pack_start(hbox3, False, False, 0)
        vbox.pack_start(hbox4, False, False, 0)
        vbox.pack_start(hbox5, False, False, 0)
        
        self.add(vbox)

if __name__ == "__main__":
    win = RemoteControllerGUI()
    win.connect("destroy", lambda *args: Gtk.main_quit())
    win.show_all()
    Gtk.main()
