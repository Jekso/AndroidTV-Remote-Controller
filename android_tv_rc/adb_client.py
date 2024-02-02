import re
import sys
import shlex
import time
import subprocess
from typing import Any
from .logger import Logger
from .key_codes import KeyCodes



class ADBClient:
 


    def __init__(self, verbose: bool=False, show_command: bool=False):
        """Pythonic way to execute adb commands on Android TV devices.
        
        The ADBClient class is used to interact with the ADB command-line tool in Python, allowing for
        communication with Android TV devices in TCP Wireless mode.
        1-Before running you need Android Platform Tools installed and available on your PATH environment variable.
            `https://developer.android.com/studio/releases/platform-tools#download`
        2-Make sure your computer running the python library and the android device is on the same network.
        3-Enable the USB/Wireless/ADB debugging feature on your android TV device depending on your version & get your TV IP address.
            you can follow this link `https://www.makeuseof.com/how-to-use-adb-on-android-tv/`
        
        Some important resources:
            https://developer.android.com/tools/adb
            https://developer.android.com/studio/command-line/adb
            https://technastic.com/set-up-adb-over-wifi-android/
            https://technastic.com/adb-shell-commands-list/
            https://technastic.com/adb-commands-list-adb-cheat-sheet/
            https://www.makeuseof.com/how-to-use-adb-on-android-tv/
        
        Args:
            verbose (bool): The `verbose` parameter is a boolean flag that determines whether or not to
                enable verbose logging. If set to `True`, it will display additional information during the
                execution of the code. If set to `False` (default), it will not display any additional
                information. Defaults to False.
            show_command (bool): The `show_command` parameter is a boolean flag that determines whether or
                not to display the executed ADB commands. If `show_command` is set to `True`, the executed ADB
                commands will be shown. If `show_command` is set to `False`, the executed ADB commands will.
                Defaults to False.
        """
        # logs verbose 
        self.__verbose = verbose
        self.__show_command = show_command
        if self.__verbose:
            Logger.welcome('use ADB command-line tool with python.')
        
        # adb params
        self.__devices = []
        self.__selected_device = None
        self.__server_process = None
        
        # start adb server to start sending commands to devices
        self.start_server()



    
    def __execute_command(self, command_str: str, blocking: bool=True, include_selected_serial: bool=True) -> Any:
        """
        The function executes a shell command using the adb tool, with the option to run it in blocking
        or non-blocking mode.

        Args:
            command_str (str): The `command_str` parameter is a string that represents the shell command
                to be executed. It can be any valid adb command or a combination of adb commands.
            blocking (bool): The `blocking` parameter is a boolean flag that determines whether the
                command should be executed synchronously (blocking) or asynchronously (non-blocking). Defaults
                to True.
            include_selected_serial (bool): Whether to include selected device serial in the command, Defaults 
                to True.

        Returns:
            The method `__execute_command` returns the output of the shell command that is executed. If
            the `blocking` parameter is set to `True`, it returns the stdout of the command as a string. If
            `blocking` is set to `False`, it returns a `subprocess.Popen` object.
            
        Raises:
            OSError: This occurs, for example, when trying to execute a non-existent file.
            ValueError: will be raised if process is called with invalid arguments.
            CalledProcessError: if the called process returns a non-zero return code.
            TimeoutExpired: if the timeout expires before the process exits.
        """
        
        # adb base command
        command = 'adb '
        
        # specify a device serial
        if self.__selected_device and include_selected_serial:
            command += f'-s {self.__selected_device} '
            
        # append the command to base adb
        command += command_str
        
        # show executed command if needed
        if self.__verbose and self.__show_command:
            Logger.info(f'[bold]Command:[/bold] [blue]{command}[/blue]')
            
        # convert command string to list of splitted tokens
        command_parts = shlex.split(command, posix="win" not in sys.platform)
        
        if blocking:
            # run the command and waits for full execution
            proc = subprocess.run(command_parts, check=True, capture_output=True, text=True)
            return proc.stdout.strip()
        else:
            # run the process in background and continue the python script
            return subprocess.Popen(command_parts, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    
    
    
    # ------------------------------[ Server Commands ]------------------------------



    def start_server(self) -> bool:
        """
        The function `start_server` starts an ADB server and waits for it to start up.
        
        Returns:
            Boolean indicating whether the server is running or not.
        """
        Logger.info('Starting ADB server..')
        
        # start the adb server as background process
        self.__server_process = self.__execute_command('start-server', blocking=False, include_selected_serial=False)
        
        # give time to start up
        time.sleep(5)
        
        if self.__server_process:
            Logger.success('ADB server is started')
            return True
        else:
            Logger.error(f'Unable to start ADB server')
            return False



    def kill_server(self) -> bool:
        """
        The function `kill_server` stops the ADB server and terminates any running server process.
                
        Returns:
            Boolean indicating whether the server is stopped or not.
        """
        Logger.info('Stopping ADB server..')
        self.__execute_command('kill-server', include_selected_serial=False)
        if self.__server_process:
            self.__server_process.terminate()
            self.__server_process = None
            self.clean()
            Logger.success('ADB server is stopped')
            return True
        else:
            Logger.error(f'No ADB server process running')
            return False
    
    
    
    def clean(self):
        """Resets and clean"""
        Logger.info('Cleaning up')
        self.__devices = []
        self.__selected_device = None
        self.__server_process = None



    # ------------------------------[ Connectivity Commands ]------------------------------



    def connect(self, ip: str) -> bool:
        """
        The function connects to an IP address and raises an error if the connection fails.
        
        Args:
            ip (str): The `ip` parameter in the `connect` method is a string that represents the IP
                address of the device you want to connect.
        
        Returns:
            Boolean: True if the connection succeeded, False if the connection failed.
        """
        Logger.info(f'Connecting to [bold green]{ip}[/bold green] ..')
        result = self.__execute_command(f'connect {ip}', include_selected_serial=False)
        if "connected" in result:
            self.__devices = self.get_devices()
            self.__selected_device = self.__devices[-1]
            Logger.success(f'Device: [bold blue]{self.__selected_device}[/bold blue] is connected successfully')
            return True
        else: # "failed" in result
            Logger.error(f'Connection with [bold blue]{ip}[/bold blue] failed')
            return False
    


    def is_connected(self, ip: str) -> bool:
        """
        The function checks if a device with a given IP address is connected to adb server.
        
        Args:
            ip (str): The `ip` parameter is a string that represents an IP address.
        
        Returns:
            Boolean value. It returns True if there is a device in the list of devices with the
            specified IP address, and False otherwise.
        """
        for device in self.__devices:
            if device.split(':')[0] == ip:
                Logger.success(f'Device: [bold blue]{ip}[/bold blue] is connected')
                return True
        Logger.error(f'Device [bold blue]{ip}[/bold blue] is not connected')
        return False



    def disconnect(self) -> bool:
        """
        Disconnect selected device.
        
        Returns:
            Boolean: True if the device is disconnected.
        """
        Logger.info(f'Disconnecting device..')
        if 'disconnected' in self.__execute_command('disconnect'):
            self.__devices = self.get_devices()
            self.__selected_device = None
            Logger.success(f'Device: [bold blue]{self.__selected_device}[/bold blue] is disconnected')
            return True
        else:
            Logger.error(f'Error while disconnecting device: [bold blue]{self.__selected_device}[/bold blue]')
            return False


 
    # ------------------------------[ Info Commands ]------------------------------
    
    
    
    def get_devices(self, include_descriptions: bool=True) -> list:
        """
        The function `get_devices` retrieves a list of connected devices, including their IP address,
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
        """
        Logger.info(f'Getting connected devices..')
        self.__devices = []
        command = 'devices'
        if include_descriptions:
            command += ' -l'
        result = self.__execute_command(command, include_selected_serial=False)
        devices = result.split("\n")[1:]
        Logger.info(f'There are [bold green]{len(devices)}[/bold green] connected devices')
        for i, device in enumerate(devices):
            data = device.split()
            serial_number = data[0]
            self.__devices.append(serial_number)
            if self.__verbose:
                Logger.print(f'[bold green]Device[/bold green] ({i+1}): [yellow]{serial_number}[/yellow]')
        return self.__devices
    
    
    
    def select_device(self, device_serial: str) -> bool:
        """
        The function selects a device based on its serial number.
        
        Args:
            device_serial (str): The `device_serial` parameter is a string that represents the serial
                number of a device.
        
        Returns:
            Boolean: True if the device is found and selected.
        """
        if device_serial in self.__devices:
            self.__selected_device = device_serial
            Logger.success(f'Selected device: [bold blue]{self.__selected_device}[/bold blue]')
            return True
        else:
            Logger.error(f'Device: [bold blue]{device_serial}[/bold blue] is not found')
            return False
    
    
    
    def get_selected_device(self) -> str|None:
        """
        Get current selected device.
        
        Returns:
            Selected device serial number. `None` if no device found.
        """
        if self.__selected_device:
            Logger.success(f'Selected device: [bold blue]{self.__selected_device}[/bold blue]')
        else:
            Logger.error(f'No device found')
        return self.__selected_device
        
        
        
    def get_device_info(self) -> dict|None:
        """
        The function `get_device_info` retrieves device information.
        
        Returns:
            Dictionary containing device information. `None` if no device found.
        """
        if self.__selected_device is None:
            return
        device_info = {}
        results = self.execute_shell_command('getprop').split('\n')
        for data in results:
            match = re.match(r"\[([^:]+)\]: \[([^:]+)\]", data)
            if match:
                prop = match.group(1)
                value = match.group(2)
                device_info[prop] = value
                if self.__verbose:
                    Logger.print(f'[bold green]{prop}[/bold green]: [yellow]{value}[/yellow]')
        return device_info
       
       
       
    def get_state(self) -> str|None:
        """
        The function `get_state` returns the state of connected device.
        
        Returns:
            String represents device state. `None` if no device found.
        """
        if self.__selected_device is None:
            return
        device_state = self.__execute_command('get-state')
        Logger.info(f'Device: ({self.__selected_device}) state is {device_state}')
        return device_state



    def get_serialno(self) -> str|None:
        """
        The function `get_serialno` returns the serial number of a selected device.
        
        Returns:
            String represents device serial number of the selected device. `None` if no device found.
        """
        if self.__selected_device is None:
            return
        device_serialno = self.__execute_command('get-serialno')
        Logger.info(f'Device Serial number: {device_serialno}')
        return device_serialno



    def get_devpath(self) -> str|None:
        """
        The function `get_devpath` retrieves the device path of a connected Android device'.
        
        Returns:
            String represents the device path, for example usb:1-4.3 for usb connected device. `None` if no device found.
        """
        if self.__selected_device is None:
            return
        device_devpath = self.__execute_command('get-devpath')
        Logger.info(f'Device dev_path: {device_devpath}')
        return device_devpath
    
    
    
    def get_ip_address(self, interface: str='wlan0') -> str|None:
        """
        The function `get_ip_address` returns the device IP address of a specified network interface.
        
        Args:
            interface (str): The `interface` parameter is a string that specifies the network interface to
                retrieve the IP address from. In this case, the default value is set to "wlan0", which is a
                common interface name for wireless LAN connections on Linux-based systems. Defaults to wlan0
        
        Returns:
            The IP address of the selected device. `None` if no device found.
        """
        if self.__selected_device is None:
            return
        device_ip = ''
        if result := self.execute_shell_command(f'ifconfig {interface}'):
            if match_obj := re.search(r"inet addr:(.+)  Bcast", result, re.M | re.I):
                device_ip = match_obj[1]
                Logger.info(f'Device ip: {device_ip}')
        return device_ip
    
    

    # ------------------------------[ File Operations Commands ]------------------------------



    def push(self, local: str, remote: str='/data/local/tmp/') -> bool|None:
        """
        Copy files and directories from the local device (computer) to
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
            Boolean indicating whether the upload operation was successful. `None` if no device found.
        """
        if self.__selected_device is None:
            return
        Logger.info(f'Uploading: [bold green]{local}[/bold green] to [bold green]{remote}[/bold green] ..')
        result = self.__execute_command(f'push {local} {remote}') 
        if '1 file pushed' in result:
            Logger.success(f'File [bold blue]{local}[/bold blue] uploaded to [bold blue]{remote}[/bold blue] successfully')
            return True
        else:
            Logger.error(f'Uploading [bold blue]{local}[/bold blue] to [bold blue]{remote}[/bold blue] failed')
            return False
        



    def pull(self, remote: str, local: str, preserve_meta: bool=False) -> bool|None:
        """
        The function `pull` copies remote files and directories to a device, with an option to preserve
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
            Boolean indicating whether the download operation was successful. `None` if no device found.
        """
        if self.__selected_device is None:
            return
        command = 'pull '
        if preserve_meta:
            command += '-k '
        command += f'{remote} {local}'
        Logger.info(f'Downloading: [bold green]{remote}[/bold green] to [bold green]{local}[/bold green] ..')
        result = self.__execute_command(command)
        if '1 file pulled,' in result:
            Logger.success(f'File [bold blue]{remote}[/bold blue] downloaded to [bold blue]{local}[/bold blue] successfully')
            return True
        else:
            Logger.error(f'Downloading [bold blue]{remote}[/bold blue] to [bold blue]{local}[/bold blue] failed')
            return False


    # ------------------------------[ Apps Operations Commands ]------------------------------
    


    def is_installed(self, package_name: str) -> bool|None:
        """
        The function checks if the specified package is installed or not.
        
        Args:
            package_name (str): The name of the package, for example 'com.google.chrome'
        
        Returns:
            Boolean indicates if app is installed or not. `None` if no device found.
        """
        if self.__selected_device is None:
            return
        command = f'pm list packages'
        app_installed =  package_name in self.execute_shell_command(command)
        if app_installed:
            Logger.success(f'App [bold blue]{package_name}[/bold blue] is installed')
            return True
        else:
            Logger.error(f'App [bold blue]{package_name}[/bold blue] is not installed')
            return False
        
        
        
    def install(self, apk_file: str, replace: bool=True) -> bool|None:
        """
        The function installs an APK file on a device, with an option to replace/update an existing
        installation.
        
        Args:
            apk_file (str): The `apk_file` parameter is a string that represents the file path of the APK
                file that you want to install.
            replace (bool): The `replace` parameter is a boolean value that determines whether to replace
                an existing installation of the APK file. If `replace` is set to `True`, the existing
                installation will be replaced. If `replace` is set to `False`, the existing installation will
                not be replaced and an error will. Defaults to True
        
        Returns:
            Boolean indicates if installation process is successful. `None` if no device found.
        """
        if self.__selected_device is None:
            return
        command = 'install '
        if replace:
            command += '-r '
        command += apk_file
        Logger.info(f'Installing APK file [bold green]{apk_file}[/bold green], it will took up to 2 minutes to complete..')
        result = self.__execute_command(command)
        if 'Success' in result:
            Logger.success(f'APK [bold blue]{apk_file}[/bold blue] is installed successfully')
            return True
        else:
            Logger.error(f'Installation process failed')
            return False



    def uninstall(self, package: str, keep_data: bool=False) -> bool|None:
        """
        The `uninstall` function removes an app package from a device, with an option to keep the data
        and cache directories.
        
        Args:
            package (str): The package parameter is a string that represents the app package name that you
                want to uninstall from the device.
            keep_data (bool): A boolean parameter that determines whether to keep the data and cache
                directories of the app package when uninstalling. If set to True, the directories will be kept.
                If set to False (default), the directories will be removed along with the app package. Defaults
                to False
        
        Returns:
            Boolean indicates if uninstalling process is successful. `None` if no device found.
        """
        if self.__selected_device is None:
            return
        command = 'uninstall '
        if keep_data:
            command += '-k '
        command += package
        message = f'Uninstalling package [bold green]{package}[/bold green]'
        message += 'while keeping the data' if keep_data else ''
        message += ', it will took up to 2 minutes to complete..'
        Logger.info(message)
        result = self.__execute_command(command)
        if 'Success' in result:
            Logger.success(f'Package [bold blue]{package}[/bold blue] is uninstalled successfully')
            return True
        else:
            Logger.error(f'Uninstalling process failed')
            return False
    
    
    
    def start_app(self, package: str, activity: str, wait: bool=True, stop: bool=True) -> bool|None:
        """
        The function starts an Android app with the specified package and activity, optionally waiting
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
            Boolean indicates if app starting process is successful. `None` if no device found.
        """
        if self.__selected_device is None:
            return
        # check if app is installed
        if not self.is_installed(package):
            return False
        self.send_keyevent_input(KeyCodes.KEYCODE_HOME)
        command = 'am start '
        # wait for launch to complete
        if wait:
            command += '-W '
        if stop: # force stop the target app before starting the activity
            command += '-S '
        command += f'{package}/{activity}'
        Logger.info(f'Starting app: [bold green]{package}[/bold green] ..')
        result = self.execute_shell_command(command)
        if 'Error' in result:
            Logger.error(f'Starting app [bold blue]{package}[/bold blue] failed')
            return False
        else:
            Logger.success(f'App: [bold blue]{package}[/bold blue] started successfully')
            return True



    def stop_app(self, package: str) -> bool|None:
        """
        The function stops an Android app with the specified package.
        
        Args:
            package (str): The package parameter is a string that represents the package name of the app
                you want to stop.
        
        Returns:
            Boolean indicates if app stopping process is successful. `None` if no device found.
        """
        if self.__selected_device is None:
            return
        Logger.info(f'Stopping app: [bold green]{package}[/bold green] ..')
        result =  self.execute_shell_command(f'am force-stop {package}')
        if 'Error' in result:
            Logger.error(f'Stopping app [bold blue]{package}[/bold blue] failed')
            return False
        else:
            Logger.success(f'App: [bold blue]{package}[/bold blue] stopped successfully')
            return True



    def list_packages(self, package_type: str='all') -> list|None:
        """
        The function "list_packages" lists device android packages, you can also filter package type.
        
        Args:
            package_type (str): The `package_type` parameter is a string that specifies the type of
                packages to list. It has a default value of `all` that gets all packages on the device,
                but it can also take the following values: [all | enabled | disabled | system | third-party].
                Defaults to all
        
        Returns:
            List of packages. `None` if no device found.
        """
        if self.__selected_device is None:
            return
        packages = []
        if self.__selected_device:
            package_type_flags = {'all': '', 'enabled': '-e', 'disabled': '-d', 'system': '-s', 'third-party': '-3'}
            if package_type not in package_type_flags:
                package_type = 'all'
            results = self.execute_shell_command(f'pm list packages {package_type_flags[package_type]}').split("\n")
            packages = sorted([x.replace('package:', '') for x in results])
            Logger.info(f'There are [bold green]{len(packages)}[/bold green] [bold blue]{package_type}[/bold blue] packages')
            if self.__verbose:
                for package in packages:
                    Logger.print(f'[bold green]{package}[/bold green]')
        return packages
    
    
    
    def get_package_activities(self, package: str) -> list|None:
        """
        The function `get_package_activities` retrieves the activities associated with a given package
        in order to start the app. this is useful to be able to start the app
        
        Args:
            package (str): The "package" parameter is a string that represents the name of the package for
                which you want to retrieve the activities.
        
        Returns:
            List of package activities. `None` if no device found.
        """
        if self.__selected_device is None:
            return
        results = self.execute_shell_command(f'dumpsys package {package}').split()
        activities = []
        for res in results:
            if f'{package}/' in res:
                activity = res.replace('"', '').replace(':', '').replace('}', '').strip()
                activities.append(activity)
                if self.__verbose:
                    Logger.print(f'[bold green]{activity}[/bold green]')
        unique_activities = []
        for activity in activities:
            if activity not in unique_activities and activity.startswith(package):
                unique_activities.append(activity) 
        Logger.info(f'There are [bold green]{len(unique_activities)}[/bold green] activities for package: {package}')
        return unique_activities



    # ------------------------------[ Device related Commands ]------------------------------



    def reboot(self, mode: str|None=None) -> bool|None:
        """
        The function `reboot` reboots the device with the specified mode, or with no mode if none is
        provided.
        
        Args:
            mode (str|None): The `mode` parameter is a string that specifies the type of reboot to
                perform. It can have one of the following values: [bootloader | recovery | sideload | sideload-auto-reboot]
        
        Returns:
            Boolean indicates if tv is rebooted successfully. `None` if no device found.
        """
        if self.__selected_device is None:
            return
        command = 'reboot '
        if mode:
            command += mode
        Logger.info(f'Rebooting TV' + f' in mode [bold green]{mode}[bold green]' if mode else '' + ' ..')
        result =  self.__execute_command(command)
        if 'error' in result:
            Logger.error(f'Rebooting failed')
            return False
        else:
            Logger.success(f'Rebooted successfully')
            return True
    
    
    
    def is_powered_on(self) -> bool|None:
        """
        Check if device is working or not. (Power ON/OFF)
        
        Return:
            Statues of device power on or off.
        """
        if self.__selected_device is None:
            return
        try:
            # results = self.execute_shell_command(f'dumpsys power | grep mHoldingDisplaySuspendBlocker') (true, false)
            # results = self.execute_shell_command(f'dumpsys power | grep mWakefulness') (Asleep | Awake | Dreaming)
            results = self.execute_shell_command(f'dumpsys power | grep "Display Power"')
            return 'ON' in results
        except:
            return
        
        
        
        
        
    def execute_shell_command(self, command: str) -> str:
        """
        The function executes an adb shell command by calling `adb shell` command.
        
        Args:
            command (str): The `command` parameter is a string that represents the shell command that you
                want to execute.
        
        Returns:
            String of the output results of executing the shell command.
        """
        return self.__execute_command(f'shell {command}')



    # ------------------------------[ Inputs Commands ]------------------------------



    def send_keyevent_input(self, keycode: KeyCodes, long_press: bool=False):
        """
        The function executes an adb shell command to send key event input that simulates pressing button keys.
        
        Args:
            keycode (KeyCode): the keycode to send, table of key codes: https://www.temblast.com/ref/akeyscode.htm
            long_press (bool): specify if simulate a long press for the key or not. Defaults to False.
        """
        if self.__selected_device is None:
            return
        command = f'input keyevent {keycode.name}'
        if long_press:
            command += ' --longpress'
        self.execute_shell_command(command)
    
    
    
    def send_text_input(self, text: str, encode_spaces: bool=True):
        """
        The function executes an adb shell command to send text input.
        
        Args:
            text (str): the text string to send.
            encode_spaces (bool): specify if spaces should be replaced by `%s` or not. Defaults to True.
        """
        if self.__selected_device is None:
            return
        processed_text = text.replace(' ', '%s') if encode_spaces else text
        self.execute_shell_command(f'input text {processed_text}')
