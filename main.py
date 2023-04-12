#TODO: make sure to start using new CLI libaries https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df

import filelistner
import modhandler
import consoleoutcolors as coc
import keyboard

def main():
        def listen():
                while 1:
                        if filelistner.programlistner():
                               break
                        if keyboard.is_pressed('s'):
                                break
        
        def operationchoice():
                print("What operation would you like to perform? Type 'help' for list of commands")
                answear = input('--> ')

                if answear == "load":
                        print(f"{coc.BColors.OKBLUE}Selected: {coc.BColors.BOLD}load{coc.BColors.ENDC}")
                        modhandler.equipmodpack()
                elif answear == "unload":
                        print(f"{coc.BColors.OKBLUE}Selected: {coc.BColors.BOLD}unload{coc.BColors.ENDC}")
                        modhandler.removemodpackfrommc()
                
                elif answear == "make":
                        print(f"{coc.BColors.OKBLUE}Selected: {coc.BColors.BOLD}make{coc.BColors.ENDC}")
                        modhandler.createmodpack()

                elif answear == "delete":
                        print(f"{coc.BColors.OKBLUE}Selected: {coc.BColors.BOLD}make{coc.BColors.ENDC}")
                        modhandler.deletemodpack()

                elif answear == "help":
                        print(f"{coc.BColors.OKBLUE}Selected: {coc.BColors.BOLD}help{coc.BColors.ENDC}")
                        print(f"""
List of commands (case sensitive):
- {coc.BColors.UNDERLINE}load{coc.BColors.ENDC} Loads a chosen modpack.
- {coc.BColors.UNDERLINE}unload{coc.BColors.ENDC} Unloads a chosen modpack.
- {coc.BColors.UNDERLINE}make{coc.BColors.ENDC} Makes a modpack folder which is ready to put files into.
- {coc.BColors.UNDERLINE}delete{coc.BColors.ENDC} Deletes a modpack.
- {coc.BColors.UNDERLINE}exit{coc.BColors.ENDC} Exits MEM-L.
- {coc.BColors.UNDERLINE}help{coc.BColors.ENDC} Displays this text.
""")
                        operationchoice()

                elif answear == "exit":
                        print(f"{coc.BColors.OKBLUE}Selected: {coc.BColors.BOLD}exit{coc.BColors.ENDC}")
                        print(f"{coc.BColors.OKBLUE}Goodbye!{coc.BColors.ENDC}")
                        quit()

                else:
                        print(f"{coc.BColors.WARNING}/!\ This command does not exist! Type 'help' for list of commands...{coc.BColors.ENDC}")
                        operationchoice()

                main()

        print(f"{coc.BColors.HEADER}\nWelcome to Minecraft External Mod-Loader! To get started, open offical Minecraft Launcher or press 's'.\npress control + c at anytime to quit{coc.BColors.ENDC}")
        
        listen() #Wait for start...
        operationchoice() #Execute...

if __name__ == "__main__":
    main()