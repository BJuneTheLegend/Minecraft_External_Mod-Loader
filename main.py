from __future__ import print_function, unicode_literals

import modhandler

from PyInquirer import prompt
from examples import custom_style_3
import colored #https://pypi.org/project/colored/

def main():
        class commands():
                def __init__(self) -> None:
                        self.possibilities = { #This makes it easier to grow codebase in future, also makes it easier to add things.
                                'load': {'method': modhandler.equipmodpack, 'help': 'Loads a chosen modpack.'},
                                'unload': {'method': modhandler.removemodpackfrommc, 'help': 'Unloads a chosen modpack.'},
                                'make': {'method': modhandler.createmodpack, 'help': 'Deletes a modpack.'},
                                'delete': {'method': modhandler.deletemodpack, 'help': 'Deletes a modpack.'},
                                'help': {'method': self.help, 'help': 'Displays this text.'},
                                'exit': {'method': quit, 'help': 'Exits MEM-L.'}
                        }

                def run(self, method: str):
                        self.possibilities[method]['method']() #Using the fact that variables can be assigned to methods,
                        #you can run any with some selectors and add a "()" to the end.

                def help(self, command: str):
                        print(self.possibilities[command]['help'])

                def operationchoice(self):
                        keysList = list(self.possibilities.keys())               
                        choices = [
                                {
                                'type': 'list',
                                'name': 'choice',
                                'message': 'What operation do you want to do?',
                                'choices': [keysList[i] for i in range(0, len(keysList))]
                                },
                                {
                                'type': 'list',
                                'name': 'help',
                                'message': 'What command do you need help on?',
                                'choices': [keysList[i] for i in range(0, len(keysList))],
                                'when': lambda answers: answers['choice'] == 'help'
                                }
                        ]
                        answer = prompt(choices, style=custom_style_3) #get response from questionnaire

                        if answer['choice'] == 'help':
                                self.help(answer['help'])
                                self.operationchoice() #go back to beginning
                        else:
                                self.run(answer['choice'])
                        

        print(colored.fore.PURPLE_3 + "\nWelcome to Minecraft External Mod-Loader!\npress control + c at anytime to quit" + colored.style.RESET)

        c = commands()
        c.operationchoice() #Execute...

if __name__ == "__main__":
    main()