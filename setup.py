import os
import jsonhandler

def main():
    PATH = os.getcwd().replace("\\", "/")
    modFolder = f"{os.getenv('APPDATA')}.minecraft\mods".replace("\\", "/")

    jsonhandler.write({
    "data": {
        "applicationToListenForCaption": "Minecraft.exe",
        "mcModFolder": modFolder,
        "appRootFolder": PATH
    }
}, "config.json")
    print('Done!')

if __name__ == "__main__":
    main()