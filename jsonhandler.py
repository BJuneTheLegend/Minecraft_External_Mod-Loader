import json
import sys
import consoleoutcolors as coc
import os

def read(name):
    try:
        with open(name, 'r') as j:
             contents = json.loads(j.read())
        return contents
    
    except Exception as e:
        print(f"{coc.BColors.FAIL}/!\ Json file could not be loaded! Has it been moved or renamed? error: {e}{coc.BColors.ENDC}")
        sys.exit()

def write(content, name):
    json_object = json.dumps(content, indent=4)
    
    with open(name, "w") as outfile:
        outfile.write(json_object)

def writemcmetadata(content, name):
    #TODO: make this not switch dirs everytime...
    appRootFolder = read("config.json")["data"]["appRootFolder"] #remeber PATH because when we change dirs, we cannot find a config.json file

    os.chdir(read("config.json")["data"]["mcModFolder"]) #CD to Minecraft mod folder dir
    open(name, "a")

    json_object = json.dumps(content, indent=4) #Dump contents into 
    
    with open(name, "w") as outfile:
        outfile.write(json_object)

    os.chdir(appRootFolder) #Change back to PATH

def writemodpackmetadata(content, name, dirName):
    json_object = json.dumps(content, indent=4)
    
    with open(f"ModPacks/{dirName}/{name}", "w") as outfile:
        outfile.write(json_object)
