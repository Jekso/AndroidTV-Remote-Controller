 # AndroidTV-Remote-Controller

**Effortlessly control your Android TV using Python and ADB!**

This python library empowers you to seamlessly interact with your Android TV device programmatically, simulating key presses, launching apps, and executing various commands through ADB (Android Debug Bridge).
This means you can use it to control your Android TV or even any android devices with very simple python methods, very useful for creating custom apps for smart homes.

## Features

- **Comprehensive command set:**
    - Works with any Android TV device.
    - Easy and clean API to use a lot of adb commands without going deep into details and different options.
    - Connect many Android devices like Phones, TVs, Wearables, etc using USB and Wireless TCP connections.
    - List rich devices information.
    - Upload and download files (eg. APK files, Images, Videos, etc).
    - Install/Uninstall android apps.
    - List all packages and easily filter them as system, third-party, enabled, disabled apps.
    - Get package activities to easily use it for auto starting and stopping apps.
    - Interact with device shell and invoke any shell commands.
    - List services and stop them
    - Power On/Off, Sleep, Soft sleep & Wake up the TV.
    - Easily navigate home screen and menus using D-Pad navigation
    - Control volume (up, down, mute)
    - Control channel buttons (up, down) or using channel number
    - Send text input for any input fields (e.g., Search).
    - Open famous apps (e.g., YouTube, Netflix, Amazon Prime, Watch IT)
    - Start any other application by using its package name.
    - Simulate all android key codes not just for TV but any android device: <a href="https://www.temblast.com/ref/akeyscode.htm" target="_blank">Check Supported Key Codes List</a>
- **Clear and concise API:**
    - Intuitive methods for common actions
    - Well-organized code structure
    - Open for extensions
- **ADB integration:**
    - Handles ADB communication smoothly
    - No need for manual ADB setup
- **Cross-platform compatibility:**
    - Works seamlessly on Windows, macOS, and Linux

## Installation


1. Before running you need to Android Platform Tools installed and available in your PATH environment variable. you can do this from <a href="https://developer.android.com/tools/releases/platform-tools" target="_blank">here</a>, then you can check by open a terminal and write `adb --version` if this gives an error make sure you follow the instructions and the platform-tools folder is in your PATH environment variable.
            

2. Make sure your Computer and the Android TV is on the same WiFi network.
3. Pair your Android TV device.<a href="https://developer.android.com/tools/adb" target="_blank"> Instructions</a>
4. Download the repository by click download from github or by cloning it using this command `git clone https://github.com/Jekso/AndroidTV-Remote-Controller.git`, I will upload it to PyPi soon to easily download it using pip but for now use it locally as mentioned.
5. You are ready to go, start hacking your TV xD
## Usage


you can use `AndroidTVController` class to invoke TV commands.
```python
from android_tv_controller import AndroidTVController

# Replace with your device's IP
# To get your Android TV ip address follow this link: https://www.androidtvtricks.com/ip-address-on-android-tv-box/
controller = AndroidTVController("192.168.1.100")  

# --------------[ Navigation Commands ]--------------
controller.press_home()
controller.press_back()
controller.press_dpad_up()
controller.press_dpad_down()
controller.press_dpad_left()
controller.press_dpad_right()
controller.press_enter()


# --------------[ Volume Commands ]--------------
controller.press_volume_up()
controller.press_volume_down()
controller.press_volume_mute()


# --------------[ Power Commands ]--------------
controller.press_power()
controller.press_sleep()
controller.press_soft_sleep()
controller.press_wakeup()


# --------------[ Power Commands ]--------------
controller.press_channel_up()
controller.press_channel_down()
controller.press_channel_number('213')


# --------------[ Apps Commands ]--------------
controller.open_chrome()
controller.open_youtube()
controller.open_netflix()
controller.open_amazon_prime()
controller.open_watch_it()
controller.open_app('com.android.chrome', 'com.google.android.apps.chrome.Main')
```

Also you can use ADB commands API from `ADBClient` class.
```python
from adb_client import ADBClient
from key_codes import KeyCodes


client = ADBClient()  


# --------------[ Connectivity Commands ]--------------
adb_client.connect('192.168.1.103')
adb_client.is_connected('192.168.1.103')
adb_client.disconnect()


# --------------[ Info Commands ]--------------
adb_client.get_devices()
adb_client.select_device('192.168.1.103:5555')
adb_client.get_device_info()
adb_client.get_state()
adb_client.get_serialno()
adb_client.get_devpath()
adb_client.get_ip_address()


# --------------[ File Operations Commands ]--------------
adb_client.push('./test_app.apk', remote str='/data/local/tmp/')
adb_client.pull('/data/local/tmp/test.apk', './')


# --------------[ Apps Operations Commands ]--------------
adb_client.list_packages(package_type='all') # system, enabled, disabled
adb_client.get_package_activities('com.spotify.lite')
adb_client.is_installed('com.spotify.lite')
adb_client.install('test.apk')
adb_client.uninstall('com.spotify.lite')
adb_client.start_app('com.android.chrome', 'com.google.android.apps.chrome.Main')
adb_client.stop_app('com.android.chrome')


# --------------[ Device related Commands ]--------------
adb_client.reboot()
adb_client.execute_shell_command('rm -f /sdcard/test.apk')


# --------------[ Services Commands ]--------------
adb_client.list_services()
adb_client.start_service('com.android.Settings/com.android.Settings.ServiceName')
adb_client.stop_service('com.android.Settings/com.android.Settings.ServiceName')


# --------------[ Inputs Commands ]--------------
adb_client.send_keyevent_input(KeyCodes.KeyCodes.KEYCODE_HOME)
adb_client.send_text_input('Welcome to Metaverse')
```

For all key codes you can use any of these enum values
```text
KeyCodes.KEYCODE_UNKNOWN
KeyCodes.KEYCODE_SOFT_LEFT
KeyCodes.KEYCODE_SOFT_RIGHT
KeyCodes.KEYCODE_HOME
KeyCodes.KEYCODE_BACK
KeyCodes.KEYCODE_CALL
KeyCodes.KEYCODE_ENDCALL
KeyCodes.KEYCODE_0
KeyCodes.KEYCODE_1
KeyCodes.KEYCODE_2
KeyCodes.KEYCODE_3
KeyCodes.KEYCODE_4
KeyCodes.KEYCODE_5
KeyCodes.KEYCODE_6
KeyCodes.KEYCODE_7
KeyCodes.KEYCODE_8
KeyCodes.KEYCODE_9
KeyCodes.KEYCODE_STAR
KeyCodes.KEYCODE_POUND
KeyCodes.KEYCODE_DPAD_UP
KeyCodes.KEYCODE_DPAD_DOWN
KeyCodes.KEYCODE_DPAD_LEFT
KeyCodes.KEYCODE_DPAD_RIGHT
KeyCodes.KEYCODE_DPAD_CENTER
KeyCodes.KEYCODE_VOLUME_UP
KeyCodes.KEYCODE_VOLUME_DOWN
KeyCodes.KEYCODE_POWER
KeyCodes.KEYCODE_CAMERA
KeyCodes.KEYCODE_CLEAR
KeyCodes.KEYCODE_A
KeyCodes.KEYCODE_B
KeyCodes.KEYCODE_C
KeyCodes.KEYCODE_D
KeyCodes.KEYCODE_E
KeyCodes.KEYCODE_F
KeyCodes.KEYCODE_G
KeyCodes.KEYCODE_H
KeyCodes.KEYCODE_I
KeyCodes.KEYCODE_J
KeyCodes.KEYCODE_K
KeyCodes.KEYCODE_L
KeyCodes.KEYCODE_M
KeyCodes.KEYCODE_N
KeyCodes.KEYCODE_O
KeyCodes.KEYCODE_P
KeyCodes.KEYCODE_Q
KeyCodes.KEYCODE_R
KeyCodes.KEYCODE_S
KeyCodes.KEYCODE_T
KeyCodes.KEYCODE_U
KeyCodes.KEYCODE_V
KeyCodes.KEYCODE_W
KeyCodes.KEYCODE_X
KeyCodes.KEYCODE_Y
KeyCodes.KEYCODE_Z
KeyCodes.KEYCODE_COMMA
KeyCodes.KEYCODE_PERIOD
KeyCodes.KEYCODE_ALT_LEFT
KeyCodes.KEYCODE_ALT_RIGHT
KeyCodes.KEYCODE_SHIFT_LEFT
KeyCodes.KEYCODE_SHIFT_RIGHT
KeyCodes.KEYCODE_TAB
KeyCodes.KEYCODE_SPACE
KeyCodes.KEYCODE_SYM
KeyCodes.KEYCODE_EXPLORER
KeyCodes.KEYCODE_ENVELOPE
KeyCodes.KEYCODE_ENTER
KeyCodes.KEYCODE_DEL
KeyCodes.KEYCODE_GRAVE
KeyCodes.KEYCODE_MINUS
KeyCodes.KEYCODE_EQUALS
KeyCodes.KEYCODE_LEFT_BRACKET
KeyCodes.KEYCODE_RIGHT_BRACKET
KeyCodes.KEYCODE_BACKSLASH
KeyCodes.KEYCODE_SEMICOLON
KeyCodes.KEYCODE_APOSTROPHE
KeyCodes.KEYCODE_SLASH
KeyCodes.KEYCODE_AT
KeyCodes.KEYCODE_NUM
KeyCodes.KEYCODE_HEADSETHOOK
KeyCodes.KEYCODE_FOCUS
KeyCodes.KEYCODE_PLUS
KeyCodes.KEYCODE_MENU
KeyCodes.KEYCODE_NOTIFICATION
KeyCodes.KEYCODE_SEARCH
KeyCodes.KEYCODE_MEDIA_PLAY_PAUSE
KeyCodes.KEYCODE_MEDIA_STOP
KeyCodes.KEYCODE_MEDIA_NEXT
KeyCodes.KEYCODE_MEDIA_PREVIOUS
KeyCodes.KEYCODE_MEDIA_REWIND
KeyCodes.KEYCODE_MEDIA_FAST_FORWARD
KeyCodes.KEYCODE_MUTE
KeyCodes.KEYCODE_PAGE_UP
KeyCodes.KEYCODE_PAGE_DOWN
KeyCodes.KEYCODE_PICTSYMBOLS
KeyCodes.KEYCODE_SWITCH_CHARSET
KeyCodes.KEYCODE_BUTTON_A
KeyCodes.KEYCODE_BUTTON_B
KeyCodes.KEYCODE_BUTTON_C
KeyCodes.KEYCODE_BUTTON_X
KeyCodes.KEYCODE_BUTTON_Y
KeyCodes.KEYCODE_BUTTON_Z
KeyCodes.KEYCODE_BUTTON_L1
KeyCodes.KEYCODE_BUTTON_R1
KeyCodes.KEYCODE_BUTTON_L2
KeyCodes.KEYCODE_BUTTON_R2
KeyCodes.KEYCODE_BUTTON_THUMBL
KeyCodes.KEYCODE_BUTTON_THUMBR
KeyCodes.KEYCODE_BUTTON_START
KeyCodes.KEYCODE_BUTTON_SELECT
KeyCodes.KEYCODE_BUTTON_MODE
KeyCodes.KEYCODE_ESCAPE
KeyCodes.KEYCODE_FORWARD_DEL
KeyCodes.KEYCODE_CTRL_LEFT
KeyCodes.KEYCODE_CTRL_RIGHT
KeyCodes.KEYCODE_CAPS_LOCK
KeyCodes.KEYCODE_SCROLL_LOCK
KeyCodes.KEYCODE_META_LEFT
KeyCodes.KEYCODE_META_RIGHT
KeyCodes.KEYCODE_FUNCTION
KeyCodes.KEYCODE_SYSRQ
KeyCodes.KEYCODE_BREAK
KeyCodes.KEYCODE_MOVE_HOME
KeyCodes.KEYCODE_MOVE_END
KeyCodes.KEYCODE_INSERT
KeyCodes.KEYCODE_FORWARD
KeyCodes.KEYCODE_MEDIA_PLAY
KeyCodes.KEYCODE_MEDIA_PAUSE
KeyCodes.KEYCODE_MEDIA_CLOSE
KeyCodes.KEYCODE_MEDIA_EJECT
KeyCodes.KEYCODE_MEDIA_RECORD
KeyCodes.KEYCODE_F1
KeyCodes.KEYCODE_F2
KeyCodes.KEYCODE_F3
KeyCodes.KEYCODE_F4
KeyCodes.KEYCODE_F5
KeyCodes.KEYCODE_F6
KeyCodes.KEYCODE_F7
KeyCodes.KEYCODE_F8
KeyCodes.KEYCODE_F9
KeyCodes.KEYCODE_F10
KeyCodes.KEYCODE_F11
KeyCodes.KEYCODE_F12
KeyCodes.KEYCODE_NUM_LOCK
KeyCodes.KEYCODE_NUMPAD_0
KeyCodes.KEYCODE_NUMPAD_1
KeyCodes.KEYCODE_NUMPAD_2
KeyCodes.KEYCODE_NUMPAD_3
KeyCodes.KEYCODE_NUMPAD_4
KeyCodes.KEYCODE_NUMPAD_5
KeyCodes.KEYCODE_NUMPAD_6
KeyCodes.KEYCODE_NUMPAD_7
KeyCodes.KEYCODE_NUMPAD_8
KeyCodes.KEYCODE_NUMPAD_9
KeyCodes.KEYCODE_NUMPAD_DIVIDE
KeyCodes.KEYCODE_NUMPAD_MULTIPLY
KeyCodes.KEYCODE_NUMPAD_SUBTRACT
KeyCodes.KEYCODE_NUMPAD_ADD
KeyCodes.KEYCODE_NUMPAD_DOT
KeyCodes.KEYCODE_NUMPAD_COMMA
KeyCodes.KEYCODE_NUMPAD_ENTER
KeyCodes.KEYCODE_NUMPAD_EQUALS
KeyCodes.KEYCODE_NUMPAD_LEFT_PAREN
KeyCodes.KEYCODE_NUMPAD_RIGHT_PAREN
KeyCodes.KEYCODE_VOLUME_MUTE
KeyCodes.KEYCODE_INFO
KeyCodes.KEYCODE_CHANNEL_UP
KeyCodes.KEYCODE_CHANNEL_DOWN
KeyCodes.KEYCODE_ZOOM_IN
KeyCodes.KEYCODE_ZOOM_OUT
KeyCodes.KEYCODE_TV
KeyCodes.KEYCODE_WINDOW
KeyCodes.KEYCODE_GUIDE
KeyCodes.KEYCODE_DVR
KeyCodes.KEYCODE_BOOKMARK
KeyCodes.KEYCODE_CAPTIONS
KeyCodes.KEYCODE_SETTINGS
KeyCodes.KEYCODE_TV_POWER
KeyCodes.KEYCODE_TV_INPUT
KeyCodes.KEYCODE_STB_POWER
KeyCodes.KEYCODE_STB_INPUT
KeyCodes.KEYCODE_AVR_POWER
KeyCodes.KEYCODE_AVR_INPUT
KeyCodes.KEYCODE_PROG_RED
KeyCodes.KEYCODE_PROG_GREEN
KeyCodes.KEYCODE_PROG_YELLOW
KeyCodes.KEYCODE_PROG_BLUE
KeyCodes.KEYCODE_APP_SWITCH
KeyCodes.KEYCODE_BUTTON_1
KeyCodes.KEYCODE_BUTTON_2
KeyCodes.KEYCODE_BUTTON_3
KeyCodes.KEYCODE_BUTTON_4
KeyCodes.KEYCODE_BUTTON_5
KeyCodes.KEYCODE_BUTTON_6
KeyCodes.KEYCODE_BUTTON_7
KeyCodes.KEYCODE_BUTTON_8
KeyCodes.KEYCODE_BUTTON_9
KeyCodes.KEYCODE_BUTTON_10
KeyCodes.KEYCODE_BUTTON_11
KeyCodes.KEYCODE_BUTTON_12
KeyCodes.KEYCODE_BUTTON_13
KeyCodes.KEYCODE_BUTTON_14
KeyCodes.KEYCODE_BUTTON_15
KeyCodes.KEYCODE_BUTTON_16
KeyCodes.KEYCODE_LANGUAGE_SWITCH
KeyCodes.KEYCODE_MANNER_MODE
KeyCodes.KEYCODE_3D_MODE
KeyCodes.KEYCODE_CONTACTS
KeyCodes.KEYCODE_CALENDAR
KeyCodes.KEYCODE_MUSIC
KeyCodes.KEYCODE_CALCULATOR
KeyCodes.KEYCODE_ZENKAKU_HANKAKU
KeyCodes.KEYCODE_EISU
KeyCodes.KEYCODE_MUHENKAN
KeyCodes.KEYCODE_HENKAN
KeyCodes.KEYCODE_KATAKANA_HIRAGANA
KeyCodes.KEYCODE_YEN
KeyCodes.KEYCODE_RO
KeyCodes.KEYCODE_KANA
KeyCodes.KEYCODE_ASSIST
KeyCodes.KEYCODE_BRIGHTNESS_DOWN
KeyCodes.KEYCODE_BRIGHTNESS_UP
KeyCodes.KEYCODE_MEDIA_AUDIO_TRACK
KeyCodes.KEYCODE_SLEEP
KeyCodes.KEYCODE_WAKEUP
KeyCodes.KEYCODE_PAIRING
KeyCodes.KEYCODE_MEDIA_TOP_MENU
KeyCodes.KEYCODE_11
KeyCodes.KEYCODE_12
KeyCodes.KEYCODE_LAST_CHANNEL
KeyCodes.KEYCODE_TV_DATA_SERVICE
KeyCodes.KEYCODE_VOICE_ASSIST
KeyCodes.KEYCODE_TV_RADIO_SERVICE
KeyCodes.KEYCODE_TV_TELETEXT
KeyCodes.KEYCODE_TV_NUMBER_ENTRY
KeyCodes.KEYCODE_TV_TERRESTRIAL_ANALOG
KeyCodes.KEYCODE_TV_TERRESTRIAL_DIGITAL
KeyCodes.KEYCODE_TV_SATELLITE
KeyCodes.KEYCODE_TV_SATELLITE_BS
KeyCodes.KEYCODE_TV_SATELLITE_CS
KeyCodes.KEYCODE_TV_SATELLITE_SERVICE
KeyCodes.KEYCODE_TV_NETWORK
KeyCodes.KEYCODE_TV_ANTENNA_CABLE
KeyCodes.KEYCODE_TV_INPUT_HDMI_1
KeyCodes.KEYCODE_TV_INPUT_HDMI_2
KeyCodes.KEYCODE_TV_INPUT_HDMI_3
KeyCodes.KEYCODE_TV_INPUT_HDMI_4
KeyCodes.KEYCODE_TV_INPUT_COMPOSITE_1
KeyCodes.KEYCODE_TV_INPUT_COMPOSITE_2
KeyCodes.KEYCODE_TV_INPUT_COMPONENT_1
KeyCodes.KEYCODE_TV_INPUT_COMPONENT_2
KeyCodes.KEYCODE_TV_INPUT_VGA_1
KeyCodes.KEYCODE_TV_AUDIO_DESCRIPTION
KeyCodes.KEYCODE_TV_AUDIO_DESCRIPTION_MIX_UP
KeyCodes.KEYCODE_TV_AUDIO_DESCRIPTION_MIX_DOWN
KeyCodes.KEYCODE_TV_ZOOM_MODE
KeyCodes.KEYCODE_TV_CONTENTS_MENU
KeyCodes.KEYCODE_TV_MEDIA_CONTEXT_MENU
KeyCodes.KEYCODE_TV_TIMER_PROGRAMMING
KeyCodes.KEYCODE_HELP
KeyCodes.KEYCODE_NAVIGATE_PREVIOUS
KeyCodes.KEYCODE_NAVIGATE_NEXT
KeyCodes.KEYCODE_NAVIGATE_IN
KeyCodes.KEYCODE_NAVIGATE_OUT
KeyCodes.KEYCODE_STEM_PRIMARY
KeyCodes.KEYCODE_STEM_1
KeyCodes.KEYCODE_STEM_2
KeyCodes.KEYCODE_STEM_3
KeyCodes.KEYCODE_DPAD_UP_LEFT
KeyCodes.KEYCODE_DPAD_DOWN_LEFT
KeyCodes.KEYCODE_DPAD_UP_RIGHT
KeyCodes.KEYCODE_DPAD_DOWN_RIGHT
KeyCodes.KEYCODE_MEDIA_SKIP_FORWARD
KeyCodes.KEYCODE_MEDIA_SKIP_BACKWARD
KeyCodes.KEYCODE_MEDIA_STEP_FORWARD
KeyCodes.KEYCODE_MEDIA_STEP_BACKWARD
KeyCodes.KEYCODE_SOFT_SLEEP
KeyCodes.KEYCODE_CUT
KeyCodes.KEYCODE_COPY
KeyCodes.KEYCODE_PASTE
KeyCodes.KEYCODE_SYSTEM_NAVIGATION_UP
KeyCodes.KEYCODE_SYSTEM_NAVIGATION_DOWN
KeyCodes.KEYCODE_SYSTEM_NAVIGATION_LEFT
KeyCodes.KEYCODE_SYSTEM_NAVIGATION_RIGHT
KeyCodes.KEYCODE_ALL_APPS
KeyCodes.KEYCODE_REFRESH
KeyCodes.KEYCODE_THUMBS_UP
KeyCodes.KEYCODE_THUMBS_DOWN
KeyCodes.KEYCODE_PROFILE_SWITCH
KeyCodes.KEYCODE_VIDEO_APP_1
KeyCodes.KEYCODE_VIDEO_APP_2
KeyCodes.KEYCODE_VIDEO_APP_3
KeyCodes.KEYCODE_VIDEO_APP_4
KeyCodes.KEYCODE_VIDEO_APP_5
KeyCodes.KEYCODE_VIDEO_APP_6
KeyCodes.KEYCODE_VIDEO_APP_7
KeyCodes.KEYCODE_VIDEO_APP_8
KeyCodes.KEYCODE_FEATURED_APP_1
KeyCodes.KEYCODE_FEATURED_APP_2
KeyCodes.KEYCODE_FEATURED_APP_3
KeyCodes.KEYCODE_FEATURED_APP_4
KeyCodes.KEYCODE_DEMO_APP_1
KeyCodes.KEYCODE_DEMO_APP_2
KeyCodes.KEYCODE_DEMO_APP_3
KeyCodes.KEYCODE_DEMO_APP_4
```
## Documentation

For detailed usage instructions and a complete list of available commands, refer to the comprehensive documentation: https://jekso.github.io/AndroidTV-Remote-Controller/

## Contributing

Contributions are welcome! Feel free to open issues or pull requests to help improve this library.

## License

This library is released under the MIT License: [https://choosealicense.com/licenses/mit/](https://choosealicense.com/licenses/mit/).
