# AndroidTV-Remote-Controller

**Effortlessly control your Android TV using Python and ADB!**

This python library empowers you to seamlessly interact with your Android TV device programmatically, simulating key presses, launching apps, and executing various commands through ADB (Android Debug Bridge).
This means you can use it to control your Android TV or even any android devices with very simple python methods, very useful for creating custom apps for smart homes.

This is video demo for using the API to control my Android TV
[https://www.youtube.com/watch?v=TchUzv5wb5E](https://www.youtube.com/watch?v=TchUzv5wb5E&t=50)

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/TchUzv5wb5E/0.jpg)](https://www.youtube.com/watch?v=TchUzv5wb5E)

## Features

- **Comprehensive command set:**
  - Works with any Android TV device.
  - Easy and clean API to use a lot of adb commands without going deep into details and different options.
  - Connect multiple Android TVs using Wireless TCP connections.
  - List rich devices information.
  - Upload and download files (eg. APK files, Images, Videos, etc).
  - Install/Uninstall android apps.
  - List all packages and easily filter them as system, third-party, enabled, disabled apps.
  - Get package activities to easily use it for auto starting apps.
  - Interact with device shell and invoke any shell commands.
  - Check if TV is on of off, Power ON/OFF, Sleep, Soft sleep & Wake up the TV.
  - Easily navigate home screen and menus using D-Pad navigation
  - Control volume (up, down, mute)
  - Control TV channel buttons (up, down) or using channel number
  - Send text input for any input fields (e.g., Search).
  - Open famous apps (e.g., YouTube, Netflix, Amazon Prime, Watch IT)
  - Start any other application by using its package name.
  - Simulate all android key codes not just for TV but for any android device: [Check Supported Key Codes List](https://www.temblast.com/ref/akeyscode.htm)
- **Clear and concise API:**
  - Intuitive methods for common actions
  - Well-organized code structure
  - Open for extensions
- **ADB integration:**
  - Handles ADB communication smoothly
  - No need for manual ADB interaction
- **Cross-platform compatibility:**
  - Works seamlessly on Windows, macOS, and Linux
  - Tested on Toshiba Android TV.

## Requirements

- Python 3.11
- Android Platform Tools installed and available in your PATH environment variable. you can do this from [Here](https://developer.android.com/tools/releases/platform-tools), then you can check by open a terminal and write `adb --version` if this gives an error make sure you follow the instructions and the platform-tools folder is in your PATH environment variable.
- Make sure your Computer and the Android TV is on the same WiFi network.
- Get TV IP address and pair your Android TV with adb server. [Instructions](https://www.makeuseof.com/how-to-use-adb-on-android-tv/)
- You are ready to go.

## Installation

1. Download the repository by click download from github or by cloning it using this command `git clone https://github.com/Jekso/AndroidTV-Remote-Controller.git`, I will upload it to PyPi soon to easily download it using pip but for now use it locally as mentioned.
2. Start hacking your TV xD

## Usage

you can use `AndroidTVController` class to invoke TV commands.

```python
from android_tv_rc import AndroidTVController


# Replace with your device's IP
# To get your Android TV ip address follow this link: https://www.androidtvtricks.com/ip-address-on-android-tv-box/
# When running this code for first time and your TV is not paired, check your TV and click Allow
# Then run the code again
ip = '192.168.1.28'
controller = AndroidTVController(ip)
controller.connect()
controller.is_connected()


# --------------[ Navigation Commands ]--------------
controller.press_home()
controller.press_tv()
controller.press_enter()
controller.press_back()
controller.press_dpad_up()
controller.press_dpad_down()
controller.press_dpad_left()
controller.press_dpad_right()


# --------------[ Volume Commands ]--------------
controller.press_volume_up()
controller.press_volume_down()
controller.press_volume_mute()


# --------------[ Power Commands ]--------------
controller.is_powered_on()
controller.press_power()
controller.press_sleep()
controller.press_soft_sleep()
controller.press_wakeup()


# --------------[ TV Satellite channels Commands ]--------------
controller.press_channel_up()
controller.press_channel_down()
controller.press_channel_number('213')


# --------------[ Apps Commands ]--------------)
controller.open_youtube()
controller.open_netflix()
controller.open_amazon_prime()
controller.open_watch_it()
controller.open_shahid()
controller.open_app('net.mbc.shahidTV', '.MainActivity')

```

Also you can use ADB commands API from `ADBClient` class.

```python
from android_tv_rc import ADBClient, KeyCodes


adb_client = controller.get_adb_client()
# or you can use it as standalone without using TV Controller
adb_client = ADBClient()  


# --------------[ Connectivity Commands ]--------------
adb_client.connect('192.168.1.103')
adb_client.is_connected('192.168.1.103')
adb_client.disconnect()


# --------------[ Info Commands ]--------------
adb_client.get_devices()
adb_client.select_device('192.168.1.103:5555')
adb_client.get_selected_device()
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
adb_client.start_app('net.mbc.shahidTV', '.MainActivity')
adb_client.stop_app('com.android.chrome')


# --------------[ Device related Commands ]--------------
adb_client.reboot()
adb_client.is_powered_on()
adb_client.execute_shell_command('rm -f /sdcard/test.apk')


# --------------[ Inputs Commands ]--------------
adb_client.send_keyevent_input(KeyCodes.KEYCODE_HOME)
adb_client.send_text_input('Welcome to Metaverse')

```

For all key codes you can use any of these enum values

```python

class KeyCodes(Enum):
    KEYCODE_UNKNOWN = 0
    KEYCODE_SOFT_LEFT = 1
    KEYCODE_SOFT_RIGHT = 2
    KEYCODE_HOME = 3
    KEYCODE_BACK = 4
    KEYCODE_CALL = 5
    KEYCODE_ENDCALL = 6
    KEYCODE_0 = 7
    KEYCODE_1 = 8
    KEYCODE_2 = 9
    KEYCODE_3 = 10
    KEYCODE_4 = 11
    KEYCODE_5 = 12
    KEYCODE_6 = 13
    KEYCODE_7 = 14
    KEYCODE_8 = 15
    KEYCODE_9 = 16
    KEYCODE_STAR = 17
    KEYCODE_POUND = 18
    KEYCODE_DPAD_UP = 19
    KEYCODE_DPAD_DOWN = 20
    KEYCODE_DPAD_LEFT = 21
    KEYCODE_DPAD_RIGHT = 22
    KEYCODE_DPAD_CENTER = 23
    KEYCODE_VOLUME_UP = 24
    KEYCODE_VOLUME_DOWN = 25
    KEYCODE_POWER = 26
    KEYCODE_CAMERA = 27
    KEYCODE_CLEAR = 28
    KEYCODE_A = 29
    KEYCODE_B = 30
    KEYCODE_C = 31
    KEYCODE_D = 32
    KEYCODE_E = 33
    KEYCODE_F = 34
    KEYCODE_G = 35
    KEYCODE_H = 36
    KEYCODE_I = 37
    KEYCODE_J = 38
    KEYCODE_K = 39
    KEYCODE_L = 40
    KEYCODE_M = 41
    KEYCODE_N = 42
    KEYCODE_O = 43
    KEYCODE_P = 44
    KEYCODE_Q = 45
    KEYCODE_R = 46
    KEYCODE_S = 47
    KEYCODE_T = 48
    KEYCODE_U = 49
    KEYCODE_V = 50
    KEYCODE_W = 51
    KEYCODE_X = 52
    KEYCODE_Y = 53
    KEYCODE_Z = 54
    KEYCODE_COMMA = 55
    KEYCODE_PERIOD = 56
    KEYCODE_ALT_LEFT = 57
    KEYCODE_ALT_RIGHT = 58
    KEYCODE_SHIFT_LEFT = 59
    KEYCODE_SHIFT_RIGHT = 60
    KEYCODE_TAB = 61
    KEYCODE_SPACE = 62
    KEYCODE_SYM = 63
    KEYCODE_EXPLORER = 64
    KEYCODE_ENVELOPE = 65
    KEYCODE_ENTER = 66
    KEYCODE_DEL = 67
    KEYCODE_GRAVE = 68
    KEYCODE_MINUS = 69
    KEYCODE_EQUALS = 70
    KEYCODE_LEFT_BRACKET = 71
    KEYCODE_RIGHT_BRACKET = 72
    KEYCODE_BACKSLASH = 73
    KEYCODE_SEMICOLON = 74
    KEYCODE_APOSTROPHE = 75
    KEYCODE_SLASH = 76
    KEYCODE_AT = 77
    KEYCODE_NUM = 78
    KEYCODE_HEADSETHOOK = 79
    KEYCODE_FOCUS = 80
    KEYCODE_PLUS = 81
    KEYCODE_MENU = 82
    KEYCODE_NOTIFICATION = 83
    KEYCODE_SEARCH = 84
    KEYCODE_MEDIA_PLAY_PAUSE = 85
    KEYCODE_MEDIA_STOP = 86
    KEYCODE_MEDIA_NEXT = 87
    KEYCODE_MEDIA_PREVIOUS = 88
    KEYCODE_MEDIA_REWIND = 89
    KEYCODE_MEDIA_FAST_FORWARD = 90
    KEYCODE_MUTE = 91
    KEYCODE_PAGE_UP = 92
    KEYCODE_PAGE_DOWN = 93
    KEYCODE_PICTSYMBOLS = 94
    KEYCODE_SWITCH_CHARSET = 95
    KEYCODE_BUTTON_A = 96
    KEYCODE_BUTTON_B = 97
    KEYCODE_BUTTON_C = 98
    KEYCODE_BUTTON_X = 99
    KEYCODE_BUTTON_Y = 100
    KEYCODE_BUTTON_Z = 101
    KEYCODE_BUTTON_L1 = 102
    KEYCODE_BUTTON_R1 = 103
    KEYCODE_BUTTON_L2 = 104
    KEYCODE_BUTTON_R2 = 105
    KEYCODE_BUTTON_THUMBL = 106
    KEYCODE_BUTTON_THUMBR = 107
    KEYCODE_BUTTON_START = 108
    KEYCODE_BUTTON_SELECT = 109
    KEYCODE_BUTTON_MODE = 110
    KEYCODE_ESCAPE = 111
    KEYCODE_FORWARD_DEL = 112
    KEYCODE_CTRL_LEFT = 113
    KEYCODE_CTRL_RIGHT = 114
    KEYCODE_CAPS_LOCK = 115
    KEYCODE_SCROLL_LOCK = 116
    KEYCODE_META_LEFT = 117
    KEYCODE_META_RIGHT = 118
    KEYCODE_FUNCTION = 119
    KEYCODE_SYSRQ = 120
    KEYCODE_BREAK = 121
    KEYCODE_MOVE_HOME = 122
    KEYCODE_MOVE_END = 123
    KEYCODE_INSERT = 124
    KEYCODE_FORWARD = 125
    KEYCODE_MEDIA_PLAY = 126
    KEYCODE_MEDIA_PAUSE = 127
    KEYCODE_MEDIA_CLOSE = 128
    KEYCODE_MEDIA_EJECT = 129
    KEYCODE_MEDIA_RECORD = 130
    KEYCODE_F1 = 131
    KEYCODE_F2 = 132
    KEYCODE_F3 = 133
    KEYCODE_F4 = 134
    KEYCODE_F5 = 135
    KEYCODE_F6 = 136
    KEYCODE_F7 = 137
    KEYCODE_F8 = 138
    KEYCODE_F9 = 139
    KEYCODE_F10 = 140
    KEYCODE_F11 = 141
    KEYCODE_F12 = 142
    KEYCODE_NUM_LOCK = 143
    KEYCODE_NUMPAD_0 = 144
    KEYCODE_NUMPAD_1 = 145
    KEYCODE_NUMPAD_2 = 146
    KEYCODE_NUMPAD_3 = 147
    KEYCODE_NUMPAD_4 = 148
    KEYCODE_NUMPAD_5 = 149
    KEYCODE_NUMPAD_6 = 150
    KEYCODE_NUMPAD_7 = 151
    KEYCODE_NUMPAD_8 = 152
    KEYCODE_NUMPAD_9 = 153
    KEYCODE_NUMPAD_DIVIDE = 154
    KEYCODE_NUMPAD_MULTIPLY = 155
    KEYCODE_NUMPAD_SUBTRACT = 156
    KEYCODE_NUMPAD_ADD = 157
    KEYCODE_NUMPAD_DOT = 158
    KEYCODE_NUMPAD_COMMA = 159
    KEYCODE_NUMPAD_ENTER = 160
    KEYCODE_NUMPAD_EQUALS = 161
    KEYCODE_NUMPAD_LEFT_PAREN = 162
    KEYCODE_NUMPAD_RIGHT_PAREN = 163
    KEYCODE_VOLUME_MUTE = 164
    KEYCODE_INFO = 165
    KEYCODE_CHANNEL_UP = 166
    KEYCODE_CHANNEL_DOWN = 167
    KEYCODE_ZOOM_IN = 168
    KEYCODE_ZOOM_OUT = 169
    KEYCODE_TV = 170
    KEYCODE_WINDOW = 171
    KEYCODE_GUIDE = 172
    KEYCODE_DVR = 173
    KEYCODE_BOOKMARK = 174
    KEYCODE_CAPTIONS = 175
    KEYCODE_SETTINGS = 176
    KEYCODE_TV_POWER = 177
    KEYCODE_TV_INPUT = 178
    KEYCODE_STB_POWER = 179
    KEYCODE_STB_INPUT = 180
    KEYCODE_AVR_POWER = 181
    KEYCODE_AVR_INPUT = 182
    KEYCODE_PROG_RED = 183
    KEYCODE_PROG_GREEN = 184
    KEYCODE_PROG_YELLOW = 185
    KEYCODE_PROG_BLUE = 186
    KEYCODE_APP_SWITCH = 187
    KEYCODE_BUTTON_1 = 188
    KEYCODE_BUTTON_2 = 189
    KEYCODE_BUTTON_3 = 190
    KEYCODE_BUTTON_4 = 191
    KEYCODE_BUTTON_5 = 192
    KEYCODE_BUTTON_6 = 193
    KEYCODE_BUTTON_7 = 194
    KEYCODE_BUTTON_8 = 195
    KEYCODE_BUTTON_9 = 196
    KEYCODE_BUTTON_10 = 197
    KEYCODE_BUTTON_11 = 198
    KEYCODE_BUTTON_12 = 199
    KEYCODE_BUTTON_13 = 200
    KEYCODE_BUTTON_14 = 201
    KEYCODE_BUTTON_15 = 202
    KEYCODE_BUTTON_16 = 203
    KEYCODE_LANGUAGE_SWITCH = 204
    KEYCODE_MANNER_MODE = 205
    KEYCODE_3D_MODE = 206
    KEYCODE_CONTACTS = 207
    KEYCODE_CALENDAR = 208
    KEYCODE_MUSIC = 209
    KEYCODE_CALCULATOR = 210
    KEYCODE_ZENKAKU_HANKAKU = 211
    KEYCODE_EISU = 212
    KEYCODE_MUHENKAN = 213
    KEYCODE_HENKAN = 214
    KEYCODE_KATAKANA_HIRAGANA = 215
    KEYCODE_YEN = 216
    KEYCODE_RO = 217
    KEYCODE_KANA = 218
    KEYCODE_ASSIST = 219
    KEYCODE_BRIGHTNESS_DOWN = 220
    KEYCODE_BRIGHTNESS_UP = 221
    KEYCODE_MEDIA_AUDIO_TRACK = 222
    KEYCODE_SLEEP = 223
    KEYCODE_WAKEUP = 224
    KEYCODE_PAIRING = 225
    KEYCODE_MEDIA_TOP_MENU = 226
    KEYCODE_11 = 227
    KEYCODE_12 = 228
    KEYCODE_LAST_CHANNEL = 229
    KEYCODE_TV_DATA_SERVICE = 230
    KEYCODE_VOICE_ASSIST = 231
    KEYCODE_TV_RADIO_SERVICE = 232
    KEYCODE_TV_TELETEXT = 233
    KEYCODE_TV_NUMBER_ENTRY = 234
    KEYCODE_TV_TERRESTRIAL_ANALOG = 235
    KEYCODE_TV_TERRESTRIAL_DIGITAL = 236
    KEYCODE_TV_SATELLITE = 237
    KEYCODE_TV_SATELLITE_BS = 238
    KEYCODE_TV_SATELLITE_CS = 239
    KEYCODE_TV_SATELLITE_SERVICE = 240
    KEYCODE_TV_NETWORK = 241
    KEYCODE_TV_ANTENNA_CABLE = 242
    KEYCODE_TV_INPUT_HDMI_1 = 243
    KEYCODE_TV_INPUT_HDMI_2 = 244
    KEYCODE_TV_INPUT_HDMI_3 = 245
    KEYCODE_TV_INPUT_HDMI_4 = 246
    KEYCODE_TV_INPUT_COMPOSITE_1 = 247
    KEYCODE_TV_INPUT_COMPOSITE_2 = 248
    KEYCODE_TV_INPUT_COMPONENT_1 = 249
    KEYCODE_TV_INPUT_COMPONENT_2 = 250
    KEYCODE_TV_INPUT_VGA_1 = 251
    KEYCODE_TV_AUDIO_DESCRIPTION = 252
    KEYCODE_TV_AUDIO_DESCRIPTION_MIX_UP = 253
    KEYCODE_TV_AUDIO_DESCRIPTION_MIX_DOWN = 254
    KEYCODE_TV_ZOOM_MODE = 255
    KEYCODE_TV_CONTENTS_MENU = 256
    KEYCODE_TV_MEDIA_CONTEXT_MENU = 257
    KEYCODE_TV_TIMER_PROGRAMMING = 258
    KEYCODE_HELP = 259
    KEYCODE_NAVIGATE_PREVIOUS = 260
    KEYCODE_NAVIGATE_NEXT = 261
    KEYCODE_NAVIGATE_IN = 262
    KEYCODE_NAVIGATE_OUT = 263
    KEYCODE_STEM_PRIMARY = 264
    KEYCODE_STEM_1 = 265
    KEYCODE_STEM_2 = 266
    KEYCODE_STEM_3 = 267
    KEYCODE_DPAD_UP_LEFT = 268
    KEYCODE_DPAD_DOWN_LEFT = 269
    KEYCODE_DPAD_UP_RIGHT = 270
    KEYCODE_DPAD_DOWN_RIGHT = 271
    KEYCODE_MEDIA_SKIP_FORWARD = 272
    KEYCODE_MEDIA_SKIP_BACKWARD = 273
    KEYCODE_MEDIA_STEP_FORWARD = 274
    KEYCODE_MEDIA_STEP_BACKWARD = 275
    KEYCODE_SOFT_SLEEP = 276
    KEYCODE_CUT = 277
    KEYCODE_COPY = 278
    KEYCODE_PASTE = 279
    KEYCODE_SYSTEM_NAVIGATION_UP = 280
    KEYCODE_SYSTEM_NAVIGATION_DOWN = 281
    KEYCODE_SYSTEM_NAVIGATION_LEFT = 282
    KEYCODE_SYSTEM_NAVIGATION_RIGHT = 283
    KEYCODE_ALL_APPS = 284
    KEYCODE_REFRESH = 285
    KEYCODE_THUMBS_UP = 286
    KEYCODE_THUMBS_DOWN = 287
    KEYCODE_PROFILE_SWITCH = 288
    KEYCODE_VIDEO_APP_1 = 289
    KEYCODE_VIDEO_APP_2 = 290
    KEYCODE_VIDEO_APP_3 = 291
    KEYCODE_VIDEO_APP_4 = 292
    KEYCODE_VIDEO_APP_5 = 293
    KEYCODE_VIDEO_APP_6 = 294
    KEYCODE_VIDEO_APP_7 = 295
    KEYCODE_VIDEO_APP_8 = 296
    KEYCODE_FEATURED_APP_1 = 297
    KEYCODE_FEATURED_APP_2 = 298
    KEYCODE_FEATURED_APP_3 = 299
    KEYCODE_FEATURED_APP_4 = 300
    KEYCODE_DEMO_APP_1 = 301
    KEYCODE_DEMO_APP_2 = 302
    KEYCODE_DEMO_APP_3 = 303
    KEYCODE_DEMO_APP_4 = 304

```

## Documentation

For detailed usage instructions and a complete list of available commands, refer to the comprehensive documentation: <https://jekso.github.io/AndroidTV-Remote-Controller/>

## Contributing

Contributions are welcome! Feel free to open issues or pull requests to help improve this library.

## License

This library is released under the MIT License: [https://choosealicense.com/licenses/mit/](https://choosealicense.com/licenses/mit/).
