from .key_codes import KeyCodes
from .adb_client import ADBClient
from .tv_apps import AndroidTVApps



class AndroidTVController:



    def __init__(self, ip: str):
        """
        The class has many important utils to interact with android TV using adb.
        
        Args:
            ip (str): the ip address of the Android TV device
        """
        self.__adb_client = ADBClient()
        self.__adb_client.connect(ip)
        


    # ------------------------------[ Navigation Commands ]------------------------------



    def press_home(self):
        """Simulates pressing home button on Android TV device remote control."""
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_HOME)



    def press_back(self):
        """Simulates pressing back button on Android TV device remote control."""
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_BACK)



    def press_dpad_up(self):
        """Simulates pressing up button on Android TV device remote control."""
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_DPAD_UP)



    def press_dpad_down(self):
        """Simulates pressing down button on Android TV device remote control."""
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_DPAD_DOWN)



    def press_dpad_left(self):
        """Simulates pressing left button on Android TV device remote control."""
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_DPAD_LEFT)



    def press_dpad_right(self):
        """Simulates pressing right button on Android TV device remote control."""
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_DPAD_RIGHT)



    def press_enter(self):
        """Simulates pressing enter button on Android TV device remote control."""
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_ENTER)

    
    
    # ------------------------------[ Volume Commands ]------------------------------
    
    
    
    def press_volume_up(self):
        """Simulates pressing volume up button on Android TV device remote control."""
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_VOLUME_UP)



    def press_volume_down(self):
        """Simulates pressing volume down button on Android TV device remote control."""
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_VOLUME_DOWN)



    def press_volume_mute(self):
        """Simulates pressing volume mute button on Android TV device remote control."""
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_VOLUME_MUTE)



    # ------------------------------[ Power Commands ]------------------------------



    def press_power(self):
        """
        Simulates pressing power button on Android TV device remote control.
        you can use it to power on/off the TV device.
        """
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_POWER)
        
        
        
    def press_sleep(self):
        """
        Puts the TV into a low-power state. The TV will still be able to receive
        signals from the remote control, and it will wake up quickly when you press a button. 
        """
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_SLEEP)
        
        
        
    def press_soft_sleep(self):
        """
        This is a deeper sleep option than sleep, and it uses even less power.
        The TV will not be able to receive signals from the remote control while in soft sleep,
        and it will take a few seconds to wake up when you press a button.
        """
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_SOFT_SLEEP)



    def press_wakeup(self):
        """
        Tell the TV when you want it to wake up from sleep.
        """
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_WAKEUP)



    # ------------------------------[ Channels Commands ]------------------------------



    def press_channel_up(self):
        """Simulates pressing channel up button on Android TV device remote control."""
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_TV)
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_CHANNEL_UP)



    def press_channel_down(self):
        """Simulates pressing channel down button on Android TV device remote control."""
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_TV)
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_CHANNEL_DOWN)
        
        
        
    def press_channel_number(self, channel_number: str):
        """Simulates pressing channel number digits buttons on Android TV device remote control."""
        numbers_key_codes = {
            '0': KeyCodes.KEYCODE_0,
            '1': KeyCodes.KEYCODE_1,
            '2': KeyCodes.KEYCODE_2,
            '3': KeyCodes.KEYCODE_3,
            '4': KeyCodes.KEYCODE_4,
            '5': KeyCodes.KEYCODE_5,
            '6': KeyCodes.KEYCODE_6,
            '7': KeyCodes.KEYCODE_7,
            '8': KeyCodes.KEYCODE_8,
            '9': KeyCodes.KEYCODE_9,
        }
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_TV)
        for digit in channel_number:
            self.__adb_client.send_keyevent_input(numbers_key_codes[digit])
    
    
    
    # ------------------------------[ Apps Commands ]------------------------------

    
    
    def open_app(self, package: str, activity: str):
        """
        The function checks if the TV Android app is installed and then starts this app with the specified package and activity.
        
        To get the package name for an app search for it on google, or
        if the app is installed use `adb_client.list_packages()` method.
        To get main activity name use `adb_client.get_package_activities(package_name)`
        and try to interpret the output dump to extract the main launcher activity.
    
        Args:
            package (str): The package parameter is a string that represents the package name of the
                Android application you want to start. This is typically the unique identifier for the app and
                is specified in the AndroidManifest.xml file of the app.
            activity (str): The "activity" parameter refers to the specific activity or screen within the
                Android app that you want to start. An activity represents a single screen with a user
                interface, and it is the basic building block of an Android app. Each activity has a unique name
                that is specified in the AndroidManifest.xml file
        """
        if self.__adb_client.is_installed(package):
            self.__adb_client.start_app(package, activity)
    
    
    
    def open_chrome(self):
        """Opens Google Chrome application"""
        app = AndroidTVApps.CHROME.value.split('/')
        self.open_app(app[0], app[1])

    
    
    def open_youtube(self):
        """Opens Youtube TV application"""
        app = AndroidTVApps.YOUTUBE.value.split('/')
        self.open_app(app[0], app[1])
    
    
    
    def open_netflix(self):
        """Opens Netflix application"""
        app = AndroidTVApps.NETFLIX.value.split('/')
        self.open_app(app[0], app[1])
    
    
    
    def open_amazon_prime(self):
        """Opens Amazon Prime Video application"""
        app = AndroidTVApps.AMAZON_PRIME.value.split('/')
        self.open_app(app[0], app[1])
        
        
        
    def open_watch_it(self):
        """Opens Watch IT application"""
        app = AndroidTVApps.WATCH_IT.value.split('/')
        self.open_app(app[0], app[1])