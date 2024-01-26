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
        """Pythonic way to interact with adb commands.
        
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



    
    def __execute_command(self, command_str: str, blocking: bool=True) -> Any:
        """
        The function executes a shell command using the adb tool, with the option to run it in blocking
        or non-blocking mode.

        Args:
            command_str (str): The `command_str` parameter is a string that represents the shell command
                to be executed. It can be any valid adb command or a combination of adb commands.
            blocking (bool): The `blocking` parameter is a boolean flag that determines whether the
                command should be executed synchronously (blocking) or asynchronously (non-blocking). Defaults
                to True

        Returns:
            The method `__execute_command` returns the output of the shell command that is executed. If
            the `blocking` parameter is set to `True`, it returns the stdout of the command as a string. If
            `blocking` is set to `False`, it returns a `subprocess.Popen` object.
        """
        command = 'adb '
        if self.__selected_device is not None:
            command += f'-s {self.__selected_device} '
        command += command_str
        if self.__verbose and self.__show_command:
            Logger.info(f'[bold]Command:[/bold] {command}')
        command_parts = shlex.split(command, posix="win" not in sys.platform)
        if blocking:
            proc = subprocess.run(command_parts, check=True, capture_output=True, text=True)
            return proc.stdout.strip()
        else:
            return subprocess.Popen(command_parts, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    
    
    
    # ------------------------------[ Server Commands ]------------------------------



    def start_server(self):
        """
        The function starts an ADB server and waits for it to start up.
        """
        command = 'start-server'
        if self.__verbose:
            Logger.success('ADB server is started')
        self.__server_process = self.__execute_command(command, False)
        time.sleep(5) # give time to start up



    def kill_server(self):
        """
        The function `kill_server` stops the ADB server and terminates any running server process.
        """
        command = 'kill-server'
        self.__execute_command(command)
        if self.__server_process:
            self.__server_process.terminate()
        self.clean()
        if self.__verbose:
            Logger.success('ADB server is stopped')
    
    
    
    def clean(self):
        """Resets and clean"""
        self.__devices = []
        self.__selected_device = None
        self.__server_process = None



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
        command = 'devices'
        if include_descriptions:
            command += ' -l'
        result = self.__execute_command(command)
        devices = result.split("\n")[1:]
        Logger.info(f'There are {len(devices)} connected devices')
        for i, device in enumerate(devices):
            data = device.split()
            serial_number = data[0]
            ip = serial_number.split(':')[0]
            state = data[1]
            description = {}
            for meta in data[2:]:
                meta_pairs = meta.split(':')
                if len(meta_pairs) == 2:
                    description[meta_pairs[0]] = meta_pairs[1]
            self.__devices.append({'ip': ip, 'serial_number': serial_number, 'state': state, 'description': description})
            if self.__verbose:
                Logger.print(f'[bold green]Device[/bold green]: [yellow]{i+1}[/yellow]')
                Logger.print(f'[bold green]IP address[/bold green]: [yellow]{ip}[/yellow]')
                Logger.print(f'[bold green]Serial number[/bold green]: [yellow]{serial_number}[/yellow]')
                Logger.print(f'[bold green]State[/bold green]: [yellow]{state}[/yellow]')
                for key, val in description.items():
                    Logger.print(f'[bold green]{key.title()}[/bold green]: [yellow]{val}[/yellow]')
                Logger.print('\n')
        return self.__devices
    
    
    
    def select_device(self, device_serial: str):
        """
        The function selects a device based on its serial number.
        
        Args:
            device_serial (str): The `device_serial` parameter is a string that represents the serial
                number of a device.
        """
        self.__selected_device = device_serial
        
        
        
    def get_device_info(self) -> dict:
        """
        The function `get_device_info` retrieves device information.
        
        Returns:
            Dictionary containing device information.
        """
        results = self.__execute_command('getprop').split('\n')
        device_info = {}
        for data in results:
            match = re.match(r"\[([^:]+)\]: \[([^:]+)\]", data)
            if match:
                device_info[match.group(1)] = match.group(2)
        return device_info
       
       
       
    def get_state(self) -> str:
        """
        The function `get_state` returns the state of connected device.
        
        Returns:
            String represents device state.
        """
        return self.__execute_command('get-state')



    def get_serialno(self) -> str:
        """
        The function `get_serialno` returns the serial number of a selected device.
        
        Returns:
            The method is returning the serial number of the selected device.
        """
        if self.__selected_device:
            return self.__selected_device
        self.__selected_device = self.__execute_command('get-serialno')
        return self.__selected_device



    def get_devpath(self) -> str:
        """
        The function `get_devpath` retrieves the device path of a connected Android device'.
        
        Returns:
            String represents the device path, for example usb:1-4.3 for usb connected device.
        """
        return self.__execute_command('get-devpath')
    
    
    
    def get_ip_address(self, interface: str='wlan0') -> Any:
        """
        The function `get_ip_address` returns the device IP address of a specified network interface.
        
        Args:
            interface (str): The `interface` parameter is a string that specifies the network interface to
                retrieve the IP address from. In this case, the default value is set to "wlan0", which is a
                common interface name for wireless LAN connections on Linux-based systems. Defaults to wlan0
        
        Returns:
            The IP address of the selected device.
        """
        if self.__selected_device is not None:
            return self.__selected_device.split(':')[0]
        # if result := self.execute_shell_command(f'ifconfig {interface}'):
        #     if match_obj := re.search(r"inet addr:(.+)  Bcast", result, re.M | re.I):
        #         return match_obj[1]
    
    

    # ------------------------------[ Connectivity Commands ]------------------------------



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
            if device['ip'] == ip:
                return True
        return False



    def connect(self, ip: str):
        """
        The function connects to an IP address and raises an error if the connection fails.
        
        Args:
            ip (str): The `ip` parameter in the `connect` method is a string that represents the IP
                address of the device you want to connect to.
                
        Raises:
            RuntimeError
        """
        result = self.__execute_command(f'connect {ip}')
        if "failed" in result:
            raise RuntimeError(f"Unable to connect to {ip}")
        elif "connected" in result:
            self.__selected_device = self.get_serialno()



    def disconnect(self) -> str:
        """
        Disconnect device.
        
        Returns:
            String of the disconnect process result.
        """
        return self.__execute_command('disconnect')


 
    # ------------------------------[ File Operations Commands ]------------------------------



    def push(self, local: str, remote: str='/data/local/tmp/') -> str:
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
            String of the file upload process result.
        """
        return self.__execute_command(f'push {local} {remote}')



    def pull(self, remote: str, local: str, preserve_meta: bool=False) -> str:
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
            String of the file download process result.
        """
        command = 'pull '
        if preserve_meta:
            command += '-k '
        command += f'{remote} {local}'
        return self.__execute_command(command)



    # ------------------------------[ Apps Operations Commands ]------------------------------
    


    def is_installed(self, package_name: str) -> bool:
        """
        The function checks if the specified package is installed or not.
        
        Args:
            package_name (str): The name of the package, for example 'com.google.chrome'
        
        Returns:
            Boolean indicates if app is installed or not.
        """
        command = f'pm list packages | grep {package_name}'
        return len(self.execute_shell_command(command)) > 0
        
        
        
    def install(self, apk_file: str, replace: bool=True) -> str:
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
            String of the app installation process result.
        """
        command = 'install '
        if replace:
            command += '-r '
        command += apk_file
        return self.__execute_command(command)



    def uninstall(self, package: str, keep_data: bool=False) -> str:
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
            String of the app removal process result.
        """
        command = 'uninstall '
        if keep_data:
            command += '-k '
        command += package
        return self.__execute_command(command)
    
    
    
    def start_app(self, package: str, activity: str, wait: bool=True, stop: bool=True) -> str:
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
            String of the app launch process result.
        """
        command = 'am start '
        # wait for launch to complete
        if wait:
            command += '-W '
        if stop: # force stop the target app before starting the activity
            command += '-S '
        command += f'{package}/{activity}'
        return self.execute_shell_command(command)



    def stop_app(self, package: str) -> str:
        """
        The function stops an Android app with the specified package.
        
        Args:
            package (str): The package parameter is a string that represents the package name of the app
                you want to stop.
        
        Returns:
            String of the app stopping process result.
        """
        return self.execute_shell_command(f'am force-stop {package}')



    def list_packages(self, package_type: str='all') -> list:
        """
        The function "list_packages" lists device android packages, you can also filter package type.
        
        Args:
            package_type (str): The `package_type` parameter is a string that specifies the type of
                packages to list. It has a default value of `all` that gets all packages on the device,
                but it can also take the following values: [all | enabled | disabled | system | third-party].
                Defaults to all
        
        Returns:
            List of packages.
        """
        package_type_flags = {'all': '', 'enabled': '-e', 'disabled': '-d', 'system': '-s', 'third-party': '-3'}
        if package_type not in package_type_flags:
            package_type = 'all'
        results = self.execute_shell_command(f'pm list packages {package_type_flags[package_type]}').split("\n")
        packages = sorted([x.replace('package:', '') for x in results])
        if self.__verbose:
            for package in packages:
                Logger.print(f'[bold green]{package}[/bold green]')
        return packages
    
    
    
    def get_package_activities(self, package: str) -> list:
        """
        The function `get_package_activities` retrieves the activities associated with a given package
        in order to start the app.
        
        Args:
            package (str): The "package" parameter is a string that represents the name of the package for
                which you want to retrieve the activities.
        
        Returns:
            List of package activities.
        """
        '''Get package activities, this is useful to be able to start the app'''
        results = self.execute_shell_command(f'dumpsys package {package}').split()
        activities = set()
        for res in results:
            if 'activity' in res.lower() and 'com' in res.lower():
                activities.add(res.replace('"', '').strip())
        return list(activities)



    # def kill_all(self):
    #     """
    #     Kill all background processes.
    #     """
    #     return self.execute_shell_command('am kill-all')



    # ------------------------------[ Device related Commands ]------------------------------



    def reboot(self, mode: str|None=None) -> str:
        """
        The function `reboot` reboots the device with the specified mode, or with no mode if none is
        provided.
        
        Args:
            mode (str|None): The `mode` parameter is a string that specifies the type of reboot to
                perform. It can have one of the following values: [bootloader | recovery | sideload | sideload-auto-reboot]
        
        Returns:
            The method is returning the result of executing the reboot command on the device.
        """
        command = 'reboot '
        if mode:
            command += mode
        return self.__execute_command(command)
    
    
    
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



    # ------------------------------[ Services Commands ]------------------------------
    


    def list_services(self) -> list:
        """
        The `list_services` function retrieves a list of services along with their IDs, names, and
        associated packages.
        
        Returns:
            List of dictionaries, where each dictionary represents a service. Each dictionary contains
            the following keys: 'id' (integer), 'name' (string), and 'package' (string).
        """
        results = self.execute_shell_command('service list')
        lines = results.split("\n")
        lines = lines[1:]
        services = []
        pattern = r"(\d+)\t(\w+):\s+\[(.*?)\]"
        for line in lines:
            if match := re.search(pattern, line):
                service_id = int(match[1])
                service_name = match[2]
                service_process = match[3]
                service_info = {'id': service_id, 'name': service_name, 'package': service_process}
                services.append(service_info)
        return services



    def start_service(self, service: str) -> str:
        """
        The function executes an adb shell command to start a service.
        
        Args:
            service (str): The `service` parameter is a string that represents service name that you
                want to start.
        
        Returns:
            String of the output results of service starting processing.
        """
        return self.execute_shell_command(f'am startservice {service}')



    def stop_service(self, service: str) -> str:
        """
        The function executes an adb shell command to stop a running service.
        
        Args:
            service (str): The `service` parameter is a string that represents service name that you
                want to stop.
        
        Returns:
            String of the output results of service stopping processing.
        """
        return self.execute_shell_command(f'am stopservice {service}')
        # return self.execute_shell_command(f'am force-stop {service}')



    # ------------------------------[ Inputs Commands ]------------------------------



    def send_keyevent_input(self, keycode: KeyCodes, long_press: bool=False) -> str:
        """
        The function executes an adb shell command to send key event input that simulates pressing button keys.
        
        Args:
            keycode (KeyCode): the keycode to send, table of key codes: https://www.temblast.com/ref/akeyscode.htm
            long_press (bool): specify if simulate a long press for the key or not. Defaults to False.
        
        Returns:
            String of the output results of sending input.
        """
        command = f'input keyevent {keycode.name}'
        if long_press:
            command += '--longpress'
        return self.execute_shell_command(command)
    
    
    
    def send_text_input(self, text: str, encode_spaces: bool=True):
        """
        The function executes an adb shell command to send text input.
        
        Args:
            text (str): the text string to send.
            encode_spaces (bool): specify if spaces should be replaced by `%s` or not. Defaults to True.
        
        Returns:
            String of the output results of sending input.
        """
        '''Send text.'''
        processed_text = text.replace(' ', '%s') if encode_spaces else text
        return self.execute_shell_command(f'input text {processed_text}')
