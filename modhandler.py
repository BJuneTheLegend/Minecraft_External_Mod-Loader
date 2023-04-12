import datetime
import os
import shutil
import sys

import keyboard

import consoleoutcolors as coc
import jsonhandler


def copymodpacktomc(modpack):
    try: #get all modpacks
        contentsOfPack = os.listdir(f"ModPacks/{modpack}")
    except Exception as e:
        print(f"{coc.BColors.FAIL}/!\ Mod Pack could not be found! error: {e}{coc.BColors.ENDC}")
        sys.exit()

    jsonData = {"name": modpack, "mods": [contentsOfPack[i] for i in range(0, len(contentsOfPack))]} #make metadata file

    jsonhandler.writemcmetadata(jsonData, f"{modpack}-LOADED_METADATA_MEM-L.json") #create the metadatafile which tells you all files being added, usfull for when deleting.
    print(f"{coc.BColors.OKGREEN}Succesfully wrote metadata file...{coc.BColors.ENDC}")

    shutil.copytree(src=f"ModPacks/{modpack}", dst=jsonhandler.read("config.json")["data"]["mcModFolder"], dirs_exist_ok = True) #get all the files in the modpack and 
    #add them all to mod folder
    print(f"{coc.BColors.OKGREEN}Succesfully wrote mod files...{coc.BColors.ENDC}")

    data = jsonhandler.read(f"ModPacks/{modpack}/{modpack}-PACK_METADATA_MEM-L.json")
    print(f"{coc.BColors.BOLD}{coc.BColors.OKGREEN}Done!{coc.BColors.ENDC}")
    print(f"{coc.BColors.OKCYAN}Ready to load {data['name']}, in {data['version']} for {data['loader']}")

def createmodpack():
    def create():
        dateCreated = datetime.datetime.now() #get time and data
        dateCreated = dateCreated.strftime("%B %d, %Y %H:%M:%S")

        newpath = os.path.join(jsonhandler.read("config.json")["data"]["appRootFolder"],"ModPacks",name)
        if not os.path.exists(newpath): #create the modpack folder
            print(f"{coc.BColors.OKGREEN}Creating new folder...{coc.BColors.ENDC}")
            os.makedirs(newpath)
        else:
            print(f"{coc.BColors.WARNING}/!\ There is already a modpack with the same name!{coc.BColors.ENDC}")
            createmodpack()
        print(f"{coc.BColors.OKGREEN}Creating metadata...{coc.BColors.ENDC}")
        jsonhandler.writemodpackmetadata({"name": name, "version": version, "loader": loader, "dateCreated": dateCreated}, f"{name}-PACK_METADATA_MEM-L.json", name) #make
        #a meta data file that has information about pack, not be confused with the meta data file being added to the mods folder.
        print(f"{coc.BColors.BOLD}{coc.BColors.OKGREEN}Done!{coc.BColors.ENDC}")

    name = input("What are you naming this mod pack? --> ")
    version = input("What Minecraft version is this pack? --> ")
    loader = input("What loader is this pack using? ex. Fabric, Forge... --> ")

    print(f"{coc.BColors.OKCYAN}preview...\n{coc.BColors.ENDC}") #open yes/no prompt with keyboard
    print(f"{coc.BColors.OKBLUE}{name} {version} {loader}{coc.BColors.ENDC}")
    print(f"[{coc.BColors.BOLD}{coc.BColors.OKCYAN}Y{coc.BColors.ENDC}/{coc.BColors.BOLD}{coc.BColors.OKCYAN}N{coc.BColors.ENDC}]")

    while True:
        if keyboard.is_pressed('y'):
            create()
            break
        elif keyboard.is_pressed('n'):
            createmodpack()
            break

def equipmodpack():

    try: #find all modpacks
        modPacks = os.listdir("ModPacks")
    except Exception as e:
        print(f"{coc.BColors.FAIL}/!\ Mod Packs folder could not be found! Has the folder been moved or renamed? error: {e}{coc.BColors.ENDC}")
        sys.exit()

    print("Please provide mod pack you wish to use. (case sensitive)")
    print("\nMod Packs:")
    for i in modPacks:
        print(f"- {coc.BColors.UNDERLINE}{i}{coc.BColors.ENDC}")

    def select():
        selectedModPack = input("\n--> ")

        if modPacks.__contains__(selectedModPack):
            print(f"{coc.BColors.OKBLUE}Selected: {coc.BColors.BOLD}{selectedModPack}{coc.BColors.ENDC}")
            copymodpacktomc(selectedModPack)

        else:
            print(f"{coc.BColors.WARNING}/!\ We could not find that mod pack! Please try again...{coc.BColors.ENDC}")
            select()
    select()

def removemodpackfrommc():
        def select():
            selectedModPack = input("\n--> ")

            if loadedModPacks.__contains__(selectedModPack):
                print(f"{coc.BColors.OKBLUE}Selected: {coc.BColors.BOLD}{selectedModPack}{coc.BColors.ENDC}")
                return selectedModPack

            else:
                print(f"{coc.BColors.WARNING}/!\ We could not find that mod pack! Please try again...{coc.BColors.ENDC}")
                select()

        loadedModPacks = [] 
        mcModFolder = jsonhandler.read("config.json")["data"]["mcModFolder"]
        for file in os.listdir(mcModFolder): #TODO: make this code more safe
            if file.__contains__("-LOADED_METADATA_MEM-L.json"): #check if it the correct metadate file, this can be broken if someone adds a non MEM-L file
                #that contains this string
                loadedModPacks.append(jsonhandler.read(os.path.join(mcModFolder, file))["name"]) #find all loaded mods 
        
        print("Please provide mod pack you wish to unload. (case sensitive)")
        print("\nMod Packs:")
        for i in loadedModPacks:
            print(f"- {coc.BColors.UNDERLINE}{i}{coc.BColors.ENDC}")   
        selectedModPack = select()

        appRootFolder = jsonhandler.read("config.json")["data"]["appRootFolder"]
        os.chdir(jsonhandler.read("config.json")["data"]["mcModFolder"]) #TODO: find a better solution to chdir

        filesToRemove = jsonhandler.read(f"{selectedModPack}-LOADED_METADATA_MEM-L.json")["mods"]
        filesToRemove.append(f"{selectedModPack}-LOADED_METADATA_MEM-L.json")
        
        print(f"{coc.BColors.OKGREEN}Unloading files...")
        for file in filesToRemove: #loop thru all files in the loadedModPacks varible and delete them. A copy of the modpack is always save on PATH
            os.remove(file)
            print(f"Succesfully unloaded {file}...")

        print(f"{coc.BColors.BOLD}Done!{coc.BColors.ENDC}")

        os.chdir(appRootFolder)

def deletemodpack():
    def delete(modpack):
        print(f"{coc.BColors.OKGREEN}Deleting files...")
        for file in os.listdir(f"ModPacks/{modpack}"): #find all files in modpack and delete them
            os.remove(f"ModPacks/{modpack}/{file}")
            print(f"Succesfully deleted {file}...")
        os.rmdir(f"ModPacks/{modpack}") #remove the dir
        print(f"Succesfully deleted folder...")
        print(f"{coc.BColors.BOLD}Done!{coc.BColors.ENDC}")

    try:
        modPacks = os.listdir("ModPacks") #get all modpacks
    except Exception as e:
        print(f"{coc.BColors.FAIL}/!\ Mod Packs folder could not be found! Has the folder been moved or renamed? error: {e}{coc.BColors.ENDC}")
        sys.exit()

    print(f"{coc.BColors.BOLD}{coc.BColors.OKCYAN}WARNING: DELETING MOD PACKS IS {coc.BColors.UNDERLINE}PERMANT!{coc.BColors.ENDC}")
    print("Please provide mod pack you wish to delete. (case sensitive)")
    print("\nMod Packs:")
    for i in modPacks:
        print(f"- {coc.BColors.UNDERLINE}{i}{coc.BColors.ENDC}")

    def select():
        selectedModPack = input("\n--> ")

        if modPacks.__contains__(selectedModPack):
            print(f"{coc.BColors.OKBLUE}Selected: {coc.BColors.BOLD}{selectedModPack}{coc.BColors.ENDC}")
            print(f"[{coc.BColors.BOLD}{coc.BColors.OKCYAN}Y{coc.BColors.ENDC}/{coc.BColors.BOLD}{coc.BColors.OKCYAN}N{coc.BColors.ENDC}]")
            while True:
                if keyboard.is_pressed('y'):
                    delete(selectedModPack)
                    break
                elif keyboard.is_pressed('n'):
                    deletemodpack()
                    break

        else:
            print(f"{coc.BColors.WARNING}/!\ We could not find that mod pack! Please try again...{coc.BColors.ENDC}")
            select()
    select()