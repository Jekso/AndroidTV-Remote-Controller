Module AndroidTVController.android_tv_controller
================================================

Classes
-------

`AndroidTVController(ip: str)`
:   The class has many important utils to interact with android TV using adb.
    
    Args:
        ip (str): the ip address of the Android TV device

    ### Methods

    `open_amazon_prime(self)`
    :   Opens Amazon Prime Video application

    `open_app(self, package: str, activity: str)`
    :   The function checks if the TV Android app is installed and then starts this app with the specified package and activity.
        
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

    `open_chrome(self)`
    :   Opens Google Chrome application

    `open_netflix(self)`
    :   Opens Netflix application

    `open_watch_it(self)`
    :   Opens Watch IT application

    `open_youtube(self)`
    :   Opens Youtube TV application

    `press_back(self)`
    :   Simulates pressing back button on Android TV device remote control.

    `press_channel_down(self)`
    :   Simulates pressing channel down button on Android TV device remote control.

    `press_channel_number(self, channel_number: str)`
    :   Simulates pressing channel number digits buttons on Android TV device remote control.

    `press_channel_up(self)`
    :   Simulates pressing channel up button on Android TV device remote control.

    `press_dpad_down(self)`
    :   Simulates pressing down button on Android TV device remote control.

    `press_dpad_left(self)`
    :   Simulates pressing left button on Android TV device remote control.

    `press_dpad_right(self)`
    :   Simulates pressing right button on Android TV device remote control.

    `press_dpad_up(self)`
    :   Simulates pressing up button on Android TV device remote control.

    `press_enter(self)`
    :   Simulates pressing enter button on Android TV device remote control.

    `press_home(self)`
    :   Simulates pressing home button on Android TV device remote control.

    `press_power(self)`
    :   Simulates pressing power button on Android TV device remote control.
        you can use it to power on/off the TV device.

    `press_sleep(self)`
    :   Puts the TV into a low-power state. The TV will still be able to receive
        signals from the remote control, and it will wake up quickly when you press a button.

    `press_soft_sleep(self)`
    :   This is a deeper sleep option than sleep, and it uses even less power.
        The TV will not be able to receive signals from the remote control while in soft sleep,
        and it will take a few seconds to wake up when you press a button.

    `press_volume_down(self)`
    :   Simulates pressing volume down button on Android TV device remote control.

    `press_volume_mute(self)`
    :   Simulates pressing volume mute button on Android TV device remote control.

    `press_volume_up(self)`
    :   Simulates pressing volume up button on Android TV device remote control.

    `press_wakeup(self)`
    :   Tell the TV when you want it to wake up from sleep.