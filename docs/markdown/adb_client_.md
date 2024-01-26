Module AndroidTVController.adb_client
=====================================
  
Classes
-------
  
`ADBClient(verbose: bool = False, show_command: bool = False)`
:   Python way to interact with adb commands.
  
    The ADBClient class is used to interact with the ADB command-line tool in Python, allowing for
    communication with Android devices.
    1-Before running
        You need Android Platform Tools installed and available on your PATH environment variable.
        https://developer.android.com/studio/releases/platform-tools#download
        Ensure you run `adb tcpip 5555` to enable TCP mode.
    2-ADB commands references
        https://developer.android.com/tools/adb
        https://developer.android.com/studio/command-line/adb
        https://technastic.com/set-up-adb-over-wifi-android/
        https://technastic.com/adb-shell-commands-list/
        https://technastic.com/adb-commands-list-adb-cheat-sheet/
  
    Args:
        verbose (bool): The `verbose` parameter is a boolean flag that determines whether or not to
            enable verbose logging. If set to `True`, it will display additional information during the
            execution of the code. If set to `False` (default), it will not display any additional
            information. Defaults to False
        show_command (bool): The `show_command` parameter is a boolean flag that determines whether or
            not to display the executed ADB commands. If `show_command` is set to `True`, the executed ADB
            commands will be shown. If `show_command` is set to `False`, the executed ADB commands will.
            Defaults to False
  
    ### Methods
  
    `clean(self)`
    :   Resets and clean
  
    `connect(self, ip: str)`
    :   The function connects to an IP address and raises an error if the connection fails.
  
        Args:
            ip (str): The `ip` parameter in the `connect` method is a string that represents the IP
                address of the device you want to connect to.
  
        Raises:
            RuntimeError
  
    `disconnect(self) ‑> str`
    :   Disconnect device.
  
        Returns:
            String of the disconnect process result.
  
    `execute_shell_command(self, command: str) ‑> str`
    :   The function executes an adb shell command by calling `adb shell` command.
  
        Args:
            command (str): The `command` parameter is a string that represents the shell command that you
                want to execute.
  
        Returns:
            String of the output results of executing the shell command.
  
    `get_device_info(self) ‑> dict`
    :   The function `get_device_info` retrieves device information.
  
        Returns:
            Dictionary containing device information.
  
    `get_devices(self, include_descriptions: bool = True) ‑> list`
    :   The function `get_devices` retrieves a list of connected devices, including their IP address,
        serial number, state, and optional descriptions.
  
        Args:
            include_descriptions (bool): The `include_descriptions` parameter is a boolean flag that
                determines whether or not to include descriptions for the connected devices. If set to `True`,
                the descriptions will be included in the returned list of devices. If set to `False`, the
                descriptions will be excluded. Defaults to True
  
        Returns:
            The method `get_devices` returns a list of dictionaries, where each dictionary represents a
            connected device. Each dictionary contains the following keys: 'ip', 'serial_number', 'state',
            and 'description'.
  
    `get_devpath(self) ‑> str`
    :   The function `get_devpath` retrieves the device path of a connected Android device'.
  
        Returns:
            String represents the device path, for example usb:1-4.3 for usb connected device.
  
    `get_ip_address(self, interface: str = 'wlan0') ‑> Any`
    :   The function `get_ip_address` returns the device IP address of a specified network interface.
  
        Args:
            interface (str): The `interface` parameter is a string that specifies the network interface to
                retrieve the IP address from. In this case, the default value is set to "wlan0", which is a
                common interface name for wireless LAN connections on Linux-based systems. Defaults to wlan0
  
        Returns:
            The IP address of the selected device.
  
    `get_package_activities(self, package: str) ‑> list`
    :   The function `get_package_activities` retrieves the activities associated with a given package
        in order to start the app.
  
        Args:
            package (str): The "package" parameter is a string that represents the name of the package for
                which you want to retrieve the activities.
  
        Returns:
            List of package activities.
  
    `get_serialno(self) ‑> str`
    :   The function `get_serialno` returns the serial number of a selected device.
  
        Returns:
            The method is returning the serial number of the selected device.
  
    `get_state(self) ‑> str`
    :   The function `get_state` returns the state of connected device.
  
        Returns:
            String represents device state.
  
    `install(self, apk_file: str, replace: bool = True) ‑> str`
    :   The function installs an APK file on a device, with an option to replace/update an existing
        installation.
  
        Args:
            apk_file (str): The `apk_file` parameter is a string that represents the file path of the APK
                file that you want to install.
            replace (bool): The `replace` parameter is a boolean value that determines whether to replace
                an existing installation of the APK file. If `replace` is set to `True`, the existing
                installation will be replaced. If `replace` is set to `False`, the existing installation will
                not be replaced and an error will. Defaults to True
  
        Returns:
            String of the app installation process result.
  
    `is_connected(self, ip: str) ‑> bool`
    :   The function checks if a device with a given IP address is connected to adb server.
  
        Args:
            ip (str): The `ip` parameter is a string that represents an IP address.
  
        Returns:
            Boolean value. It returns True if there is a device in the list of devices with the
            specified IP address, and False otherwise.
  
    `is_installed(self, package_name: str) ‑> bool`
    :   The function checks if the specified package is installed or not.
  
        Args:
            package_name (str): The name of the package, for example 'com.google.chrome'
  
        Returns:
            Boolean indicates if app is installed or not.
  
    `kill_all(self)`
    :   Kill all background processes.
  
    `kill_server(self)`
    :   The function `kill_server` stops the ADB server and terminates any running server process.
  
    `list_packages(self, package_type: str = 'all') ‑> list`
    :   The function "list_packages" lists device android packages, you can also filter package type.
  
        Args:
            package_type (str): The `package_type` parameter is a string that specifies the type of
                packages to list. It has a default value of `all` that gets all packages on the device,
                but it can also take the following values: [all | enabled | disabled | system | third-party].
                Defaults to all
  
        Returns:
            List of packages.
  
    `list_services(self) ‑> list`
    :   The `list_services` function retrieves a list of services along with their IDs, names, and
        associated packages.
  
        Returns:
            List of dictionaries, where each dictionary represents a service. Each dictionary contains
            the following keys: 'id' (integer), 'name' (string), and 'package' (string).
  
    `pull(self, remote: str, local: str, preserve_meta: bool = False) ‑> str`
    :   The function `pull` copies remote files and directories to a device, with an option to preserve
        file metadata like time stamp and mode.
  
        Args:
            remote (str): The `remote` parameter is a string that represents the path of the remote file
                or directory that you want to copy to the device.
            local (str): The "local" parameter is a string that represents the local directory or file
                path where the remote files and directories will be copied to.
            preserve_meta (bool): The `preserve_meta` parameter is a boolean flag that determines whether
                to preserve the file time stamp and mode during the file transfer process. If `preserve_meta` is
                set to `True`, the `-k` option will be added to the command, indicating that the file time stamp
                and mode should be. Defaults to False
  
        Returns:
            String of the file download process result.
  
    `push(self, local: str, remote: str = '/data/local/tmp/') ‑> str`
    :   Copy files and directories from the local device (computer) to
        a remote location on the device.
  
        Args:
            local (str): The `local` parameter is a string that represents the path of the file or
                directory on the local device (computer) that you want to copy to the remote location on the
                device.
            remote (str): The `remote` parameter is a string that specifies the destination location on
                the device where the files or directories from the local device will be copied to. By default,
                the destination location is set to `/data/local/tmp/`, but you can provide a different path if
                needed. Defaults to /data/local/tmp/
  
        Returns:
            String of the file upload process result.
  
    `reboot(self, mode: str | None = None) ‑> str`
    :   The function `reboot` reboots the device with the specified mode, or with no mode if none is
        provided.
  
        Args:
            mode (str|None): The `mode` parameter is a string that specifies the type of reboot to
                perform. It can have one of the following values: [bootloader | recovery | sideload | sideload-auto-reboot]
  
        Returns:
            The method is returning the result of executing the reboot command on the device.
  
    `select_device(self, device_serial: str)`
    :   The function selects a device based on its serial number.
  
        Args:
            device_serial (str): The `device_serial` parameter is a string that represents the serial
                number of a device.
  
    `send_keyevent_input(self, keycode: AndroidTVController.key_codes.KeyCodes, long_press: bool = False) ‑> str`
    :   The function executes an adb shell command to send key event input that simulates pressing button keys.
  
        Args:
            keycode (KeyCode): the keycode to send, table of key codes: https://www.temblast.com/ref/akeyscode.htm
            long_press (bool): specify if simulate a long press for the key or not. Defaults to False.
  
        Returns:
            String of the output results of sending input.
  
    `send_text_input(self, text: str, encode_spaces: bool = True)`
    :   The function executes an adb shell command to send text input.
  
        Args:
            text (str): the text string to send.
            encode_spaces (bool): specify if spaces should be replaced by `%s` or not. Defaults to True.
  
        Returns:
            String of the output results of sending input.
  
    `start_app(self, package: str, activity: str, wait: bool = True, stop: bool = True) ‑> str`
    :   The function starts an Android app with the specified package and activity, optionally waiting
        for the launch to complete and stopping the app before starting the activity.
  
        Args:
            package (str): The package parameter is a string that represents the package name of the
                Android application you want to start. This is typically the unique identifier for the app and
                is specified in the AndroidManifest.xml file of the app.
            activity (str): The "activity" parameter refers to the specific activity or screen within the
                Android app that you want to start. An activity represents a single screen with a user
                interface, and it is the basic building block of an Android app. Each activity has a unique name
                that is specified in the AndroidManifest.xml file
            wait (bool): The "wait" parameter is a boolean value that determines whether the command
                should wait for the launch to complete before returning. If set to True, the command will wait
                for the launch to complete. If set to False, the command will not wait and will return
                immediately after starting the activity. Defaults to True
            stop (bool): The "stop" parameter is a boolean value that determines whether to force stop the
                target app before starting the activity. If it is set to True, the target app will be stopped
                before starting the activity. If it is set to False, the target app will not be stopped.
                Defaults to True
  
        Returns:
            String of the app launch process result.
  
    `start_server(self)`
    :   The function starts an ADB server and waits for it to start up.
  
    `stop_app(self, package: str) ‑> str`
    :   The function stops an Android app with the specified package.
  
        Args:
            package (str): The package parameter is a string that represents the package name of the app
                you want to stop.
  
        Returns:
            String of the app stopping process result.
  
    `stop_service(self, service: str) ‑> str`
    :   The function executes an adb shell command to stop a running service.
  
        Args:
            service (str): The `service` parameter is a string that represents service name that you
                want to stop.
  
        Returns:
            String of the output results of service stopping processing.
  
    `uninstall(self, package: str, keep_data: bool = False) ‑> str`
    :   The `uninstall` function removes an app package from a device, with an option to keep the data
        and cache directories.
  
        Args:
            package (str): The package parameter is a string that represents the app package name that you
                want to uninstall from the device.
            keep_data (bool): A boolean parameter that determines whether to keep the data and cache
                directories of the app package when uninstalling. If set to True, the directories will be kept.
                If set to False (default), the directories will be removed along with the app package. Defaults
                to False
  
        Returns:
            String of the app removal process result.
  