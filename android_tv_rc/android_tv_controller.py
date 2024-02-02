from .adb_client import ADBClient
from .tv_apps import AndroidTVApps
from .key_codes import KeyCodes


class AndroidTVController:



    def __init__(self, ip: str, verbose: bool=False, show_command: bool=False):
        """
        The class has many important utils to interact with android TV using adb.
        
        Args:
            ip (str): the ip address of the Android TV device
            verbose (bool): The `verbose` parameter is a boolean flag that determines whether or not to
                enable verbose logging. If set to `True`, it will display additional information during the
                execution of the code. If set to `False` (default), it will not display any additional
                information. Defaults to False.
            show_command (bool): The `show_command` parameter is a boolean flag that determines whether or
                not to display the executed ADB commands. If `show_command` is set to `True`, the executed ADB
                commands will be shown. If `show_command` is set to `False`, the executed ADB commands will.
                Defaults to False.
        """
        self.__adb_client = ADBClient(verbose, show_command)
        self.__ip = ip
    
    
    
    def connect(self) -> bool:
        """
        Start connection to TV IP.
        """
        return self.__adb_client.connect(self.__ip)
    
    
    
    def is_connected(self) -> bool:
        """
        Check if connection is successfully established.
        """
        return self.__adb_client.is_connected(self.__ip)
        
        
        
    def get_adb_client(self):
        """
        Return the adb session client.
        """
        return self.__adb_client
        


    # ------------------------------[ Navigation Commands ]------------------------------



    def press_home(self):
        """Simulates pressing home button on Android TV device remote control."""
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_HOME)



    def press_tv(self):
        """Simulates pressing TV input button on Android TV device remote control."""
        self.__adb_client.send_keyevent_input(KeyCodes.KEYCODE_TV)
        
        
        
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



    def is_powered_on(self) -> bool|None:
        """
        Check if TV is working or not. (Power ON/OFF)
        
        Return:
            Statues of TV power on or off.
        """
        return self.__adb_client.is_powered_on()
    
    
    
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

    
    
    def open_app(self, app: AndroidTVApps):
        """
        The function starts app with the specified package and activity.
        
        To get the package name for an app search for it on google, or
        if the app is installed use `adb_client.list_packages()` method.
        To get main activity name use `adb_client.get_package_activities(package_name)`
        and try to interpret the output dump to extract the main launcher activity.
    
        Args:
            app (AndroidTVApps): The app name in form of package/activity.
        """
        package, activity = app.value.split('/')
        self.__adb_client.start_app(package, activity)

    
    
    def open_youtube(self):
        """Opens Youtube TV application"""
        self.open_app(AndroidTVApps.YOUTUBE)
    
    
    
    def open_netflix(self):
        """Opens Netflix application"""
        self.open_app(AndroidTVApps.NETFLIX)

    
    
    
    def open_amazon_prime(self):
        """Opens Amazon Prime Video application"""
        self.open_app(AndroidTVApps.AMAZON_PRIME)
        
        
        
    def open_watch_it(self):
        """Opens Watch IT application"""
        self.open_app(AndroidTVApps.WATCH_IT)
        
    
    
    def open_shahid(self):
        """Opens Shahid application"""
        self.open_app(AndroidTVApps.SHAHID)