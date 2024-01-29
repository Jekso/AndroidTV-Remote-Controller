import cowsay
import random
from rich.console import Console



class Logger:
    """Pretty logging utils by the awesome Rich library"""


    console = Console(force_jupyter=False)



    @classmethod
    def welcome(cls, class_desc=''):
        welcome_message = f'''
            Hello people of Earth, this class is to
            {class_desc}
        '''
        cls.console.print('\n\n[green bold]--------------------[ [yellow2]Made with [red]:heart:[/red] and :coffee: by [i sky_blue1]Jekso[/i sky_blue1][/yellow2] ]--------------------[/green bold]\n\n')
        cls.console.print('[green bold]' + cowsay.get_output_string('cow', welcome_message) + '[/green bold]')
        # cls.console.print('\n\n[green bold]--------------------[ [yellow2]Made with [red]:heart:[/red] and :coffee: by [i sky_blue1]Jekso[/i sky_blue1][/yellow2] ]--------------------[/green bold]\n\n')
                


    @classmethod
    def error(cls, message, exit_script=False):
        emoji_list = ['face_with_rolling_eyes', 'sob', 'face_with_steam_from_nose', 'face_without_mouth', 'face_screaming_in_fear', 'face_with_head__bandage', 'tired_face']
        err_emoji = random.choice(emoji_list)
        err_message = f'\n[red bold]:{err_emoji}: Error: {message}![/red bold]\n'
        cls.console.print(err_message) 
        cls.console.print('\n') 
        if exit_script:
            exit()
    
    
    
    @classmethod
    def success(cls, message):
        cls.console.print(f'[bold green]:sunglasses: {message}.[/bold green]\n')



    @classmethod
    def info(cls, message):
        cls.console.print(f'[bold yellow1]:bulb: {message}.[/bold yellow1]\n')
    
    
    
    @classmethod
    def warning(cls, message):
        cls.console.print(f'[bold orange1]:prohibited: {message}.[/bold orange1]\n')
        
        
        
    @classmethod
    def print(cls, message):
        cls.console.print(f'{message}')



